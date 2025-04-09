
from db.db import Db as DataBase
from pydantic import BaseModel
from schema.pqr import pqrs
from schema.user import user_schema_post
from models.orders.order2 import Order2
from datetime import datetime, timedelta
from typing import Dict, List
import json
import os
from collections import defaultdict


class Menu(BaseModel):
    data:list[Dict]
    local_id:int
    
class Producto(BaseModel):
    producto_id:int
    english_description:str
    english_name: str
    index: int
    last_price:float
    

class UpdatePrices(BaseModel):
    productos:List[Producto]
    
    
    
class Users(BaseModel):
    user_id:int
    user_name:str
    user_phone:str
    cedula_nit:str
    email:str
    first_last_name:str
    second_last_name:str
    second_name:str
    visible:str

class UpdateUsers(BaseModel):
    users:List[Users]


class Categoria(BaseModel):
    categoria_id:int
    index:int
    visible:bool
    

class UpdateCategorias(BaseModel):
    categorias:List[Categoria]

class Tiendas:
    
    def __init__(self):
        self.db = DataBase()

    def getMenu(self):
        query = self.db.cargar_archivo_sql('./sql/menu.sql')
        print(query)
        result = self.db.fetch_all(query=query)
        return result




    
    def getUnitMeasures(self):
        query1 = "SELECT id, name FROM distrimonster.unit_measures;"
    
        result1 = self.db.fetch_all(query=query1)
        
        query2 = "SELECT id, name FROM distrimonster.presentation_unit_measures;"

        result2 = self.db.fetch_all(query=query2)

        return {"unit_measures":result1, "presentation_measures":result2}



    def updateMenu(self, data:Menu):
        query = self.db.cargar_archivo_sql('./sql/insert_menu.sql')
        result = self.db.execute_query_json(query=query,params=[data.data,data.local_id],fetch=True)
        # query = 'SELECT distrimonster.create_missing_prices()'
        # result2 = self.db.execute_query(query=query,fetch=True)
        return result
    
    
    def updatePrices(self, data: UpdatePrices):
        # Cargamos el SQL "update_prices.sql"
        query = self.db.cargar_archivo_sql('./sql/update_prices.sql')
        
        results = []
        for producto in data.productos:
            # Ejecutamos la consulta para cada elemento de la lista
            # pasando mayor, distribuidor, id en ese orden
            result = self.db.execute_query_json(
                query=query,
                params=[producto.index,producto.english_name, producto.english_description, producto.last_price, producto.producto_id],
                fetch=True
            )
            results.append(result)

        return results
    
    
    
    
    def update_categorias(self, data: UpdateCategorias):
        # Cargamos el SQL "update_prices.sql"
        query = self.db.cargar_archivo_sql('./sql/update_categorias.sql')
        
        results = []
        for categoria in data.categorias:
            # Ejecutamos la consulta para cada elemento de la lista
            # pasando mayor, distribuidor, id en ese orden
            result = self.db.execute_query(
                query=query,
                params=[categoria.index,categoria.visible, categoria.categoria_id],
                fetch=True
            )
            results.append(result)

        return results
    
    
    
    
    
    def updateCategory(self, english_name:str,categoria_id:int):
        # Cargamos el SQL "update_prices.sql"
        query = self.db.cargar_archivo_sql('./sql/update_category.sql')

        result = self.db.execute_query(
                query=query,
                params=[english_name,categoria_id ],
                fetch=True
            )


        return result



    def getMenu(self, local_id:int):
        query = self.db.cargar_archivo_sql('./sql/menu.sql')
        
        print(query)
        result = self.db.fetch_all(query=query,params= [local_id])
        return result




    
    
        
    def updateUsers(self, data: UpdateUsers):
        # Cargamos el SQL "update_prices.sql"
        query = self.db.cargar_archivo_sql('./sql/update_users.sql')
        
        results = []
        
        for user in data.users:
            # Ejecutamos la consulta para cada elemento de la lista
            # pasando mayor, distribuidor, id en ese orden
            
            
            result = self.db.execute_query(
                query=query,
                params=[user.user_name,user.user_phone, user.cedula_nit, user.email, user.first_last_name, user.second_last_name, user.second_name, user.visible,user.user_id ],
                fetch=True
            )
            results.append(result)

        return results

    
    