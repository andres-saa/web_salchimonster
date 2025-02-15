
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
    data:Dict
    
class Price(BaseModel):
    id:int
    mayor:int
    distribuidor:int
    
    
class UpdatePrices(BaseModel):
    prices:List[Price]

class Distrimonster:
    
    def __init__(self):
        self.db = DataBase()

    def getMenuDistrimonster(self):
        query = self.db.cargar_archivo_sql('./sql/menu_distrimonster.sql')
        
        print(query)
        result = self.db.fetch_all(query=query)
        return result


    def updateMenu(self, data:Menu):
        query = self.db.cargar_archivo_sql('./sql/insert_menu.sql')
        result = self.db.execute_query_json(query=query,params=[data.data,1],fetch=True)
        query = 'SELECT distrimonster.create_missing_prices()'
        result2 = self.db.execute_query(query=query,fetch=True)
        return result
    
    
    def updatePrices(self, data: UpdatePrices):
        # Cargamos el SQL "update_prices.sql"
        query = self.db.cargar_archivo_sql('./sql/update_prices.sql')
        
        results = []
        for price in data.prices:
            # Ejecutamos la consulta para cada elemento de la lista
            # pasando mayor, distribuidor, id en ese orden
            result = self.db.execute_query_json(
                query=query,
                params=[price.mayor, price.distribuidor, price.id],
                fetch=True
            )
            results.append(result)

        return results

    
    
    