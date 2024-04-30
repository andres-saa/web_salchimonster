# producto.py

import psycopg2
from dotenv import load_dotenv
import os
from schema.user import user_schema_post
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class User:
    def __init__(self, user_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.user_id = user_id

    def select_all_users(self):
        select_query = "SELECT * FROM users;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_user_by_id(self, user_id):
        select_query = "SELECT * FROM users WHERE user_id = %s;"
        self.cursor.execute(select_query, (user_id,))
        columns = [desc[0] for desc in self.cursor.description]
        user_data = self.cursor.fetchone()

        if user_data:
            return dict(zip(columns, user_data))
        else:
            return None

    def user_exists(self, user_phone):
        select_query = "SELECT user_id FROM users WHERE user_phone = %s;"
        self.cursor.execute(select_query, (user_phone,))
        return self.cursor.fetchone()

    def insert_user(self, user_data: user_schema_post):
        # Verifica si el usuario ya existe por número de teléfono
        existing_user = self.user_exists(user_data.user_phone)
        if existing_user:
            user_id = existing_user[0]
            # Actualiza el usuario si ya existe
            update_query = """
            UPDATE users
            SET user_name = %s, user_address = %s, site_id = %s
            WHERE user_id = %s
            RETURNING user_id;
            """
            self.cursor.execute(update_query, (
                user_data.user_name, user_data.user_address, user_data.site_id, user_id
            ))
            self.conn.commit()
            return user_id  # Retorna el user_id actualizado

        # Inserta un nuevo usuario si no existe
        insert_query = """
        INSERT INTO users (
            user_name, user_phone, user_address, site_id
        ) VALUES (%s, %s, %s, %s) RETURNING user_id;
        """
        self.cursor.execute(insert_query, (
            user_data.user_name, user_data.user_phone, user_data.user_address, user_data.site_id
        ))
        user_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return user_id


    def delete_user(self, user_id):
        # delete_query = "DELETE FROM users WHERE user_id = %s;"
        # self.cursor.execute(delete_query, (user_id,))
        # self.conn.commit()
        return 'solo desactiva el usuario'

    def update_user(self, user_id, updated_data: user_schema_post):
        update_query = """
        UPDATE users
        SET user_name = %s, user_phone = %s, user_address = %s, site_id = %s
        WHERE user_id = %s
        RETURNING *;
        """

        self.cursor.execute(update_query, (
            updated_data.user_name, updated_data.user_phone, updated_data.user_address, updated_data.site_id, user_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_user_data = self.cursor.fetchone()

        if updated_user_data:
            return dict(zip(columns, updated_user_data))
        else:
            return None
    def close_connection(self):
        self.conn.close()

