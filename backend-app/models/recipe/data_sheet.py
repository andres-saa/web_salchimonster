import psycopg2
from dotenv import load_dotenv
import os
from schema.recipe import RecipeDataSheet, RecipeDataIngredient
from typing import List
from fastapi import status

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class RecipeDataSheetManager:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def create_recipe_data_sheet(self, data_sheet: RecipeDataSheet, ingredient_details: List[RecipeDataIngredient]):
        try:
            # Primero, insertamos la hoja de datos de la receta y obtenemos su ID
            insert_query = """
            INSERT INTO recipe.recipe_data_sheet (
                date, portion_size, portion_number, preparation_time, 
                cooking_time, service_temperature, selling_price, taxes,
                presentation, preparation_equipment, recipe_id
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;
            """
            self.cursor.execute(insert_query, (
                data_sheet.date, data_sheet.portion_size, data_sheet.portion_number,
                data_sheet.preparation_time, data_sheet.cooking_time, data_sheet.service_temperature,
                data_sheet.selling_price, data_sheet.taxes, data_sheet.presentation,
                data_sheet.preparation_equipment, data_sheet.recipe_id
            ))
            data_sheet_id = self.cursor.fetchone()[0]

            # Ahora, insertamos cada uno de los detalles de los ingredientes
            details_insert_query = """
            INSERT INTO recipe.recipe_data_ingredients (
                recipe_data_sheet_id, ingredient_id, unit_of_measure, quantity
            ) VALUES (%s, %s, %s, %s);
            """
            for detail in ingredient_details:
                self.cursor.execute(details_insert_query, (
                    data_sheet_id, detail.ingredient_id, detail.unit_measure, detail.quantity
                ))

            self.conn.commit()
            return data_sheet_id

        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            return "Database error occurred"

        except Exception as e:
            print(f"Unexpected error: {e}")
            return "An unexpected error occurred"

            
    def get_recipe_data_sheet_by_id(self, sheet_id: int):
        try:
            # Fetch the recipe data sheet with the recipe name and the associated product name
            select_query = """
            SELECT rds.*, r.product_id, p.name AS product_name
            FROM recipe.recipe_cost_details rds
            JOIN recipe.recipes r ON rds.recipe_id = r.id
            JOIN inventory.products p ON r.product_id = p.id
            WHERE rds.recipe_id = %s;
            """
            self.cursor.execute(select_query, (sheet_id,))
            columns = [desc[0] for desc in self.cursor.description]
            data_sheet = self.cursor.fetchone()

            if data_sheet:
                data_sheet_dict = dict(zip(columns, data_sheet))
                
                # Fetch the ingredient details for the data sheet
                details_query = "SELECT * FROM recipe.recipe_ingredient_details WHERE recipe_id = %s;"  # Adjust table name and column if necessary
                self.cursor.execute(details_query, (data_sheet_dict["recipe_id"],))
                details_columns = [desc[0] for desc in self.cursor.description]
                details = [dict(zip(details_columns, detail_row)) for detail_row in self.cursor.fetchall()]
                
                # Include the details in the data sheet response
                data_sheet_dict['ingredient_details'] = details
                return data_sheet_dict
            return None

        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")
        return "Database error occurred"
    def update_recipe_data_sheet(self, sheet_id: int, updated_data: RecipeDataSheet):
        try:
            update_query = """
            UPDATE recipe.recipe_data_sheet
            SET date = %s, portion_size = %s, portion_number = %s, preparation_time = %s, 
                cooking_time = %s, service_temperature = %s, selling_price = %s, taxes = %s,
                presentation = %s, preparation_equipment = %s
            WHERE id = %s;
            """
            self.cursor.execute(update_query, (
                updated_data.date, updated_data.portion_size, updated_data.portion_number,
                updated_data.preparation_time, updated_data.cooking_time, updated_data.service_temperature,
                updated_data.selling_price, updated_data.taxes, updated_data.presentation,
                updated_data.preparation_equipment, sheet_id
            ))
            self.conn.commit()

        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            return "Database error occurred"

    def delete_recipe_data_sheet(self, sheet_id: int):
        try:
            delete_query = "DELETE FROM recipe.recipe_data_sheet WHERE id = %s;"
            self.cursor.execute(delete_query, (sheet_id,))
            self.conn.commit()

        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            return "Database error occurred"
        
    def list_recipe_data_sheets(self):
        try:
            select_query = "SELECT * FROM recipe.recipe_data_sheet;"
            self.cursor.execute(select_query)
            columns = [desc[0] for desc in self.cursor.description]
            data_sheets = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
            
            # Agregar detalles a cada data sheet
            for data_sheet in data_sheets:
                sheet_id = data_sheet['recipe_id']
                details_query = "SELECT * FROM recipe.recipe_ingredient_details WHERE recipe_id = %s;"
                self.cursor.execute(details_query, (sheet_id,))
                details_columns = [desc[0] for desc in self.cursor.description]
                details = [dict(zip(details_columns, detail_row)) for detail_row in self.cursor.fetchall()]
                data_sheet['details'] = details

            return data_sheets

        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")
            return "Database error occurred"
    
    def create_recipe_data_ingredient(self, data_sheet_id: int, ingredient: RecipeDataIngredient):
        try:
            insert_query = """
            INSERT INTO recipe.recipe_data_ingredients (recipe_data_sheet_id, ingredient_id, unit_of_measure_id, quantity)
            VALUES (%s, %s, %s, %s);
            """
            self.cursor.execute(insert_query, (data_sheet_id, ingredient.ingredient_id, ingredient.unit_measure_id, ingredient.quantity))
            self.conn.commit()
            return {"message": "Ingredient detail deleted successfully"}, status.HTTP_200_OK
 
        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            return "Database error occurred"
        except Exception as e:
            print(f"Unexpected error: {e}")
            return "An unexpected error occurred"

    def delete_recipe_data_ingredient(self, ingredient_detail_id: int):
        try:
            delete_query = "DELETE FROM recipe.recipe_data_ingredients WHERE id = %s;"
            self.cursor.execute(delete_query, (ingredient_detail_id,))
            self.conn.commit()
            return f"Ingredient detail with ID {ingredient_detail_id} deleted successfully."
        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")
            self.conn.rollback()
            return "Database error occurred"
        except Exception as e:
            print(f"Unexpected error: {e}")
            return "An unexpected error occurred"    
    def close_connection(self):
        self.conn.close()
