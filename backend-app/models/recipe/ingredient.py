from schema.site import site_schema_post  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os
from schema.recipe import Ingredient

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

import psycopg2

class Ingredient:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def create_ingredient(self, ingredient: Ingredient):
        insert_query = """
        INSERT INTO recipe.ingredient (
            name, purchasing_unit_measure, purchasing_price, number_units_purchasing,
            purchasing_format, net_gross_weight, shrinkage_percent
        ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (
            ingredient.name, ingredient.purchasing_unit_measure, ingredient.purchasing_price,
            ingredient.number_units_purchasing, ingredient.purchasing_format,
            ingredient.net_gross_weight, ingredient.shrinkage_percent
        ))
        ingredient_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return ingredient_id

    def get_ingredient_by_id(self, ingredient_id: int):
        select_query = "SELECT * FROM recipe.ingredient WHERE id = %s;"
        self.cursor.execute(select_query, (ingredient_id,))
        columns = [desc[0] for desc in self.cursor.description]
        ingredient_data = self.cursor.fetchone()
        if ingredient_data:
            return dict(zip(columns, ingredient_data))
        return None

    def update_ingredient(self, ingredient_id: int, updated_data: Ingredient):
        update_query = """
        UPDATE recipe.ingredient
        SET name = %s, purchasing_unit_measure = %s, purchasing_price = %s, number_units_purchasing = %s,
            purchasing_format = %s, net_gross_weight = %s, shrinkage_percent = %s
        WHERE id = %s;
        """
        self.cursor.execute(update_query, (
            updated_data.name, updated_data.purchasing_unit_measure, updated_data.purchasing_price,
            updated_data.number_units_purchasing, updated_data.purchasing_format,
            updated_data.net_gross_weight, updated_data.shrinkage_percent,
            ingredient_id
        ))
        self.conn.commit()

    def delete_ingredient(self, ingredient_id: int):
        delete_query = "DELETE FROM recipe.ingredient WHERE id = %s;"
        self.cursor.execute(delete_query, (ingredient_id,))
        self.conn.commit()

    def list_ingredients(self):
        select_query = "SELECT * FROM recipe.ingredient;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def close_connection(self):
        self.conn.close()
