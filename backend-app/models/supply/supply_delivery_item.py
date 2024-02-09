from schema.supply import SupplyDeliveryItemSchema
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


class SupplyDeliveryItem:
    def __init__(self, item_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.item_id = item_id


    def select_items_by_delivery_id(self, delivery_id):
        select_query = "SELECT * FROM supply_delivery_items WHERE delivery_id = %s;"
        self.cursor.execute(select_query, (delivery_id,))
        columns = [desc[0] for desc in self.cursor.description]
        items_data = self.cursor.fetchall()

        if items_data:
            return [dict(zip(columns, row)) for row in items_data]
        else:
            return []
    
    
    def select_all_items(self):
        select_query = "SELECT * FROM supply_delivery_items;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_item_by_id(self, item_id):
        select_query = "SELECT * FROM supply_delivery_items WHERE item_id = %s;"
        self.cursor.execute(select_query, (item_id,))
        columns = [desc[0] for desc in self.cursor.description]
        item_data = self.cursor.fetchone()

        if item_data:
            return dict(zip(columns, item_data))
        else:
            return None

    def insert_item(self, item_data: SupplyDeliveryItemSchema):
        insert_query = """
        INSERT INTO supply_delivery_items (name, quantity, delivery_id)
        VALUES (%s, %s, %s) RETURNING item_id;
        """
        self.cursor.execute(insert_query, (
            item_data.name, item_data.quantity, item_data.delivery_id
        ))
        item_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return item_id

    def update_item(self, item_id, updated_data: SupplyDeliveryItemSchema):
        update_query = """
        UPDATE supply_delivery_items
        SET name = %s, quantity = %s, delivery_id = %s
        WHERE item_id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.name, updated_data.quantity, updated_data.delivery_id, item_id
        ))
        columns = [desc[0] for desc in self.cursor.description]
        updated_item_data = self.cursor.fetchone()

        if updated_item_data:
            return dict(zip(columns, updated_item_data))
        else:
            return None

    def delete_item(self, item_id):
        # Implementación específica de la lógica de desactivación o eliminación
        return 'Función para desactivar o eliminar un ítem aún no implementada'

    def close_connection(self):
        self.conn.close()
