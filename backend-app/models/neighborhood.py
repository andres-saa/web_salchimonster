import psycopg2
from dotenv import load_dotenv
import os
from schema.neighborhood import NeighborhoodSchema
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Neighborhood:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_neighborhoods(self):
        select_query = "SELECT * FROM neighborhoods;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_neighborhood_by_id(self, neighborhood_id):
        select_query = "SELECT * FROM neighborhoods WHERE neighborhood_id = %s;"
        self.cursor.execute(select_query, (neighborhood_id,))
        columns = [desc[0] for desc in self.cursor.description]
        neighborhood_data = self.cursor.fetchone()
        if neighborhood_data:
            return dict(zip(columns, neighborhood_data))
        else:
            return None

    def insert_neighborhood(self, neighborhood_data: NeighborhoodSchema):
        # Verificamos si ya existe un barrio con el mismo nombre y city_id, ignorando mayúsculas/minúsculas para el nombre.
        check_query = """
        SELECT neighborhood_id FROM neighborhoods 
        WHERE LOWER(name) = LOWER(%s) AND city_id = %s;
        """
        self.cursor.execute(check_query, (neighborhood_data.name, neighborhood_data.city_id))
        existing_neighborhood = self.cursor.fetchone()

        # Si existe, lo eliminamos.
        if existing_neighborhood is not None:
            delete_query = """
            DELETE FROM neighborhoods WHERE neighborhood_id = %s;
            """
            self.cursor.execute(delete_query, (existing_neighborhood[0],))

        # Luego, insertamos el nuevo barrio.
        insert_query = """
        INSERT INTO neighborhoods (name, delivery_price, site_id, city_id)
        VALUES (%s, %s, %s, %s) RETURNING neighborhood_id;
        """
        self.cursor.execute(insert_query, (
            neighborhood_data.name, neighborhood_data.delivery_price,
            neighborhood_data.site_id, neighborhood_data.city_id
        ))
        neighborhood_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return neighborhood_id


    def delete_neighborhood(self, neighborhood_id):
        delete_query = "DELETE FROM neighborhoods WHERE neighborhood_id = %s;"
        self.cursor.execute(delete_query, (neighborhood_id,))
        self.conn.commit()
        return "Neighborhood deleted"

    def update_neighborhood(self, neighborhood_id, updated_data: NeighborhoodSchema):
        update_query = """
        UPDATE neighborhoods
        SET name = %s, delivery_price = %s, site_id = %s, city_id = %s
        WHERE neighborhood_id = %s RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.name, updated_data.delivery_price, 
            updated_data.site_id, updated_data.city_id, neighborhood_id
        ))
        self.conn.commit()
        columns = [desc[0] for desc in self.cursor.description]
        updated_neighborhood_data = self.cursor.fetchone()
        if updated_neighborhood_data:
            return dict(zip(columns, updated_neighborhood_data))
        else:
            return None

    def select_neighborhoods_by_city_id(self, city_id: int):
        select_query = "SELECT * FROM neighborhoods WHERE city_id = %s;"
        self.cursor.execute(select_query, (city_id,))
        columns = [desc[0] for desc in self.cursor.description]
        neighborhoods_data = self.cursor.fetchall()

        if neighborhoods_data:
            return [dict(zip(columns, row)) for row in neighborhoods_data]
        else:
            return []



    def select_neighborhoods_by_site_id(self, site_id: int):
        select_query = "SELECT * FROM neighborhoods WHERE site_id = %s;"
        self.cursor.execute(select_query, (site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        neighborhoods_data = self.cursor.fetchall()

        if neighborhoods_data:
            return [dict(zip(columns, row)) for row in neighborhoods_data]
        else:
            return []

    def close_connection(self):
        self.conn.close()
