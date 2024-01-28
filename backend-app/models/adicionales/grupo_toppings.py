import psycopg2
import psycopg2.extras
import os
from schema.adicionales.grupo_toppings import GrupoToppingsSchemaPost

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')





class GrupoToppings:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_grupo_toppings(self, grupo_data: GrupoToppingsSchemaPost):
        insert_query = """
        INSERT INTO grupo_toppings (name, toppings)
        VALUES (%s, %s) RETURNING grupo_topping_id;
        """
        self.cursor.execute(insert_query, (
            grupo_data.name, 
            grupo_data.toppings
        ))
        grupo_topping_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return grupo_topping_id

    def select_all_grupos_toppings(self):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            select_query = "SELECT * FROM grupo_toppings;"
            cursor.execute(select_query)
            grupos = cursor.fetchall()
            return [dict(grupo) for grupo in grupos]  # Convertir cada fila en un diccionario

    def select_grupo_toppings_by_id(self, grupo_topping_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            select_query = "SELECT * FROM grupo_toppings WHERE grupo_topping_id = %s;"
            cursor.execute(select_query, (grupo_topping_id,))
            grupo = cursor.fetchone()
            return dict(grupo) if grupo else None 

    def update_grupo_toppings(self, grupo_topping_id, grupo_data: GrupoToppingsSchemaPost):
        update_query = """
        UPDATE grupo_toppings SET
            name = %s,
            toppings = %s
        WHERE grupo_topping_id = %s;
        """
        self.cursor.execute(update_query, (
            grupo_data.name, grupo_data.toppings, grupo_topping_id
        ))
        self.conn.commit()

    def delete_grupo_toppings(self, grupo_topping_id):
        delete_query = "DELETE FROM grupo_toppings WHERE grupo_topping_id = %s;"
        self.cursor.execute(delete_query, (grupo_topping_id,))
        self.conn.commit()


    def get_toppings_by_grupo_id(self, grupo_topping_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = """
            SELECT t.topping_id, t.name, t.price
            FROM grupo_toppings gt
            JOIN LATERAL UNNEST(gt.toppings) AS unnest_topping_id(topping_id) ON true
            JOIN toppings t ON t.topping_id = unnest_topping_id.topping_id
            WHERE gt.grupo_topping_id = %s;
            """
            cursor.execute(query, (grupo_topping_id,))
            toppings = cursor.fetchall()
            return [dict(topping) for topping in toppings]

    def close_connection(self):
        self.conn.close()
