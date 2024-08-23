from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.city import citySchema

# Definición del esquema Pydantic para ciudades


# Asegúrate de importar tu esquema de ciudad adecuado
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class City:
    def __init__(self, city_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.city_id = city_id

    def select_all_cities(self):
        select_query = "SELECT * FROM cities where visible = true;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_city_by_id(self, city_id):
        select_query = "SELECT * FROM cities WHERE city_id = %s;"
        self.cursor.execute(select_query, (city_id,))
        columns = [desc[0] for desc in self.cursor.description]
        city_data = self.cursor.fetchone()

        if city_data:
            return dict(zip(columns, city_data))
        else:
            return None

    def insert_city(self, city_data: citySchema):
        insert_query = """
        INSERT INTO cities (
            city_name
        ) VALUES (%s) RETURNING city_id;
        """
        # Como city_id es generado automáticamente, no necesitamos insertarlo manualmente
        self.cursor.execute(insert_query, (city_data.city_name,))
        city_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return city_id

    def delete_city(self, city_id):
        # Implementa la lógica de desactivación o eliminación según tus requisitos.
        return 'Solo desactiva la ciudad'

    def update_city(self, city_id, updated_data: citySchema):
        update_query = """
        UPDATE cities
        SET city_name = %s
        WHERE city_id = %s
        RETURNING *;
        """
        # Actualizamos solo el nombre de la ciudad, ya que es el único campo mutable en este esquema
        self.cursor.execute(update_query, (
            updated_data.city_name, city_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_city_data = self.cursor.fetchone()

        if updated_city_data:
            return dict(zip(columns, updated_city_data))
        else:
            return None

    def close_connection(self):
        self.conn.close()
