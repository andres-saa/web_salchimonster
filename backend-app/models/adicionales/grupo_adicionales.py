# models/grupo_adicionales.py
import psycopg2
import os
from schema.adicionales.grupo_adicionales import GrupoAdicionalesSchemaPost
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv



load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


# models/grupo_adicionales.py


class GrupoAdicionales:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_grupo_adicionales(self, grupo_data: GrupoAdicionalesSchemaPost):
        insert_query = """
        INSERT INTO grupo_adicionales (name, adicionales)
        VALUES (%s, %s) RETURNING grupo_id;
        """
        self.cursor.execute(insert_query, (
            grupo_data.name, 
            grupo_data.adicionales
        ))
        grupo_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return grupo_id

    def select_all_grupos(self):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SELECT * FROM grupo_adicionales;")
            grupos = cursor.fetchall()
            return [dict(grupo) for grupo in grupos]  # Convertir cada fila en un diccionario

    def select_grupo_by_id(self, grupo_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SELECT * FROM grupo_adicionales WHERE grupo_id = %s;", (grupo_id,))
            grupo = cursor.fetchone()
            return dict(grupo) if grupo else None

    def update_grupo(self, grupo_id, grupo_data: GrupoAdicionalesSchemaPost):
        update_query = """
        UPDATE grupo_adicionales SET
            name = %s,
            adicionales = %s
        WHERE grupo_id = %s;
        """
        self.cursor.execute(update_query, (
            grupo_data.name, grupo_data.adicionales, grupo_id
        ))
        self.conn.commit()
        
    def get_adicionales_by_grupo_id(self, grupo_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = """
            SELECT a.adicional_id, a.name, a.price
            FROM grupo_adicionales ga
            JOIN LATERAL UNNEST(ga.adicionales) AS unnest_adicional_id(adicional_id) ON true
            JOIN adicionales a ON a.adicional_id = unnest_adicional_id.adicional_id
            WHERE ga.grupo_id = %s;
            """
            cursor.execute(query, (grupo_id,))
            adicionales = cursor.fetchall()
            return [dict(adicional) for adicional in adicionales]


    def delete_grupo(self, grupo_id):
        delete_query = "DELETE FROM grupo_adicionales WHERE grupo_id = %s;"
        self.cursor.execute(delete_query, (grupo_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


