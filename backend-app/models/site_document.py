# site_document.py

import psycopg2
from schema.site_document import SiteDocumentSchemaPost  # Asegúrate de crear este esquema
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class SiteDocument:
    def __init__(self, document_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.document_id = document_id

    def select_documents_by_site_id(self, site_id):
        select_query = "SELECT * FROM site_documents WHERE site_id = %s;"
        self.cursor.execute(select_query, (site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_all_documents(self):
        select_query = "SELECT * FROM site_documents;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_document_by_id(self, document_id):
        select_query = "SELECT * FROM site_documents WHERE document_id = %s;"
        self.cursor.execute(select_query, (document_id,))
        columns = [desc[0] for desc in self.cursor.description]
        document_data = self.cursor.fetchone()

        if document_data:
            return dict(zip(columns, document_data))
        else:
            return None

    def insert_document(self, document_data: SiteDocumentSchemaPost):
        insert_query = """
        INSERT INTO site_documents (
            document_name, document_type, renovation_date, site_id
        ) VALUES (%s, %s, %s, %s) RETURNING document_id;
        """
        self.cursor.execute(insert_query, (
            document_data.document_name, document_data.document_type, document_data.renovation_date, document_data.site_id
        ))
        document_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return document_id

    def update_document(self, document_id, updated_data: SiteDocumentSchemaPost):
        update_query = """
        UPDATE site_documents
        SET document_name = %s, document_type = %s, renovation_date = %s, site_id = %s
        WHERE document_id = %s
        RETURNING *;
        """

        self.cursor.execute(update_query, (
            updated_data.document_name, updated_data.document_type, updated_data.renovation_date, updated_data.site_id, document_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_document_data = self.cursor.fetchone()

        if updated_document_data:
            self.conn.commit()  # ¡Agrega el commit aquí para guardar los cambios!
            return dict(zip(columns, updated_document_data))
        else:
            return None

    def delete_document(self, document_id):
        # Implementa la lógica de eliminación según tus necesidades
        return 'Implementar lógica de eliminación'

    def close_connection(self):
        self.conn.close()
