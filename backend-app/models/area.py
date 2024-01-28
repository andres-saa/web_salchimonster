import psycopg2
import os
from dotenv import load_dotenv
from schema.area import AreaSchemaPost, NeighborhoodSchema

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

class Area:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_areas(self):
        select_query = """
        SELECT 
            a.area_id, a.name, a.city_id, a.site_id, a.wsp,
            json_agg(
                json_build_object(
                    'name', n.name,
                    'deliveryPrice', n.delivery_price
                )
            ) AS neighborhoods
        FROM 
            areas a
        JOIN 
            neighborhoods n ON a.area_id = n.area_id
        GROUP BY 
            a.area_id;
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_area_by_id(self, area_id):
        select_query = """
        SELECT 
            a.area_id, a.name, a.city_id, a.site_id, a.wsp,
            json_agg(
                json_build_object(
                    'name', n.name,
                    'deliveryPrice', n.delivery_price
                )
            ) AS neighborhoods
        FROM 
            areas a
        JOIN 
            neighborhoods n ON a.area_id = n.area_id
        WHERE 
            a.area_id = %s
        GROUP BY 
            a.area_id;
        """
        self.cursor.execute(select_query, (area_id,))
        columns = [desc[0] for desc in self.cursor.description]
        area_data = self.cursor.fetchone()

        if area_data:
            return dict(zip(columns, area_data))
        else:
            return None

    def select_areas_by_site_id(self, site_id):
        select_query = """
        SELECT 
            a.area_id, a.name, a.city_id, a.site_id, a.wsp,
            json_agg(
                json_build_object(
                    'name', n.name,
                    'deliveryPrice', n.delivery_price
                )
            ) AS neighborhoods
        FROM 
            areas a
        JOIN 
            neighborhoods n ON a.area_id = n.area_id
        WHERE 
            a.site_id = %s
        GROUP BY 
            a.area_id;
        """
        self.cursor.execute(select_query, (site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        areas = self.cursor.fetchall()

        return [dict(zip(columns, area)) for area in areas] if areas else []

    def insert_area(self, area_data: AreaSchemaPost):
        insert_query = "INSERT INTO areas (name, city_id, site_id, wsp) VALUES (%s, %s, %s, %s) RETURNING area_id;"
        self.cursor.execute(insert_query, (area_data.name, area_data.city_id, area_data.site_id, area_data.wsp))
        area_id = self.cursor.fetchone()[0]

        for neighborhood in area_data.neighborhoods:
            neighborhood_insert_query = "INSERT INTO neighborhoods (area_id, name, delivery_price) VALUES (%s, %s, %s);"
            self.cursor.execute(neighborhood_insert_query, (area_id, neighborhood.name, neighborhood.delivery_price))

        self.conn.commit()
        return area_id

    def update_area(self, area_id, updated_data: AreaSchemaPost):
        update_query = "UPDATE areas SET name = %s, city_id = %s, site_id = %s, wsp = %s WHERE area_id = %s;"
        self.cursor.execute(update_query, (updated_data.name, updated_data.city_id, updated_data.site_id, updated_data.wsp, area_id))

        # Borrar y reinsertar barrios para simplificar la lógica de actualización
        delete_neighborhoods_query = "DELETE FROM neighborhoods WHERE area_id = %s;"
        self.cursor.execute(delete_neighborhoods_query, (area_id,))

        for neighborhood in updated_data.neighborhoods:
            neighborhood_insert_query = "INSERT INTO neighborhoods (area_id, name, delivery_price) VALUES (%s, %s, %s);"
            self.cursor.execute(neighborhood_insert_query, (area_id, neighborhood.name, neighborhood.delivery_price))

        self.conn.commit()
        return self.select_area_by_id(area_id)

    def select_areas_by_city_id(self, city_id):
        select_query = """
        SELECT 
            a.area_id, a.name, a.city_id, a.site_id, a.wsp,
            json_agg(
                json_build_object(
                    'name', n.name,
                    'deliveryPrice', n.delivery_price
                )
            ) AS neighborhoods
        FROM 
            areas a
        JOIN 
            neighborhoods n ON a.area_id = n.area_id
        WHERE 
            a.city_id = %s
        GROUP BY 
            a.area_id;
        """
        self.cursor.execute(select_query, (city_id,))
        columns = [desc[0] for desc in self.cursor.description]
        areas = self.cursor.fetchall()

        return [dict(zip(columns, area)) for area in areas] if areas else []

    def delete_area(self, area_id):
        delete_neighborhoods_query = "DELETE FROM neighborhoods WHERE area_id = %s;"
        self.cursor.execute(delete_neighborhoods_query, (area_id,))

        delete_area_query = "DELETE FROM areas WHERE area_id = %s;"
        self.cursor.execute(delete_area_query, (area_id,))
        self.conn.commit()

        return f"Area with ID {area_id} deleted successfully"

    def close_connection(self):
        self.conn.close()
