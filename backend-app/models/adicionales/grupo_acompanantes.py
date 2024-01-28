import psycopg2
import psycopg2.extras
import os
from schema.adicionales.grupo_acompanantes import GrupoAcompanantesSchemaPost
from dotenv import load_dotenv

 

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')




class GrupoAcompanantes:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_grupo_acompanantes(self, grupo_data: GrupoAcompanantesSchemaPost):
        insert_query = """
        INSERT INTO grupo_acompanantes (name, acompanantes)
        VALUES (%s, %s) RETURNING grupo_acompanante_id;
        """
        self.cursor.execute(insert_query, (
            grupo_data.name, 
            grupo_data.acompanantes
        ))
        grupo_acompanante_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return grupo_acompanante_id

    def select_all_grupos_acompanantes(self):
        self.cursor.execute("SELECT * FROM grupo_acompanantes;")
        grupos = self.cursor.fetchall()

        column_names = [desc[0] for desc in self.cursor.description]
        grupos_with_names = [dict(zip(column_names, grupo)) for grupo in grupos]

        return grupos_with_names

    def select_grupo_acompanantes_by_id(self, grupo_acompanante_id):
        self.cursor.execute("SELECT * FROM grupo_acompanantes WHERE grupo_acompanante_id = %s;", (grupo_acompanante_id,))
        grupo = self.cursor.fetchone()

        if grupo is None:
            return None

        column_names = [desc[0] for desc in self.cursor.description]
        grupo_with_names = dict(zip(column_names, grupo))

        return grupo_with_names

    def get_acompanantes_by_grupo_id(self, grupo_acompanante_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = """
            SELECT a.acompanante_id, a.name, a.price
            FROM grupo_acompanantes ga
            JOIN LATERAL UNNEST(ga.acompanantes) AS unnest_acompanante_id(acompanante_id) ON true
            JOIN acompanantes a ON a.acompanante_id = unnest_acompanante_id.acompanante_id
            WHERE ga.grupo_acompanante_id = %s;
            """
            cursor.execute(query, (grupo_acompanante_id,))
            acompanantes = cursor.fetchall()
            return [dict(acompanante) for acompanante in acompanantes]

    def update_grupo_acompanantes(self, grupo_acompanante_id, grupo_data: GrupoAcompanantesSchemaPost):
        update_query = """
        UPDATE grupo_acompanantes SET
            name = %s,
            acompanantes = %s
        WHERE grupo_acompanante_id = %s;
        """
        self.cursor.execute(update_query, (
            grupo_data.name, grupo_data.acompanantes, grupo_acompanante_id
        ))
        self.conn.commit()

    def delete_grupo_acompanantes(self, grupo_acompanante_id):
        delete_query = "DELETE FROM grupo_acompanantes WHERE grupo_acompanante_id = %s;"
        self.cursor.execute(delete_query, (grupo_acompanante_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
