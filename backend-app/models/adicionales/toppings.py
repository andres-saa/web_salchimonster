# models/toppings.py
import psycopg2
import os
from schema.adicionales.toppings import ToppingSchemaPost

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class Toppings:
    def __init__(self):
        self.conn_str = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')} port={os.getenv('DB_PORT')}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_topping(self, topping_data: ToppingSchemaPost):
        insert_query = """
        INSERT INTO toppings (name, price)
        VALUES (%s, %s) RETURNING topping_id;
        """
        self.cursor.execute(insert_query, (
            topping_data.name, 
            topping_data.price
        ))
        topping_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return topping_id

    def select_all_toppings(self):
        select_query = "SELECT * FROM toppings;"
        self.cursor.execute(select_query)
        toppings = self.cursor.fetchall()

        # Obtener los nombres de los campos
        column_names = [desc[0] for desc in self.cursor.description]

        # Crear una lista de diccionarios, cada uno representando una fila
        toppings_with_names = []
        for topping in toppings:
            toppings_with_names.append(dict(zip(column_names, topping)))

        return toppings_with_names

    def select_topping_by_id(self, topping_id):
        select_query = "SELECT * FROM toppings WHERE topping_id = %s;"
        self.cursor.execute(select_query, (topping_id,))
        topping = self.cursor.fetchone()

        # Si no hay resultados, devuelve None
        if topping is None:
            return None

        # Obtener los nombres de los campos
        column_names = [desc[0] for desc in self.cursor.description]

        # Crear un diccionario para el topping
        topping_with_names = dict(zip(column_names, topping))

        return topping_with_names

    def update_topping(self, topping_id, topping_data: ToppingSchemaPost):
        update_query = """
        UPDATE toppings SET
            name = %s,
            price = %s
        WHERE topping_id = %s;
        """
        self.cursor.execute(update_query, (
            topping_data.name, topping_data.price, topping_id
        ))
        self.conn.commit()

    def delete_topping(self, topping_id):
        delete_query = "DELETE FROM toppings WHERE topping_id = %s;"
        self.cursor.execute(delete_query, (topping_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
