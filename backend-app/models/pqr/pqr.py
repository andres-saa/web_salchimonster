
from db.db import Db as DataBase
from pydantic import BaseModel
from schema.pqr import pqrs
from schema.user import user_schema_post
from models.orders.order2 import Order2
from datetime import datetime, timedelta
import json
import os
from collections import defaultdict



def formatear_fecha(fecha: datetime) -> str:
    """ Formatea la fecha al estilo '01-ene' con traducción de mes y día. """
    fecha_str = fecha.strftime('%a %d-%b').lower()
    return (fecha_str
        # Traducción de los meses
        .replace('jan', 'ene')
        .replace('feb', 'feb')
        .replace('mar', 'mar')
        .replace('apr', 'abr')
        .replace('may', 'may')
        .replace('jun', 'jun')
        .replace('jul', 'jul')
        .replace('aug', 'ago')
        .replace('sep', 'sept')
        .replace('oct', 'oct')
        .replace('nov', 'nov')
        .replace('dec', 'dic')
        # Traducción de los días
        .replace('mon', 'lun')
        .replace('tue', 'mar')
        .replace('wed', 'mié')
        .replace('thu', 'jue')
        .replace('fri', 'vie')
        .replace('sat', 'sáb')
        .replace('sun', 'dom')
    )

def formatear_rango_fechas(inicio: datetime, fin: datetime) -> str:
    """
    Devuelve un string tipo "10/ene - 15/feb" usando formatear_fecha() 
    solo para día y mes, ignorando el día de la semana.
    """
    # Ajusta si quieres mostrar también el día de la semana
    inicio_str = inicio.strftime('%d-%b').lower()
    fin_str = fin.strftime('%d-%b').lower()

    # Mismo truco de traducción rápida que en formatear_fecha
    for eng, esp in [('jan', 'ene'), ('feb', 'feb'), ('mar', 'mar'), ('apr', 'abr'),
                     ('may', 'may'), ('jun', 'jun'), ('jul', 'jul'), ('aug', 'ago'),
                     ('sep', 'sept'), ('oct', 'oct'), ('nov', 'nov'), ('dec', 'dic')]:
        inicio_str = inicio_str.replace(eng, esp)
        fin_str = fin_str.replace(eng, esp)

    return f"{inicio_str} - {fin_str}"

class StatusHistory(BaseModel):
    pqr_request_id: int
    status_id: int
    notes: str
    
    
    
class ChangeStatusRequest(BaseModel):
    pqr_request_id: int
    status_id: int
    responsible_id: int
    value: float = 0.0
    notes: str = ''
    order_id:str
    


