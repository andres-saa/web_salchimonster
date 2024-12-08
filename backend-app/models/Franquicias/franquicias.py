
from db.db import Db as DataBase
from schema.franquicias.franquicias import Franquicias

class Franquis:
    
    def __init__(self):
        self.db = DataBase()
        
        
    def create_franquicia_request(self, data: Franquicias):
        # Define una subclase para incluir el user_id en el esquema de PQR
        query, params = self.db.build_insert_query(table_name='franquicias.pre_registration',data=data,returning='id')
        result = self.db.execute_query(query=query,params=params,fetch=True)
        return result

            
    def get_franquicia_request(self):
        # Define una subclase para incluir el user_id en el esquema de PQR
        query = self.db.build_select_query(table_name='franquicias.franquicias_view',fields=["*"],order_by='created_at')
        result = self.db.fetch_all(query=query)
        return result


    def change_status(self,data:Franquicias,id:int):
        # Define una subclase para incluir el user_id en el esquema de PQR
        query, params = self.db.build_update_query(table_name="franquicias.pre_registration ",data=data,condition=f"id = {id}",returning='id  ')
        result = self.db.execute_query(query=query, params=params,fetch=True)
        return result


