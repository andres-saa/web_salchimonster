from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.category import CategorySchemaPost

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')





class Category:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_category(self, category_data: CategorySchemaPost):
        insert_query = "INSERT INTO categories (category_name) VALUES (%s) RETURNING category_id;"
        self.cursor.execute(insert_query, (category_data.category_name,))
        category_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return category_id

    def select_all_categories(self, site_id,resturant_id):
        # Definimos la consulta que verifica la existencia de instancias activas de productos por cada categoría
        select_query = f"""
        SELECT c.*
        FROM inventory.active_product_categories_with_site AS c
        WHERE c.site_id = {site_id}
        AND C.restaurant_id = {resturant_id}
        AND EXISTS (
            SELECT 1
            FROM inventory.complete_product_instances AS p
            WHERE p.site_id = c.site_id
            AND p.category_id = c.category_id
            AND p.status = TRUE
            AND p.restaurant_id = {resturant_id}
            order by index
        )
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    
    def select_main_categories(self, site_id,resturant_id):
        # Definimos la consulta que verifica la existencia de instancias activas de productos por cada categoría
        select_query = f"""
        SELECT c.*
        FROM inventory.active_product_categories_with_site AS c
        WHERE c.site_id = {site_id}
        AND C.restaurant_id = {resturant_id}
        AND c.main = true
        AND EXISTS (
            SELECT 1
            FROM inventory.complete_product_instances AS p
            WHERE p.site_id = c.site_id
            AND p.category_id = c.category_id
            AND p.status = TRUE
            AND p.restaurant_id = {resturant_id}
            order by index
        )
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]



    def select_all_categories_all(self, site_id,restaurant_id):
        # Definimos la consulta que verifica la existencia de instancias activas de productos por cada categoría
        select_query = f"""
        SELECT c.*
        FROM inventory.active_product_categories_with_site AS c
        WHERE c.site_id = {site_id} AND c.restaurant_id = {restaurant_id};
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    
    def select_all_categories_all_add_product(self,restaurant_id):
        # Definimos la consulta que verifica la existencia de instancias activas de productos por cada categoría
        select_query = f"""
        SELECT *
        FROM inventory.product_categories  where resturant_id = {restaurant_id};
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]





    def close_connection(self):
        self.conn.close()