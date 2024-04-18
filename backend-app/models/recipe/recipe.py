import psycopg2
from typing import Optional
from dotenv import load_dotenv
import os
from schema.recipe import Recipe
from models.product import Product
load_dotenv()
import datetime
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



class RecipeManager:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def create_recipe(self, recipe: Recipe):
        # Insertar la receta en la tabla de recetas
        insert_query = f"""
        INSERT INTO recipe.recipes (product_id) VALUES ({recipe.product_id}) RETURNING id;
        """
        self.cursor.execute(insert_query)
        recipe_id = self.cursor.fetchone()[0]  # Obtener el ID de la receta insertada

        # Obtener la fecha actual en formato 'YYYY-MM-DD'
        current_date = datetime.date.today().strftime('%Y-%m-%d')

        # Insertar una hoja de datos vacía (o con valores predeterminados) para la nueva receta, incluyendo la fecha actual
        insert_data_sheet_query = f"""
        INSERT INTO recipe.recipe_data_sheet (recipe_id, date, portion_number) VALUES ({recipe_id}, '{current_date}',{1});
        """
        self.cursor.execute(insert_data_sheet_query)
        
        self.conn.commit()  # Confirmar ambas inserciones
        return recipe_id

    def get_recipe_by_id(self, recipe_id: int):
        select_query = "SELECT * FROM recipe.recipe_product_category WHERE recipe_id = %s;"
        self.cursor.execute(select_query, (recipe_id,))
        columns = [desc[0] for desc in self.cursor.description]
        recipe_data = self.cursor.fetchone()
        if recipe_data:
            return dict(zip(columns, recipe_data))
        return None

    def update_recipe(self, recipe_id: int, updated_data: Recipe):
        update_query = """
        UPDATE recipe.recipes
        SET name = %s, product_id = %s
        WHERE id = %s;
        """
        self.cursor.execute(update_query, (
            updated_data.name, updated_data.product_id, recipe_id
        ))
        self.conn.commit()

    def delete_recipe(self, recipe_id: int):
        
        delete_query = "DELETE FROM recipe.recipe_data_sheet WHERE recipe_id = %s;"
        self.cursor.execute(delete_query, (recipe_id,))
        self.conn.commit()
        delete_query = "DELETE FROM recipe.recipes WHERE id = %s;"
        self.cursor.execute(delete_query, (recipe_id,))
        self.conn.commit()

    def list_recipes(self):
        select_query = "SELECT * FROM recipe.recipe_product_category;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    
    def list_unit_measures(self):
        select_query = "SELECT * FROM recipe.unit_of_measures;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    
    
    

    def close_connection(self):
        self.conn.close()
