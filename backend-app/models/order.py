import psycopg2
from dotenv import load_dotenv
import os
import json
import locale
from datetime import datetime, timedelta

from schema.order import order_schema_post
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

    
    def get_sales_report_by_site_and_status(self, site_ids, status, start_date, end_date):
        # Convertir site_ids en una lista si solo se proporciona un ID
        if not isinstance(site_ids, list):
            site_ids = [site_ids]

        # Consulta SQL ajustada para incluir el total de la orden en orders_info y añadir site_name
        query = """
        SELECT
    SUM(
        product_prices.total_product_price +
        COALESCE(addition_prices.total_addition_price, 0) +
        COALESCE(topping_prices.total_topping_price, 0) +
        COALESCE(change_prices.total_change_price, 0) +
        COALESCE(accompaniment_prices.total_accompaniment_price, 0) +
        o.delivery_price -- Sumar el precio de entrega al total de ventas
    ) AS total_sales,
    COUNT(o.order_id) AS total_orders,
    CAST(
        SUM(
            product_prices.total_product_price +
            COALESCE(addition_prices.total_addition_price, 0) +
            COALESCE(topping_prices.total_topping_price, 0) +
            COALESCE(change_prices.total_change_price, 0) +
            COALESCE(accompaniment_prices.total_accompaniment_price, 0) +
            o.delivery_price -- Incluir en el cálculo del ticket promedio
        ) / NULLIF(COUNT(o.order_id), 0)
        AS NUMERIC
    ) AS average_ticket,
    JSON_AGG(
        JSON_BUILD_OBJECT(
            'order_id', o.order_id,
            'status', o.order_status,
            'total_price', product_prices.total_product_price +
            COALESCE(addition_prices.total_addition_price, 0) +
            COALESCE(topping_prices.total_topping_price, 0) +
            COALESCE(change_prices.total_change_price, 0) +
            COALESCE(accompaniment_prices.total_accompaniment_price, 0), -- Agregar el precio de entrega a cada orden
            'site_name', s.site_name,
            'products', o.order_products,  -- Incluir los productos de la orden
            'delivery_price', o.delivery_price -- Incluir el precio de entrega específico de la orden
        )
    ) AS orders_info
FROM
    public.orders o
JOIN public.sites s ON o.site_id = s.site_id 
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
    (o.order_status->>'timestamp')::timestamp >= %s AND
    (o.order_status->>'timestamp')::timestamp <= %s AND
    o.site_id = ANY(%s) AND
    o.order_status->>'status' = %s

        """

        # Ejecutar la consulta con rango de fechas, site_ids y status como parámetros
        self.cursor.execute(query, (start_date, end_date, site_ids, status))
        result = self.cursor.fetchone()
        if result:
            total_sales, total_orders, average_ticket, orders_info = result
            if average_ticket:
                average_ticket = round(average_ticket)  # Redondear el ticket promedio
        else:
            total_sales = total_orders = average_ticket = 0
            orders_info = []

        return {
            'total_sales': total_sales,
            'total_orders': total_orders,
            'average_ticket': average_ticket,
            'orders_info': orders_info
        }


    def get_order_total_price(self, order_id):
        query = """
        SELECT
        SUM(
            product_prices.total_product_price +
            COALESCE(addition_prices.total_addition_price, 0) +
            COALESCE(topping_prices.total_topping_price, 0) +
            COALESCE(change_prices.total_change_price, 0) +
            COALESCE(accompaniment_prices.total_accompaniment_price, 0)
        ) AS total_price
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
        o.order_id = %s
        """
        self.cursor.execute(query, (order_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]  # Devuelve el precio total de la orden
        else:
            return 0  # Devuelve 0 si no se encuentra la orden o si no tiene elementos



    def get_daily_sales_report(self, site_ids, status, start_date, end_date):
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
            FROM generate_series(%s::date, (%s::date - '2 day'::interval), '1 day'::interval) date
        ), sales AS (
            SELECT
                DATE((o.order_status->>'timestamp')::timestamp) AS order_date,
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
                (o.order_status->>'timestamp')::timestamp BETWEEN %s AND (%s - '1 day'::interval) AND
                o.site_id = ANY(%s) AND
                o.order_status->>'status' = %s
            GROUP BY
                order_date
        )
        SELECT
            d.date AS order_date,
            COALESCE(s.total_sales, 0) AS total_sales
        FROM
            date_range d
        LEFT JOIN sales s ON
            d.date = s.order_date
        ORDER BY
            d.date;
        """
        self.cursor.execute(query, (start_date, end_date, start_date, end_date, site_ids, status))
        results = self.cursor.fetchall()
        daily_sales = []
        for result in results:
            formatted_date = result[0].strftime("%a-%d-%b").replace('.', '')
            total_sales = result[1]
            daily_sales.append({formatted_date: total_sales})
        return daily_sales

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


