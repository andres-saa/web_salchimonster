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
from schema.recipes.ingredients import IngredientsPost,IngredientsUpdate
from schema.permision.permision import toggle_permision
from datetime import time
from typing import Dict, List

class Permission:
    def __init__(self):
        self.db = DataBase()


    def get_all_rol(self):
        query = self.db.build_select_query(table_name='permission.rol',fields=['*'],condition='exist = true')
        return self.db.fetch_all(query)
    
    def get_all_rol_by_rol_id(self,rol_id):
        query = self.db.build_select_query(table_name='permission.permission_rol',fields=['*'],condition=f"rol_id = {rol_id}")
        return self.db.fetch_all(query)
    

    def toggle_permisssion(self,datos:toggle_permision,id:int,status:bool):
        
        if (status):
            query , params = self.db.build_insert_query(table_name='permission.permission_rol',data=datos,returning='id')
            return self.db.execute_query(query,params,fetch=False)

        

        delete = self.db.build_delete_query(table_name='permission.permission_rol',condition=f"id = {id}")
        self.db.execute_query(delete,params=[]) 
    
    
    def get_all_permission(self):
        query = self.db.build_select_query(table_name='permission.permission',fields=['*'],)
        return self.db.fetch_all(query)
    
    def get_all_permission_group_by_group(self):
        query = self.db.build_select_query(table_name='permission.group_permissions',fields=['*'],)
        return self.db.fetch_all(query)
    
    def get_all_permission_by_employer_id(self,employer_id):
        query = self.db.build_select_query(table_name='permission.permision_employer',fields=['*'],condition=f'employer_id ={employer_id}')
        return self.db.fetch_all(query)
    

    # def create_ingredient(self,data:IngredientsPost):
    #     query , params = self.db.build_insert_query('recipes.ingredient',data,'id')
    #     return self.db.execute_query(query,params,True)
    

    # def update_ingredient(self,id,data:IngredientsUpdate):
    #     query , params = self.db.build_update_query(table_name='recipes.ingredient',data=data,condition=f'id = {id}',returning='id')
    #     return self.db.execute_query(query,params,True)
    
    # def delete_ingredient(self,id):
    #     query  = self.db.build_soft_delete_query(table_name='recipes.ingredient',condition=f'id = {id}',returning='id')
    #     return self.db.execute_query(query,fetch=True)
        
        


    # def get_recipe_data_sheet_by_product_id(self, id: int) -> Dict[str, List[Dict]]:
    # # Primero, verificamos si el producto existe en la tabla inventory.products y si tiene has_recipe en true
    #     query_check_product = self.db.build_select_query(
    #         table_name='inventory.products',
    #         fields=['has_recipe'],
    #         condition=f'id = {id}'
    #     )
    #     product_result = self.db.fetch_all(query_check_product)
        
    #     if not product_result or not product_result[0]['has_recipe']:
    #         raise Exception(f"Product with id {id} does not exist or has no recipe")

    #     # Intentamos obtener el recipe_data_sheet para el product_id
    #     query = self.db.build_select_query(
    #         table_name='recipes.recipe_data_sheet',
    #         fields=['*'],
    #         condition=f'product_id = {id}'
    #     )
    #     result = self.db.fetch_all(query)
        
    #     if not result:
    #         # Crear un nuevo recipe_data_sheet con valores predeterminados
    #         new_data_sheet = RecipeDataSheetPost(
    #             product_id=id,
    #             portion_size=0,
    #             portion_number=0,
    #             preparation_time=time(0, 0),
    #             cooking_time=time(0, 0),
    #             service_temperature=0,
    #             selling_price=0,
    #             taxes=0,
    #             presentation="",
    #             preparation_equipment="",
    #             elaboration=""
    #         )

    #         self.create_recipe_data_sheet(new_data_sheet)
    #         # Volvemos a intentar obtener el recipe_data_sheet recién creado
    #         query = self.db.build_select_query(
    #             table_name='recipes.recipe_data_sheet',
    #             fields=['*'],
    #             condition=f'product_id = {id}'
    #         )
    #         result = self.db.fetch_all(query)
        
    #     # Si aún no tenemos datos, lanzamos un error
    #     if not result:
    #         raise Exception(f"Failed to retrieve or create recipe data sheet for product_id {id}")
        
    #     recipe_data_sheet_id = result[0]['id']
    #     query2 = self.db.build_select_query(
    #         table_name='recipes.recipe_ingredients_view',
    #         fields=['*'],
    #         condition=f'recipe_data_sheet_id = {recipe_data_sheet_id}'
    #     )
    #     ingredients = self.db.fetch_all(query2)
        
    #     return {'recipe_data_sheet': result, 'ingredients': ingredients}

    




    # # def get_recipe_data_sheet_by_product_id(self,id):
    # #     query = self.db.build_select_query(table_name='recipes.recipe_data_sheet',fields=['*'],condition=f'product_id = {id}')
    # #     result = self.db.fetch_all(query)
    # #     recipe_data_sheet_id = result[0]['id']
    # #     query2 = self.db.build_select_query(table_name='recipes.recipe_ingredients_view',fields=['*'],condition=f'recipe_data_sheet_id = {recipe_data_sheet_id}')
    # #     ingredients = self.db.fetch_all(query2)
    # #     return {'recipe_data_sheet':result , 'ingredients':ingredients}
    

    # def create_recipe_data_sheet(self,data:RecipeDataSheetPost):
    #     query , params = self.db.build_insert_query('recipes.recipe_data_sheet',data,'id')
    #     return self.db.execute_query(query,params,True)
    

    # def update_recipe_data_sheet(self,id:int,data:RecipeDataSheetUpdate):
    #     query, params = self.db.build_update_query(
    #         table_name='recipes.recipe_data_sheet',
    #         data=data, 
    #         condition=f'id = {id}',
    #         returning='id')
    #     return self.db.execute_query(query,params,True)


    def close_connection(self):
        self.db.conn.close()