from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.adicionales.adicional    import adicionalSchemaPost

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Adicional:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_adicional(self, adicional_data: adicionalSchemaPost):
        insert_query = """
        INSERT INTO adicionales (name, price)
        VALUES (%s, %s) RETURNING adicional_id;
        """
        self.cursor.execute(insert_query, (
            adicional_data.name, 
            adicional_data.price
        ))
        adicional_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return adicional_id

    # ... [resto de tus métodos] ...


    def select_all_adicionales(self):
        select_query = "SELECT * FROM adicionales;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_adicional_by_id(self, adicional_id):
        select_query = "SELECT * FROM adicionales WHERE adicional_id = %s;"
        self.cursor.execute(select_query, (adicional_id,))
        return self.cursor.fetchone()

    def update_adicional(self, adicional_id, adicional_data: adicionalSchemaPost):
        update_query = """
        UPDATE adicionales SET
            name = %s,
            price = %s
        WHERE adicional_id = %s;
        """
        self.cursor.execute(update_query, (
            adicional_data.name, adicional_data.price, adicional_id
        ))
        self.conn.commit()

    def delete_adicional(self, adicional_id):
        delete_query = "DELETE FROM adicionales WHERE adicional_id = %s;"
        self.cursor.execute(delete_query, (adicional_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
