import psycopg2
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class DeliveryPerson:
    def __init__(self, delivery_person_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.delivery_person_id = delivery_person_id

    def select_all_delivery_persons(self):
        select_query = "SELECT * FROM deliverypersons;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_delivery_person_by_id(self, delivery_person_id):
        select_query = "SELECT * FROM deliverypersons WHERE delivery_person_id = %s;"
        self.cursor.execute(select_query, (delivery_person_id,))
        columns = [desc[0] for desc in self.cursor.description]
        delivery_person_data = self.cursor.fetchone()

        if delivery_person_data:
            return dict(zip(columns, delivery_person_data))
        else:
            return None

    def insert_delivery_person(self, delivery_person_data):
        insert_query = """
        INSERT INTO deliverypersons (
            delivery_person_name, delivery_person_phone
        ) VALUES (%s, %s) RETURNING delivery_person_id;
        """
        self.cursor.execute(insert_query, (
            delivery_person_data.delivery_person_name, delivery_person_data.delivery_person_phone
        ))
        delivery_person_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return delivery_person_id

    def delete_delivery_person(self, delivery_person_id):
        delete_query = "DELETE FROM deliverypersons WHERE delivery_person_id = %s;"
        self.cursor.execute(delete_query, (delivery_person_id,))
        self.conn.commit()

    def update_delivery_person(self, delivery_person_id, updated_data):
        update_query = """
        UPDATE deliverypersons
        SET delivery_person_name = %s, delivery_person_phone = %s
        WHERE delivery_person_id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.delivery_person_name, updated_data.delivery_person_phone, delivery_person_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_delivery_person_data = self.cursor.fetchone()

        if updated_delivery_person_data:
            return dict(zip(columns, updated_delivery_person_data))
        else:
            return None

    def close_connection(self):
        self.conn.close()
