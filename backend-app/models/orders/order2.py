from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.city import citySchema
# from schema.order import OrderSchemaPost
from schema.order import OrderSchemaPost
from models.user import User
from schema.user import user_schema_post
from datetime import datetime, timedelta
from datetime import datetime, timedelta

import pytz
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


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
            self.insert_order_details(order_id, order_data)
            self.insert_order_products(order_id, order_data)
            self.insert_order_aditionals(order_id, order_data)
            self.update_order_status(order_id, order_data.order_status)
            self.insert_order_notes(order_id,order_data.order_notes)
            # Actualizar la última hora de compra
            self.update_last_order_time(user_id)
            self.conn.commit()
            return order_id
        else:
            
            last_order_query = f"SELECT id FROM orders.orders where user_id = {user_id} ORDER BY id DESC LIMIT 1;"
            self.cursor.execute(last_order_query)
            order_id = self.cursor.fetchone()[0]   
            return order_id
            
            
            
            

    def create_user(self, user_data):
        user_id = User().insert_user(user_data)
        return user_id

    def create_order_entry(self, user_id, order_data):
        order_insert_query = """
        INSERT INTO orders.orders (user_id, site_id, delivery_person_id)
        VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(order_insert_query, (user_id, order_data.site_id, order_data.delivery_person_id))
        order_id = self.cursor.fetchone()[0]
        return order_id

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

    def update_order_status(self, order_id, order_status):
        
        # Define la zona horaria de Colombia
        colombia_tz = pytz.timezone('America/Bogota')
        
        # Obtiene la fecha y hora actual en la zona horaria de Colombia
        now_colombia = datetime.now(colombia_tz)
        
        # Consulta para insertar el estado de la orden
        order_status_insert_query = """
        INSERT INTO orders.order_status (order_id, status,timestamp)
        VALUES (%s, %s,CURRENT_TIMESTAMP );
        """
        self.cursor.execute(order_status_insert_query, (order_id, 'generada',))
        
        # Consulta para insertar el historial del estado de la orden
        order_status_history_insert_query = """
        INSERT INTO orders.order_status_history (order_id, status,timestamp)
        VALUES (%s, %s,CURRENT_TIMESTAMP );
        """
        self.cursor.execute(order_status_history_insert_query, (order_id, 'generada',))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def get_order_count_by_site_id(self,site_id):
        order_query = f"""
        SELECT COUNT(*) FROM orders.orders WHERE site_id = {site_id};
        """
        
        self.cursor.execute(order_query)
        result  = self.cursor.fetchone()[0]

        return result
        
    
    def is_recent_order_generated(self, site_id):
    # Consulta para obtener el ID de la última orden con estado 'generada' en los últimos 3 segundos usando la hora del servidor UTC
        recent_order_query = """
        SELECT order_id
        FROM (
            SELECT os.order_id, os.status, os.timestamp,
                ROW_NUMBER() OVER (PARTITION BY os.order_id ORDER BY os.timestamp DESC) AS rn
            FROM orders.order_status os
            JOIN orders.orders o ON os.order_id = o.id
            WHERE o.site_id = %s AND os.status = 'generada'
        ) AS latest_status
        WHERE latest_status.rn = 1 AND latest_status.timestamp >= (CURRENT_TIMESTAMP - INTERVAL '30 seconds')
        ORDER BY latest_status.timestamp DESC
        LIMIT 1;
        """
        self.cursor.execute(recent_order_query, (site_id,))
        result = self.cursor.fetchone()
        # Devuelve None si no hay resultados o el ID de la orden si existe una reciente con estado 'generada'
        return None if result is None else result[0]
                

    


    def get_orders_by_site_id_for_today(self, site_id):
        # Get today's date in Colombia timezone
        colombia_tz = pytz.timezone('America/Bogota')
        today_date = datetime.now(colombia_tz).date()
        tomorrow_date = today_date + timedelta(days=1)

        # Convert dates to datetime at midnight for use in SQL query
        today_start = datetime.combine(today_date, datetime.min.time()).astimezone(colombia_tz).isoformat()
        tomorrow_start = datetime.combine(tomorrow_date, datetime.min.time()).astimezone(colombia_tz).isoformat()

        # Fetch only today's orders from the combined order view
        combined_order_query = f"""
            SELECT DISTINCT ON (order_id) order_id, order_notes, delivery_price, payment_method, total_order_price, current_status, latest_status_timestamp, user_name, user_address, user_phone
            FROM orders.combined_order_view
            WHERE site_id = %s AND latest_status_timestamp >= %s AND latest_status_timestamp < %s
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
            SELECT name, price, quantity, total_price, product_id 
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


