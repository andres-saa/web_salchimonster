# models/grupo_salsas.py
import psycopg2
import psycopg2.extras
import os
from schema.adicionales.grupo_salsas import GrupoSalsasSchemaPost
from dotenv import load_dotenv


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class GrupoSalsas:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_grupo_salsas(self, grupo_data: GrupoSalsasSchemaPost):
        insert_query = """
        INSERT INTO grupo_salsas (name, salsas)
        VALUES (%s, %s) RETURNING grupo_salsa_id;
        """
        self.cursor.execute(insert_query, (
            grupo_data.name, 
            grupo_data.salsas
        ))
        grupo_salsa_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return grupo_salsa_id

    def select_all_grupos_salsas(self):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SELECT * FROM grupo_salsas;")
            grupos = cursor.fetchall()
            return [dict(grupo) for grupo in grupos]  # Convert each row to a dictionary

    def select_grupo_salsas_by_id(self, grupo_salsa_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SELECT * FROM grupo_salsas WHERE grupo_salsa_id = %s;", (grupo_salsa_id,))
            grupo = cursor.fetchone()
            return dict(grupo) if grupo else None  # Convert row to a dictionary

    def update_grupo_salsas(self, grupo_salsa_id, grupo_data: GrupoSalsasSchemaPost):
        update_query = """
        UPDATE grupo_salsas SET
            name = %s,
            salsas = %s
        WHERE grupo_salsa_id = %s;
        """
        self.cursor.execute(update_query, (
            grupo_data.name, grupo_data.salsas, grupo_salsa_id
        ))
        self.conn.commit()

    def delete_grupo_salsas(self, grupo_salsa_id):
        delete_query = "DELETE FROM grupo_salsas WHERE grupo_salsa_id = %s;"
        self.cursor.execute(delete_query, (grupo_salsa_id,))
        self.conn.commit()

    def get_salsas_by_grupo_id(self, grupo_salsa_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = """
            SELECT s.salsa_id, s.name, s.price
            FROM grupo_salsas g
            JOIN LATERAL UNNEST(g.salsas) AS unnest_salsa_id(salsa_id) ON true
            JOIN salsas s ON s.salsa_id = unnest_salsa_id.salsa_id
            WHERE g.grupo_salsa_id = %s;
            """
            cursor.execute(query, (grupo_salsa_id,))
            salsas = cursor.fetchall()
            return [dict(salsa) for salsa in salsas] 

    def close_connection(self):
        self.conn.close()
