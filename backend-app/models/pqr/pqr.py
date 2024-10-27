
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
            network_id = data.network_id
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
        
        return {'pqr_id': pqr_id, 'initial_status_id': result_status}
    
    
    def get_all_pqrs(self):
        query = self.db.build_select_query(table_name='pqr.pqr_details_full_view',fields=["*"])
        pqr_id = self.db.execute_query(query=query,fetch=True)
        return pqr_id
    
        
    def get_all_networks(self):
        query = self.db.build_select_query(table_name='pqr.networks',fields=["*"])
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
        query = self.db.build_select_query(table_name='pqr.pqr_status',fields=["*"])
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
    

    
    
