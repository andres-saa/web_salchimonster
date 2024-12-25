
from db.db import Db as DataBase
from pydantic import BaseModel
from schema.pqr import pqrs
from schema.user import user_schema_post
from models.orders.order2 import Order2




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
    
        
    def get_all_networks(self):
        query = self.db.build_select_query(table_name='pqr.networks',fields=["*"])
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
    
    def get_pqrs_by_date_range(self, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene las PQRs por sede y estado en un rango de fechas, incluyendo estados sin registros (con valor 0),
        y agrega tanto una columna "total" en cada sede como una fila final "total" con la suma de los valores por estado.
        
        :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD)
        :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD)
        :return: Lista de JSON planos agrupados por sede, incluyendo un total general.
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
                COUNT(pqr.pqr_request_id) AS cantidad
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
            jsonb_object_agg(estado, cantidad) || jsonb_build_object('sede', sede) AS result
        FROM state_counts
        GROUP BY sede
        ORDER BY sede;
        """
        params = {
            "fecha_inicio": f"{fecha_inicio} 00:00:00",
            "fecha_fin": f"{fecha_fin} 23:59:59"
        }
        result = self.db.execute_query(query=query, params=params, fetch=True)

        # Convertir el resultado SQL en una lista de Python
        data = [row["result"] for row in result]

        # 1. Agregar la columna "total" a cada sede (la suma de sus estados)
        for entry in data:
            row_sum = 0
            for key, value in entry.items():
                if key != "sede":  # Ignoramos la clave "sede" al sumar
                    row_sum += value
            entry["total"] = row_sum

        # 2. Calcular la fila de totales globales
        total_entry = {"sede": "total"}
        for entry in data:
            for key, value in entry.items():
                if key not in ("sede", "total"):  # Sumamos solo los estados, no la clave "total" del propio entry
                    total_entry[key] = total_entry.get(key, 0) + value

        # 3. Agregar la columna "total" también en la fila final
        global_sum = 0
        for key, value in total_entry.items():
            if key != "sede":  # Excluimos la clave "sede" (que es "total")
                global_sum += value
        total_entry["total"] = global_sum

        # 4. Agregar la fila de totales al final de la lista
        data.append(total_entry)

        return data







    def get_pqrs_by_date_range_and_type(self, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene las PQRs por sede y etiqueta (tag) en un rango de fechas, incluyendo etiquetas sin registros (con valor 0),
        y agrega una fila "total" con la suma de los valores por etiqueta.
        :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD)
        :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD)
        :return: Lista de JSON planos agrupados por sede, incluyendo un total general.
        """
        query = self.db.cargar_archivo_sql('./sql/get_pqrs_by_date_range_and_type.sql')
        params = {"fecha_inicio": f"{fecha_inicio} 00:00:00", "fecha_fin": f"{fecha_fin} 23:59:59"}
        result = self.db.execute_query(query=query, params=params, fetch=True)

        # Convertir el resultado SQL en una lista de Python
        data = []
        for row in result:
            sede = row['sede']
            tags = row['tags']
            # Crear un diccionario con 'sede' como primer elemento
            ordered_entry = {"sede": sede}
            ordered_entry.update(tags)  # Agregar las demás claves
            data.append(ordered_entry)

        # Calcular totales
        total_entry = {"sede": "TOTAL"}
        for entry in data:
            for key, value in entry.items():
                if key != "sede":  # Saltar la clave 'sede'
                    total_entry[key] = total_entry.get(key, 0) + value

        # Agregar el total al final de la lista
        data.append(total_entry)

        return data



    def get_pqrs_by_responsible_and_state(self, fecha_inicio: str, fecha_fin: str):
        """
        Obtiene las PQRs por responsable y estado en un rango de fechas, incluyendo estados sin registros (con valor 0),
        y agrega una fila "total" con la suma de los valores por estado y otra columna "total" con la suma de los estados por responsable.
        Además, las PQRs sin responsable se marcan con 'responsible_name' = 'pendiente' y, si no tienen estado, 
        se les asigna el estado 'generada' (ya existente en la tabla pqr.pqr_status).
        
        :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD)
        :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD)
        :return: Lista de JSON planos agrupados por responsable, incluyendo un total general.
        """

        query = self.db.cargar_archivo_sql('./sql/get_pqrs_by_responsible_and_state.sql')

        params = {
            "fecha_inicio": f"{fecha_inicio} 00:00:00",
            "fecha_fin": f"{fecha_fin} 23:59:59"
        }
        result = self.db.execute_query(query=query, params=params, fetch=True)

        # Convertir el resultado SQL en una lista de Python
        data = [row['result'] for row in result]

        # Reestructurar cada entrada para asegurar que 'responsible_name' sea la primera clave
        structured_data = []
        for entry in data:
            ordered_entry = {"responsible_name": entry["responsible_name"]}
            for key, value in entry.items():
                if key != "responsible_name":
                    ordered_entry[key] = value
            structured_data.append(ordered_entry)

        # Calcular totales por estado (fila "total")
        total_entry = {"responsible_name": "total"}

        # Añadimos la columna "total" (suma de sus estados) a cada responsable.
        for entry in structured_data:
            sum_for_responsible = 0
            for key, value in entry.items():
                if key != "responsible_name":  
                    sum_for_responsible += value
                    # Vamos acumulando en el total_entry por estado
                    total_entry[key] = total_entry.get(key, 0) + value
            # Agregamos la columna total a cada responsable
            entry["total"] = sum_for_responsible

        # Calculamos la suma "total" para la fila "total" (la suma de todos los estados)
        sum_for_all = 0
        for key, value in total_entry.items():
            if key not in ("responsible_name", "total"):
                sum_for_all += value
        total_entry["total"] = sum_for_all

        # Agregar la fila de totales al final
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
    

    
    
