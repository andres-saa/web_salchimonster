import psycopg2
from dotenv import load_dotenv
import os
import json
import locale
from datetime import datetime, timedelta
import pytz
from datetime import datetime
from schema.order import order_schema_post
from datetime import datetime, timedelta
import requests

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class Order:
    def __init__(self, order_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.order_id = order_id

    def select_order_by_id(self, order_id):
        select_query = "SELECT * FROM orders WHERE order_id = %s ORDER BY order_id DESC LIMIT 50;"
        self.cursor.execute(select_query, (order_id,))
        columns = [desc[0] for desc in self.cursor.description]
        result = self.cursor.fetchone()
        if result:
            return dict(zip(columns, result))
        else:
            return None
            
    def select_all_orders(self):
        select_query = "SELECT * FROM orders ORDER BY order_id DESC LIMIT 50;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def select_orders_by_site_id(self, site_id):
            select_query = "SELECT * FROM orders WHERE site_id = %s ORDER BY order_id DESC LIMIT 50;"
            self.cursor.execute(select_query, (site_id,))
            columns = [desc[0] for desc in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_sales_report_by_site_and_status(self, site_ids, status, start_date, end_date):
        # Define the time zones
        tz_colombia = pytz.timezone('America/Bogota')
        tz_utc = pytz.utc

        # Check if the dates are datetime objects, if not, convert from string
        


        start_date_utc = start_date
        end_date_utc = end_date
        # Convert start_date and end_date from Colombia to UTC
       
        # # Adjust end_date_utc to include the entire last day
        # end_date_utc += timedelta(days=0)

        # if not isinstance(site_ids, list):
        #     site_ids = [site_ids]

        query = """
        SELECT
            SUM(co.total_order_price) AS total_sales,
            COUNT(co.order_id) AS total_orders,
            CAST(
                AVG(co.total_order_price)
                AS NUMERIC
            ) AS average_ticket,
            COALESCE(
                JSON_AGG(
                    JSON_BUILD_OBJECT(
                        'order_id', co.order_id,
                        'user_id', co.user_id,
                        'site_name', co.site_name,
                        'delivery_person_id', co.delivery_person_id,
                        'order_notes', co.order_notes,
                        'delivery_price', co.delivery_price,
                        'payment_method', co.payment_method,
                        'total_order_price', co.total_order_price,
                        'current_status', co.current_status,
                        'latest_status_timestamp', co.latest_status_timestamp,
                        'responsible', co.responsible,
                        'reason', co.reason,
                        'user_name', co.user_name,
                        'user_address', co.user_address,
                        'user_phone', co.user_phone
                    ) ORDER BY co.order_id
                ), '[]') AS orders_info
        FROM
            orders.combined_order_view co
        WHERE
        co.latest_status_timestamp BETWEEN %s AND %s
        AND co.site_id = ANY(%s)
        AND co.current_status = %s
        """

        self.cursor.execute(query, (start_date_utc, end_date_utc, site_ids, status))
        
        # print("start",start_date_utc.isoformat())
        # print("end",end_date_utc.isoformat())
        result = self.cursor.fetchone()

        if result:
            total_sales, total_orders, average_ticket, orders_info_json = result
            if average_ticket:
                average_ticket = round(average_ticket)  # Round the average ticket

            # Convert timestamp to Colombia time zone (UTC-5)
            orders_info = []
            for order in orders_info_json:
                timestamp_utc = datetime.fromisoformat(order['latest_status_timestamp'].replace("Z", "+00:00"))
                timestamp_colombia = timestamp_utc.astimezone(tz_colombia)
                order['latest_status_timestamp'] = timestamp_colombia.isoformat()
                orders_info.append(order)
        else:
            total_sales = total_orders = average_ticket = 0
            orders_info = []

        return {
            'total_sales': total_sales,
            'total_orders': total_orders,
            'average_ticket': average_ticket,
            'orders_info': orders_info
        }

    
    def get_daily_orders_report(self, site_ids, status, start_date, end_date):
        if not isinstance(site_ids, list):
            site_ids = [site_ids]

        tz_colombia = pytz.timezone('America/Bogota')
        tz_utc = pytz.utc

        # Check if the dates are datetime objects, if not, convert from string
        


        start_date_utc = start_date
        end_date_utc = end_date

        # Preparar la consulta SQL
        query = """
        SELECT
            DATE(order_date ) AS local_order_date,
            SUM(total_orders) AS total_orders
        FROM
            orders.daily_order_status_count_view
        WHERE
            order_date BETWEEN %s AND %s
            AND site_id = ANY(%s)
            AND current_status = %s
        GROUP BY
            local_order_date
        ORDER BY
            local_order_date;
        """

        # Ajuste para sumar un día adicional en la fecha final
        end_date_adjusted = end_date_utc 

        self.cursor.execute(query, (start_date_utc, end_date_adjusted, site_ids, status))
        results = self.cursor.fetchall()

        # Crear un diccionario de todos los días en el rango
        daily_report = {}
        # current_date = start_date
        # while current_date <= end_date:
        #     formatted_date = current_date.strftime("%a-%d-%b").lower().replace('.', '')
        #     daily_report[formatted_date] = 0.0
        #     current_date += timedelta(days=1)

        # Actualizar con los resultados reales
        for result in results:
            formatted_date = result[0].strftime("%a-%d-%b").lower().replace('.', '')
            daily_report[formatted_date] = float(result[1])

        # Convertir el diccionario a una lista de diccionarios como se especificó
        formatted_daily_report = [{date: orders} for date, orders in daily_report.items()]

        return formatted_daily_report


    def get_sales_report_by_site(self, site_ids, start_date, end_date):
        tz_colombia = pytz.timezone('America/Bogota')
        tz_utc = pytz.utc

        # Check if the dates are datetime objects, if not, convert from string
        start_date_utc = start_date
        end_date_utc = end_date

        # Preparar la consulta SQL
        query = """
        SELECT
            site_id,
            site_name,
            SUM(CASE WHEN current_status = 'enviada' THEN total_sales ELSE 0 END) AS total_sales_sent,
            SUM(CASE WHEN current_status = 'cancelada' THEN total_sales ELSE 0 END) AS total_sales_cancelled,
            SUM(CASE WHEN current_status = 'enviada' THEN total_orders ELSE 0 END) AS total_orders_sent,
            SUM(CASE WHEN current_status = 'cancelada' THEN total_orders ELSE 0 END) AS total_orders_cancelled
        FROM
            orders.daily_order_sales_view
        WHERE
            (order_date at time zone 'America/Bogota')  BETWEEN %s AND %s
            AND site_id = ANY(%s)
        GROUP BY
            ROLLUP((site_id, site_name))
        ORDER BY
            site_id;
        """

        self.cursor.execute(query, (start_date_utc, end_date_utc, site_ids))
        results = self.cursor.fetchall()

        sales_report = []
        for result in results:
            report = {
                'site_id': result[0] if result[0] is not None else 'TOTAL',
                'site_name': result[1] if result[1] is not None else 'TOTAL',
                'total_sales_sent': float(result[2]) if result[2] is not None else 0,
                'total_sales_cancelled': float(result[3]) if result[3] is not None else 0,
                'total_orders_sent': int(result[4]) if result[4] is not None else 0,
                'total_orders_cancelled': int(result[5]) if result[5] is not None else 0
            }
            sales_report.append(report)

        
        
        return sales_report














    def enviar_mensaje_template(self, destino, params):
        url = "https://api.gupshup.io/wa/api/v1/template/msg"
        headers = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
            'apikey': 'obg0iystmnq4v0ln4r5fnjcvankhtjp0',
            'cache-control': 'no-cache'
        }
        # Asegurarse de que los parámetros están en el formato correcto para el JSON
        json_params = str(params).replace("'", '"')
        data = {
            'channel': 'whatsapp',
            'source': '573053447255',
            'destination': destino,
            'src.name': 'Salchimonster',
            'template': '{"id":"03930a95-275d-42c1-b295-72a6d364666b","params":' + json_params + '}'
        }

        response = requests.post(url, headers=headers, data=data)
        return response.text










    def get_daily_sales_report(self, site_ids, status, start_date, end_date):
    # Asegurarse de que site_ids es una lista
        if not isinstance(site_ids, list):
            site_ids = [site_ids]

        # Definir las zonas horarias
        tz_colombia = pytz.timezone('America/Bogota')
        tz_utc = pytz.utc

        # Check if the dates are datetime objects, if not, convert from string
        


        start_date_utc = start_date
        end_date_utc = end_date

        # Preparar la consulta SQL
        query = """
        SELECT
            DATE(order_date) AS local_order_date,
            SUM(total_sales) AS total_sales
        FROM
            orders.daily_order_sales_view
        WHERE
            order_date BETWEEN %s AND %s
            AND site_id = ANY(%s)
            AND current_status = %s
        GROUP BY
            local_order_date
        ORDER BY
            local_order_date;
        """

        # Ajuste para sumar un día adicional en la fecha final
        end_date_adjusted = end_date_utc

        self.cursor.execute(query, (start_date_utc, end_date_adjusted, site_ids, status))
        results = self.cursor.fetchall()

        # Crear un diccionario de todos los días en el rango
        daily_sales = {}
       

        # Actualizar con los resultados reales
        for result in results:
            formatted_date = result[0].strftime("%a-%d-%b").lower().replace('.', '')
            daily_sales[formatted_date] = float(result[1])

        # Convertir el diccionario a una lista de diccionarios como se especificó
        formatted_daily_sales = [{date: sales} for date, sales in daily_sales.items()]

        return formatted_daily_sales


    def get_daily_average_ticket(self, site_ids, status, start_date, end_date):
        if not isinstance(site_ids, list):
            site_ids = [site_ids]

        # Definir las zonas horarias
        tz_colombia = pytz.timezone('America/Bogota')
        tz_utc = pytz.utc

        # Check if the dates are datetime objects, if not, convert from string
        


        start_date_utc = start_date
        end_date_utc = end_date

        # Preparar la consulta SQL
        query = """
        SELECT
            order_date,
            average_ticket
        FROM
            orders.daily_average_ticket_view
        WHERE
            order_date BETWEEN %s AND %s
            AND site_id = ANY(%s)
            AND current_status = %s
        ORDER BY
            order_date;
        """

        self.cursor.execute(query, (start_date_utc, end_date_utc, site_ids, status))
        results = self.cursor.fetchall()

        # Crear un diccionario de todos los días en el rango
        daily_average_ticket = {}
        current_date = start_date
       

        # Actualizar con los resultados reales
        for result in results:
            formatted_date = result[0].strftime("%a-%d-%b").lower().replace('.', '')
            daily_average_ticket[formatted_date] = float(result[1])

        # Convertir el diccionario a una lista de diccionarios como se especificó
        formatted_daily_average_ticket = [{date: round(ticket, 0)} for date, ticket in daily_average_ticket.items()]

        return formatted_daily_average_ticket























    def select_orders_by_delivery_person(self, delivery_person_id):
        select_query = "SELECT * FROM orders WHERE delivery_person_id = %s ORDER BY order_id DESC LIMIT 50;"
        self.cursor.execute(select_query, (delivery_person_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def select_orders_by_user(self, user_id):
        select_query = "SELECT * FROM orders WHERE user_id = %s ORDER BY order_id DESC LIMIT 50;"
        self.cursor.execute(select_query, (user_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def delete_order(self, order_id):
        delete_query = "DELETE FROM orders WHERE order_id = %s;"
        self.cursor.execute(delete_query, (order_id,))
        self.conn.commit()

    def create_order(self, order_data: order_schema_post):
        insert_query = """
        INSERT INTO orders (order_products, user_id, site_id, order_status, payment_method, delivery_person_id, status_history, delivery_price, order_notes, user_data)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;
        """
        self.cursor.execute(insert_query, (
            json.dumps(order_data.order_products),
            order_data.user_id,
            order_data.site_id,
            json.dumps(order_data.order_status),
            order_data.payment_method,
            order_data.delivery_person_id,
            json.dumps(order_data.status_history),
            order_data.delivery_price,
            order_data.order_notes,
            json.dumps(order_data.user_data)  # Asegúrate de serializar el user_data
        ))
        self.conn.commit()
        columns = [desc[0] for desc in self.cursor.description]
        updated_order_id = dict(zip(columns, self.cursor.fetchone()))["order_id"]

        return updated_order_id     
    
    def update_order(self, order_id: int, order_data: order_schema_post):
        update_query = """
        UPDATE orders 
        SET 
            order_products = COALESCE(%s, order_products),
            user_id = COALESCE(%s, user_id),
            site_id = COALESCE(%s, site_id),
            order_status = COALESCE(%s, order_status),
            payment_method = COALESCE(%s, payment_method),
            delivery_person_id = COALESCE(%s, delivery_person_id),
            status_history = COALESCE(%s, status_history),
            delivery_price = COALESCE(%s, delivery_price),
            order_notes = COALESCE(%s, order_notes),
            user_data = COALESCE(%s, user_data)  
        WHERE order_id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            json.dumps(order_data.order_products) if order_data.order_products is not None else None,
            order_data.user_id if order_data.user_id is not None else None,
            order_data.site_id if order_data.site_id is not None else None,
            json.dumps(order_data.order_status) if order_data.order_status is not None else None,
            order_data.payment_method if order_data.payment_method is not None else None,
            order_data.delivery_person_id if order_data.delivery_person_id is not None else None,
            json.dumps(order_data.status_history) if order_data.status_history is not None else None,
            order_data.delivery_price if order_data.delivery_price is not None else None,
            order_data.order_notes if order_data.order_notes is not None else None,
            json.dumps(order_data.user_data) if order_data.user_data is not None else None,  # Asegúrate de serializar el user_data
            order_id
        ))
        self.conn.commit()
        columns = [desc[0] for desc in self.cursor.description]
        updated_order = dict(zip(columns, self.cursor.fetchone()))
        return updated_order

    def close_connection(self):
        self.conn.close()
    def close_connection(self):
        self.conn.close()


