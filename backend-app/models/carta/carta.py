from db.db import Db as DataBase
from pydantic import BaseModel
from typing import List, Optional




class CartaSchema(BaseModel):
    index: int
    img_identifier: str
    carta_id:int

class CartaReorderSchema(BaseModel):
    cartas: List[CartaSchema]


class Carta:
    
    
    def __init__(self):
        self.db = DataBase()
    


    def create_carta(self, data: CartaSchema):
        query, params = self.db.build_insert_query(
            table_name='app.carta_image',
            data=data,
            returning='id'
        )
        result = self.db.execute_query(query=query, params=params, fetch=True)
        return result

    def get_carta(self,carta_id:int):
        query = self.db.build_select_query(
            'app.carta_image',
            fields=["*"],
            order_by='id',
              condition=f'exist = true and carta_id = {carta_id}'  # Ordenar por id
        )
        result = self.db.execute_query(query=query,fetch=True)
        return result
    
    
    
    def get_cartas(self):
        query = self.db.build_select_query(
            'app.carta',
            fields=["*"],
            order_by='id' # Ordenar por id
        )
        result = self.db.execute_query(query=query,fetch=True)
        return result
    
    
    

    
    
        
    
    def get_cartas_all(self):
        query = self.db.build_select_query(
            'app.vista_cartas',
            fields=["*"],
            order_by='id' # Ordenar por id
        )
        result = self.db.execute_query(query=query,fetch=True)
        return result
    

    def get_carta_by_id(self, carta_id: int):
        query = self.db.build_select_query(
            'app.carta_app',
            fields=["*"],
            condition=f'id = {carta_id}'
        )
        result = self.db.fetch_one(query=query)
        return result
    
    
    

    def update_carta(self, carta_id: int, data: CartaSchema):
        query, params = self.db.build_update_query(
            table_name='app.carta_image',
            data=data,
            condition=f'id = {carta_id}',
            returning='id'
        )
        result = self.db.execute_query(query=query, params=params, fetch=True)
        return result

    def delete_carta(self, carta_id: int):
        query = self.db.build_soft_delete_query(
            'app.carta_image',
            condition=f'id = {carta_id}',
            returning='id'
        )
        result = self.db.execute_query(query=query, fetch=True)
        return result

    # Método para reordenar cartas
    def reorder_cartas(self, cartas: List[CartaSchema]):
        # Construir la consulta para actualizar múltiples filas en una sola operación
        update_queries = []
        for carta in cartas:
            update_queries.append(
                f"UPDATE app.carta_image SET index = {carta.index} WHERE id = {carta.id}"
            )
        
        # Unir todas las consultas en un solo comando usando un punto y coma
        final_query = ";\n".join(update_queries)
        
        # Ejecutar la consulta final
        self.db.execute_query(query=final_query, fetch=False)
        return {"status": "success", "message": "cartas reordered successfully"}


