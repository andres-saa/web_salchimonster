
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import os
from pydantic import BaseModel
from typing import Tuple,Dict,Any
from typing import List, Dict, Optional
from pydantic import BaseModel
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

    



#     def build_bulk_update_query(
#     table_name: str,
#     data_list: List[BaseModel],
#     id_field: str = 'id',
#     returning: str = ''
# ) -> (str, Dict[str, Any]):
#     if not data_list:
#         raise ValueError("The data list cannot be empty")

#     # Convertir cada modelo a un diccionario
#     data_dict_list = [model.dict() for model in data_list]

#     # Obtener las columnas de los modelos
#     first_data_dict = data_dict_list[0]
#     columns = [key for key in first_data_dict.keys() if key != id_field]

#     # Crear las cláusulas SET y VALUES
#     set_clauses = ', '.join([f"{col} = updates.{col}" for col in columns])
#     values_clauses = ', '.join([
#         f"(%({col}_{i})s, %({id_field}_{i})s)"
#         for i in range(len(data_list))
#     ])
#     update_clauses = ' OR '.join([f"{id_field} = %({id_field}_{i})s" for i in range(len(data_list))])

#     # Construir la consulta
#     query = f'''
#     WITH updates AS (
#         SELECT * FROM (VALUES {values_clauses}) AS v ({', '.join(columns + [id_field])})
#     )
#     UPDATE {table_name}
#     SET {set_clauses}
#     FROM updates
#     WHERE {table_name}.{id_field} = updates.{id_field}
#     '''

#     if returning:
#         query += f' RETURNING {returning}'

#     # Construir el diccionario de parámetros
#     parameters = {}
#     for i, data in enumerate(data_dict_list):
#         for col in columns:
#             parameters[f"{col}_{i}"] = data.get(col)
#         parameters[f"{id_field}_{i}"] = data.get(id_field)

#     return query, parameters






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