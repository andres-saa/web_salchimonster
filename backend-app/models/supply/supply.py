from schema.supply import SupplySchema
# from schema.site import site_schema_post  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class Supply:



    def __init__(self, supply_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.supply_id = supply_id

    def select_all_supplies(self):
        select_query = "SELECT * FROM supplies;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_supply_by_id(self, supply_id):
        select_query = "SELECT * FROM supplies WHERE supply_id = %s;"
        self.cursor.execute(select_query, (supply_id,))
        columns = [desc[0] for desc in self.cursor.description]
        supply_data = self.cursor.fetchone()

        if supply_data:
            return dict(zip(columns, supply_data))
        else:
            return None

    def insert_supply(self, supply_data: SupplySchema):
        insert_query = """
        INSERT INTO supplies (name, description) VALUES (%s, %s) RETURNING supply_id;
        """
        self.cursor.execute(insert_query, (supply_data.name, supply_data.description))
        supply_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return supply_id

    def update_supply(self, supply_id, updated_data: SupplySchema):
        update_query = """
        UPDATE supplies SET name = %s, description = %s WHERE supply_id = %s RETURNING *;
        """
        self.cursor.execute(update_query, (updated_data.name, updated_data.description, supply_id))
        columns = [desc[0] for desc in self.cursor.description]
        updated_supply_data = self.cursor.fetchone()

        if updated_supply_data:
            return dict(zip(columns, updated_supply_data))
        else:
            return None

    def delete_supply(self, supply_id):
        # Implementación específica de la lógica de desactivación o eliminación
        return 'Función para desactivar o eliminar un suministro aún no implementada'

    def close_connection(self):
        self.conn.close()
