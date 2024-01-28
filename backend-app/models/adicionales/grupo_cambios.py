import psycopg2
import psycopg2.extras
import os
from schema.adicionales.grupo_cambios import GrupoCambiosSchemaPost
from dotenv import load_dotenv


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



class GrupoCambios:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_grupo_cambios(self, grupo_data: GrupoCambiosSchemaPost):
        insert_query = """
        INSERT INTO grupo_cambios (name, cambios)
        VALUES (%s, %s) RETURNING grupo_cambio_id;
        """
        self.cursor.execute(insert_query, (
            grupo_data.name, 
            grupo_data.cambios
        ))
        grupo_cambio_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return grupo_cambio_id

    def select_all_grupos_cambios(self):
        self.cursor.execute("SELECT * FROM grupo_cambios;")
        grupos = self.cursor.fetchall()

        column_names = [desc[0] for desc in self.cursor.description]
        grupos_with_names = [dict(zip(column_names, grupo)) for grupo in grupos]

        return grupos_with_names

    def get_cambios_by_grupo_id(self, grupo_cambio_id):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            query = """
            SELECT c.cambio_id, c.name, c.price
            FROM grupo_cambios gc
            JOIN LATERAL UNNEST(gc.cambios) AS unnest_cambio_id(cambio_id) ON true
            JOIN cambios c ON c.cambio_id = unnest_cambio_id.cambio_id
            WHERE gc.grupo_cambio_id = %s;
            """
            cursor.execute(query, (grupo_cambio_id,))
            cambios = cursor.fetchall()
            return [dict(cambio) for cambio in cambios]
            
    def select_grupo_cambios_by_id(self, grupo_cambio_id):
        self.cursor.execute("SELECT * FROM grupo_cambios WHERE grupo_cambio_id = %s;", (grupo_cambio_id,))
        grupo = self.cursor.fetchone()

        if grupo is None:
            return None

        column_names = [desc[0] for desc in self.cursor.description]
        grupo_with_names = dict(zip(column_names, grupo))

        return grupo_with_names

    def update_grupo_cambios(self, grupo_cambio_id, grupo_data: GrupoCambiosSchemaPost):
        update_query = """
        UPDATE grupo_cambios SET
            name = %s,
            cambios = %s
        WHERE grupo_cambio_id = %s;
        """
        self.cursor.execute(update_query, (
            grupo_data.name, grupo_data.cambios, grupo_cambio_id
        ))
        self.conn.commit()

    def delete_grupo_cambios(self, grupo_cambio_id):
        delete_query = "DELETE FROM grupo_cambios WHERE grupo_cambio_id = %s;"
        self.cursor.execute(delete_query, (grupo_cambio_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
