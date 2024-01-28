import psycopg2
import os
from schema.adicionales.cambios import CambioSchemaPost

from dotenv import load_dotenv


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# models/cambios.py


class Cambios:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_cambio(self, cambio_data: CambioSchemaPost):
        insert_query = """
        INSERT INTO cambios (name, price)
        VALUES (%s, %s) RETURNING cambio_id;
        """
        self.cursor.execute(insert_query, (
            cambio_data.name, 
            cambio_data.price
        ))
        cambio_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return cambio_id

    def select_all_cambios(self):
        select_query = "SELECT * FROM cambios;"
        self.cursor.execute(select_query)
        cambios = self.cursor.fetchall()

        column_names = [desc[0] for desc in self.cursor.description]
        cambios_with_names = [dict(zip(column_names, cambio)) for cambio in cambios]

        return cambios_with_names

    def select_cambio_by_id(self, cambio_id):
        select_query = "SELECT * FROM cambios WHERE cambio_id = %s;"
        self.cursor.execute(select_query, (cambio_id,))
        cambio = self.cursor.fetchone()

        if cambio is None:
            return None

        column_names = [desc[0] for desc in self.cursor.description]
        cambio_with_names = dict(zip(column_names, cambio))

        return cambio_with_names


    def update_cambio(self, cambio_id, cambio_data: CambioSchemaPost):
        update_query = """
        UPDATE cambios SET
            name = %s,
            price = %s
        WHERE cambio_id = %s;
        """
        self.cursor.execute(update_query, (
            cambio_data.name, cambio_data.price, cambio_id
        ))
        self.conn.commit()

    def delete_cambio(self, cambio_id):
        delete_query = "DELETE FROM cambios WHERE cambio_id = %s;"
        self.cursor.execute(delete_query, (cambio_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