class Pqrs:
    
    def __init__(self):
        self.db = DataBase()
        
        
    def create_pqr(self, data: pqrs.PQRRequest, user: user_schema_post):
        # Define una subclase para incluir el user_id en el esquema de PQR
        class PQRSchema(pqrs.PQRRequest):
            user_id: int

        # Instancia para crear usuario
        order_instance = Order2()
        user_id = order_instance.create_user(user)
        
        # Prepara datos de la PQR incluyendo el user_id
        data_to_send = PQRSchema(
            reques_type_id=data.reques_type_id,
            content=data.content,
            channel_id=data.channel_id,
            user_id=user_id,
            rating=data.rating,
            order_id = data.order_id,
            site_id = data.site_id,
            network_id = data.network_id,
            tag_id= data.tag_id,
            restaurant_id=data.restaurant_id
        )
        
        
        # Inserta la nueva PQR en la base de datos
        query, params = self.db.build_insert_query(table_name='pqr.pqr_request', data=data_to_send, returning='id')
        pqr_id = self.db.execute_query(query=query, params=params, fetch=True)

        initial_status = StatusHistory(
            pqr_request_id=pqr_id[0]["id"],
            status_id=2,  # Asumiendo que '1' es el ID para el estado 'Generada'
            notes='Pqr generada'
            
            
        )
        
        query_status, params_status = self.db.build_insert_query(
            table_name='pqr.status_history',
            data=initial_status,
            returning='id'
        )
        result_status = self.db.execute_query(query=query_status, params=params_status, fetch=True)
        
        
        id_pqr_event = order_instance.create_or_update_event_pqr(7, 1, 1132, '1 minutes', False)
        print(id_pqr_event)
        
        return {'pqr_id': pqr_id, 'initial_status_id': result_status}
    
    
    def get_all_pqrs(self):
        query = self.db.build_select_query(table_name='pqr.pqr_details_full_view',fields=["*"])
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
    
    def is_recent_pqr_generated(self):
        # Consulta para verificar si existe algún evento de tipo 1 para la sede especificada en la vista 'recent_events'
        recent_event_query = """
        SELECT id
        FROM public.recent_events
        WHERE event_type_id = 7
        ORDER BY id DESC
        LIMIT 1;
        """
        query = self.db.build_select_query(table_name='public.recent_events',fields=["id"],condition='event_type_id = 7',order_by='id desc',limit=1)
        result = self.db.execute_query(query=query, fetch=True)
        result = None if not result else result
        # Devuelve None si no hay resultados o el timestamp del evento si existe un evento reciente de tipo 1
        return result
    


        
    def is_recent_order_generated(self):
        # Consulta para verificar si existe algún evento de tipo 1 para la sede especificada en la vista 'recent_events'
        recent_event_query = """
        SELECT id
        FROM public.recent_events
        WHERE event_type_id = 8
        ORDER BY id DESC
        LIMIT 1;
        """
        query = self.db.build_select_query(table_name='public.recent_events',fields=["id"],condition='event_type_id = 8',order_by='id desc',limit=1)
        result = self.db.execute_query(query=query, fetch=True)
        result = None if not result else result
        # Devuelve None si no hay resultados o el timestamp del evento si existe un evento reciente de tipo 1
        return result
    
        
    def get_all_networks(self):
        query = self.db.build_select_query(table_name='pqr.networks',fields=["*"])
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
        
    def get_pqrs_by_date_range(self, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene las PQRs por sede y estado en un rango de fechas, incluyendo estados sin registros.
        Estructura final de cada sede (y una fila global "total"):

        {
            "sede":    { "valor": <nombre_sede>, "pqrs": [] },
            "Abierta": { "valor": X,             "pqrs": [IDs...] },
            "Cerrada": { "valor": Y,             "pqrs": [IDs...] },
            ...
            "total":   { "valor": SumaEstados,   "pqrs": [...] }  # <-- Debe contener la unión de IDs
        }

        En la fila final (sede=total):
        - Se suman las cantidades de todos los estados
        - Se concatenan las listas de PQR de todos los estados en la clave "total"
        """

        query = """
        WITH all_states AS (
            SELECT DISTINCT name AS state_name
            FROM pqr.pqr_status
        ),
        all_sites AS (
            SELECT DISTINCT site_name
            FROM pqr.pqr_details_full_view
        ),
        state_counts AS (
            SELECT
                s.site_name AS sede,
                st.state_name AS estado,
                COUNT(pqr.pqr_request_id) AS cantidad,
                jsonb_agg(pqr.pqr_request_id) FILTER (WHERE pqr.pqr_request_id IS NOT NULL) AS pqr_ids
            FROM all_sites s
            CROSS JOIN all_states st
            LEFT JOIN pqr.pqr_details_full_view pqr
                ON pqr.site_name = s.site_name
                AND (pqr.current_status->>'status') = st.state_name
                AND TO_TIMESTAMP(pqr.current_status->>'timestamp', 'DD-MM-YYYY HH12:MI am')
                    BETWEEN %(fecha_inicio)s AND %(fecha_fin)s
            GROUP BY s.site_name, st.state_name
        )
        SELECT
            jsonb_object_agg(
                estado,
                jsonb_build_object(
                    'valor', COALESCE(cantidad, 0),
                    'pqrs',  COALESCE(pqr_ids, '[]'::jsonb)
                )
            )
            || jsonb_build_object('sede', sede) AS result
        FROM state_counts
        GROUP BY sede
        ORDER BY sede;
        """

        params = {
            "fecha_inicio": f"{fecha_inicio} 00:00:00",
            "fecha_fin": f"{fecha_fin} 23:59:59"
        }

        # Ejecutamos la consulta y obtenemos los resultados
        result = self.db.execute_query(query=query, params=params, fetch=True)
        data = [row["result"] for row in result]

        # 1. Reemplazar "sede" (string) por la forma { "valor": <sede>, "pqrs": [] }
        #    y agregar "total" por sede con la suma de los 'valor' de los estados + concatenación de IDs.
        for entry in data:
            row_sum = 0
            row_pqrs = []  # <--- Para acumular los IDs de esta sede
            for key, value in entry.items():
                if key not in ("sede", "total"):
                    # value = { "valor": x, "pqrs": [...] }
                    row_sum += value["valor"]
                    row_pqrs.extend(value["pqrs"])

            # Convertir la sede en { "valor": <nombre_sede>, "pqrs": [] }
            sede_str = entry["sede"]  # Esto era un string
            entry["sede"] = {"valor": sede_str, "pqrs": []}

            # Agregar la clave "total" con la estructura { "valor": suma_estados, "pqrs": union_de_ids }
            entry["total"] = {"valor": row_sum, "pqrs": row_pqrs}

        # 2. Construir la fila de totales (sede=total) sumando valores y unificando IDs
        total_entry = {
            "sede": {"valor": "total", "pqrs": []}  # Estructura redundante, para mantener el formato
        }

        # Sumamos estado por estado a nivel global
        for entry in data:
            for key, value in entry.items():
                # Omitimos "sede" y "total" de la sede
                if key not in ("sede", "total"):
                    # value = { "valor": int, "pqrs": [...] }
                    if key not in total_entry:
                        total_entry[key] = {"valor": 0, "pqrs": []}
                    total_entry[key]["valor"] += value["valor"]
                    total_entry[key]["pqrs"].extend(value["pqrs"])

        # 3. En la fila final (total), calcular la suma de todos los estados y unificar sus IDs
        global_sum = 0
        global_pqrs = []
        for key, value in total_entry.items():
            if key not in ("sede", "total"):
                global_sum += value["valor"]
                global_pqrs.extend(value["pqrs"])

        total_entry["total"] = {
            "valor": global_sum,
            "pqrs": global_pqrs
        }

        # 4. Agregar este total_entry al final de la lista
        data.append(total_entry)

        return data


    def get_pqrs_by_date_range_and_type(self, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene las PQRs por sede y etiqueta (tag) en un rango de fechas,
        devuelve cada fila con el siguiente formato:
            
            {
                "sede":  { "valor": <nombre_sede>, "pqrs": [] },
                "tagA":  { "valor": X,    "pqrs": [IDs...] },
                "tagB":  { "valor": Y,    "pqrs": [IDs...] },
                ...
                "total": { "valor": suma, "pqrs": [IDs...] }
            }
            
        Y al final, agrega un registro 'total' global:

            {
                "sede":  { "valor": "total", "pqrs": [] },
                "tagA":  { "valor": SumaX,   "pqrs": [...] },
                "tagB":  { "valor": SumaY,   "pqrs": [...] },
                ...
                "total": { "valor": SumaGlobal, "pqrs": [...] }
            }
            
        Además, nos aseguramos de que la clave 'sede' sea la primera del diccionario.
        """

        # 1. Cargar la consulta SQL desde el archivo
        query = self.db.cargar_archivo_sql('./sql/get_pqrs_by_date_range_and_type.sql')

        # 2. Parámetros de fecha
        params = {
            "fecha_inicio": f"{fecha_inicio} 00:00:00",
            "fecha_fin": f"{fecha_fin} 23:59:59"
        }

        # 3. Ejecutar la consulta
        result = self.db.execute_query(query=query, params=params, fetch=True)

        # 4. Convertir a lista de dicts, cada fila trae la clave "result"
        data = [row["result"] for row in result]

        # 5. Para cada sede, reemplazar el string en 'sede' por { "valor": <sede>, "pqrs": [] }
        #    y **acumular** los IDs de PQR de todos los tags en la clave "total".
        for entry in data:
            row_sum = 0
            row_pqrs = []  # <-- Acumularemos aquí todos los IDs de la sede
            for key, value in entry.items():
                if key not in ("sede", "total"):
                    # value = { "valor": x, "pqrs": [...] }
                    row_sum += value["valor"]
                    row_pqrs.extend(value["pqrs"])

            # Guardar el valor de la sede y reemplazarlo por la estructura
            sede_str = entry["sede"]
            entry["sede"] = {"valor": sede_str, "pqrs": []}

            # Agregar la clave "total" con la suma y la lista de todos los IDs de la sede
            entry["total"] = {"valor": row_sum, "pqrs": row_pqrs}

        # 6. Construir la fila "total" global, que acumula todo lo anterior
        total_entry = {
            "sede": {"valor": "total", "pqrs": []}
        }

        # 7. Acumular valores e IDs de cada tag en total_entry
        for entry in data:
            for key, value in entry.items():
                if key not in ("sede", "total"):
                    if key not in total_entry:
                        total_entry[key] = {"valor": 0, "pqrs": []}
                    total_entry[key]["valor"] += value["valor"]
                    total_entry[key]["pqrs"].extend(value["pqrs"])

        # 8. Calcular el total global sumando todos los tags y unificando IDs
        global_sum = 0
        global_pqrs = []
        for key, value in total_entry.items():
            if key not in ("sede", "total"):
                global_sum += value["valor"]
                global_pqrs.extend(value["pqrs"])

        total_entry["total"] = {"valor": global_sum, "pqrs": global_pqrs}

        # 9. Agregar la fila total global a la lista principal
        data.append(total_entry)

        # 10. Asegurar que 'sede' vaya primero en cada entrada
        #     (Python 3.7+ mantiene orden de inserción, así que
        #      simplemente reconstruimos el dict en ese orden).
        final_data = []
        for entry in data:
            sede_val = entry.pop("sede")   # dict: {"valor": <>, "pqrs": []}
            total_val = entry.pop("total") # dict: {"valor": <>, "pqrs": []}
            
            # Crear un diccionario nuevo para forzar el orden
            new_entry = {}
            # 1) sede
            new_entry["sede"] = sede_val
            # 2) tags (todas las claves restantes que no sean "sede"/"total")
            for k, v in entry.items():
                new_entry[k] = v
            # 3) total
            new_entry["total"] = total_val

            final_data.append(new_entry)

        return final_data
    
    def get_pqrs_by_responsible_and_state(self, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene las PQRs por responsable y estado en un rango de fechas, 
        con estructura uniforme para cada columna, y agrega una fila "total" global.
        
        Formato por responsable, por ejemplo:
        {
        "responsible_name": { "valor": "Juan Pérez", "pqrs": [] },
        "generada": { "valor": 5, "pqrs": [101, 102, ...] },
        "abierta":  { "valor": 2, "pqrs": [201, 205] },
        ...
        "total":    { "valor": 7, "pqrs": [...] }
        }
        
        Fila final global:
        {
        "responsible_name": { "valor": "total", "pqrs": [] },
        "generada": { "valor": 10, "pqrs": [...] },
        "abierta":  { "valor": 15, "pqrs": [...] },
        ...
        "total":    { "valor": 25, "pqrs": [...] }
        }
        """

        # 1. Cargamos la consulta SQL (la versión que devuelve {valor, pqrs} por estado)
        query = self.db.cargar_archivo_sql('./sql/get_pqrs_by_responsible_and_state.sql')

        # 2. Parámetros de fecha
        params = {
            "fecha_inicio": f"{fecha_inicio} 00:00:00",
            "fecha_fin": f"{fecha_fin} 23:59:59"
        }

        # 3. Ejecutar la consulta y obtener resultados
        result = self.db.execute_query(query=query, params=params, fetch=True)

        # 4. Convertir la respuesta en una lista de dicts
        #    Cada fila del SQL tiene la clave 'result'
        data = [row["result"] for row in result]
        # Por ejemplo, data[i] = {
        #    "responsible_name": "Juan Pérez",
        #    "generada": { "valor": 5, "pqrs": [101, 102] },
        #    "abierta":  { "valor": 2, "pqrs": [201, 205] },
        #    ...
        # }

        # 5. Para cada entrada, transformar "responsible_name" 
        #    en { "valor": <nombre>, "pqrs": [] }, y dejarlo como primera clave
        structured_data = []
        for entry in data:
            # Sacamos el valor string y lo reemplazamos
            resp_name_str = entry.pop("responsible_name")

            new_entry = {
                "responsible_name": {
                    "valor": resp_name_str,
                    "pqrs": []
                }
            }
            # Agregamos el resto de estados (ya tienen {valor, pqrs})
            for state_key, state_val in entry.items():
                new_entry[state_key] = state_val

            structured_data.append(new_entry)

        # 6. Calcular la columna "total" en cada responsable 
        #    con la suma de valores y la unión de IDs.
        for entry in structured_data:
            sum_for_responsible = 0
            pqrs_for_responsible = []

            # Recorrer todas las claves excepto "responsible_name" y "total"
            for key, value in entry.items():
                if key not in ("responsible_name", "total"):
                    # value = { "valor": <int>, "pqrs": [IDs...] }
                    sum_for_responsible += value["valor"]
                    pqrs_for_responsible.extend(value["pqrs"])

            # Agregamos la clave "total"
            entry["total"] = {
                "valor": sum_for_responsible,
                "pqrs": pqrs_for_responsible
            }

        # 7. Construir la fila de totales global
        total_entry = {
            "responsible_name": {
                "valor": "total",
                "pqrs": []
            }
        }

        # 8. Sumar estado por estado a nivel global
        for entry in structured_data:
            for key, value in entry.items():
                if key not in ("responsible_name", "total"):
                    # value: { "valor": int, "pqrs": [...] }
                    if key not in total_entry:
                        total_entry[key] = {
                            "valor": 0,
                            "pqrs": []
                        }
                    total_entry[key]["valor"] += value["valor"]
                    total_entry[key]["pqrs"].extend(value["pqrs"])

        # 9. Crear el "total" global uniendo todos los estados
        global_sum = 0
        global_pqrs = []
        for key, val in total_entry.items():
            if key in ("responsible_name", "total"):
                continue
            global_sum += val["valor"]
            global_pqrs.extend(val["pqrs"])

        total_entry["total"] = {
            "valor": global_sum,
            "pqrs": global_pqrs
        }

        # 10. Agregar la fila global a la lista
        structured_data.append(total_entry)

        return structured_data



   
    def get_daily_pqrs_report(self, site_ids: list, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene las PQRs por día y tipo en un rango de fechas, filtrando por múltiples site_ids.
        Devuelve un JSON con las fechas como labels, los colores en hexadecimal y los valores de cantidad del tipo como datasets.

        :param site_ids: Lista de IDs de sitios a filtrar.
        :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD).
        :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD).
        :return: JSON para graficar.
        """
        query = self.db.cargar_archivo_sql('./sql/get_daily_pqrs_report.sql')
        params = {
            "site_ids": site_ids,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin
        }

        result = self.db.execute_query(query=query, params=params, fetch=True)

        # Inicializar estructura de datos para el JSON final
        labels = []
        datasets = {}

        for row in result:
            # Formatear la fecha
            fecha = row['fecha'].strftime('%d-%b').lower()
            fecha = (fecha
                    .replace('jan', 'ene')
                    .replace('feb', 'feb')
                    .replace('mar', 'mar')
                    .replace('apr', 'abr')
                    .replace('may', 'may')
                    .replace('jun', 'jun')
                    .replace('jul', 'jul')
                    .replace('aug', 'ago')
                    .replace('sep', 'sept')
                    .replace('oct', 'oct')
                    .replace('nov', 'nov')
                    .replace('dec', 'dic'))

            labels.append(fecha)
            tags = row['tags']

            # Procesar los datos por tipo
            for tipo, details in tags.items():
                cantidad = details['cantidad']
                color = details['color']

                if tipo not in datasets:
                    datasets[tipo] = {
                        "label": tipo,
                        "backgroundColor": color,
                        "borderColor": color,
                        "data": [],
                        "tension": 0.4
                    }
                datasets[tipo]["data"].append(cantidad)

        # Convertir los datasets a la estructura final
        final_datasets = list(datasets.values())

        return {
            "labels": labels,
            "datasets": final_datasets
        }
        






    def get_all_tags(self):
        query = self.db.build_select_query(table_name='pqr.pqr_tag',fields=["*"],condition='exist = true')
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
    
    def get_all_channels(self):
        query = self.db.build_select_query(table_name='pqr.pqr_channel',fields=["*"])
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
        
    def get_all_types(self):
        query = self.db.build_select_query(table_name='pqr.pqr_request_type',fields=["*"],order_by='index')
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
            
    def get_all_status(self):
        query = self.db.build_select_query(table_name='pqr.pqr_status',fields=["*"],order_by='index')
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
    
    def update_pqr_status(self, data: ChangeStatusRequest):
        # Prepara los datos para el nuevo registro en status_history
        data_to_insert = {
            'pqr_request_id': data.pqr_request_id,
            'status_id': data.status_id,
            'responsible_id': data.responsible_id,
            'value': data.value,
            'notes': data.notes,
            'order_id':data.order_id
        }

        # Construcción de la consulta de inserción
        query, params = self.db.build_insert_query(
            table_name='pqr.status_history',
            data=data,
            returning='id'
        )

        # Ejecución de la consulta
        new_status_id = self.db.execute_query(query=query, params=params, fetch=True)
        
        return {'new_status_id': new_status_id}
    




    def get_daily_average_ticket_report(self, site_ids: list, start_date: str, end_date: str):
        """
        Obtiene el ticket promedio diario por canal (web, chatbot, callcenter) 
        en un rango de fechas, considerando el día desde las 4:00 am hasta las 3:59 am 
        del siguiente día.
        
        Además, genera comparaciones respecto al mismo rango "desplazado" 7 días antes.
        Retorna un JSON con distintos reportes para graficar:
            - reporte_basico   (ticket promedio día a día por canal y total)
            - callcenter       (comparación: "antes" vs "ahora")
            - total           (comparación: "antes" vs "ahora")
            - chatbot         (comparación: "antes" vs "ahora")
            - web             (comparación: "antes" vs "ahora")

        :param site_ids: Lista de IDs de sitios a filtrar.
        :param start_date: Fecha de inicio (formato ISO: YYYY-MM-DDTHH:MM:SS.sssZ).
        :param end_date: Fecha de fin (formato ISO: YYYY-MM-DDTHH:MM:SS.sssZ).
        :return: Dict con datos para graficar.
        """

        cache_folder = "cache"
        cache_file = os.path.join(cache_folder, "daily_average_ticket_report.json")

        if not os.path.exists(cache_folder):
            os.makedirs(cache_folder)

        # Si no existe el archivo, lo creamos con un dict vacío
        if not os.path.exists(cache_file):
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

        # ------------------------------------------------------------------
        # 1) GENERAR UNA CLAVE DE CACHÉ UNÍVOCA PARA ESTOS PARÁMETROS
        # ------------------------------------------------------------------
        #    - site_ids podría tener distinto orden, así que lo ordenamos
        #    - Usamos un string como "clave" que combine los parámetros
        # ------------------------------------------------------------------

        # Ordenamos site_ids para evitar duplicados por orden distinto
        site_ids_sorted = sorted(site_ids)
        # Creamos la clave (string) a partir de los parámetros
        cache_key = f"{site_ids_sorted}-{start_date}-{end_date}"

        # ------------------------------------------------------------------
        # 2) LEER EL ARCHIVO DE CACHÉ Y VER SI LA CLAVE YA EXISTE
        # ------------------------------------------------------------------
        with open(cache_file, "r", encoding="utf-8") as f:
            cache_data = json.load(f)

        if cache_key in cache_data:
            # Si la clave existe, retornamos inmediatamente lo que está en caché
            return cache_data[cache_key]
        


        # -----------------------------------------------------------
        # 1) Convertir fechas de formato ISO a datetime y preparar
        #    rangos "ahora" vs. "antes" (7 días atrás)
        # -----------------------------------------------------------
        fmt_iso = "%Y-%m-%dT%H:%M:%S.%fZ"
        start_date_dt = datetime.strptime(start_date, fmt_iso)
        end_date_dt = datetime.strptime(end_date, fmt_iso)





        # Rango principal (para la consulta "ahora")
        start_date_str = start_date_dt.strftime("%Y-%m-%d")
        end_date_str = end_date_dt.strftime("%Y-%m-%d")

        # Rango 7 días antes (para la consulta "antes")
        start_date_before_dt = start_date_dt - timedelta(days=28)
        end_date_before_dt = end_date_dt - timedelta(days=28)
        start_date_before_str = start_date_before_dt.strftime("%Y-%m-%d")
        end_date_before_str = end_date_before_dt.strftime("%Y-%m-%d")

        # Etiquetas de los rangos para mostrar en gráficas
        label_rango_ahora = formatear_rango_fechas(start_date_dt, end_date_dt)  # p.ej. "10/ene - 15/feb"
        label_rango_antes = formatear_rango_fechas(start_date_before_dt, end_date_before_dt)  # p.ej. "03/ene - 08/feb"

        # -----------------------------------------------------------
        # 2) Consulta "ahora"
        # -----------------------------------------------------------
        query_now = """
            WITH date_range AS (
                SELECT generate_series(
                    %(start_date)s::date,
                    %(end_date)s::date,
                    '1 day'::interval
                )::date AS fecha
            ),
            daily_data AS (
                SELECT
                    (order_date - INTERVAL '4 hours')::date AS day,

                    -- Ventas por canal
                    SUM(CASE WHEN inserted_by = 1082 
                            AND current_status = 'enviada' 
                        THEN total_sales ELSE 0 END) AS sales_chatbot,
                    SUM(CASE WHEN inserted_by != 1082 
                            AND inserted_by IS NOT NULL 
                            AND current_status = 'enviada' 
                        THEN total_sales ELSE 0 END) AS sales_callcenter,
                    SUM(CASE WHEN inserted_by IS NULL 
                            AND current_status = 'enviada' 
                        THEN total_sales ELSE 0 END) AS sales_web,

                    -- Órdenes por canal
                    SUM(CASE WHEN inserted_by = 1082 
                            AND current_status = 'enviada' 
                        THEN 1 ELSE 0 END) AS orders_chatbot,
                    SUM(CASE WHEN inserted_by != 1082 
                            AND inserted_by IS NOT NULL 
                            AND current_status = 'enviada' 
                        THEN 1 ELSE 0 END) AS orders_callcenter,
                    SUM(CASE WHEN inserted_by IS NULL 
                            AND current_status = 'enviada' 
                        THEN 1 ELSE 0 END) AS orders_web
                FROM orders.daily_order_sales_view
                WHERE
                    (order_date - INTERVAL '4 hours')::date 
                        BETWEEN %(start_date)s AND %(end_date)s
                    AND site_id = ANY(%(site_ids)s)
                GROUP BY 1
            )
            SELECT
                d.fecha,
                COALESCE(dd.sales_chatbot, 0) AS sales_chatbot,
                COALESCE(dd.sales_callcenter, 0) AS sales_callcenter,
                COALESCE(dd.sales_web, 0) AS sales_web,

                COALESCE(dd.orders_chatbot, 0) AS orders_chatbot,
                COALESCE(dd.orders_callcenter, 0) AS orders_callcenter,
                COALESCE(dd.orders_web, 0) AS orders_web
            FROM date_range d
            LEFT JOIN daily_data dd ON d.fecha = dd.day
            ORDER BY d.fecha;
        """

        params_now = {
            "site_ids": site_ids,
            "start_date": start_date_str,
            "end_date": end_date_str
        }

        result_now = self.db.execute_query(query=query_now, params=params_now, fetch=True)

        # -----------------------------------------------------------
        # 3) Consulta "antes" (mismo SQL, pero con fechas desplazadas)
        # -----------------------------------------------------------
        query_before = """
            WITH date_range AS (
                SELECT generate_series(
                    %(start_date_before)s::date,
                    %(end_date_before)s::date,
                    '1 day'::interval
                )::date AS fecha
            ),
            daily_data AS (
                SELECT
                    (order_date - INTERVAL '4 hours')::date AS day,

                    -- Ventas por canal
                    SUM(CASE WHEN inserted_by = 1082 
                            AND current_status = 'enviada' 
                        THEN total_sales ELSE 0 END) AS sales_chatbot,
                    SUM(CASE WHEN inserted_by != 1082 
                            AND inserted_by IS NOT NULL 
                            AND current_status = 'enviada' 
                        THEN total_sales ELSE 0 END) AS sales_callcenter,
                    SUM(CASE WHEN inserted_by IS NULL 
                            AND current_status = 'enviada' 
                        THEN total_sales ELSE 0 END) AS sales_web,

                    -- Órdenes por canal
                    SUM(CASE WHEN inserted_by = 1082 
                            AND current_status = 'enviada' 
                        THEN 1 ELSE 0 END) AS orders_chatbot,
                    SUM(CASE WHEN inserted_by != 1082 
                            AND inserted_by IS NOT NULL 
                            AND current_status = 'enviada' 
                        THEN 1 ELSE 0 END) AS orders_callcenter,
                    SUM(CASE WHEN inserted_by IS NULL 
                            AND current_status = 'enviada' 
                        THEN 1 ELSE 0 END) AS orders_web
                FROM orders.daily_order_sales_view
                WHERE
                    (order_date - INTERVAL '4 hours')::date 
                        BETWEEN %(start_date_before)s AND %(end_date_before)s
                    AND site_id = ANY(%(site_ids)s)
                GROUP BY 1
            )
            SELECT
                d.fecha,
                COALESCE(dd.sales_chatbot, 0) AS sales_chatbot,
                COALESCE(dd.sales_callcenter, 0) AS sales_callcenter,
                COALESCE(dd.sales_web, 0) AS sales_web,

                COALESCE(dd.orders_chatbot, 0) AS orders_chatbot,
                COALESCE(dd.orders_callcenter, 0) AS orders_callcenter,
                COALESCE(dd.orders_web, 0) AS orders_web
            FROM date_range d
            LEFT JOIN daily_data dd ON d.fecha = dd.day
            ORDER BY d.fecha;
        """

        params_before = {
            "site_ids": site_ids,
            "start_date_before": start_date_before_str,
            "end_date_before": end_date_before_str
        }

        result_before = self.db.execute_query(query=query_before, params=params_before, fetch=True)

        # -----------------------------------------------------------
        # 4) Construir "reporte_basico"
        #    => Ticket promedio diario (labels, datasets)
        # -----------------------------------------------------------
        labels_basico = []
        data_chatbot_basico = []
        data_callcenter_basico = []
        data_web_basico = []
        data_total_basico = []

        for row in result_now:
            fecha_str = formatear_fecha(row['fecha'])  # p.ej. "10-ene"
            labels_basico.append(fecha_str)

            # Ventas y órdenes por canal
            s_chatbot = row['sales_chatbot'] or 0
            o_chatbot = row['orders_chatbot'] or 0

            s_callcenter = row['sales_callcenter'] or 0
            o_callcenter = row['orders_callcenter'] or 0

            s_web = row['sales_web'] or 0
            o_web = row['orders_web'] or 0

            # Ticket promedio por canal
            avg_chatbot = s_chatbot / o_chatbot if o_chatbot > 0 else 0
            avg_callcenter = s_callcenter / o_callcenter if o_callcenter > 0 else 0
            avg_web = s_web / o_web if o_web > 0 else 0

            # Ticket promedio total
            total_sales = s_chatbot + s_callcenter + s_web
            total_orders = o_chatbot + o_callcenter + o_web
            avg_total = total_sales / total_orders if total_orders > 0 else 0

            data_chatbot_basico.append(round(avg_chatbot, 2))
            data_callcenter_basico.append(round(avg_callcenter, 2))
            data_web_basico.append(round(avg_web, 2))
            data_total_basico.append(round(avg_total, 2))

        # Colores de ejemplo
        color_chatbot = "#36a2eb"
        color_callcenter = "#ff6384"
        color_web = "#ffce56"
        color_total = "#4bc0c0"

        datasets_basico = [
            {
                "label": "web",
                "backgroundColor": color_web,
                "borderColor": color_web,
                "data": data_web_basico,
                "tension": 0.4
            },
            {
                "label": "chatbot",
                "backgroundColor": color_chatbot,
                "borderColor": color_chatbot,
                "data": data_chatbot_basico,
                "tension": 0.4
            },
            {
                "label": "callcenter",
                "backgroundColor": color_callcenter,
                "borderColor": color_callcenter,
                "data": data_callcenter_basico,
                "tension": 0.4
            },
            {
                "label": "total",
                "backgroundColor": color_total,
                "borderColor": color_total,
                "data": data_total_basico,
                "tension": 0.4
            }
        ]

        reporte_basico = {
            "labels": labels_basico,
            "datasets": datasets_basico
        }

        # -----------------------------------------------------------
        # 5) Mapear resultados "antes" a un dict para comparaciones
        #    Clave: fecha "actual" = fecha de 'antes' + 7 días
        # -----------------------------------------------------------
        dict_before = {}
        for row in result_before:
            fecha_actual = row['fecha'] + timedelta(days=28)

            s_chatbot = row['sales_chatbot'] or 0
            o_chatbot = row['orders_chatbot'] or 0

            s_callcenter = row['sales_callcenter'] or 0
            o_callcenter = row['orders_callcenter'] or 0

            s_web = row['sales_web'] or 0
            o_web = row['orders_web'] or 0

            total_sales = s_chatbot + s_callcenter + s_web
            total_orders = o_chatbot + o_callcenter + o_web

            # Guardar ticket promedio en dict
            dict_before[fecha_actual] = {
                "chatbot": round(s_chatbot / o_chatbot, 2) if o_chatbot else 0,
                "callcenter": round(s_callcenter / o_callcenter, 2) if o_callcenter else 0,
                "web": round(s_web / o_web, 2) if o_web else 0,
                "total": round(total_sales / total_orders, 2) if total_orders else 0
            }

        # -----------------------------------------------------------
        # 6) Construir listas comparativas (now vs. before)
        # -----------------------------------------------------------
        labels_cmp = []
        now_chatbot = []
        now_callcenter = []
        now_web = []
        now_total = []

        before_chatbot = []
        before_callcenter = []
        before_web = []
        before_total = []

        for row in result_now:
            fecha = row['fecha']
            fecha_str = formatear_fecha(fecha)
            labels_cmp.append(fecha_str)

            # Ticket promedio "now"
            s_chatbot = row['sales_chatbot'] or 0
            o_chatbot = row['orders_chatbot'] or 0
            avg_chatbot_now = round(s_chatbot / o_chatbot, 2) if o_chatbot else 0

            s_callcenter = row['sales_callcenter'] or 0
            o_callcenter = row['orders_callcenter'] or 0
            avg_callcenter_now = round(s_callcenter / o_callcenter, 2) if o_callcenter else 0

            s_web = row['sales_web'] or 0
            o_web = row['orders_web'] or 0
            avg_web_now = round(s_web / o_web, 2) if o_web else 0

            t_now_sales = s_chatbot + s_callcenter + s_web
            t_now_orders = o_chatbot + o_callcenter + o_web
            avg_total_now = round(t_now_sales / t_now_orders, 2) if t_now_orders else 0

            # Ticket promedio "before"
            if fecha in dict_before:
                ch_before = dict_before[fecha]["chatbot"]
                c_before = dict_before[fecha]["callcenter"]
                w_before = dict_before[fecha]["web"]
                t_before = dict_before[fecha]["total"]
            else:
                ch_before = 0
                c_before = 0
                w_before = 0
                t_before = 0

            now_chatbot.append(avg_chatbot_now)
            now_callcenter.append(avg_callcenter_now)
            now_web.append(avg_web_now)
            now_total.append(avg_total_now)

            before_chatbot.append(ch_before)
            before_callcenter.append(c_before)
            before_web.append(w_before)
            before_total.append(t_before)

        # -----------------------------------------------------------
        # 7) Construir reportes comparativos (callcenter, total, chatbot, web)
        # -----------------------------------------------------------
        # Con "antes" (línea punteada) y "ahora" (fill)
        # Ejemplo de colores:
        reporte_callcenter = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_callcenter,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#ffa5b550",
                    "borderColor": "#ffa5b5",
                    "fill": True,
                    "data": now_callcenter,
                    "tension": 0.4
                }
            ]
        }

        reporte_total = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_total,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#4bc0c050",
                    "borderColor": "#4bc0c0",
                    "fill": True,
                    "data": now_total,
                    "tension": 0.4
                }
            ]
        }

        reporte_chatbot = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_chatbot,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#36a2eb50",
                    "borderColor": "#36a2eb",
                    "fill": True,
                    "data": now_chatbot,
                    "tension": 0.4
                }
            ]
        }

        reporte_web = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_web,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#ffce5650",
                    "borderColor": "#ffce56",
                    "fill": True,
                    "data": now_web,
                    "tension": 0.4
                }
            ]
        }

        # -----------------------------------------------------------
        # 8) Devolver la estructura final con todos los reportes
        # -----------------------------------------------------------
        result_data =  {
            "reporte_basico": reporte_basico,
            "callcenter": reporte_callcenter,
            "total": reporte_total,
            "chatbot": reporte_chatbot,
            "web": reporte_web
        }


        cache_data[cache_key] = result_data
        with open(cache_file, "w", encoding="utf-8") as f:
            # `default=str` para evitar error con objetos datetime, etc.
            json.dump(cache_data, f, ensure_ascii=False, default=str)

        return result_data




    def get_daily_sales_report(self, site_ids: list, start_date: str, end_date: str):
        """
        Obtiene las ventas diarias por canal (web, chatbot, callcenter) en un rango de fechas,
        considerando un día desde las 4:00 am hasta las 3:59 am del siguiente día.
        
        Además, genera comparaciones respecto al mismo rango "desplazado" 7 días antes.
        Retorna un JSON con distintos reportes para graficar:
            - reporte_basico  (ventas día a día web, chatbot, callcenter, total)
            - callcenter      (comparación: "antes" vs "ahora")
            - total          (comparación: "antes" vs "ahora")
            - chatbot        (comparación: "antes" vs "ahora")
            - web            (comparación: "antes" vs "ahora")

        :param site_ids: Lista de IDs de sitios a filtrar.
        :param start_date: Fecha de inicio (formato ISO: YYYY-MM-DDTHH:MM:SS.sssZ).
        :param end_date: Fecha de fin (formato ISO: YYYY-MM-DDTHH:MM:SS.sssZ).
        :return: Dict con datos para graficar (reporte_basico y reportes comparativos).
        """
        # ---------------------------------------------------------
        # 1) Conversión de fechas (ISO a datetime) y rangos "antes"
        # ---------------------------------------------------------

        cache_folder = "cache"
        cache_file = os.path.join(cache_folder, "daily_sales_report.json")

        if not os.path.exists(cache_folder):
            os.makedirs(cache_folder)

        # Si no existe el archivo, lo creamos con un dict vacío
        if not os.path.exists(cache_file):
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

        # ------------------------------------------------------------------
        # 1) GENERAR UNA CLAVE DE CACHÉ UNÍVOCA PARA ESTOS PARÁMETROS
        # ------------------------------------------------------------------
        #    - site_ids podría tener distinto orden, así que lo ordenamos
        #    - Usamos un string como "clave" que combine los parámetros
        # ------------------------------------------------------------------

        # Ordenamos site_ids para evitar duplicados por orden distinto
        site_ids_sorted = sorted(site_ids)
        # Creamos la clave (string) a partir de los parámetros
        cache_key = f"{site_ids_sorted}-{start_date}-{end_date}"

        # ------------------------------------------------------------------
        # 2) LEER EL ARCHIVO DE CACHÉ Y VER SI LA CLAVE YA EXISTE
        # ------------------------------------------------------------------
        with open(cache_file, "r", encoding="utf-8") as f:
            cache_data = json.load(f)

        if cache_key in cache_data:
            # Si la clave existe, retornamos inmediatamente lo que está en caché
            return cache_data[cache_key]
        


        fmt_iso = "%Y-%m-%dT%H:%M:%S.%fZ"
        start_date_dt = datetime.strptime(start_date, fmt_iso)
        end_date_dt = datetime.strptime(end_date, fmt_iso)

        # Rango principal
        start_date_str = start_date_dt.strftime("%Y-%m-%d")
        end_date_str = end_date_dt.strftime("%Y-%m-%d")

        # Rango "antes" (7 días atrás)
        start_date_before_dt = start_date_dt - timedelta(days=28)
        end_date_before_dt = end_date_dt - timedelta(days=28)
        start_date_before_str = start_date_before_dt.strftime("%Y-%m-%d")
        end_date_before_str = end_date_before_dt.strftime("%Y-%m-%d")

        # Labels de rangos para reportes comparativos
        label_rango_ahora = formatear_rango_fechas(start_date_dt, end_date_dt)
        label_rango_antes = formatear_rango_fechas(start_date_before_dt, end_date_before_dt)

        # ---------------------------------------------------------
        # 2) Consulta SQL para el rango "actual"
        # ---------------------------------------------------------
        query_now = """
            WITH date_range AS (
                SELECT generate_series(
                    %(start_date)s::date,
                    %(end_date)s::date,
                    '1 day'::interval
                )::date AS fecha
            ),
            daily_sales AS (
                SELECT
                    (order_date - INTERVAL '4 hours')::date AS day,
                    SUM(
                        CASE 
                            WHEN inserted_by = 1082 
                                AND current_status = 'enviada' 
                            THEN total_sales 
                            ELSE 0 
                        END
                    ) AS sales_chatbot,
                    SUM(
                        CASE 
                            WHEN inserted_by != 1082 
                                AND inserted_by IS NOT NULL 
                                AND current_status = 'enviada' 
                            THEN total_sales 
                            ELSE 0 
                        END
                    ) AS sales_callcenter,
                    SUM(
                        CASE 
                            WHEN inserted_by IS NULL 
                                AND current_status = 'enviada'
                            THEN total_sales 
                            ELSE 0 
                        END
                    ) AS sales_web
                FROM orders.daily_order_sales_view
                WHERE
                    (order_date - INTERVAL '4 hours')::date BETWEEN %(start_date)s AND %(end_date)s
                    AND site_id = ANY(%(site_ids)s)
                GROUP BY 1
            )
            SELECT
                d.fecha,
                COALESCE(s.sales_chatbot, 0) AS chatbot,
                COALESCE(s.sales_callcenter, 0) AS callcenter,
                COALESCE(s.sales_web, 0) AS web
            FROM date_range d
            LEFT JOIN daily_sales s ON d.fecha = s.day
            ORDER BY d.fecha;
        """

        params_now = {
            "site_ids": site_ids,
            "start_date": start_date_str,
            "end_date": end_date_str
        }

        result_now = self.db.execute_query(query=query_now, params=params_now, fetch=True)

        # ---------------------------------------------------------
        # 3) Consulta SQL para el rango "antes"
        # ---------------------------------------------------------
        query_before = """
            WITH date_range AS (
                SELECT generate_series(
                    %(start_date_before)s::date,
                    %(end_date_before)s::date,
                    '1 day'::interval
                )::date AS fecha
            ),
            daily_sales AS (
                SELECT
                    (order_date - INTERVAL '4 hours')::date AS day,
                    SUM(
                        CASE 
                            WHEN inserted_by = 1082 
                                AND current_status = 'enviada' 
                            THEN total_sales 
                            ELSE 0 
                        END
                    ) AS sales_chatbot,
                    SUM(
                        CASE 
                            WHEN inserted_by != 1082 
                                AND inserted_by IS NOT NULL 
                                AND current_status = 'enviada' 
                            THEN total_sales 
                            ELSE 0 
                        END
                    ) AS sales_callcenter,
                    SUM(
                        CASE 
                            WHEN inserted_by IS NULL 
                                AND current_status = 'enviada'
                            THEN total_sales 
                            ELSE 0 
                        END
                    ) AS sales_web
                FROM orders.daily_order_sales_view
                WHERE
                    (order_date - INTERVAL '4 hours')::date BETWEEN %(start_date_before)s AND %(end_date_before)s
                    AND site_id = ANY(%(site_ids)s)
                GROUP BY 1
            )
            SELECT
                d.fecha,
                COALESCE(s.sales_chatbot, 0) AS chatbot,
                COALESCE(s.sales_callcenter, 0) AS callcenter,
                COALESCE(s.sales_web, 0) AS web
            FROM date_range d
            LEFT JOIN daily_sales s ON d.fecha = s.day
            ORDER BY d.fecha;
        """

        params_before = {
            "site_ids": site_ids,
            "start_date_before": start_date_before_str,
            "end_date_before": end_date_before_str
        }

        result_before = self.db.execute_query(query=query_before, params=params_before, fetch=True)

        # ---------------------------------------------------------
        # 4) Construir "reporte_basico" (ventas día a día)
        # ---------------------------------------------------------
        labels_basico = []
        data_chatbot_basico = []
        data_callcenter_basico = []
        data_web_basico = []
        data_total_basico = []

        for row in result_now:
            fecha_str = formatear_fecha(row['fecha'])  # p.ej. "10-ene"
            labels_basico.append(fecha_str)

            chatbot_val = row['chatbot'] or 0
            callcenter_val = row['callcenter'] or 0
            web_val = row['web'] or 0
            total_val = chatbot_val + callcenter_val + web_val

            data_chatbot_basico.append(chatbot_val)
            data_callcenter_basico.append(callcenter_val)
            data_web_basico.append(web_val)
            data_total_basico.append(total_val)

        # Colores de ejemplo
        color_chatbot = "#36a2eb"
        color_callcenter = "#ff6384"
        color_web = "#ffce56"
        color_total = "#4bc0c0"

        datasets_basico = [
            {
                "label": "web",
                "backgroundColor": color_web,
                "borderColor": color_web,
                "data": data_web_basico,
                "tension": 0.4
            },
            {
                "label": "chatbot",
                "backgroundColor": color_chatbot,
                "borderColor": color_chatbot,
                "data": data_chatbot_basico,
                "tension": 0.4
            },
            {
                "label": "callcenter",
                "backgroundColor": color_callcenter,
                "borderColor": color_callcenter,
                "data": data_callcenter_basico,
                "tension": 0.4
            },
            {
                "label": "total",
                "backgroundColor": color_total,
                "borderColor": color_total,
                "data": data_total_basico,
                "tension": 0.4
            }
        ]

        reporte_basico = {
            "labels": labels_basico,
            "datasets": datasets_basico
        }

        # ---------------------------------------------------------
        # 5) Mapear resultados del "antes" a un diccionario
        #    para poder compararlos (clave: fecha actual)
        # ---------------------------------------------------------
        dict_before = {}
        for row in result_before:
            fecha_actual = row['fecha'] + timedelta(days=28)
            dict_before[fecha_actual] = {
                "chatbot": row['chatbot'] or 0,
                "callcenter": row['callcenter'] or 0,
                "web": row['web'] or 0
            }

        # ---------------------------------------------------------
        # 6) Construir listas de comparaciones (now vs. before)
        # ---------------------------------------------------------
        labels_cmp = []
        now_chatbot = []
        now_callcenter = []
        now_web = []
        now_total = []

        before_chatbot = []
        before_callcenter = []
        before_web = []
        before_total = []

        for row in result_now:
            fecha = row['fecha']
            fecha_str = formatear_fecha(fecha)
            labels_cmp.append(fecha_str)

            c_now = row['callcenter'] or 0
            ch_now = row['chatbot'] or 0
            w_now = row['web'] or 0
            t_now = c_now + ch_now + w_now

            if fecha in dict_before:
                ch_before = dict_before[fecha]["chatbot"]
                c_before = dict_before[fecha]["callcenter"]
                w_before = dict_before[fecha]["web"]
                t_before = ch_before + c_before + w_before
            else:
                ch_before = 0
                c_before = 0
                w_before = 0
                t_before = 0

            now_chatbot.append(ch_now)
            now_callcenter.append(c_now)
            now_web.append(w_now)
            now_total.append(t_now)

            before_chatbot.append(ch_before)
            before_callcenter.append(c_before)
            before_web.append(w_before)
            before_total.append(t_before)

        # ---------------------------------------------------------
        # 7) Reportes comparativos (callcenter, total, chatbot, web)
        # ---------------------------------------------------------
        # Ejemplo con distintos colores y líneas punteadas para "antes"
        reporte_callcenter = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_callcenter,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#ffa5b550",
                    "borderColor": "#ffa5b5",
                    "fill": True,
                    "data": now_callcenter,
                    "tension": 0.4
                }
            ]
        }

        reporte_total = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_total,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#4bc0c050",
                    "borderColor": "#4bc0c0",
                    "fill": True,
                    "data": now_total,
                    "tension": 0.4
                }
            ]
        }

        reporte_chatbot = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_chatbot,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#36a2eb50",
                    "borderColor": "#36a2eb",
                    "fill": True,
                    "data": now_chatbot,
                    "tension": 0.4
                }
            ]
        }

        reporte_web = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_web,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#ffce5650",
                    "borderColor": "#ffce56",
                    "fill": True,
                    "data": now_web,
                    "tension": 0.4
                }
            ]
        }

        # ---------------------------------------------------------
        # 8) Retorno final con todos los reportes
        # ---------------------------------------------------------
        result_data =  {
            "reporte_basico": reporte_basico,
            "callcenter": reporte_callcenter,
            "total": reporte_total,
            "chatbot": reporte_chatbot,
            "web": reporte_web
        }

        cache_data[cache_key] = result_data
        with open(cache_file, "w", encoding="utf-8") as f:
            # `default=str` para evitar error con objetos datetime, etc.
            json.dump(cache_data, f, ensure_ascii=False, default=str)

        return result_data




    def get_daily_orders_report(self, site_ids: list, start_date: str, end_date: str):
        """
        Ejemplo de reporte adaptado, con caché en archivo JSON.
        Cuando se solicitan los mismos parámetros, se retorna directamente
        del caché en lugar de volver a consultar la base de datos.
        """

        # ------------------------------------------------------------------
        # 0) CONFIGURACIÓN DEL ARCHIVO DE CACHÉ
        # ------------------------------------------------------------------
        #  - Verificamos que exista la carpeta "cache"; si no, la creamos.
        #  - Verificamos que exista el archivo JSON; si no, lo creamos vacío.
        # ------------------------------------------------------------------

        cache_folder = "cache"
        cache_file = os.path.join(cache_folder, "daily_orders_report.json")

        if not os.path.exists(cache_folder):
            os.makedirs(cache_folder)

        # Si no existe el archivo, lo creamos con un dict vacío
        if not os.path.exists(cache_file):
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump({}, f)

        # ------------------------------------------------------------------
        # 1) GENERAR UNA CLAVE DE CACHÉ UNÍVOCA PARA ESTOS PARÁMETROS
        # ------------------------------------------------------------------
        #    - site_ids podría tener distinto orden, así que lo ordenamos
        #    - Usamos un string como "clave" que combine los parámetros
        # ------------------------------------------------------------------

        # Ordenamos site_ids para evitar duplicados por orden distinto
        site_ids_sorted = sorted(site_ids)
        # Creamos la clave (string) a partir de los parámetros
        cache_key = f"{site_ids_sorted}-{start_date}-{end_date}"

        # ------------------------------------------------------------------
        # 2) LEER EL ARCHIVO DE CACHÉ Y VER SI LA CLAVE YA EXISTE
        # ------------------------------------------------------------------
        with open(cache_file, "r", encoding="utf-8") as f:
            cache_data = json.load(f)

        if cache_key in cache_data:
            # Si la clave existe, retornamos inmediatamente lo que está en caché
            return cache_data[cache_key]
        
        # ------------------------------------------------------------------
        # 3) SI LLEGAMOS AQUÍ, NO ESTÁ EN CACHÉ -> HACEMOS LA LÓGICA NORMAL
        # ------------------------------------------------------------------
        
        # -- Conversión de fechas --
        fmt_iso = "%Y-%m-%dT%H:%M:%S.%fZ"
        start_date_dt = datetime.strptime(start_date, fmt_iso)
        end_date_dt = datetime.strptime(end_date, fmt_iso)

        # Intervalo principal
        start_date_str = start_date_dt.strftime("%Y-%m-%d")
        end_date_str = end_date_dt.strftime("%Y-%m-%d")

        # Intervalo "antes"
        start_date_before_dt = start_date_dt - timedelta(days=28)
        end_date_before_dt = end_date_dt - timedelta(days=28)
        start_date_before_str = start_date_before_dt.strftime("%Y-%m-%d")
        end_date_before_str = end_date_before_dt.strftime("%Y-%m-%d")

        # Labels de ejemplo
        label_rango_ahora = formatear_rango_fechas(start_date_dt, end_date_dt)  # p. ej. "10/ene - 15/feb"
        label_rango_antes = formatear_rango_fechas(start_date_before_dt, end_date_before_dt)  # p. ej. "03/ene - 08/feb"

        # ------------------------------------------------------------------
        # 4) CONSULTA "ACTUAL"
        # ------------------------------------------------------------------
        query_now = """
            WITH date_range AS (
                SELECT generate_series(
                    %(start_date)s::date,
                    %(end_date)s::date,
                    '1 day'::interval
                )::date AS fecha
            ),
            daily_orders AS (
                SELECT
                    (order_date - INTERVAL '4 hours')::date AS day,
                    SUM(
                        CASE 
                            WHEN inserted_by = 1082 
                                AND current_status = 'enviada' THEN 1 
                            ELSE 0 
                        END
                    ) AS orders_chatbot,
                    SUM(
                        CASE 
                            WHEN inserted_by != 1082 
                                AND inserted_by IS NOT NULL 
                                AND current_status = 'enviada' THEN 1 
                            ELSE 0 
                        END
                    ) AS orders_callcenter,
                    SUM(
                        CASE 
                            WHEN inserted_by IS NULL 
                                AND current_status = 'enviada' THEN 1 
                            ELSE 0 
                        END
                    ) AS orders_web
                FROM orders.daily_order_sales_view
                WHERE
                    (order_date - INTERVAL '4 hours')::date BETWEEN %(start_date)s AND %(end_date)s
                    AND site_id = ANY(%(site_ids)s)
                GROUP BY 1
            )
            SELECT
                d.fecha,
                COALESCE(o.orders_chatbot, 0) AS chatbot,
                COALESCE(o.orders_callcenter, 0) AS callcenter,
                COALESCE(o.orders_web, 0) AS web
            FROM date_range d
            LEFT JOIN daily_orders o ON d.fecha = o.day
            ORDER BY d.fecha;
        """
        params_now = {
            "site_ids": site_ids,
            "start_date": start_date_str,
            "end_date": end_date_str
        }
        result_now = self.db.execute_query(query=query_now, params=params_now, fetch=True)

        # ------------------------------------------------------------------
        # 5) CONSULTA "ANTES"
        # ------------------------------------------------------------------
        query_before = """
            WITH date_range AS (
                SELECT generate_series(
                    %(start_date_before)s::date,
                    %(end_date_before)s::date,
                    '1 day'::interval
                )::date AS fecha
            ),
            daily_orders AS (
                SELECT
                    (order_date - INTERVAL '4 hours')::date AS day,
                    SUM(
                        CASE 
                            WHEN inserted_by = 1082 
                                AND current_status = 'enviada' THEN 1 
                            ELSE 0 
                        END
                    ) AS orders_chatbot,
                    SUM(
                        CASE 
                            WHEN inserted_by != 1082 
                                AND inserted_by IS NOT NULL 
                                AND current_status = 'enviada' THEN 1 
                            ELSE 0 
                        END
                    ) AS orders_callcenter,
                    SUM(
                        CASE 
                            WHEN inserted_by IS NULL 
                                AND current_status = 'enviada' THEN 1 
                            ELSE 0 
                        END
                    ) AS orders_web
                FROM orders.daily_order_sales_view
                WHERE
                    (order_date - INTERVAL '4 hours')::date BETWEEN %(start_date_before)s AND %(end_date_before)s
                    AND site_id = ANY(%(site_ids)s)
                GROUP BY 1
            )
            SELECT
                d.fecha,
                COALESCE(o.orders_chatbot, 0) AS chatbot,
                COALESCE(o.orders_callcenter, 0) AS callcenter,
                COALESCE(o.orders_web, 0) AS web
            FROM date_range d
            LEFT JOIN daily_orders o ON d.fecha = o.day
            ORDER BY d.fecha;
        """
        params_before = {
            "site_ids": site_ids,
            "start_date_before": start_date_before_str,
            "end_date_before": end_date_before_str
        }
        result_before = self.db.execute_query(query=query_before, params=params_before, fetch=True)

        # ------------------------------------------------------------------
        # 6) Reporte básico
        # ------------------------------------------------------------------
        labels_basico = []
        data_chatbot_basico = []
        data_callcenter_basico = []
        data_web_basico = []
        data_total_basico = []

        for row in result_now:
            fecha_str = formatear_fecha(row['fecha'])
            labels_basico.append(fecha_str)

            chatbot_val = row['chatbot'] or 0
            callcenter_val = row['callcenter'] or 0
            web_val = row['web'] or 0
            total_val = chatbot_val + callcenter_val + web_val

            data_chatbot_basico.append(chatbot_val)
            data_callcenter_basico.append(callcenter_val)
            data_web_basico.append(web_val)
            data_total_basico.append(total_val)

        # Colores (ejemplo)
        color_chatbot = "#36a2eb"
        color_callcenter = "#ff6384"
        color_web       = "#ffce56"
        color_total     = "#4bc0c0"

        datasets_basico = [
            {
                "label": "web",
                "backgroundColor": color_web,
                "borderColor": color_web,
                "data": data_web_basico,
                "tension": 0.4
            },
            {
                "label": "chatbot",
                "backgroundColor": color_chatbot,
                "borderColor": color_chatbot,
                "data": data_chatbot_basico,
                "tension": 0.4
            },
            {
                "label": "callcenter",
                "backgroundColor": color_callcenter,
                "borderColor": color_callcenter,
                "data": data_callcenter_basico,
                "tension": 0.4
            },
            {
                "label": "total",
                "backgroundColor": color_total,
                "borderColor": color_total,
                "data": data_total_basico,
                "tension": 0.4
            }
        ]
        reporte_basico = {
            "labels": labels_basico,
            "datasets": datasets_basico
        }

        # ------------------------------------------------------------------
        # 7) Mapeo "antes" a dict
        # ------------------------------------------------------------------
        dict_before = {}
        for row in result_before:
            fecha_actual = row['fecha'] + timedelta(days=28)
            dict_before[fecha_actual] = {
                "chatbot": row['chatbot'] or 0,
                "callcenter": row['callcenter'] or 0,
                "web": row['web'] or 0
            }

        # ------------------------------------------------------------------
        # 8) Construir comparaciones
        # ------------------------------------------------------------------
        labels_cmp = []
        now_callcenter = []
        now_total = []
        now_chatbot = []
        now_web = []

        before_callcenter = []
        before_total = []
        before_chatbot = []
        before_web = []

        for row in result_now:
            fecha = row['fecha']
            fecha_str = formatear_fecha(fecha)
            labels_cmp.append(fecha_str)

            c_now = row['callcenter'] or 0
            ch_now = row['chatbot'] or 0
            w_now = row['web'] or 0
            t_now = c_now + ch_now + w_now

            if fecha in dict_before:
                ch_before = dict_before[fecha]["chatbot"]
                c_before = dict_before[fecha]["callcenter"]
                w_before = dict_before[fecha]["web"]
                t_before = ch_before + c_before + w_before
            else:
                ch_before = 0
                c_before = 0
                w_before = 0
                t_before = 0

            now_callcenter.append(c_now)
            now_total.append(t_now)
            now_chatbot.append(ch_now)
            now_web.append(w_now)

            before_callcenter.append(c_before)
            before_total.append(t_before)
            before_chatbot.append(ch_before)
            before_web.append(w_before)

        # ------------------------------------------------------------------
        # 9) Reportes de comparación: callcenter, total, chatbot, web
        # ------------------------------------------------------------------
        reporte_callcenter = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,  # p. ej. "03/ene - 08/feb"
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_callcenter,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,  # p. ej. "10/ene - 15/feb"
                    "backgroundColor": "#ffa5b550",
                    "borderColor": "#ffa5b5",
                    "data": now_callcenter,
                    "fill": True,
                    "tension": 0.4
                }
            ]
        }

        reporte_total = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_total,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#4bc0c050",
                    "borderColor": "#4bc0c0",
                    "data": now_total,
                    "fill": True,
                    "tension": 0.4
                },
            ]
        }

        reporte_chatbot = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderColor": "#000",
                    "borderDash": [5, 5],
                    "data": before_chatbot,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#36a2eb50",
                    "borderColor": "#36a2eb",
                    "data": now_chatbot,
                    "fill": True,
                    "tension": 0.4
                },
            ]
        }

        reporte_web = {
            "labels": labels_cmp,
            "datasets": [
                {
                    "label": label_rango_antes,
                    "backgroundColor": "#00000050",
                    "borderDash": [5, 5],
                    "borderColor": "#000",
                    "data": before_web,
                    "tension": 0.4
                },
                {
                    "label": label_rango_ahora,
                    "backgroundColor": "#ffce5650",
                    "borderColor": "#ffce56",
                    "fill": True,
                    "data": now_web,
                    "tension": 0.4
                },
            ]
        }

        # ------------------------------------------------------------------
        # 10) Armamos el resultado final
        # ------------------------------------------------------------------
        result_data = {
            "reporte_basico": reporte_basico,
            "reporte_callcenter": reporte_callcenter,
            "reporte_total": reporte_total,
            "reporte_chatbot": reporte_chatbot,
            "reporte_web": reporte_web
        }

        # ------------------------------------------------------------------
        # 11) GUARDAR EN EL CACHÉ Y RETORNAR
        # ------------------------------------------------------------------
        cache_data[cache_key] = result_data
        with open(cache_file, "w", encoding="utf-8") as f:
            # `default=str` para evitar error con objetos datetime, etc.
            json.dump(cache_data, f, ensure_ascii=False, default=str)

        return result_data



    def get_orders_by_site_and_responsible_transfer(self, site_ids: list, fecha_inicio: str, fecha_fin: str):
            """
            Genera un reporte de órdenes atendidas por transferencia agrupadas por sede y responsable.
            Las órdenes seleccionadas tienen payment_method_id = 6 y authorized = true.
            El reporte incluye una columna por cada responsable y una columna total.

            :param site_ids: Lista de IDs de sitios a filtrar.
            :param fecha_inicio: Fecha de inicio en formato 'YYYY-MM-DD'.
            :param fecha_fin: Fecha de fin en formato 'YYYY-MM-DD'.
            :return: Lista de diccionarios con el reporte.
            """
            # ------------------------------------------------------------------
            # 0) CONFIGURACIÓN DEL ARCHIVO DE CACHÉ
            # ------------------------------------------------------------------
            cache_folder = "cache"
            cache_file = os.path.join(cache_folder, "orders_by_site_and_responsible_transfer.json")

            if not os.path.exists(cache_folder):
                os.makedirs(cache_folder)

            # Si no existe el archivo, lo creamos con un dict vacío
            if not os.path.exists(cache_file):
                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump({}, f)

            # ------------------------------------------------------------------
            # 1) GENERAR UNA CLAVE DE CACHÉ ÚNICA PARA ESTOS PARÁMETROS
            # ------------------------------------------------------------------
            site_ids_sorted = sorted(site_ids)
            cache_key = f"{site_ids_sorted}-{fecha_inicio}-{fecha_fin}"

            # ------------------------------------------------------------------
            # 2) LEER EL ARCHIVO DE CACHÉ Y VER SI LA CLAVE YA EXISTE
            # ------------------------------------------------------------------
            with open(cache_file, "r", encoding="utf-8") as f:
                cache_data = json.load(f)

            if cache_key in cache_data:
                # Si la clave existe, retornamos lo que está en caché
                return cache_data[cache_key]

            # ------------------------------------------------------------------
            # 3) CONSULTA A LA BASE DE DATOS
            # ------------------------------------------------------------------
            query = """
                SELECT 
                    site_name,
                    COALESCE(name, 'Sin Responsable') AS responsible_name,
                    COUNT(*) AS order_count
                FROM orders.combined_order_view
                WHERE 
                    payment_method_id = 6
                    AND authorized = true
                    AND rol_id = 40
                    AND latest_status_timestamp BETWEEN %(fecha_inicio)s AND %(fecha_fin)s
                    AND site_id = ANY(%(site_ids)s)
                    
                GROUP BY site_name, responsible_name
                ORDER BY site_name, responsible_name;
            """

            params = {
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin,
                "site_ids": site_ids_sorted
            }

            result = self.db.execute_query(query=query, params=params, fetch=True)

            # ------------------------------------------------------------------
            # 4) PROCESAMIENTO DE LOS DATOS PARA EL PIVOTE
            # ------------------------------------------------------------------
            # Identificar todos los responsables únicos
            responsables_set = set()
            for row in result:
                responsables_set.add(row['responsible_name'])

            responsables = sorted(responsables_set)  # Ordenar alfabéticamente

            # Crear una lista de diccionarios para cada sede
            sede_dict = defaultdict(lambda: {responsible: 0 for responsible in responsables})
            for row in result:
                sede = row['site_name']
                responsible = row['responsible_name']
                count = row['order_count']
                sede_dict[sede][responsible] += count

            # Construir la lista final con totales
            final_report = []
            for sede, counts in sede_dict.items():
                entry = {"sede": sede}
                total = 0
                for responsible in responsables:
                    entry[responsible] = counts[responsible]
                    total += counts[responsible]
                entry["total"] = total
                final_report.append(entry)

            # ------------------------------------------------------------------
            # 5) GUARDAR EN EL CACHÉ Y RETORNAR
            # ------------------------------------------------------------------
            cache_data[cache_key] = final_report
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, ensure_ascii=False, default=str)

            return final_report