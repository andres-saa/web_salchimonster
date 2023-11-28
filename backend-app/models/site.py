from schema.site import site_schema_post  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Site:
    def __init__(self, site_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.site_id = site_id

    def select_all_sites(self):
        select_query = "SELECT * FROM sites;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_site_by_id(self, site_id):
        select_query = "SELECT * FROM sites WHERE site_id = %s;"
        self.cursor.execute(select_query, (site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        site_data = self.cursor.fetchone()

        if site_data:
            return dict(zip(columns, site_data))
        else:
            return None

    def insert_site(self, site_data: site_schema_post):
        insert_query = """
        INSERT INTO sites (
            site_name, site_address, site_phone, site_business_hours
        ) VALUES (%s, %s, %s, %s) RETURNING site_id;
        """
        self.cursor.execute(insert_query, (
            site_data.site_name, site_data.site_address, site_data.site_phone, site_data.site_business_hours
        ))
        site_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return site_id

    def delete_site(self, site_id):
        # Puedes implementar la lógica de desactivación o eliminación según tus requisitos.
        return 'solo desactiva el sitio'

    def update_site(self, site_id, updated_data: site_schema_post):
        update_query = """
        UPDATE sites
        SET site_name = %s, site_address = %s, site_phone = %s, site_business_hours = %s
        WHERE site_id = %s
        RETURNING *;
        """

        self.cursor.execute(update_query, (
            updated_data.site_name, updated_data.site_address, updated_data.site_phone, updated_data.site_business_hours, site_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_site_data = self.cursor.fetchone()

        if updated_site_data:
            return dict(zip(columns, updated_site_data))
        else:
            return None

    def close_connection(self):
        self.conn.close()
