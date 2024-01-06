import psycopg2
from dotenv import load_dotenv
import os
from schema.permission import PermissionSchemaPost

from typing import List, Optional
from pydantic import BaseModel
from datetime import date
import json

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class Permission:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_permissions(self):
        select_query = "SELECT * FROM permissions;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_permission_by_id(self, permission_id):
        select_query = "SELECT * FROM permissions WHERE id = %s;"
        self.cursor.execute(select_query, (permission_id,))
        columns = [desc[0] for desc in self.cursor.description]
        permission_data = self.cursor.fetchone()

        if permission_data:
            return dict(zip(columns, permission_data))
        else:
            return None

    def insert_permission(self, permission_data: PermissionSchemaPost):
        insert_query = """
        INSERT INTO permissions (employer_id, start_date, end_date, observations, status, history, tipo)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        self.cursor.execute(insert_query, (
            permission_data.employer_id, permission_data.start_date, permission_data.end_date, 
            permission_data.observations, json.dumps(permission_data.status), 
            json.dumps(permission_data.history), permission_data.tipo
        ))
        permission_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return permission_id

    def update_permission(self, permission_id, updated_data: PermissionSchemaPost):
        update_query = """
        UPDATE permissions
        SET employer_id = %s, start_date = %s, end_date = %s, observations = %s, status = %s, history = %s, tipo = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.employer_id, updated_data.start_date, updated_data.end_date, 
            updated_data.observations, json.dumps(updated_data.status), 
            json.dumps(updated_data.history), updated_data.tipo, permission_id
        ))

        updated_permission_data = self.cursor.fetchone()

        self.conn.commit()

        if updated_permission_data:
            return dict(zip([desc[0] for desc in self.cursor.description], updated_permission_data))
        else:
            return None


    def delete_permission(self, permission_id):
        delete_query = "DELETE FROM permissions WHERE id = %s;"
        self.cursor.execute(delete_query, (permission_id,))
        self.conn.commit()
        return 'Permission deleted'

    def close_connection(self):
        self.conn.close()