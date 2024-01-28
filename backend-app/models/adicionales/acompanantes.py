import psycopg2
import os
from schema.adicionales.acompanantes import AcompananteSchemaPost
from dotenv import load_dotenv



load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')




# models/acompanantes.py


class Acompanantes:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_acompanante(self, acompanante_data: AcompananteSchemaPost):
        insert_query = """
        INSERT INTO acompanantes (name, price)
        VALUES (%s, %s) RETURNING acompanante_id;
        """
        self.cursor.execute(insert_query, (
            acompanante_data.name, 
            acompanante_data.price
        ))
        acompanante_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return acompanante_id

    def select_all_acompanantes(self):
        select_query = "SELECT * FROM acompanantes;"
        self.cursor.execute(select_query)
        acompanantes = self.cursor.fetchall()

        column_names = [desc[0] for desc in self.cursor.description]
        acompanantes_with_names = [dict(zip(column_names, acompanante)) for acompanante in acompanantes]

        return acompanantes_with_names


    def select_acompanante_by_id(self, acompanante_id):
        select_query = "SELECT * FROM acompanantes WHERE acompanante_id = %s;"
        self.cursor.execute(select_query, (acompanante_id,))
        acompanante = self.cursor.fetchone()

        if acompanante is None:
            return None

        column_names = [desc[0] for desc in self.cursor.description]
        acompanante_with_names = dict(zip(column_names, acompanante))

        return acompanante_with_names


    def update_acompanante(self, acompanante_id, acompanante_data: AcompananteSchemaPost):
        update_query = """
        UPDATE acompanantes SET
            name = %s,
            price = %s
        WHERE acompanante_id = %s;
        """
        self.cursor.execute(update_query, (
            acompanante_data.name, acompanante_data.price, acompanante_id
        ))
        self.conn.commit()

    def delete_acompanante(self, acompanante_id):
        delete_query = "DELETE FROM acompanantes WHERE acompanante_id = %s;"
        self.cursor.execute(delete_query, (acompanante_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
