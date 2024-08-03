from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sesion import Sesion as sesion_schema, SesionUpdate as sesion_update_schema
from schema.recipes.recipe_data_seet import RecipeDataSheet,RecipeDataSheetPost,RecipeDataSheetUpdate
from schema.recipes.ingredients import RecipeDataIngredients
from schema.video_training.user_sequence import ReplaceUserSequencesInput
from schema.video_training.video import markVideo
from datetime import time
from typing import Dict, List

class Recipe:
    def __init__(self):
        self.db = DataBase()


    def get_all_recipes(self):
        query = self.db.build_select_query(table_name='recipes.recipe',fields=['*'],order_by='id')
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

    




    # def get_recipe_data_sheet_by_product_id(self,id):
    #     query = self.db.build_select_query(table_name='recipes.recipe_data_sheet',fields=['*'],condition=f'product_id = {id}')
    #     result = self.db.fetch_all(query)
    #     recipe_data_sheet_id = result[0]['id']
    #     query2 = self.db.build_select_query(table_name='recipes.recipe_ingredients_view',fields=['*'],condition=f'recipe_data_sheet_id = {recipe_data_sheet_id}')
    #     ingredients = self.db.fetch_all(query2)
    #     return {'recipe_data_sheet':result , 'ingredients':ingredients}
    

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