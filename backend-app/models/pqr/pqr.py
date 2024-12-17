
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
        y agrega una fila "total" con la suma de los valores por estado.
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
        params = {"fecha_inicio": f"{fecha_inicio} 00:00:00", "fecha_fin": f"{fecha_fin} 23:59:59"}
        result = self.db.execute_query(query=query, params=params, fetch=True)

        # Convertir el resultado SQL en una lista de Python
        data = [row['result'] for row in result]

        # Calcular totales
        total_entry = {"sede": "total"}
        for entry in data:
            for key, value in entry.items():
                if key != "sede":  # Saltar la clave 'sede'
                    total_entry[key] = total_entry.get(key, 0) + value

        # Agregar el total al final de la lista
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
        query = """
        WITH all_tags AS (
            SELECT DISTINCT name AS tag_name
            FROM pqr.pqr_tag
        ),
        all_sites AS (
            SELECT DISTINCT site_name
            FROM pqr.pqr_details_full_view
        ),
        tag_counts AS (
            SELECT 
                s.site_name AS sede,
                t.tag_name AS tipo,
                COUNT(pqr.pqr_request_id) AS cantidad
            FROM all_sites s
            CROSS JOIN all_tags t
            LEFT JOIN pqr.pqr_details_full_view pqr
                ON pqr.site_name = s.site_name
                AND pqr.tag_name = t.tag_name
                AND TO_TIMESTAMP(pqr.current_status->>'timestamp', 'DD-MM-YYYY HH12:MI am')
                    BETWEEN %(fecha_inicio)s AND %(fecha_fin)s
            GROUP BY s.site_name, t.tag_name
        )
        SELECT 
            sede,
            jsonb_object_agg(tipo, cantidad) AS tags
        FROM tag_counts
        GROUP BY sede
        ORDER BY sede;
        """
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
    

    
    
