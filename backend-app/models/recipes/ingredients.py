from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sesion import Sesion as sesion_schema, SesionUpdate as sesion_update_schema
from schema.recipes.recipe_data_seet import RecipeDataSheet,RecipeDataSheetPost,RecipeDataSheetUpdate
from schema.video_training.user_sequence import ReplaceUserSequencesInput
from schema.video_training.video import markVideo
from schema.recipes.ingredients import IngredientsPost,IngredientsUpdate,cdi_price
from datetime import time
from typing import Dict, List

class Ingredient:
    def __init__(self):
        self.db = DataBase()



    def get_cdi_prices_table(self):
        query = self.db.build_select_query(table_name='recipes.ingredient_main_value',fields=['*'],)
        return self.db.fetch_all(query)

    def get_all_ingredients(self):
        query = self.db.build_select_query(table_name='recipes.ingredient_view',fields=['*'],order_by='name')
        return self.db.fetch_all(query)
    

    def get_summary_benefit(self):
        query = self.db.build_select_query(table_name='recipes.summary_benefit',fields=['*'],)
        return self.db.fetch_all(query)
    

    def create_ingredient(self,data:IngredientsPost):
        query , params = self.db.build_insert_query('recipes.ingredient',data,'id')
        Ingredient_id =  self.db.execute_query(query,params,True)

        ingredint_price = cdi_price(
                ingredient_id = Ingredient_id[0]["id"] ,
                last_price_purchase = data.purchasing_price,
                iva = data.iva
        )







        query2 , params2 = self.db.build_insert_query('inventory.purchase_prices',ingredint_price,'id')
        price_id =  self.db.execute_query(query2,params2,True)

        return price_id
    

    def update_ingredient(self,id,data:IngredientsUpdate):
        query , params = self.db.build_update_query(table_name='recipes.ingredient',data=data,condition=f'id = {id}',returning='id')
        return self.db.execute_query(query,params,True)
    
    def delete_ingredient(self,id):
        query  = self.db.build_soft_delete_query(table_name='recipes.ingredient',condition=f'id = {id}',returning='id')
        return self.db.execute_query(query,fetch=True)
        



    def close_connection(self):
        self.db.conn.close()