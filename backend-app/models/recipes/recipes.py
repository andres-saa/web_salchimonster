from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sesion import Sesion as sesion_schema, SesionUpdate as sesion_update_schema
from schema.recipes.recipe_data_seet import RecipeDataSheet,RecipeDataSheetPost,RecipeDataSheetUpdate,cdi_percent,update_cdi_percent,updateLastPurchasePrice
from schema.recipes.ingredients import RecipeDataIngredients
from schema.video_training.user_sequence import ReplaceUserSequencesInput
from schema.video_training.video import markVideo
from datetime import time
from typing import Dict, List

class Recipe:
    def __init__(self):
        self.db = DataBase()



    def create_cdi_percent_price(self,data:cdi_percent):
        query , params = self.db.build_insert_query('inventory.cdi_percent_prices',data,'id')
        return self.db.execute_query(query,params,True)
    

    
    

    def delete_cdi_percent_price(self, id: int):
        # Paso 1: Verificar cuántos registros existen para el `percent_price` dado.
        query_check = self.db.build_select_query(
            table_name='inventory.cdi_percent_prices',
            fields=['COUNT(*) AS count']
            
        )
        result_check = self.db.fetch_all(query_check)
        
        if not result_check or result_check[0]['count'] <= 1:
            # Si solo hay uno o ninguno, no se permite eliminar.
            raise Exception(f"Cannot delete `cdi_percent_price` with id {id}. It must have more than one record.")
        
        # Paso 2: Proceder con la eliminación si hay más de uno.
        query_delete = self.db.build_delete_query('inventory.cdi_percent_prices', f'id = {id}', 'id')
        return self.db.execute_query(query=query_delete, fetch=True)
    

    def update_bulk_last_price(self,data:List[updateLastPurchasePrice]):

        # query, params = self.db.build_bulk_update_query(table_name='inventory.purchase_prices',data_list=data, id_field='ingredient_id', returning='id')
        # return self.db.execute_bulk_update(query=query,params=params,fetch=True)
    
        # print(query)

        for item in data:
            query=f'UPDATE inventory.purchase_prices set last_price_purchase = %s where ingredient_id = %s'
            self.db.execute_query(query, [item.last_price_purchase, item.ingredient_id])


    def set_main_percent_to_sell(self, id: int):
        # Paso 1: Establecer todos los registros en 'main' a False
        query_update_all = self.db.build_update_query(
            table_name='inventory.cdi_percent_prices',
            data=update_cdi_percent(main=False),
            condition='1=1'  # Actualiza todos los registros
        )
        self.db.execute_query(query_update_all[0], query_update_all[1])

        # Paso 2: Establecer el registro con el ID dado en 'main' a True
        query_update_one = self.db.build_update_query(
            table_name='inventory.cdi_percent_prices',
            data=update_cdi_percent(main=True),
            condition=f'id = {id}',
            returning='id'
        )
        return self.db.execute_query(query_update_one[0], query_update_one[1], True)

    def close_connection(self):
        self.db.conn.close()
        

    def get_all_recipes(self):
        query = self.db.build_select_query(table_name='recipes.recipe',fields=['*'],order_by='id')
        return self.db.fetch_all(query)
    

    def get_cdi_prices_table(self):
        query = self.db.build_select_query(table_name='recipes.ingredient_main_value',fields=['*'],)
        return self.db.fetch_all(query)
    

    def get_cdi_percent_prices(self):
        query = self.db.build_select_query(table_name='inventory.cdi_percent_prices',fields=['*'],order_by='id')
        return self.db.fetch_all(query)

    def get_all_get_summary_benefit(self):
        query = self.db.build_select_query(table_name='recipes.summary_benefit',fields=['*'],order_by='category_name')
        return self.db.fetch_all(query)
    

    def get_all_recipes_enabled(self):
        query = self.db.build_select_query(table_name='recipes.recipe',fields=['*'],condition='has_recipe = true',order_by='id')
        return self.db.fetch_all(query)


    def get_recipe_data_sheet_by_product_id(self, id: int) -> Dict[str, List[Dict]]:
    # Primero, verificamos si el producto existe en la tabla inventory.products y si tiene has_recipe en true
        query_check_product = self.db.build_select_query(
            table_name='inventory.products',
            fields=['has_recipe'],
            condition=f'id = {id}'
        )
        product_result = self.db.fetch_all(query_check_product)
        
        if not product_result or not product_result[0]['has_recipe']:
            raise Exception(f"Product with id {id} does not exist or has no recipe")

        # Intentamos obtener el recipe_data_sheet para el product_id
        query = self.db.build_select_query(
            table_name='recipes.recipe_data_sheet_view',
            fields=['*'],
            condition=f'product_id = {id}'
        )
        result = self.db.fetch_all(query)
        
        if not result:
            # Crear un nuevo recipe_data_sheet con valores predeterminados
            new_data_sheet = RecipeDataSheetPost(
                product_id=id,
                portion_size=0,
                portion_number=0,
                preparation_time='00:00:00',
                cooking_time='00:00:00',
                service_temperature=0,
                selling_price=0,
                taxes=0,
                presentation="",
                preparation_equipment="",
                elaboration=""
            )

            self.create_recipe_data_sheet(new_data_sheet)
            # Volvemos a intentar obtener el recipe_data_sheet recién creado
            query = self.db.build_select_query(
                table_name='recipes.recipe_data_sheet_view',
                fields=['*'],
                condition=f'product_id = {id}'
            )
            result = self.db.fetch_all(query)
        
        # Si aún no tenemos datos, lanzamos un error
        if not result:
            raise Exception(f"Failed to retrieve or create recipe data sheet for product_id {id}")
        
        recipe_data_sheet_id = result[0]['id']
        query2 = self.db.build_select_query(
            table_name='recipes.recipe_ingredients_view',
            fields=['*'],
            condition=f'recipe_data_sheet_id = {recipe_data_sheet_id}',order_by='id'
        )
        ingredients = self.db.fetch_all(query2)
        
        return {'recipe_data_sheet': result[0], 'ingredients': ingredients}

    

    def create_recipe_data_sheet(self,data:RecipeDataSheetPost):
        query , params = self.db.build_insert_query('recipes.recipe_data_sheet',data,'id')
        return self.db.execute_query(query,params,True)
    

    def create_recipe_data_ingredient(self,data:RecipeDataIngredients):
        query, params = self.db.build_insert_query('recipes.recipe_data_ingredient',data,'id')
        return self.db.execute_query(query=query, params=params,fetch=True)
    
    def delete_recipe_data_ingredient(self,id):
        query = 'DELETE from recipes.recipe_data_ingredient where id = %s'
        return self.db.execute_query(query=query,params=[id])
    
    def update_recipe_data_ingredient(self,id,data:RecipeDataIngredients):
        query, params = self.db.build_update_query('recipes.recipe_data_ingredient',data,f'id = {id}','id')
        return self.db.execute_query(query=query,params=params,fetch=True)
    

    def update_recipe_data_sheet(self,id:int,data:RecipeDataSheetUpdate):
        query, params = self.db.build_update_query(
            table_name='recipes.recipe_data_sheet',
            data=data, 
            condition=f'id = {id}',
            returning='id')
        return self.db.execute_query(query,params,True)


    def toggle_product_to_recipe(self,id:int,status:bool):
        query=f'UPDATE inventory.products SET has_recipe = %s where id = %s returning id'
        return self.db.execute_query(query,[status,id],True)


    def close_connection(self):
        self.db.conn.close()