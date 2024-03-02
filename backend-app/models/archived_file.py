# Asumiendo que tienes un esquema definido para los archivos
from schema.archived_file import ArchivedFile  # Importa tu esquema adecuado
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class ArchivedFiles:
    def __init__(self, file_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.file_id = file_id

    def select_all_files(self):
        select_query = """
        SELECT af.*, a.area_name, dt.type_name 
        FROM archived_files af
        JOIN areas a ON af.id_area = a.id_area
        JOIN DocumentTypes dt ON af.id_type = dt.id_type;
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        # Asegúrate de incluir 'area_name' y 'type_name' en el resultado
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_file_by_id(self, file_id):
        select_query = """
        SELECT af.*, a.area_name, dt.type_name 
        FROM archived_files af
        JOIN areas a ON af.id_area = a.id_area
        JOIN DocumentTypes dt ON af.id_type = dt.id_type
        WHERE af.id_file = %s;
        """
        self.cursor.execute(select_query, (file_id,))
        columns = [desc[0] for desc in self.cursor.description]
        file_data = self.cursor.fetchone()

        if file_data:
            # Asegúrate de incluir 'area_name' y 'type_name' en el resultado
            return dict(zip(columns, file_data))
        else:
            return None


    def insert_file(self, file_data: ArchivedFile):
        insert_query = """
        INSERT INTO archived_files (
            file_name, file_url, file_type, upload_date, id_area, id_type, file_extension
        ) VALUES (%s, %s,%s, %s, %s, %s, %s) RETURNING id_file;
        """
        self.cursor.execute(insert_query, (
            file_data.file_name, file_data.file_url, file_data.file_type,
            file_data.upload_date, file_data.id_area, file_data.id_type,file_data.file_extension
        ))
        file_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return file_id


    def select_files_by_area(self, area_id):
        select_query = """
        SELECT af.*, a.area_name, dt.type_name 
        FROM archived_files af
        JOIN areas a ON af.id_area = a.id_area
        JOIN DocumentTypes dt ON af.id_type = dt.id_type
        WHERE af.id_area = %s;
        """
        self.cursor.execute(select_query, (area_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_files_by_type(self, type_id):
        select_query = """
        SELECT af.*, a.area_name, dt.type_name 
        FROM archived_files af
        JOIN areas a ON af.id_area = a.id_area
        JOIN DocumentTypes dt ON af.id_type = dt.id_type
        WHERE af.id_type = %s;
        """
        self.cursor.execute(select_query, (type_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_files_by_area_and_type(self, area_id, type_id):
        select_query = """
        SELECT af.*, a.area_name, dt.type_name 
        FROM archived_files af
        JOIN areas a ON af.id_area = a.id_area
        JOIN DocumentTypes dt ON af.id_type = dt.id_type
        WHERE af.id_area = %s AND af.id_type = %s;
        """
        self.cursor.execute(select_query, (area_id, type_id))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]



    def update_file(self, file_id, updated_data: ArchivedFile):
        update_query = """
        UPDATE archived_files
        SET file_name = %s, file_url = %s, file_type = %s, upload_date = %s, id_area = %s, id_type = %s
        WHERE id_file = %s
        RETURNING *;
        """

        self.cursor.execute(update_query, (
            updated_data.file_name, updated_data.file_url, updated_data.file_type,
            updated_data.upload_date, updated_data.id_area, updated_data.id_type, file_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_file_data = self.cursor.fetchone()

        if updated_file_data:
            return dict(zip(columns, updated_file_data))
        else:
            return None

    def delete_file(self, file_id):
        # Primero, obtén la URL o la ruta del archivo para poder eliminarlo del sistema de archivos
        
        # Luego, elimina el archivo de la base de datos
        delete_query = "DELETE FROM archived_files WHERE id_file = %s"
        self.cursor.execute(delete_query, (file_id,))
        self.conn.commit()
        return "Archivo eliminado exitosamente"

    

    def close_connection(self):
        self.conn.close()














class Areas:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_areas(self):
        select_query = "SELECT * FROM areas;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_area_by_id(self, area_id):
        select_query = "SELECT * FROM areas WHERE id_area = %s;"
        self.cursor.execute(select_query, (area_id,))
        columns = [desc[0] for desc in self.cursor.description]
        area_data = self.cursor.fetchone()

        if area_data:
            return dict(zip(columns, area_data))
        else:
            return None

    def insert_area(self, area_name):
        insert_query = "INSERT INTO areas (area_name) VALUES (%s) RETURNING id_area;"
        self.cursor.execute(insert_query, (area_name,))
        area_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return area_id

    def update_area(self, area_id, new_area_name):
        update_query = "UPDATE areas SET area_name = %s WHERE id_area = %s RETURNING *;"
        self.cursor.execute(update_query, (new_area_name, area_id))
        updated_area_data = self.cursor.fetchone()
        
        if updated_area_data:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, updated_area_data))
        else:
            return None

    def delete_area(self, area_id):
        # Implementa aquí tu lógica para desactivar o eliminar el área.
        delete_query = "DELETE FROM areas WHERE id_area = %s;"
        self.cursor.execute(delete_query, (area_id,))
        self.conn.commit()
        return f"Area with id {area_id} was deleted successfully."

    def close_connection(self):
        self.conn.close()






















class DocumentTypes:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_types(self):
        select_query = "SELECT * FROM DocumentTypes;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_type_by_id(self, type_id):
        select_query = "SELECT * FROM DocumentTypes WHERE id_type = %s;"
        self.cursor.execute(select_query, (type_id,))
        columns = [desc[0] for desc in self.cursor.description]
        type_data = self.cursor.fetchone()

        if type_data:
            return dict(zip(columns, type_data))
        else:
            return None

    def insert_type(self, type_name):
        insert_query = "INSERT INTO DocumentTypes (type_name) VALUES (%s) RETURNING id_type;"
        self.cursor.execute(insert_query, (type_name,))
        type_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return type_id

    def update_type(self, type_id, new_type_name):
        update_query = "UPDATE DocumentTypes SET type_name = %s WHERE id_type = %s RETURNING *;"
        self.cursor.execute(update_query, (new_type_name, type_id))
        updated_type_data = self.cursor.fetchone()
        
        if updated_type_data:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, updated_type_data))
        else:
            return None

    def delete_type(self, type_id):
        # Implementa aquí tu lógica para desactivar o eliminar el tipo de documento.
        delete_query = "DELETE FROM DocumentTypes WHERE id_type = %s;"
        self.cursor.execute(delete_query, (type_id,))
        self.conn.commit()
        return f"Document type with id {type_id} was deleted successfully."

    def close_connection(self):
        self.conn.close()


























