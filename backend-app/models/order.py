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




        


    def get_sales_report_by_site_and_status(self, status, site_ids, start_date, end_date):
        """
        Devuelve las órdenes en una estructura lista para exportar a Excel,
        con una hoja por cada 'site_id' (sede) y una hoja extra llamada "Todas",
        que contiene las órdenes de todas las sedes juntas.

        Adicionalmente, guarda y consulta un archivo JSON de caché para no
        volver a hacer la consulta con los mismos parámetros.
        """

        # --- 1) Preparar carpeta y archivo de caché ---
        cache_folder = "cache"
        cache_file = os.path.join(cache_folder, "sales_report_cache.json")

        # Crear la carpeta si no existe
        os.makedirs(cache_folder, exist_ok=True)

        # Si el archivo no existe, inicializarlo con un diccionario vacío
        if not os.path.exists(cache_file):
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

        # Cargar el contenido actual de la caché
        with open(cache_file, "r", encoding="utf-8") as f:
            try:
                cache_data = json.load(f)
            except json.JSONDecodeError:
                cache_data = {}

        # --- 2) Construir la clave de caché con los parámetros ---
        site_ids_str = ",".join(map(str, site_ids)) if isinstance(site_ids, (list, tuple)) else str(site_ids)
        cache_key = f"{status}-{site_ids_str}-{start_date}-{end_date}"

        # --- 3) Si la consulta existe en caché, retornar esa data directamente ---
        # if cache_key in cache_data:
        #     return cache_data[cache_key]

        # --- 4) Realizar la consulta a la base de datos y procesar ---
        tz_colombia = pytz.timezone('America/Bogota')

        query = """
            SELECT
                co.site_id,
                co.site_name,
                co.order_id,
                co.user_id,
                co.user_name,
                co.user_phone,
                co.user_address,
                co.current_status,
                co.latest_status_timestamp,
                co.total_order_price,
                co.payment_method,
                co.delivery_price,
                responsible_observation,
                cancelation_solve_responsible
            FROM orders.combined_order_view co
            WHERE co.latest_status_timestamp BETWEEN %s AND %s
            AND co.site_id = ANY(%s)
            AND co.current_status IN ('enviada', 'cancelada')
            ORDER BY co.site_name, co.order_id
        """
        params = (start_date, end_date, site_ids)

        self.cursor.execute(query, params)
        results = self.cursor.fetchall()

        grouped_by_site = {}
        all_orders = []  # ← Aquí guardaremos TODAS las órdenes

        for row in results:
            (
                site_id,
                site_name,
                order_id,
                user_id,
                user_name,
                user_phone,
                user_address,
                current_status,
                latest_ts,
                total_order_price,
                payment_method,
                delivery_price,
                responsible_observation,
                cancelation_solve_responsible
            ) = row

            # Convertir fecha/hora a Colombia; separar fecha y hora
            fecha_str = ""
            hora_str = ""
            if latest_ts:
                try:
                    if isinstance(latest_ts, datetime):
                        dt_utc = latest_ts
                    else:
                        # Caso: latest_ts es una cadena
                        if 'Z' in latest_ts:
                            dt_utc = datetime.fromisoformat(latest_ts.replace('Z', '+00:00'))
                        else:
                            dt_utc = datetime.fromisoformat(latest_ts)

                    dt_col = dt_utc.astimezone(tz_colombia)
                    fecha_str = dt_col.strftime("%Y-%m-%d")
                    hora_str = dt_col.strftime("%H:%M:%S")
                except ValueError:
                    pass  # Si falla el parseo, dejamos en blanco

            if site_id not in grouped_by_site:
                grouped_by_site[site_id] = {
                    "site_name": site_name or "SIN_SEDE",
                    "orders": []
                }

            order_dict = {
                "Orden No": order_id,
                "Monto": float(total_order_price) if total_order_price else 0.0,
                "Sede": site_name or "",
                "Fecha": fecha_str,
                "Hora": hora_str,
                "Estado": current_status or "",
                "Responsable": cancelation_solve_responsible if cancelation_solve_responsible else "no aplica",
                "razon de la cancelacion": responsible_observation if responsible_observation else "no aplica",
                "Domicilio": float(delivery_price) if delivery_price else 0.0,
                "Metodo de pago": payment_method or "",
                "Nombre del usuario": user_name or "",
                "telefono del usuario": user_phone or "",
                "direccion del usuario": user_address or ""
            }

            grouped_by_site[site_id]["orders"].append(order_dict)
            all_orders.append(order_dict)  # ← Agregamos al listado global

        # Definimos los anchos de columna una sola vez para reutilizar
        column_widths = {
            "Orden No": 12,
            "Monto": 15,
            "Sede": 15,
            "Fecha": 12,
            "Hora": 12,
            "Estado": 12,
            "Responsable": 20,
            "razon de la cancelacion": 30,
            "Domicilio": 10,
            "Metodo de pago": 15,
            "Nombre del usuario": 20,
            "telefono del usuario": 15,
            "direccion del usuario": 25
        }

        hojas = []

        # Crear una hoja por cada sede
        for site_id, data_site in grouped_by_site.items():
            site_name = data_site["site_name"]
            orders = data_site["orders"]

            hoja = {
                "hoja": site_name,
                "title": f"Reporte de Ventas - {site_name}",
                "column_widths": column_widths,
                "data": orders
            }
            hojas.append(hoja)

        # Crear la hoja "Todas" con todas las órdenes de todas las sedes
        hoja_todas = {
            "hoja": "Todas",
            "title": "Reporte de Ventas - Todas las Sedes",
            "column_widths": column_widths,
            "data": all_orders
        }
        hojas.append(hoja_todas)

        final_result = {
            "hojas": hojas
        }

        # --- 5) Guardar la nueva data en caché antes de retornar ---
        cache_data[cache_key] = final_result

        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=4)

        return final_result


