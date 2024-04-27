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

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

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
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Convert start_date and end_date from Colombia to UTC
        start_date_utc = tz_colombia.localize(start_date).astimezone(tz_utc)
        end_date_utc = tz_colombia.localize(end_date).astimezone(tz_utc)

        # Adjust end_date_utc to include the entire last day
        end_date_utc += timedelta(days=0)

        if not isinstance(site_ids, list):
            site_ids = [site_ids]

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
            co.latest_status_timestamp >= %s AND
            co.latest_status_timestamp < %s AND
            co.site_id = ANY(%s) AND
            co.current_status = %s
        """

        self.cursor.execute(query, (start_date_utc.isoformat(), end_date_utc.isoformat(), site_ids, status))
        
        print("start",start_date_utc.isoformat())
        print("end",end_date_utc.isoformat())
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

    def get_daily_sales_report(self, site_ids, status, start_date, end_date):
        # Asegurarse de que site_ids es una lista
        if not isinstance(site_ids, list):
            site_ids = [site_ids]

        # Configurar la localidad para las fechas en español
        try:
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Unix/Linux
            # locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Windows
        except locale.Error:
            raise Exception("No se pudo configurar la localidad a español. Asegúrate de que 'es_ES.UTF-8' esté instalada en tu sistema.")

        # Definir las zonas horarias
        tz_colombia = pytz.timezone('America/Bogota')
        tz_utc = pytz.utc

        # Comprobar si las fechas son objetos datetime, si no, convertirlas desde string
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Convertir las fechas de Colombia a UTC
        start_date_utc = tz_colombia.localize(start_date).astimezone(tz_utc)
        end_date_utc = tz_colombia.localize(end_date + timedelta(days=1)).astimezone(tz_utc)  # Incluir todo el último día

        consulta = """
        WITH rango_fechas AS (
            SELECT generate_series(%s::timestamp, %s::timestamp, '1 day'::interval) AS fecha
        ), conteo_ordenes AS (
            SELECT
                DATE(co.latest_status_timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'America/Bogota') AS fecha_orden,
                COUNT(*) AS num_ordenes
            FROM
                orders.combined_order_view co
            WHERE
                co.latest_status_timestamp AT TIME ZONE 'UTC' BETWEEN %s AND %s AND
                co.site_id = ANY(%s) AND
                co.current_status = %s
            GROUP BY
                fecha_orden
        )
        SELECT
            d.fecha AS fecha_orden,
            COALESCE(oc.num_ordenes, 0) AS num_ordenes
        FROM
            rango_fechas d
        LEFT JOIN conteo_ordenes oc ON
            d.fecha = oc.fecha_orden
        ORDER BY
            d.fecha;
        """

        self.cursor.execute(consulta, (start_date_utc, end_date_utc, start_date_utc, end_date_utc, site_ids, status))
        resultados = self.cursor.fetchall()
        print("Fecha de inicio UTC:", start_date_utc.isoformat())
        print("Fecha de fin UTC:", end_date_utc.isoformat())
        print("IDs de sitio:", site_ids)
        print("Estado:", status)

        self.cursor.execute(consulta, (start_date_utc, end_date_utc, start_date_utc, end_date_utc, site_ids, status))
        resultados = self.cursor.fetchall()
        print("Resultados obtenidos:", resultados)

        # Formatear los resultados para la salida
        ventas_diarias = []
        for resultado in resultados:
            fecha_formateada = resultado[0].strftime("%a-%d-%b").replace('.', '')
            num_ordenes = resultado[1]
            ventas_diarias.append({fecha_formateada: num_ordenes})

        return ventas_diarias

        return ventas_diarias
    
    def get_daily_orders_report(self, site_ids, status, start_date,  end_date):
        # Convertir site_ids en una lista si solo se proporciona un ID
        if not isinstance(site_ids, list):
            site_ids = [site_ids]

        # Asegúrate de establecer la configuración regional para fechas en español
        try:
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para sistemas basados en Unix/Linux
            # locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Para sistemas Windows
        except locale.Error:
            raise Exception("No se pudo establecer la localidad a español. Asegúrate de que la localidad 'es_ES.UTF-8' esté instalada en tu sistema.")
        
        query = """
        WITH date_range AS (
            SELECT date::date
            FROM generate_series(%s::date, %s::date, '1 day'::interval) date
        ), orders AS (
            SELECT
                DATE((o.order_status->>'timestamp')::timestamp) AS order_date,
                COUNT(o.order_id) AS total_orders,
                COALESCE(SUM(
                    COALESCE(product_prices.total_product_price, 0) +
                    COALESCE(addition_prices.total_addition_price, 0) +
                    COALESCE(topping_prices.total_topping_price, 0) +
                    COALESCE(change_prices.total_change_price, 0) +
                    COALESCE(accompaniment_prices.total_accompaniment_price, 0)
                ), 0) AS total_sales
            FROM
                public.orders o
            CROSS JOIN LATERAL (
                SELECT SUM((product->>'price')::numeric) AS total_product_price
                FROM json_array_elements(o.order_products) AS product
            ) AS product_prices
            LEFT JOIN LATERAL (
                SELECT SUM((addition->>'price')::numeric) AS total_addition_price
                FROM json_array_elements(o.order_products) AS product,
                json_array_elements(product->'adiciones') AS addition
            ) AS addition_prices ON true
            LEFT JOIN LATERAL (
                SELECT SUM((topping->>'price')::numeric) AS total_topping_price
                FROM json_array_elements(o.order_products) AS product,
                json_array_elements(product->'toppings') AS topping
            ) AS topping_prices ON true
            LEFT JOIN LATERAL (
                SELECT SUM((change->>'price')::numeric) AS total_change_price
                FROM json_array_elements(o.order_products) AS product,
                json_array_elements(product->'cambios') AS change
            ) AS change_prices ON true
            LEFT JOIN LATERAL (
                SELECT SUM((accompaniment->>'price')::numeric) AS total_accompaniment_price
                FROM json_array_elements(o.order_products) AS product,
                json_array_elements(product->'acompanantes') AS accompaniment
            ) AS accompaniment_prices ON true
            WHERE
                (o.order_status->>'timestamp')::timestamp BETWEEN %s AND %s AND
                o.site_id = ANY(%s) AND
                o.order_status->>'status' = %s
            GROUP BY
                order_date
        )
        SELECT
            d.date AS order_date,
            COALESCE(o.total_orders, 0) AS total_orders,
            COALESCE(o.total_sales, 0) AS total_sales
        FROM
            date_range d
        LEFT JOIN orders o ON
            d.date = o.order_date
        ORDER BY
            d.date;
        """
        self.cursor.execute(query, (start_date, end_date, start_date, end_date, site_ids, status))
        results = self.cursor.fetchall()
        daily_report = []
        for result in results:
            formatted_date = result[0].strftime("%a-%d-%b").replace('.', '')
            total_orders = result[1]
            daily_report.append({formatted_date : total_orders})
        return daily_report
        


        # for result in results:
        #     formatted_date = result[0].strftime("%a-%d-%b").replace('.', '')
        #     total_sales = result[1]
        #     daily_sales.append({formatted_date: total_sales})
        # return daily_sales

    def get_daily_average_ticket(self, site_ids, status, start_date, end_date):
        # Asumiendo que la configuración regional y la conexión a la base de datos ya están establecidas...
        if not isinstance(site_ids, list):
            site_ids = [site_ids]

        # Asegúrate de establecer la configuración regional para fechas en español
        try:
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Para sistemas basados en Unix/Linux
            # locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  # Para sistemas Windows
        except locale.Error:
            raise Exception("No se pudo establecer la localidad a español. Asegúrate de que la localidad 'es_ES.UTF-8' esté instalada en tu sistema.")

        query = """
        WITH date_range AS (
            SELECT date::date
            FROM generate_series(%s::date, %s::date, '1 day'::interval) date
        ), orders_and_sales AS (
            SELECT
                DATE((o.order_status->>'timestamp')::timestamp) AS order_date,
                COUNT(o.order_id) AS total_orders,
                SUM(
                    COALESCE(product_prices.total_product_price, 0) +
                    COALESCE(addition_prices.total_addition_price, 0) +
                    COALESCE(topping_prices.total_topping_price, 0) +
                    COALESCE(change_prices.total_change_price, 0) +
                    COALESCE(accompaniment_prices.total_accompaniment_price, 0)
                ) AS total_sales
            FROM
                public.orders o
            CROSS JOIN LATERAL (
                SELECT SUM((product->>'price')::numeric) AS total_product_price
                FROM json_array_elements(o.order_products) AS product
            ) AS product_prices
            LEFT JOIN LATERAL (
                SELECT SUM((addition->>'price')::numeric) AS total_addition_price
                FROM json_array_elements(o.order_products) AS product,
                json_array_elements(product->'adiciones') AS addition
            ) AS addition_prices ON true
            LEFT JOIN LATERAL (
                SELECT SUM((topping->>'price')::numeric) AS total_topping_price
                FROM json_array_elements(o.order_products) AS product,
                json_array_elements(product->'toppings') AS topping
            ) AS topping_prices ON true
            LEFT JOIN LATERAL (
                SELECT SUM((change->>'price')::numeric) AS total_change_price
                FROM json_array_elements(o.order_products) AS product,
                json_array_elements(product->'cambios') AS change
            ) AS change_prices ON true
            LEFT JOIN LATERAL (
                SELECT SUM((accompaniment->>'price')::numeric) AS total_accompaniment_price
                FROM json_array_elements(o.order_products) AS product,
                json_array_elements(product->'acompanantes') AS accompaniment
            ) AS accompaniment_prices ON true
            WHERE
                (o.order_status->>'timestamp')::timestamp BETWEEN %s AND %s AND
                o.site_id = ANY(%s) AND
                o.order_status->>'status' = %s
            GROUP BY
                order_date
        )
        SELECT
            d.date AS order_date,
            CASE WHEN COALESCE(o.total_orders, 0) > 0 THEN
                COALESCE(o.total_sales, 0) / COALESCE(o.total_orders, 1)
            ELSE
                0
            END AS average_ticket
        FROM
            date_range d
        LEFT JOIN orders_and_sales o ON
            d.date = o.order_date
        ORDER BY
            d.date;
        """
        self.cursor.execute(query, (start_date, end_date, start_date, end_date, site_ids, status))
        results = self.cursor.fetchall()
        daily_report = []
        for result in results:
            formatted_date = result[0].strftime("%a-%d-%b").replace('.', '')
            average_ticket = float(result[1])
            daily_report.append({formatted_date: round(average_ticket, 0)})
        return daily_report

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


