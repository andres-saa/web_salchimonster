
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor, Json
import os
from pydantic import BaseModel
from typing import Tuple,Dict,Any
from typing import List, Dict, Optional
from pydantic import BaseModel
import os
import inspect
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



class Db:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)

    def close_connection(self):
        self.conn.close()

    def execute_query(self, query, params=None, fetch=False):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                self.conn.commit()
                if fetch:
                    return cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")



    def execute_query_json(self, query, params=None, fetch=False):
            """
            Ejecuta una consulta SQL procesando automáticamente los parámetros que sean
            de tipo dict o list, envolviéndolos con psycopg2.extras.Json.
            """
            processed_params = self._process_json_params(params)
            try:
                with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query, processed_params)
                    self.conn.commit()
                    if fetch:
                        return cursor.fetchall()
            except Exception as e:
                self.conn.rollback()
                print(f"An error occurred: {e}")

    def _process_json_params(self, params):
        """
        Si se detecta un dict o list en los parámetros, se envuelven en Json().
        """
        if params is None:
            return None

        # Si params es una tupla o lista que representa parámetros posicionales:
        if isinstance(params, (list, tuple)):
            new_params = []
            for param in params:
                if isinstance(param, (dict, list)):
                    new_params.append(Json(param))
                else:
                    new_params.append(param)
            # Si la consulta espera parámetros posicionales, se puede devolver la misma estructura (lista o tupla)
            return type(params)(new_params)
        
        # Si params es un diccionario (por parámetros nombrados):
        elif isinstance(params, dict):
            return {key: Json(value) if isinstance(value, (dict, list)) else value 
                    for key, value in params.items()}
        else:
            return params



    def cargar_archivo_sql(self, nombre_archivo):
        """
        Carga un archivo SQL y devuelve su contenido como un string,
        ajustando automáticamente la ruta en función del archivo que hace la llamada.

        Args:
            nombre_archivo (str): Nombre del archivo SQL (sin ruta).

        Returns:
            str: Contenido del archivo SQL como un string.
        """
        try:
            # Determina el archivo que hace la llamada
            frame_actual = inspect.stack()[1]
            ruta_llamador = os.path.dirname(os.path.abspath(frame_actual.filename))
            
            # Construye la ruta completa del archivo SQL
            ruta_archivo = os.path.join(ruta_llamador, nombre_archivo)
            
            # Lee el contenido del archivo
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no fue encontrado en '{ruta_llamador}'.")
            return None
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
            return None



    def execute_bulk_update(self, query: str, params: List[Dict[str, Any]], fetch: bool = False):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.executemany(query, params)
                self.conn.commit()
                if fetch:
                    return cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")





    def build_bulk_insert_query(self,table_name: str, data_list: List[BaseModel], returning: str = ''):
        if not data_list:
            raise ValueError("The data list cannot be empty")

        # Convertimos la primera instancia de 'data_list' en un diccionario para obtener las claves
        first_data_dict = data_list[0].model_dump()

        # Obtenemos las claves del diccionario, que serán los nombres de las columnas
        columns = ', '.join(first_data_dict.keys())

        # Creamos una lista de placeholders para los valores, usando la sintaxis de parámetros de psycopg2
        values_placeholders = ', '.join([f"%({key})s" for key in first_data_dict.keys()])
        
        # Construimos la parte principal de la consulta INSERT con múltiples valores
        values = ', '.join([f"({values_placeholders})" for _ in data_list])
        query = f'INSERT INTO {table_name} ({columns}) VALUES {values}'

        # Si se proporciona el parámetro 'returning', lo añadimos a la consulta
        if returning:
            query += f' RETURNING {returning}'

        # Convertimos la lista de datos en una lista de diccionarios para pasar a 'execute_bulk_insert'
        data_dict_list = [data.model_dump() for data in data_list]

        return query, data_dict_list
    

    def execute_bulk_insert(self, query: str, params: Optional[List[Dict[str, any]]] = None, fetch: bool = False):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                if params:
                    # Ejecutar consulta con múltiples conjuntos de parámetros
                    cursor.executemany(query, params)
                else:
                    cursor.execute(query)
                self.conn.commit()
                if fetch:
                    return cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
        print(f"An error occurred: {e}")


    def fetch_one(self, query, params=None):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")


    def fetch_all(self, query, params=None):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")


    def __enter__(self):
        return self
    

    def build_insert_query(self, table_name: str, data: BaseModel, returning: str = ''):
        # Convertimos el objeto 'data' en un diccionario
        data_dict = data.model_dump()

        # Obtenemos las claves del diccionario, que serán los nombres de las columnas
        columns = ', '.join(data_dict.keys())

        # Creamos una lista de placeholders para los valores, usando la sintaxis de parámetros de psycopg2
        values = ', '.join([f"%({key})s" for key in data_dict.keys()])

        # Construimos la parte principal de la consulta INSERT
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({values})'

        # Si se proporciona el parámetro 'returning', lo añadimos a la consulta
        if returning:
            query += f' RETURNING {returning}'

        # Retornamos la consulta y el diccionario de datos
        return query, data_dict
    


    def build_update_query(self, table_name: str, data: BaseModel, condition: str, returning: str = ''):
        # Convertimos el objeto 'data' en un diccionario
        data_dict = data.model_dump()

        # Creamos una lista de asignaciones columna=valor
        set_clause = ', '.join([f"{key} = %({key})s" for key in data_dict.keys()])

        # Construimos la parte principal de la consulta UPDATE
        query = f'UPDATE {table_name} SET {set_clause} WHERE {condition}'

        # Si se proporciona el parámetro 'returning', lo añadimos a la consulta
        if returning:
            query += f' RETURNING {returning}'

        # Retornamos la consulta y el diccionario de datos
        return query, data_dict



    def build_select_query(self, table_name: str, fields: list[str], condition: str = '', order_by: str = '', limit: int = 0, offset: int = 0):
        # Construimos la lista de campos a seleccionar
        columns = ', '.join(fields)

        # Construimos la parte principal de la consulta SELECT
        query = f'SELECT {columns} FROM {table_name}'

        # Si se proporciona una condición, la añadimos a la consulta
        if condition:
            query += f' WHERE {condition}'

        # Si se proporciona un orden, lo añadimos a la consulta
        if order_by:
            query += f' ORDER BY {order_by}'

        # Si se proporciona un límite, lo añadimos a la consulta
        if limit > 0:
            query += f' LIMIT {limit}'

        # Si se proporciona un offset, lo añadimos a la consulta
        if offset > 0:
            query += f' OFFSET {offset}'

        # Retornamos la consulta construida
        return query
    


    def build_soft_delete_query(self, table_name: str, condition: str, returning: str = ''):
        # Definimos el campo y el valor a asignar
        set_clause = "exist = FALSE"

        # Construimos la parte principal de la consulta UPDATE
        query = f'UPDATE {table_name} SET {set_clause} WHERE {condition}'

        # Si se proporciona el parámetro 'returning', lo añadimos a la consulta
        if returning:
            query += f' RETURNING {returning}'

        # Retornamos la consulta construida
        return query
    
    
    def build_delete_query(self, table_name: str, condition: str, returning: str = ''):
        query = f'DELETE FROM {table_name} WHERE {condition}'
        if returning:
            query += f' RETURNING {returning}'
        return query


    def __exit__(self, exc_type, exc_val, exc_tb):
       
        self.close_connection()