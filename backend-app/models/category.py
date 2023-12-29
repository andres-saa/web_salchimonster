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

    def select_all_categories(self):
        select_query = "SELECT * FROM categories;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_category_by_id(self, category_id):
        select_query = "SELECT * FROM categories WHERE category_id = %s;"
        self.cursor.execute(select_query, (category_id,))
        return self.cursor.fetchone()

    def update_category(self, category_id, category_data: CategorySchemaPost):
        update_query = "UPDATE categories SET category_name = %s WHERE category_id = %s;"
        self.cursor.execute(update_query, (category_data.category_name, category_id))
        self.conn.commit()

    def delete_category(self, category_id):
        delete_query = "DELETE FROM categories WHERE category_id = %s;"
        self.cursor.execute(delete_query, (category_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

# Ejemplo de uso para la clase Category
if __name__ == "__main__":
    category_instance = Category()

    # Insertar una categoría
    category_data = CategorySchemaPost
