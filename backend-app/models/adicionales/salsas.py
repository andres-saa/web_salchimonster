# models/salsas.py
import psycopg2
import os
from schema.adicionales.salsas import SalsaSchemaPost
from dotenv import load_dotenv


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Salsas:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_salsa(self, salsa_data: SalsaSchemaPost):
        insert_query = """
        INSERT INTO salsas (name, price)
        VALUES (%s, %s) RETURNING salsa_id;
        """
        self.cursor.execute(insert_query, (
            salsa_data.name, 
            salsa_data.price
        ))
        salsa_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return salsa_id
    def select_all_salsas(self):
        select_query = "SELECT * FROM salsas;"
        self.cursor.execute(select_query)
        salsas = self.cursor.fetchall()

        # Obtener los nombres de los campos
        column_names = [desc[0] for desc in self.cursor.description]

        # Crear una lista de diccionarios, cada uno representando una fila
        salsas_with_names = []
        for salsa in salsas:
            salsas_with_names.append(dict(zip(column_names, salsa)))

        return salsas_with_names

    def select_salsa_by_id(self, salsa_id):
        select_query = "SELECT * FROM salsas WHERE salsa_id = %s;"
        self.cursor.execute(select_query, (salsa_id,))
        salsa = self.cursor.fetchone()

        # Si no hay resultados, devuelve None
        if salsa is None:
            return None

        # Obtener los nombres de los campos
        column_names = [desc[0] for desc in self.cursor.description]

        # Crear un diccionario para la salsa
        salsa_with_names = dict(zip(column_names, salsa))

        return salsa_with_names

    def update_salsa(self, salsa_id, salsa_data: SalsaSchemaPost):
        update_query = """
        UPDATE salsas SET
            name = %s,
            price = %s
        WHERE salsa_id = %s;
        """
        self.cursor.execute(update_query, (
            salsa_data.name, salsa_data.price, salsa_id
        ))
        self.conn.commit()

    def delete_salsa(self, salsa_id):
        delete_query = "DELETE FROM salsas WHERE salsa_id = %s;"
        self.cursor.execute(delete_query, (salsa_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
