from schema.training_file import TrainingFile  # Importa tu esquema Pydantic aquí
import psycopg2
from dotenv import load_dotenv
import os



load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Suponiendo que ya tienes configurado el entorno y las variables de entorno como en el ejemplo de Site

class TrainingFileModel:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_files(self):
        select_query = "SELECT * FROM training_files;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_file_by_id(self, file_id):
        select_query = "SELECT * FROM training_files WHERE id = %s;"
        self.cursor.execute(select_query, (file_id,))
        columns = [desc[0] for desc in self.cursor.description]
        file_data = self.cursor.fetchone()

        if file_data:
            return dict(zip(columns, file_data))
        else:
            return None

    def select_files_by_training_id(self, training_id):
        select_query = "SELECT * FROM training_files WHERE training_id = %s;"
        self.cursor.execute(select_query, (training_id,))
        columns = [desc[0] for desc in self.cursor.description]
        files = self.cursor.fetchall()

        if files:
            return [dict(zip(columns, file)) for file in files]
        else:
            return []


    def update_file(self, file_id, updated_data: TrainingFile):
        update_query = """
        UPDATE training_files
        SET file_name = %s, file_url = %s, file_type = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.file_name, updated_data.file_url, updated_data.file_type, file_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_file_data = self.cursor.fetchone()

        if updated_file_data:
            self.conn.commit()
            return dict(zip(columns, updated_file_data))
        else:
            return None


    def delete_file(self, file_id):
        delete_query = "DELETE FROM training_files WHERE id = %s;"
        self.cursor.execute(delete_query, (file_id,))
        self.conn.commit()
        return {"message": "File deleted successfully"}

    def insert_file(self, file_data: TrainingFile):
        insert_query = """
        INSERT INTO training_files (
            training_id, file_name, file_url, file_type
        ) VALUES (%s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (
            file_data.training_id, file_data.file_name, file_data.file_url, file_data.file_type
        ))
        file_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return file_id

    def delete_file(self, file_id):
        # Implementar lógica de eliminación según tus requisitos.
        return 'Funcionalidad de eliminación no implementada'

    # Si necesitas actualizar archivos, puedes agregar aquí un método update_file.

    def close_connection(self):
        self.conn.close()
