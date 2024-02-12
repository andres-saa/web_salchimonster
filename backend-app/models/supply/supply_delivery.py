from schema.supply import SupplyDeliverySchema
# from schema.site import site_schema_post  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os
from schema.supply import SupplyDeliverySchema, SupplyDeliveryItemSchema
from typing import List, Optional


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class SupplyDelivery:
    def __init__(self, delivery_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.delivery_id = delivery_id

    def select_all_deliveries(self):
        select_query = "SELECT * FROM supply_deliveries order by delivery_id DESC;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    def get_deliveries_by_user_id(self, user_id: int) -> List[dict]:
        """
        Obtiene las entregas de suministros en las que el usuario especificado
        es el que entrega o recibe la dotación.

        :param user_id: ID del usuario para buscar las entregas de suministros.
        :return: Lista de diccionarios con los datos de las entregas encontradas.
        """
        select_query = """
        SELECT * FROM supply_deliveries
        WHERE user_delivery_id = %s OR user_receive_id = %s
        ORDER BY delivery_id DESC;
        """
        self.cursor.execute(select_query, (user_id, user_id))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def sign_delivery_sent(self, delivery_id):
        """
        Marca una entrega como firmada por el que envía.
        """
        update_query = """
        UPDATE supply_deliveries
        SET firmado_enviado = TRUE
        WHERE delivery_id = %s
        RETURNING delivery_id;
        """
        self.cursor.execute(update_query, (delivery_id,))
        self.conn.commit()
        updated_row_count = self.cursor.rowcount  # Obtener el número de filas afectadas

        if updated_row_count > 0:
            return True  # La actualización fue exitosa
        else:
            return False  # No se encontró la entrega o no se actualizó


    def sign_delivery_received(self, delivery_id):
        """
        Marca una entrega como firmada por el que recibe.
        """
        update_query = """
        UPDATE supply_deliveries
        SET firmado_recibido = TRUE
        WHERE delivery_id = %s
        RETURNING delivery_id;
        """
        self.cursor.execute(update_query, (delivery_id,))
        self.conn.commit()
        updated_row_count = self.cursor.rowcount  # Obtener el número de filas afectadas

        if updated_row_count > 0:
            return True  # La actualización fue exitosa
        else:
            return False  # No se encontró la entrega o no se actualizó
        
    
        



        



























    def select_delivery_by_id(self, delivery_id):
        select_query = "SELECT * FROM supply_deliveries WHERE delivery_id = %s;"
        self.cursor.execute(select_query, (delivery_id,))
        columns = [desc[0] for desc in self.cursor.description]
        delivery_data = self.cursor.fetchone()

        if delivery_data:
            return dict(zip(columns, delivery_data))
        else:
            return None
        
    

    def insert_delivery_with_items_for_multiple_receivers(self, delivery_data: SupplyDeliverySchema, items_data: List[SupplyDeliveryItemSchema], user_receive_ids: List[int]):
        """
        Inserta una entrega para múltiples receptores, con los mismos items para cada entrega.
        
        :param delivery_data: Datos de la entrega, sin incluir user_receive_id que será reemplazado por cada id en user_receive_ids.
        :param items_data: Lista de items a entregar.
        :param user_receive_ids: Lista de IDs de los usuarios receptores.
        :return: Lista de IDs de las entregas creadas.
        """
        delivery_ids = []  # Para almacenar los IDs de las entregas insertadas
        
        for user_receive_id in user_receive_ids:
            # Insertar la entrega con el ID del receptor actual
            self.cursor.execute(
                """
                INSERT INTO supply_deliveries (delivery_date, user_delivery_id, user_receive_id)
                VALUES (%s, %s, %s) RETURNING delivery_id;
                """,
                (delivery_data.delivery_date, delivery_data.user_delivery_id, user_receive_id)
            )
            delivery_id = self.cursor.fetchone()[0]
            delivery_ids.append(delivery_id)
            
            # Insertar cada item vinculado a la entrega
            for item in items_data:
                self.cursor.execute(
                    """
                    INSERT INTO supply_delivery_items (name, quantity, delivery_id)
                    VALUES (%s, %s, %s);
                    """,
                    (item.name, item.quantity, delivery_id)
                )
            
        self.conn.commit()
        return delivery_ids
    def insert_delivery(self, delivery_data: SupplyDeliverySchema):
        insert_query = """
        INSERT INTO supply_deliveries (delivery_date, user_delivery_id, user_receive_id)
        VALUES (%s, %s, %s) RETURNING delivery_id;
        """
        self.cursor.execute(insert_query, (
            delivery_data.delivery_date, delivery_data.user_delivery_id, delivery_data.user_receive_id
        ))
        delivery_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return delivery_id

    def update_delivery(self, delivery_id, updated_data: SupplyDeliverySchema):
        update_query = """
        UPDATE supply_deliveries
        SET delivery_date = %s, user_delivery_id = %s, user_receive_id = %s
        WHERE delivery_id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.delivery_date, updated_data.user_delivery_id, updated_data.user_receive_id, delivery_id
        ))
        columns = [desc[0] for desc in self.cursor.description]
        updated_delivery_data = self.cursor.fetchone()

        if updated_delivery_data:
            return dict(zip(columns, updated_delivery_data))
        else:
            return None

    def delete_delivery(self, delivery_id):
        # Implementación específica de la lógica de desactivación o eliminación
        return 'Función para desactivar o eliminar una entrega aún no implementada'

    def close_connection(self):
        self.conn.close()
