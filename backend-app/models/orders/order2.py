from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
from schema.city import citySchema
# from schema.order import OrderSchemaPost
from schema.order import OrderSchemaPost
from models.user import User
from schema.user import user_schema_post
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from datetime import datetime, time
from config.wsp import enviar_mensaje_whatsapp
import pytz
from psycopg2.extras import Json

import random
import requests





load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
TOKEN = os.getenv("API_TOKEN")


api_key = 'obg0iystmnq4v0ln4r5fnjcvankhtjp0'
source_number = '573053447255'
destination_number = '573226892988'
message = 'esta es una prueba de la api'
source_name = 'Salchimonster'

class Order2:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        
    def create_order(self, order_data: OrderSchemaPost):
        user_id = self.create_user(order_data.user_data)
        
        # Verificar si el usuario puede realizar una nueva orden
        if self.can_place_order(user_id):
            
            order_id = self.create_order_entry(user_id, order_data)

            # if (not order_data.inserted_by):

            #     self.generate_order_code(order_data.user_data.user_phone,order_id)

            self.insert_order_details(order_id, order_data)
            # self.insert_order_products(order_id, order_data)
            # self.insert_order_aditionals(order_id, order_data)
            self.update_order_status(order_id, order_data.payment_method_id,order_data.inserted_by)
            self.insert_order_notes(order_id,order_data.order_notes)
            # Actualizar la última hora de compra
            self.update_last_order_time(user_id)
            

            self.conn.commit()
            # enviar_mensaje_whatsapp(api_key,source_number,destination_number,message,source_name)

            return order_id
        else:
            
            last_order_query = f"SELECT id FROM orders.orders where user_id = {user_id} ORDER BY id DESC LIMIT 1;"
            self.cursor.execute(last_order_query)
            order_id = self.cursor.fetchone()[0]   
            return order_id
            
            
            
    def traslate_order(self, order_id:str, site_id:int):
        query = "update orders.orders set site_id = %s where id = %s returning id;"
        result = self.cursor.execute(query,(site_id,order_id,))
        
        order_status_insert_query = """
                    INSERT INTO orders.order_status (order_id, status, timestamp)
                    VALUES (%s, %s, CURRENT_TIMESTAMP)
                    """
        self.cursor.execute(order_status_insert_query, (order_id, 'generada'))
                    
        self.conn.commit()
        
        self.create_or_update_event(1, site_id, 1132, '3 minutes', False)
        return result
        
            

    def create_user(self, user_data):
        user_id = User().insert_user(user_data)
        return user_id


    def create_order_entry(self, user_id, order_data):
        # Crear el JSON inicial sin "delivery_codigointegracion"
        pe_json = {
            "delivery": {
                "local_id": order_data.pe_site_id,
                "delivery_costoenvio": order_data.delivery_price,
                "delivery_direccionenvio": order_data.user_data.user_address,
                "delivery_notageneral": order_data.order_notes,
                "delivery_horaentrega": "2020-12-06 10:00:00",
                "delivery_pagocon": order_data.total + order_data.delivery_price,
                "delivery_codigointegracion": None,
                "canaldelivery_id":500
            },
            
            "cliente": {
                "cliente_nombres": order_data.user_data.user_name,
                "cliente_apellidos": '.',
                "cliente_direccion": order_data.user_data.user_address,
                "cliente_telefono": order_data.user_data.user_phone
            },
            "listaPedidos": order_data.pe_json
        }

        
        if order_data.payment_method_id == 6:
            order_insert_query = """
            INSERT INTO orders.orders (user_id, site_id, delivery_person_id, authorized, inserted_by_id, pe_json)
            VALUES (%s, %s, %s, false, %s, %s) RETURNING id;
            """
        else:
            order_insert_query = """
            INSERT INTO orders.orders (user_id, site_id, delivery_person_id, inserted_by_id, pe_json)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
            """

        self.cursor.execute(order_insert_query, (
            user_id,
            order_data.site_id,
            4,  # delivery_person_id
            order_data.inserted_by,
            Json(pe_json)
        ))
        result = self.cursor.fetchone()
        if result is None:
            raise ValueError("La orden no pudo ser creada.")
        order_id = result[0]

        # Actualizar "delivery_codigointegracion" en el JSON
        pe_json["delivery"]["delivery_codigointegracion"] = order_id

        # Actualizar el registro en la base de datos con el JSON actualizado
        update_query = """
        UPDATE orders.orders
        SET pe_json = %s
        WHERE id = %s;
        """
        self.cursor.execute(update_query, (Json(pe_json), order_id))

        # Crear o actualizar el evento
        if order_data.payment_method_id == 6:
            self.create_or_update_event(3, 12, 1132, '3 minutes', False)
        else:
            self.create_or_update_event(1, order_data.site_id, 1132, '3 minutes', False)

        return order_id

    
    def create_or_update_event(self, event_type_id, site_id, employee_id, update_interval, solved=False):
        # Primero, intentar eliminar cualquier evento existente que coincida con los criterios
        delete_query = """
        DELETE FROM events
        WHERE event_type_id = %s AND site_id = %s AND employee_id = %s;
        """
        self.cursor.execute(delete_query, (event_type_id, site_id, employee_id))

        # Después, insertar el nuevo evento
        event_insert_query = """
        INSERT INTO events (
            event_timestamp, 
            event_type_id, 
            site_id, 
            employee_id, 
            update_interval, 
            solved
        ) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(event_insert_query, (event_type_id, site_id, employee_id, update_interval, solved))
        event_id = self.cursor.fetchone()[0]
        return event_id


    def create_or_update_event_pqr(self, event_type_id, site_id, employee_id, update_interval, solved=False):
        # Primero, intentar eliminar cualquier evento existente que coincida con los criterios
        delete_query = """
        DELETE FROM events
        WHERE event_type_id = %s AND site_id = %s AND employee_id = %s;
        """
        self.cursor.execute(delete_query, (event_type_id, site_id, employee_id))

        # Después, insertar el nuevo evento
        event_insert_query = """
        INSERT INTO events (
            event_timestamp, 
            event_type_id, 
            site_id, 
            employee_id, 
            update_interval, 
            solved
        ) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(event_insert_query, (event_type_id, site_id, employee_id, update_interval, solved))
        event_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return event_id



    def insert_order_details(self, order_id, order_data):
        order_details_insert_query = """
        INSERT INTO orders.order_details (order_id, payment_method_option_id, delivery_price)
        VALUES (%s, %s, %s);
        """
        self.cursor.execute(order_details_insert_query, (order_id, order_data.payment_method_id, order_data.delivery_price))
        
    def insert_order_notes(self, order_id, order_notes):
        order_notes_insert_query = """
        INSERT INTO orders.order_notes (order_id, notes)
        VALUES (%s, %s);
        """
        self.cursor.execute(order_notes_insert_query, (order_id, order_notes))



    def insert_cancellation_request(self, order_id,responsible,reason):
        order_notes_insert_query = """
        INSERT INTO orders.cancellation_requests (order_id, timestamp,responsible,reason)
        VALUES (%s, CURRENT_TIMESTAMP, %s, %s);
        """
        self.cursor.execute(order_notes_insert_query, (order_id, responsible,reason))

        get_site_id_query = """
        SELECT site_id FROM orders.orders
        WHERE id = %s;
        """
        self.cursor.execute(get_site_id_query, (order_id,))
        site_id_result = self.cursor.fetchone()
        site_id = site_id_result[0]

        self.mark_events_as_solved_by_site_id(site_id)
        self.create_or_update_event(2, site_id, 1132, '1 minute', False)

        self.conn.commit()

    def get_all_cancellation_request(self, ):
        order_notes_insert_query = """
        select * from orders.cancellation_request_complete;
        """
        self.cursor.execute(order_notes_insert_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    def get_all_cancellation_request_categories(self, ):
        order_notes_insert_query = """
        select * from orders.cancellation_request_categories where visible = true;
        """
        self.cursor.execute(order_notes_insert_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    def get_all_cancellation_request_pendients(self):
        colombia_tz = pytz.timezone('America/Bogota')  # Define la zona horaria de Colombia
        query = """
        SELECT *
        FROM orders.cancellation_request_complete
        WHERE solved = FALSE order by timestamp desc    ;
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        raw_results = self.cursor.fetchall()

        results = []
        for row in raw_results:
            result_dict = dict(zip(columns, row))
            # Convierte 'timestamp' de UTC a hora local de Colombia si existe en el resultado
            if 'timestamp' in result_dict and result_dict['timestamp']:
                result_dict['timestamp'] = result_dict['timestamp'].replace(tzinfo=pytz.utc).astimezone(colombia_tz)
            results.append(result_dict)

        return results
    
    def get_all_cancellation_request_solved_acepted(self, ):
        colombia_tz = pytz.timezone('America/Bogota')  # Define la zona horaria de Colombia

        order_notes_insert_query = """
        select * from orders.cancellation_request_complete where solved = true and authorized = true order by timestamp desc;
        """
        self.cursor.execute(order_notes_insert_query)
        columns = [desc[0] for desc in self.cursor.description]
        raw_results = self.cursor.fetchall()

        results = []
        for row in raw_results:
            result_dict = dict(zip(columns, row))
            # Convierte 'timestamp' de UTC a hora local de Colombia si existe en el resultado
            if 'timestamp' in result_dict and result_dict['timestamp']:
                result_dict['timestamp'] = result_dict['timestamp'].replace(tzinfo=pytz.utc).astimezone(colombia_tz)
            results.append(result_dict)

        return results

    def get_all_cancellation_request_solved_rejected(self, ):
        colombia_tz = pytz.timezone('America/Bogota')  # Define la zona horaria de Colombia

        order_notes_insert_query = """
        select * from orders.cancellation_request_complete where solved = true and authorized = false order by timestamp desc;
        """
        self.cursor.execute(order_notes_insert_query)
        columns = [desc[0] for desc in self.cursor.description]
        raw_results = self.cursor.fetchall()

        results = []
        for row in raw_results:
            result_dict = dict(zip(columns, row))
            # Convierte 'timestamp' de UTC a hora local de Colombia si existe en el resultado
            if 'timestamp' in result_dict and result_dict['timestamp']:
                result_dict['timestamp'] = result_dict['timestamp'].replace(tzinfo=pytz.utc).astimezone(colombia_tz)
            results.append(result_dict)

        return results


    def DelivZero(self, order_id):
        order_notes_insert_query = f"""
        UPDATE orders.order_details SET delivery_price = {0} where order_id = '{order_id}' ;
        """
        self.cursor.execute(order_notes_insert_query)
        self.conn.commit()





    def resolve_cancellation_request(self, cancellation_request_id, authorized,responsible_id,responsible_observation,category_id):
        """
        Resuelve una solicitud de cancelación de una orden.
        Args:
            cancellation_request_id (int): ID de la solicitud de cancelación.
            authorized (bool): Indica si la cancelación ha sido autorizada o no.
        """
        # Obtener la información de la solicitud de cancelación
        get_request_query = """
        SELECT order_id, reason, responsible
        FROM orders.cancellation_requests
        WHERE id = %s;
        """
        self.cursor.execute(get_request_query, (cancellation_request_id,))
        result = self.cursor.fetchone()
        if not result:
            raise ValueError("No se encontró la solicitud de cancelación.")
        
        order_id, reason, responsible = result
        
        # Actualizar la solicitud como resuelta y autorizada/no autorizada
        update_request_query = f"""
        UPDATE orders.cancellation_requests
        SET solved = TRUE, authorized = %s, responsible_id = %s, responsible_observation = %s, category_id = {category_id}
        WHERE id = %s;
        """
        self.cursor.execute(update_request_query, (authorized,responsible_id,responsible_observation, cancellation_request_id))

        # Si la solicitud está autorizada, cancelar la orden
        if authorized:
            self.cancel_order(order_id, responsible, reason)
        
        self.conn.commit()



    def insert_order_products(self, order_id, order_data):
        product_instance_ids = [str(product.product_instance_id) for product in order_data.order_products]
        ids_text = ', '.join(product_instance_ids)
        products_instance_item_ids_query = f"SELECT id, price FROM inventory.product_instances WHERE id IN ({ids_text});"
        self.cursor.execute(products_instance_item_ids_query)
        product_items_db = self.cursor.fetchall()
        product_prices = {item[0]: item[1] for item in product_items_db}
        for product in order_data.order_products:
            self.insert_order_item(order_id, product, product_prices)

    def insert_order_item(self, order_id, product, product_prices):
        order_items_insert_query = """
        INSERT INTO orders.order_items (order_id, product_instance_id, quantity, price)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(order_items_insert_query, (order_id, product.product_instance_id, product.quantity, product_prices[product.product_instance_id]))
        order_item_id = self.cursor.fetchone()[0]

    def insert_order_aditionals(self, order_id, order_data):
        if order_data.order_aditionals:
            aditional_instance_ids = [str(aditional.aditional_item_instance_id) for aditional in order_data.order_aditionals]
            ids_text = ', '.join(aditional_instance_ids)
            aditionals_query = f"SELECT id, price FROM orders.aditional_item_instances WHERE id IN ({ids_text});"
            self.cursor.execute(aditionals_query)
            aditional_items_db = self.cursor.fetchall()
            aditional_prices = {item[0]: item[1] for item in aditional_items_db}
            for aditional in order_data.order_aditionals:
                self.insert_order_aditional_item(order_id, aditional, aditional_prices)

    def insert_order_aditional_item(self, order_id, aditional, aditional_prices):
        order_aditionals_insert_query = """
        INSERT INTO orders.order_aditional_items (order_id, aditional_item_instance_id, quantity, price)
        VALUES (%s, %s, %s, %s);
        """
        self.cursor.execute(order_aditionals_insert_query, (order_id, aditional.aditional_item_instance_id, aditional.quantity, aditional_prices[aditional.aditional_item_instance_id]))

    def update_order_status(self, order_id, payment_method_id, inserted_by ):

        if  payment_method_id != 6:


            validation = 'generada'

            # if (not inserted_by):
            #     validation = 'in validation'
            # else:
            #     validation = 'generada'
            

            order_status_insert_query = """
            INSERT INTO orders.order_status (order_id, status,timestamp)
            VALUES (%s, %s,CURRENT_TIMESTAMP );
            """
            self.cursor.execute(order_status_insert_query, (order_id, validation,))
            
            # Consulta para insertar el historial del estado de la orden
            order_status_history_insert_query = """
            INSERT INTO orders.order_status_history (order_id, status,timestamp)
            VALUES (%s, %s,CURRENT_TIMESTAMP );
            """
            self.cursor.execute(order_status_history_insert_query, (order_id, validation,))


        else:
            
       
            # Consulta para insertar el estado de la orden
            order_status_insert_query = """
            INSERT INTO orders.order_status (order_id, status,timestamp)
            VALUES (%s, %s,CURRENT_TIMESTAMP );
            """
            self.cursor.execute(order_status_insert_query, (order_id, 'transferencia pendiente',))
            
            # Consulta para insertar el historial del estado de la orden
            order_status_history_insert_query = """
            INSERT INTO orders.order_status_history (order_id, status,timestamp)
            VALUES (%s, %s,CURRENT_TIMESTAMP );
            """
            self.cursor.execute(order_status_history_insert_query, (order_id, 'transferencia pendiente',))

    def traslate_order(self, order_id:str, site_id:int):
        query = "update orders.orders set site_id = %s where id = %s returning id;"
        result = self.cursor.execute(query,(site_id,order_id,))
        
        order_status_insert_query = """
                    INSERT INTO orders.order_status (order_id, status, timestamp)
                    VALUES (%s, %s, CURRENT_TIMESTAMP)
                    """
        self.cursor.execute(order_status_insert_query, (order_id, 'generada'))
                    
        self.conn.commit()
        
        self.create_or_update_event(1, site_id, 1132, '3 minutes', False)
        return result
        
        
        

    def enviar_mensaje_template(self,destino,bret,flo,mon,can,jam,pal,mod,sub,ken,lau,fecha,total):


        url = "https://api.gupshup.io/wa/api/v1/template/msg"
        headers = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
            'apikey': 'obg0iystmnq4v0ln4r5fnjcvankhtjp0',
            'cache-control': 'no-cache'
        }
        # Preparar los parámetros del template
        params = ["Bryan", "SalchiGest",flo,bret,mon,can,jam,pal,mod,sub,ken,lau,fecha,f"${total}"]
        data = {
            'channel': 'whatsapp',
            'source': '573053447255',
            'destination': destino,
            'src.name': 'Salchimonster',
            'template': '{"id":"56986be2-6b17-42cf-8cf7-d439b9a97757","params":' + str(params) + '}'
        }
        # Convertir la lista params a formato JSON adecuado para la URL
        data['template'] = data['template'].replace("'", '"')

        response = requests.post(url, headers=headers, data=data)
        return response.text
    


    def enviar_mensaje_code(self,destino,code):


        url = "https://api.gupshup.io/wa/api/v1/template/msg"
        headers = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
            'apikey': 'obg0iystmnq4v0ln4r5fnjcvankhtjp0',
            'cache-control': 'no-cache'
        }
        # Preparar los parámetros del template
        params = [code]
        data = {
            'channel': 'whatsapp',
            'source': '573053447255',
            'destination': f'57{destino}',
            'src.name': 'Salchimonster',
            'template': '{"id":"273c05ca-a79a-46ca-ac1f-b9f75f124367","params":' + str(params) + '}'
        }
        # Convertir la lista params a formato JSON adecuado para la URL
        data['template'] = data['template'].replace("'", '"')

        response = requests.post(url, headers=headers, data=data)
        print(destino,code)
        return response.text
    
        

        
        
    def get_order_count_by_site_id(self,site_id):
        order_query = f"""
        SELECT COUNT(*) FROM orders.orders WHERE site_id = {site_id};
        """
        
        self.cursor.execute(order_query)
        result  = self.cursor.fetchone()[0]

        return result
    

    def get_order_status_by_order_id(self, order_id):
        # Limpieza del order_id para quitar espacios y el caracter #
        clean_order_id = order_id.replace('#', '').strip().lower()
        
        order_query = f"""
        SELECT *
        FROM orders.order_status AS os
        JOIN orders.orders AS o ON os.order_id = o.id
        WHERE LOWER(REPLACE(o.id, '#', '')) = '{clean_order_id}'
        ORDER BY os.timestamp DESC
        LIMIT 1;
        """
        self.cursor.execute(order_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()][0]
    
    
    def is_recent_order_generated(self, site_id):
        # Consulta para verificar si existe algún evento de tipo 1 para la sede especificada en la vista 'recent_events'
        recent_event_query = """
        SELECT id
        FROM public.recent_events
        WHERE event_type_id = 1 AND site_id = %s
        ORDER BY id DESC
        LIMIT 1;
        """
        self.cursor.execute(recent_event_query, (site_id,))
        result = self.cursor.fetchone()
        # Devuelve None si no hay resultados o el timestamp del evento si existe un evento reciente de tipo 1
        return None if result is None else result[0]



    def generate_order_code(self,number_phone, order_id):
        if len(number_phone) < 3:
            raise ValueError("La cadena debe tener al menos 3 caracteres.")

        sampled_numbers = random.sample(number_phone, 3)  # Randomly sample 3 digits from the sequence
        code = ''.join(sampled_numbers)
        query = "INSERT INTO orders.order_code_validation (order_id, code) values (%s, %s) returning order_id"

        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (order_id, code,))
            self.conn.commit()
            self.enviar_mensaje_code(number_phone,code)
            result = cursor.fetchone()
            print(code)
    
    def validate_order_code(self, order_id, code_to_validate):
        query = "SELECT code FROM orders.order_code_validation WHERE order_id = %s"
        
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (order_id,))
            result = cursor.fetchone()
            if result:
                stored_code = result['code']
                if stored_code == code_to_validate:
                    print("Order code validated successfully.")

                    # Eliminar la validación del código de orden
                    delete_validation_query = """
                    DELETE FROM orders.order_code_validation WHERE order_id = %s
                    """
                    cursor.execute(delete_validation_query, (order_id,))
                    
                    # Insertar el estado de la orden
                    order_status_insert_query = """
                    INSERT INTO orders.order_status (order_id, status, timestamp)
                    VALUES (%s, %s, CURRENT_TIMESTAMP)
                    """
                    cursor.execute(order_status_insert_query, (order_id, 'generada'))
                    
                    # Insertar el historial del estado de la orden
                    order_status_history_insert_query = """
                    INSERT INTO orders.order_status_history (order_id, status, timestamp)
                    VALUES (%s, %s, CURRENT_TIMESTAMP)
                    """
                    cursor.execute(order_status_history_insert_query, (order_id, 'generada'))

                    site_id_query = "SELECT site_id from orders.orders where id = %s"
                    cursor.execute(site_id_query,(order_id,))


                    site_id = cursor.fetchone()['site_id']


                    self.create_or_update_event(1, site_id, 1132, '1 minute', False)
                    self.conn.commit()
                    
                    return True
                
                else:
                    print("Invalid order code.")
                    return False
            else:
                print("Order code not found.")
                return False



    def is_recent_cancellation_generated(self):
        # Consulta para verificar si existe algún evento de tipo 1 para la sede especificada en la vista 'recent_events'
        recent_event_query = """
        SELECT id
        FROM public.recent_events
        WHERE event_type_id = 2
        ORDER BY id DESC
        LIMIT 1;
        """
        self.cursor.execute(recent_event_query)
        result = self.cursor.fetchone()
        # Devuelve None si no hay resultados o el timestamp del evento si existe un evento reciente de tipo 1
        return None if result is None else result[0]
    
    def is_recent_pqr_generated(self):
        # Consulta para verificar si existe algún evento de tipo 1 para la sede especificada en la vista 'recent_events'
        recent_event_query = """
        SELECT id
        FROM public.recent_events
        WHERE event_type_id = 7
        ORDER BY id DESC
        LIMIT 1;
        """
        self.cursor.execute(recent_event_query)
        result = self.cursor.fetchone()
        # Devuelve None si no hay resultados o el timestamp del evento si existe un evento reciente de tipo 1
        return None if result is None else result[0]



    def is_recent_pendient_transfers(self):
        # Consulta para verificar si existe algún evento de tipo 1 para la sede especificada en la vista 'recent_events'
        recent_event_query = """
        SELECT id
        FROM public.recent_events
        WHERE event_type_id = 3
        ORDER BY id DESC
        LIMIT 1;
        """
        self.cursor.execute(recent_event_query)
        result = self.cursor.fetchone()
        # Devuelve None si no hay resultados o el timestamp del evento si existe un evento reciente de tipo 1
        return None if result is None else result[0]

        


    def get_orders_by_site_id_for_today(self, site_id):
        # Get today's date in Colombia timezone
         # Get today's date in Colombia timezone
        colombia_tz = pytz.timezone('America/Bogota')
        now = datetime.now(colombia_tz)
        
        # Adjusting start time to 2 AM today
        if now.time() < time(2, 0):
            today_date = (now - timedelta(days=1)).date()
        else:
            today_date = now.date()

        tomorrow_date = today_date + timedelta(days=1)

        # Convert dates to datetime at 2 AM for use in SQL query
        today_start = datetime.combine(today_date, time(2, 0)).astimezone(colombia_tz).isoformat()
        tomorrow_start = datetime.combine(tomorrow_date, time(2, 0)).astimezone(colombia_tz).isoformat()

        # Fetch only today's orders from the combined order view
        combined_order_query = f"""
            SELECT DISTINCT ON (order_id) order_id,inserted_by_id,inserted_by_name, order_notes, delivery_price, payment_method, total_order_price, current_status, latest_status_timestamp, user_name, user_address, user_phone,calcel_sol_state,calcel_sol_asnwer, cancelation_solve_responsible,responsible_observation,authorized,responsible_id,name,pe_json
            FROM orders.combined_order_view
            WHERE site_id = %s AND latest_status_timestamp >= %s AND latest_status_timestamp < %s AND authorized = true
            ORDER BY order_id, latest_status_timestamp DESC;
            """
        self.cursor.execute(combined_order_query, (site_id, today_start, tomorrow_start))
        orders_info = self.cursor.fetchall()
        columns_info = [desc[0] for desc in self.cursor.description]
        orders_dict = [dict(zip(columns_info, row)) for row in orders_info]

        # Convert and format timestamps to Colombia timezone
        for order in orders_dict:
            if 'latest_status_timestamp' in order:
                order['latest_status_timestamp'] = order['latest_status_timestamp'].astimezone(colombia_tz)

        # Fetch additional order details
        for order in orders_dict:
            order_id = order['order_id']

            # Fetch products related to the order
            products_query = f"""
            SELECT name, price, quantity, total_price, product_id, img_identifier
            FROM orders.order_products WHERE order_id = %s;
            """
            self.cursor.execute(products_query, (order_id,))
            products = self.cursor.fetchall()
            products_columns = [desc[0] for desc in self.cursor.description]
            order['products'] = [dict(zip(products_columns, row)) for row in products]

            # Fetch additional items related to the order
            additionals_query = f"""
            SELECT 
            aditional_name,
            aditional_quantity,
            aditional_type,
            aditional_price,
            total_aditional_price
            FROM orders.vw_order_aditional_items WHERE order_id = %s;
            """
            self.cursor.execute(additionals_query, (order_id,))
            additionals = self.cursor.fetchall()
            additionals_columns = [desc[0] for desc in self.cursor.description]

            # Group additional items by type
            grouped_additionals = {}
            for row in additionals:
                additional = dict(zip(additionals_columns, row))
                additional_type = additional['aditional_type']
                if additional_type not in grouped_additionals:
                    grouped_additionals[additional_type] = [additional]
                else:
                    grouped_additionals[additional_type].append(additional)

            order['additional_items'] = grouped_additionals

        return orders_dict
    




    def get_orders_to_transfer(self):
        colombia_tz = pytz.timezone('America/Bogota')
        now = datetime.now(colombia_tz)
        
        # Ajuste para empezar desde las 2 AM de hoy
        if now.time() < time(2, 0):
            today_date = (now - timedelta(days=1)).date()
        else:
            today_date = now.date()

        tomorrow_date = today_date + timedelta(days=1)

        # Convertir fechas a datetime a las 2 AM para usar en la consulta SQL
        today_start = datetime.combine(today_date, time(2, 0)).astimezone(colombia_tz).isoformat()
        tomorrow_start = datetime.combine(tomorrow_date, time(2, 0)).astimezone(colombia_tz).isoformat()

        # Consulta para obtener las órdenes de hoy desde la vista combinada de órdenes
        combined_order_query = """
            SELECT DISTINCT ON (order_id) order_id, order_notes, delivery_price, payment_method, 
            total_order_price, current_status, latest_status_timestamp, user_name, user_address, 
            user_phone, calcel_sol_state, calcel_sol_asnwer, cancelation_solve_responsible, 
            responsible_observation, pe_json
            FROM orders.combined_order_view

            WHERE 
                latest_status_timestamp >= %s 
                AND latest_status_timestamp < %s 
                AND authorized = false  AND current_status = 'transferencia pendiente'
            ORDER BY order_id, latest_status_timestamp DESC;
            """
        self.cursor.execute(combined_order_query, (today_start, tomorrow_start))
        orders_info = self.cursor.fetchall()
        columns_info = [desc[0] for desc in self.cursor.description]
        orders_dict = [dict(zip(columns_info, row)) for row in orders_info]

        # Convertir y formatear los timestamps a la zona horaria de Colombia
        for order in orders_dict:
            if 'latest_status_timestamp' in order:
                order['latest_status_timestamp'] = order['latest_status_timestamp'].astimezone(colombia_tz)

        # Obtener detalles adicionales de la orden
        for order in orders_dict:
            order_id = order['order_id']

            # Consultar productos relacionados con la orden
            products_query = """
            SELECT name, price, quantity, total_price, product_id 
            FROM orders.order_products WHERE order_id = %s;
            """
            self.cursor.execute(products_query, (order_id,))
            products = self.cursor.fetchall()
            products_columns = [desc[0] for desc in self.cursor.description]
            order['products'] = [dict(zip(products_columns, row)) for row in products]

            # Consultar ítems adicionales relacionados con la orden
            additionals_query = """
            SELECT aditional_name, aditional_quantity, aditional_type, aditional_price, 
            total_aditional_price
            FROM orders.vw_order_aditional_items WHERE order_id = %s;
            """
            self.cursor.execute(additionals_query, (order_id,))
            additionals = self.cursor.fetchall()
            additionals_columns = [desc[0] for desc in self.cursor.description]

            # Agrupar ítems adicionales por tipo
            grouped_additionals = {}
            for row in additionals:
                additional = dict(zip(additionals_columns, row))
                additional_type = additional['aditional_type']
                if additional_type not in grouped_additionals:
                    grouped_additionals[additional_type] = [additional]
                else:
                    grouped_additionals[additional_type].append(additional)

            order['additional_items'] = grouped_additionals

        # Ordenar las órdenes por latest_status_timestamp en orden descendente (más recientes primero)
        orders_dict.sort(key=lambda x: x['latest_status_timestamp'], reverse=True)

        return orders_dict





    def get_order_by_id(self, order_id):
        # Limpieza del order_id para quitar espacios y el caracter #, y convertir a minúsculas
        clean_order_id = order_id.replace('#', '').strip().lower()

        # Fetch the specific order from the combined order view
        order_query = f"""
        SELECT DISTINCT ON (order_id) order_id,site_id,responsible,reason, order_notes, delivery_price, payment_method, total_order_price, current_status, latest_status_timestamp, user_name, user_address, user_phone, calcel_sol_state, calcel_sol_asnwer, cancelation_solve_responsible, responsible_observation, responsible_id,name,pe_json
        FROM orders.combined_order_view
        WHERE LOWER(REPLACE(order_id, '#', '')) = %s
        ORDER BY order_id, latest_status_timestamp DESC
        LIMIT 1;
        """
        self.cursor.execute(order_query, (clean_order_id,))
        order_info = self.cursor.fetchone()

        if not order_info:
            return None  # Order not found

        columns_info = [desc[0] for desc in self.cursor.description]
        order_dict = dict(zip(columns_info, order_info))

        # Fetch products related to the order
        products_query = f"""
        SELECT name, price, quantity, total_price, product_id
        FROM orders.order_products WHERE LOWER(REPLACE(order_id, '#', '')) = %s;
        """
        self.cursor.execute(products_query, (clean_order_id,))
        products = self.cursor.fetchall()
        products_columns = [desc[0] for desc in self.cursor.description]
        order_dict['products'] = [dict(zip(products_columns, row)) for row in products]

        # Fetch additional items related to the order
        additionals_query = f"""
        SELECT 
        aditional_name,
        aditional_quantity,
        aditional_type,
        aditional_price,
        total_aditional_price
        FROM orders.vw_order_aditional_items WHERE LOWER(REPLACE(order_id, '#', '')) = %s;
        """
        self.cursor.execute(additionals_query, (clean_order_id,))
        additionals = self.cursor.fetchall()
        additionals_columns = [desc[0] for desc in self.cursor.description]

        # Group additional items by type
        grouped_additionals = {}
        for row in additionals:
            additional = dict(zip(additionals_columns, row))
            additional_type = additional['aditional_type']
            if additional_type not in grouped_additionals:
                grouped_additionals[additional_type] = [additional]
            else:
                grouped_additionals[additional_type].append(additional)

        order_dict['additional_items'] = grouped_additionals

        return order_dict


    def get_order_by_user_phone(self, user_phone):
        # Limpieza del order_id para quitar espacios y el caracter #, y convertir a minúsculas
        clean_order_id = user_phone.replace('#', '').strip().lower()

        # Fetch the specific order from the combined order view
        order_query = f"""
        SELECT DISTINCT ON (order_id) order_id,site_id,responsible,reason, order_notes, delivery_price, payment_method, total_order_price, current_status, latest_status_timestamp, user_name, user_address, user_phone, calcel_sol_state, calcel_sol_asnwer, cancelation_solve_responsible, responsible_observation, responsible_id,name
        FROM orders.combined_order_view
        WHERE user_phone = '{user_phone}'
        ORDER BY order_id DESC
        LIMIT 1;
        """
        self.cursor.execute(order_query)
        order_info = self.cursor.fetchone()

        if not order_info:
            return None  # Order not found

        columns_info = [desc[0] for desc in self.cursor.description]
        order_dict = dict(zip(columns_info, order_info))

        # Fetch products related to the order
        products_query = f"""
        SELECT name, price, quantity, total_price, product_id
        FROM orders.order_products WHERE LOWER(REPLACE(order_id, '#', '')) = %s;
        """
        self.cursor.execute(products_query, (clean_order_id,))
        products = self.cursor.fetchall()
        products_columns = [desc[0] for desc in self.cursor.description]
        order_dict['products'] = [dict(zip(products_columns, row)) for row in products]

        # Fetch additional items related to the order
        additionals_query = f"""
        SELECT 
        aditional_name,
        aditional_quantity,
        aditional_type,
        aditional_price,
        total_aditional_price
        FROM orders.vw_order_aditional_items LOWER(REPLACE(order_id, '#', '')) = %s
        """
        self.cursor.execute(additionals_query, (clean_order_id,))
        additionals = self.cursor.fetchall()
        additionals_columns = [desc[0] for desc in self.cursor.description]

        # Group additional items by type
        grouped_additionals = {}
        for row in additionals:
            additional = dict(zip(additionals_columns, row))
            additional_type = additional['aditional_type']
            if additional_type not in grouped_additionals:
                grouped_additionals[additional_type] = [additional]
            else:
                grouped_additionals[additional_type].append(additional)

        order_dict['additional_items'] = grouped_additionals

        return order_dict

        
    def mark_events_as_solved_by_site_id(self, site_id):
        """
        Marca todos los eventos no resueltos para un site_id específico como resueltos.
        Args:
            site_id (int): ID del sitio para resolver todos los eventos asociados.
        """
        update_event_query = """
        UPDATE events
        SET solved = TRUE
        WHERE site_id = %s AND solved = FALSE and event_type_id = 1;
        """
        self.cursor.execute(update_event_query, (site_id,))
        affected_rows = self.cursor.rowcount  # Número de filas afectadas
        self.conn.commit()
        return affected_rows
        
        
    
    def prepare_order(self, order_id):
    # Prepara la orden
        prepare_query = """
        INSERT INTO orders.order_status (order_id, status, timestamp)
        VALUES (%s, 'en preparacion', CURRENT_TIMESTAMP);
        """
        self.cursor.execute(prepare_query, (order_id,))

        # Inserta el historial del estado
        history_query = """
        INSERT INTO orders.order_status_history (order_id, status, timestamp)
        VALUES (%s, 'en preparacion', CURRENT_TIMESTAMP);
        """
        self.cursor.execute(history_query, (order_id,))

        get_site_id_query = """
        SELECT site_id FROM orders.orders
        WHERE id = %s;
        """
        self.cursor.execute(get_site_id_query, (order_id,))
        site_id_result = self.cursor.fetchone()
        site_id = site_id_result[0]

        self.mark_events_as_solved_by_site_id(site_id)
        
         # Selecciona el JSON de la orden
        select_order_query = """
        SELECT pe_json
        FROM orders.orders
        WHERE id = %s;
        """
        self.cursor.execute(select_order_query, (order_id,))
        order_json = self.cursor.fetchone()

        if not order_json:
            raise ValueError(f"No se encontró JSON para la orden con ID {order_id}")

 
        delivery_response = self.registrar_delivery(order_json[0])

        print(delivery_response)
        if isinstance(delivery_response, dict):
            print("Delivery enviado con éxito:", delivery_response)
        else:
            print("Error al enviar el delivery:", delivery_response)



        self.conn.commit()

    def cancel_order(self, order_id, responsible, reason):
        # Cancela la orden
        cancel_query = """
        INSERT INTO orders.order_status (order_id, status, reason, responsible, timestamp)
        VALUES (%s, 'cancelada', %s, %s, CURRENT_TIMESTAMP);
        """
        self.cursor.execute(cancel_query, (order_id, reason, responsible))
        
        # Inserta el historial del estado
        history_query = """
        INSERT INTO orders.order_status_history (order_id, status, reason, responsible, timestamp)
        VALUES (%s, 'cancelada', %s, %s, CURRENT_TIMESTAMP);
        """
        self.cursor.execute(history_query, (order_id, reason, responsible))
        self.conn.commit()
            
    def send_order(self, order_id):
        """
        Actualiza el estado de una orden a 'enviada', registra el historial,
        y envía los datos de la orden como delivery.
        
        Args:
            order_id (int): ID de la orden a procesar.
        """
        # Actualiza el estado de la orden a 'enviada'
        send_order_query = """
        INSERT INTO orders.order_status (order_id, status, timestamp)
        VALUES (%s, 'enviada', CURRENT_TIMESTAMP);
        """
        self.cursor.execute(send_order_query, (order_id,))

        # Inserta el historial del estado
        order_status_history_insert_query = """
        INSERT INTO orders.order_status_history (order_id, status, timestamp)
        VALUES (%s, 'enviada', CURRENT_TIMESTAMP);
        """
        self.cursor.execute(order_status_history_insert_query, (order_id,))

        
        self.conn.commit()
  
  
    def update_product_instance_status(self, product_instance_id, new_status):
        """
        Update the status of a specific product instance.
        Parameters:
        - product_instance_id: int or str, the identifier of the product instance.
        - new_status: str, the new status to set for the product instance.
        """
        update_query = """
        UPDATE inventory.product_instances
        SET status = %s
        WHERE id = %s;
        """
        self.cursor.execute(update_query, (new_status, product_instance_id))
        self.conn.commit()


    def registrar_delivery(self, data):
        """
        Realiza una solicitud POST para registrar un delivery.

        Args:
            dominio_id (int): ID del dominio.
            local_id (int): ID del local.
            data (dict): Datos a enviar en el cuerpo de la solicitud.

        Returns:
            dict: La respuesta del servidor si es exitosa.
            str: Mensaje de error si ocurre algún problema.
        """
        # Construcción de la URL con los parámetros
        url = f"https://api.restaurant.pe/restaurant/public/v2/rest/delivery/registrarDelivery/6149"

        # Encabezados
        headers = {
            "Authorization": f'Token token="{TOKEN}"',
            "Content-Type": "application/json"
        }

        try:
            # Enviar la solicitud POST
            response = requests.post(url, headers=headers, json=data)

            # Manejo de la respuesta
            if response.status_code == 200:
                print(response.json)
                return response.json()
            else:
                return f"Error {response.status_code}: {response.text}"
        except Exception as e:
            return f"Excepción durante la solicitud: {str(e)}"


    def authorize_order(self, order_id, responsible_id):
        """
        Authorize an order and update the responsible person.
        
        Args:
            order_id (int): The ID of the order to authorize.
            responsible_id (int): The ID of the responsible person authorizing the order.
        
        Returns:
            dict: A dictionary with the order_id and a confirmation message.
        """
        try:
            # Update the authorized status of the order
            update_authorization_query = """
            UPDATE orders.orders
            SET authorized = TRUE, responsible_id = %s
            WHERE id = %s;
            """
            self.cursor.execute(update_authorization_query, (responsible_id, order_id))
            
            # Insert a record into the order status history to reflect this change
            order_status_history_insert_query = """
            INSERT INTO orders.order_status (order_id, status, timestamp)
            VALUES (%s, 'generada', CURRENT_TIMESTAMP);
            """
            self.cursor.execute(order_status_history_insert_query, (order_id,))
            
            # Commit the transaction

            get_site_id_query = """
            SELECT site_id FROM orders.orders
            WHERE id = %s;
            """
            self.cursor.execute(get_site_id_query, (order_id,))
            site_id_result = self.cursor.fetchone()
            site_id = site_id_result[0]
            self.create_or_update_event(1, site_id, 1132, '1 minute', False)
            self.conn.commit()

            return {"order_id": order_id, "message": "Order authorized successfully"}
        except Exception as e:
            self.conn.rollback()
            return {"order_id": order_id, "message": f"Failed to authorize order: {str(e)}"}

        
    def can_place_order(self, user_id):
        query = """
        SELECT last_order_time
        FROM orders.user_last_order_time
        WHERE user_id = %s;
        """
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        if result:
            last_order_time = result[0]
            # Define la zona horaria de Colombia
            colombia_tz = pytz.timezone('America/Bogota')
            now_colombia = datetime.now(colombia_tz)
            elapsed_time = now_colombia - last_order_time
            # Verificar si han pasado al menos 30 segundos
            return elapsed_time.total_seconds() > 20
        else:
            # Si no hay registro previo, el usuario puede realizar una orden
            return True
        
 
    def update_last_order_time(self, user_id):
        # Define la zona horaria de Colombia
        colombia_tz = pytz.timezone('America/Bogota')
        now_colombia = datetime.now(colombia_tz)

        query = """
        UPDATE orders.user_last_order_time
        SET last_order_time = %s
        WHERE user_id = %s;
        """
        self.cursor.execute(query, (now_colombia, user_id))
        if self.cursor.rowcount == 0:  # Si no existía un registro previo
            insert_query = """
            INSERT INTO orders.user_last_order_time (user_id, last_order_time)
            VALUES (%s, %s);
            """
            self.cursor.execute(insert_query, (user_id, now_colombia))

        
    def close_connection(self):
        self.conn.close()


