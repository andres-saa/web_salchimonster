import psycopg2
from dotenv import load_dotenv
import os
import json
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

    def get_sales_report_by_site_and_status5(self, site_ids, status, start_date, end_date):
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


    def get_sales_report_by_site(self, site_ids, start_date, end_date):
        tz_colombia = pytz.timezone('America/Bogota')
        tz_utc = pytz.utc

        # Preparar la consulta SQL
        query = """
        SELECT
            site_id,
            site_name,
            SUM(CASE WHEN current_status = 'enviada' THEN total_sales ELSE 0 END) AS total_sales_sent,
            SUM(CASE WHEN current_status = 'cancelada' THEN total_sales ELSE 0 END) AS total_sales_cancelled,
            SUM(CASE WHEN current_status = 'enviada' THEN total_orders ELSE 0 END) AS total_orders_sent,
            SUM(CASE WHEN current_status = 'cancelada' THEN total_orders ELSE 0 END) AS total_orders_cancelled,
            COALESCE(creator_name, 'pagina web') AS creator_name,
            -- Ventas y órdenes Chatbot
            SUM(CASE WHEN inserted_by = 1082 AND current_status = 'enviada' THEN total_sales ELSE 0 END) AS total_sales_chatbot,
            SUM(CASE WHEN inserted_by = 1082 AND current_status = 'enviada' THEN total_orders ELSE 0 END) AS total_orders_chatbot,
            
            -- Ventas y órdenes Call Center (vendidas)
            SUM(CASE WHEN inserted_by != 1082 AND inserted_by IS NOT NULL AND current_status = 'enviada' THEN total_sales ELSE 0 END) AS total_sales_callcenter,
            SUM(CASE WHEN inserted_by != 1082 AND inserted_by IS NOT NULL AND current_status = 'enviada' THEN total_orders ELSE 0 END) AS total_orders_callcenter,
            
            -- Ventas y órdenes WEB
            SUM(CASE WHEN inserted_by IS NULL AND current_status = 'enviada' THEN total_sales ELSE 0 END) AS total_sales_web,
            SUM(CASE WHEN inserted_by IS NULL AND current_status = 'enviada' THEN total_orders ELSE 0 END) AS total_orders_web,

            -- Ventas y órdenes Call Center (canceladas)
            SUM(
                CASE WHEN inserted_by != 1082 
                        AND inserted_by IS NOT NULL 
                        AND current_status = 'cancelada' 
                    THEN total_orders 
                    ELSE 0 
                END
            ) AS total_orders_callcenter_cancelled,
            SUM(
                CASE WHEN inserted_by != 1082 
                        AND inserted_by IS NOT NULL 
                        AND current_status = 'cancelada'
                    THEN total_sales
                    ELSE 0
                END
            ) AS total_sales_callcenter_cancelled,

            COUNT(*) FILTER (WHERE responsible_id = creator_id AND creator_id IS NOT NULL) AS concreted_transferences,
            COALESCE(creator_id, 0) AS creator_id
        FROM
            orders.daily_order_sales_view
        WHERE
            (order_date AT TIME ZONE 'America/Bogota') BETWEEN %s AND %s
            AND site_id = ANY(%s)
        GROUP BY 
            ROLLUP((site_id, site_name, COALESCE(creator_name, 'pagina web'), COALESCE(creator_id, 0)))
        ORDER BY
            creator_id, creator_name;
        """

        # Ejecutar consulta
        self.cursor.execute(query, (start_date, end_date, site_ids))
        results = self.cursor.fetchall()

        # Estructura base de reporte
        sales_report = {
            'total_sales': [],
            'creators': [],
            'callcenter_report': []
        }

        total_row = None
        site_sales = {}
        creator_sales = {}

        # -- Diccionario para agrupar datos de Call Center (por site y por asesor)
        #    Formato intermedio: {
        #        "JAMUNDI": {
        #            "JUAN PEREZ": { "quantity": x, "money": y },
        #            "PEDRO GOMEZ": { "quantity": x, "money": y },
        #            ...
        #        },
        #        "CALI": { ... },
        #        ...
        #    }
        callcenter_data = {}

        # -- Set global de asesores para saber quiénes existen en total
        all_advisors = set()

        # Procesar resultados
        for row in results:
            (
                site_id,
                site_name,
                sales_sent,
                sales_cancelled,
                orders_sent,
                orders_cancelled,
                creator_name,
                sales_chatbot,
                orders_chatbot,
                sales_callcenter,
                orders_callcenter,
                sales_web,
                orders_web,
                orders_callcenter_cancelled,
                sales_callcenter_cancelled,
                concreted_transferences,
                creator_id
            ) = row[0:17]

            # Reemplazar None por 0 si aplica
            sales_sent = sales_sent or 0
            sales_cancelled = sales_cancelled or 0
            orders_sent = orders_sent or 0
            orders_cancelled = orders_cancelled or 0
            sales_chatbot = sales_chatbot or 0
            orders_chatbot = orders_chatbot or 0
            sales_callcenter = sales_callcenter or 0
            orders_callcenter = orders_callcenter or 0
            sales_web = sales_web or 0
            orders_web = orders_web or 0
            orders_callcenter_cancelled = orders_callcenter_cancelled or 0
            sales_callcenter_cancelled = sales_callcenter_cancelled or 0

            # Fila de totales (cuando site_id y site_name son None por el ROLLUP)
            if site_id is None and site_name is None:
                total_row = {
                    'site_name': 'TOTAL',
                    'total_sales_sent': sales_sent,
                    'total_sales_cancelled': sales_cancelled,
                    'total_orders_sent': orders_sent,
                    'total_orders_cancelled': orders_cancelled,
                    'creator_id': 0,
                    'site_id': 'TOTAL',
                    'sales_chatbot': sales_chatbot,
                    'sales_callcenter': sales_callcenter,
                    'sales_web': sales_web,
                    'orders_chatbot': orders_chatbot,
                    'orders_callcenter': orders_callcenter,
                    'orders_web': orders_web
                }
            else:
                # Acumular datos en site_sales
                if site_id not in site_sales:
                    site_sales[site_id] = {
                        'site_id': site_id,
                        'site_name': site_name,
                        'total_sales_sent': 0,
                        'total_sales_cancelled': 0,
                        'total_orders_sent': 0,
                        'total_orders_cancelled': 0,
                        'sales_chatbot': 0,
                        'sales_callcenter': 0,
                        'sales_web': 0,
                        'orders_chatbot': 0,
                        'orders_callcenter': 0,
                        'orders_web': 0,
                        'creator_id': 0,
                    }

                site_sales[site_id]['total_sales_sent'] += sales_sent
                site_sales[site_id]['total_sales_cancelled'] += sales_cancelled
                site_sales[site_id]['total_orders_sent'] += orders_sent
                site_sales[site_id]['total_orders_cancelled'] += orders_cancelled
                site_sales[site_id]['sales_chatbot'] += sales_chatbot
                site_sales[site_id]['sales_callcenter'] += sales_callcenter
                site_sales[site_id]['sales_web'] += sales_web
                site_sales[site_id]['orders_chatbot'] += orders_chatbot
                site_sales[site_id]['orders_callcenter'] += orders_callcenter
                site_sales[site_id]['orders_web'] += orders_web

                # Acumular datos en creator_sales
                if creator_name not in creator_sales:
                    creator_sales[creator_name] = {
                        'name': creator_name,
                        'creator_id': creator_id,
                        'sales_chatbot': sales_chatbot,
                        'sales_callcenter': sales_callcenter,
                        'sales_web': sales_web,
                        'orders_chatbot': orders_chatbot,
                        'orders_callcenter': orders_callcenter,
                        'orders_web': orders_web
                    }
                else:
                    creator_sales[creator_name]['sales_chatbot'] += sales_chatbot
                    creator_sales[creator_name]['sales_callcenter'] += sales_callcenter
                    creator_sales[creator_name]['sales_web'] += sales_web
                    creator_sales[creator_name]['orders_chatbot'] += orders_chatbot
                    creator_sales[creator_name]['orders_callcenter'] += orders_callcenter
                    creator_sales[creator_name]['orders_web'] += orders_web

                # -- Construir reporte adicional SOLO para Call Center
                #    si hubo movimiento (vendido o cancelado) de Call Center
                if (orders_callcenter + orders_callcenter_cancelled) > 0:
                    # Guardamos el asesor en nuestro set global
                    all_advisors.add(creator_name)

                    # Asegurar que site_name esté en callcenter_data
                    if site_name not in callcenter_data:
                        callcenter_data[site_name] = {}

                    # Asegurar que el asesor (creator_name) esté en callcenter_data[site_name]
                    if creator_name not in callcenter_data[site_name]:
                        callcenter_data[site_name][creator_name] = {
                            'quantity': 0,
                            'money': 0
                        }

                    callcenter_data[site_name][creator_name]['quantity'] += orders_callcenter
                    callcenter_data[site_name][creator_name]['money'] += sales_callcenter

        # Añadir los diccionarios de ventas de sitios y creadores al reporte final
        sales_report['total_sales'].extend(site_sales.values())
        sales_report['creators'].extend(creator_sales.values())

        # -- Ahora transformamos callcenter_data en el formato final deseado,
        #    mostrando TODOS los asesores (all_advisors) en cada sede.
        #
        #    Ejemplo de salida final por sede:
        #    {
        #      "SEDE ": "JAMUNDI",
        #      "JUAN PEREZ Ordenes": 22,
        #      "JUAN PEREZ Dinero": 485222,
        #      "PEDRO GOMEZ Ordenes": 34,
        #      "PEDRO GOMEZ Dinero": 126555,
        #      ... asesores sin ventas aparecerían con 0 ...
        #    }
        callcenter_report = []

        # Recuperamos todas las sedes de callcenter_data
        all_sites = list(callcenter_data.keys())  # Puedes ordenar si lo deseas

        for site in all_sites:
            site_entry = {'SEDE ': site}

            # Para cada asesor global, si no existe en la sede, ponemos 0
            for advisor_name in all_advisors:
                advisor_stats = callcenter_data[site].get(advisor_name, {'quantity': 0, 'money': 0})
                site_entry[f"{advisor_name} Ordenes"] = advisor_stats['quantity']
                site_entry[f"{advisor_name} Dinero"] = advisor_stats['money']

            callcenter_report.append(site_entry)

        # -------------------------------------------------------------------------
        # ** Agregar un registro de TOTAL para el reporte de Call Center **
        # -------------------------------------------------------------------------
        if callcenter_data:
            total_entry = {'SEDE ': 'TOTAL'}
            # Sumamos los valores de cada asesor a través de todas las sedes
            for advisor_name in all_advisors:
                total_quantity = 0
                total_money = 0
                for site in all_sites:
                    stats = callcenter_data[site].get(advisor_name, {'quantity': 0, 'money': 0})
                    total_quantity += stats['quantity']
                    total_money += stats['money']

                total_entry[f"{advisor_name} Ordenes"] = total_quantity
                total_entry[f"{advisor_name} Dinero"] = total_money

            callcenter_report.append(total_entry)
        # -------------------------------------------------------------------------

        # Añadir el nuevo reporte de Call Center al diccionario principal
        sales_report['callcenter_report'] = callcenter_report

        # Incluir la fila de totales general, si existe
        if total_row:
            sales_report['total_sales'].append(total_row)

        return sales_report



    def close_connection(self):
        self.conn.close()