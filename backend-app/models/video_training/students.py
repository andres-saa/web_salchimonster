from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sesion import Sesion as sesion_schema, SesionUpdate as sesion_update_schema

from schema.video_training.user_sequence import ReplaceUserSequencesInput
from schema.video_training.video import markVideo

class Student:
    def __init__(self):
        self.db = DataBase()

    def get_students_enrolled_by_sequence_id(self,sequence_id:int):
        query = 'SELECT * FROM video_training.enrrolled_students where sequence_id = %s'
        result = self.db.fetch_all(query,[sequence_id])
        return result
    


    def get_video_mark_users(self,video_id:int):
        query = 'SELECT * FROM video_training.mark_video_users_view where video_id = %s or video_id is null'
        result = self.db.fetch_all(query,[video_id])
        return result





    def get_students_by_sequence_id(self,sequence_id:int):
        query = """
        WITH RankedStudents AS (
            SELECT
                user_name,
                id,
                site_id,
                sequence_id,
                enrolled,
                gender,
                site_name,
                position,
                ROW_NUMBER() OVER (PARTITION BY id ORDER BY 
                    CASE 
                        WHEN sequence_id = %s AND enrolled = true THEN 0
                        ELSE 1
                    END
                ) AS rn
            FROM video_training.enrrolled_students
        )
        SELECT
            user_name,
            id,
            site_id,
            CASE 
                WHEN sequence_id = %s THEN sequence_id 
                ELSE NULL 
            END AS sequence_id,
            CASE 
                WHEN sequence_id = %s AND enrolled = true THEN true 
                ELSE false 
            END AS enrolled,
            gender,
            site_name,
            position
        FROM RankedStudents
        WHERE rn = 1
        """
        result = self.db.fetch_all(query,[sequence_id,sequence_id,sequence_id])
        return result
    

    def mark_video(self,data:markVideo):
        query, params = self.db.build_insert_query('video_training.mark_video_watch',data,'id')
        result = self.db.execute_query(query,params)
        return result


    
    def get_students_enrolled_by_sequence_id_group_by_site(self, sequence_id: int):
        query = 'SELECT * FROM video_training.enrrolled_students WHERE sequence_id = %s and enrolled = true'
        result = self.db.fetch_all(query, [sequence_id])
        
        # Crear un diccionario para almacenar los resultados agrupados
        grouped_result = {}
        
        # Iterar sobre los resultados
        for row in result:
            site_name = row['site_name']
            user_data = {
                'user_name': row['user_name'],
                'id': row['id'],
                'site_id': row['site_id'],
                'sequence_id': row['sequence_id'],
                'enrolled': row['enrolled'],
                'gender':row['gender']
            }
            
            # Si el nombre de la sede no está en el diccionario, añadirlo con una lista vacía
            if site_name not in grouped_result:
                grouped_result[site_name] = []
            
            # Añadir el usuario a la lista correspondiente en el diccionario
            grouped_result[site_name].append(user_data)
        
        return grouped_result


    def get_students_by_sequence_id_group_by_site(self, sequence_id: int):
        query = """
        WITH RankedStudents AS (
            SELECT
                user_name,
                id,
                site_id,
                sequence_id,
                enrolled,
                gender,
                site_name,
                position,
                ROW_NUMBER() OVER (PARTITION BY id ORDER BY 
                    CASE 
                        WHEN sequence_id = %s AND enrolled = true THEN 0
                        ELSE 1
                    END
                ) AS rn
            FROM video_training.enrrolled_students
        )
        SELECT
            user_name,
            id,
            site_id,
            CASE 
                WHEN sequence_id = %s THEN sequence_id 
                ELSE NULL 
            END AS sequence_id,
            CASE 
                WHEN sequence_id = %s AND enrolled = true THEN true 
                ELSE false 
            END AS enrolled,
            gender,
            site_name,
            position
        FROM RankedStudents
        WHERE rn = 1
        """
        result = self.db.fetch_all(query, [sequence_id,sequence_id,sequence_id])
        
        # Crear un diccionario para almacenar los resultados agrupados
        grouped_result = {}
        
        # Iterar sobre los resultados
        for row in result:
            site_name = row['site_name']
            user_data = {
                'user_name': row['user_name'],
                'id': row['id'],
                'site_id': row['site_id'],
                'sequence_id': row['sequence_id'],
                'enrolled': row['enrolled'],
                'gender':row['gender']
            }
            
            # Si el nombre de la sede no está en el diccionario, añadirlo con una lista vacía
            if site_name not in grouped_result:
                grouped_result[site_name] = []
            
            # Añadir el usuario a la lista correspondiente en el diccionario
            grouped_result[site_name].append(user_data)
        
        return grouped_result

    
    def get_students_enrolled_by_sequence_id_group_by_position(self, sequence_id: int):
        query = 'SELECT * FROM video_training.enrrolled_students WHERE sequence_id = %s and enrolled = true'
        result = self.db.fetch_all(query, [sequence_id])
        
        # Crear un diccionario para almacenar los resultados agrupados
        grouped_result = {}
        
        # Iterar sobre los resultados
        for row in result:
            site_name = row['position']
            user_data = {
                'user_name': row['user_name'],
                'id': row['id'],
                'site_id': row['site_id'],
                'sequence_id': row['sequence_id'],
                'enrolled': row['enrolled'],
                'gender':row['gender']
            }
            
            # Si el nombre de la sede no está en el diccionario, añadirlo con una lista vacía
            if site_name not in grouped_result:
                grouped_result[site_name] = []
            
            # Añadir el usuario a la lista correspondiente en el diccionario
            grouped_result[site_name].append(user_data)
        
        return grouped_result


    def get_students_by_sequence_id_group_by_position(self, sequence_id: int):
        query = """
        WITH RankedStudents AS (
            SELECT
                user_name,
                id,
                site_id,
                sequence_id,
                enrolled,
                gender,
                site_name,
                position,
                ROW_NUMBER() OVER (PARTITION BY id ORDER BY 
                    CASE 
                        WHEN sequence_id = %s AND enrolled = true THEN 0
                        ELSE 1
                    END
                ) AS rn
            FROM video_training.enrrolled_students
        )
        SELECT
            user_name,
            id,
            site_id,
            CASE 
                WHEN sequence_id = %s THEN sequence_id 
                ELSE NULL 
            END AS sequence_id,
            CASE 
                WHEN sequence_id = %s AND enrolled = true THEN true 
                ELSE false 
            END AS enrolled,
            gender,
            site_name,
            position
        FROM RankedStudents
        WHERE rn = 1
        
        """
        result = self.db.fetch_all(query, [sequence_id,sequence_id,sequence_id])
        
        # Crear un diccionario para almacenar los resultados agrupados
        grouped_result = {}
        
        # Iterar sobre los resultados
        for row in result:
            site_name = row['position']
            user_data = {
                'user_name': row['user_name'],
                'id': row['id'],
                'site_id': row['site_id'],
                'sequence_id': row['sequence_id'],
                'enrolled': row['enrolled'],
                'gender':row['gender']
            }
            
            # Si el nombre de la sede no está en el diccionario, añadirlo con una lista vacía
            if site_name not in grouped_result:
                grouped_result[site_name] = []
            
            # Añadir el usuario a la lista correspondiente en el diccionario
            grouped_result[site_name].append(user_data)
        
        return grouped_result


    def replace_user_sequences(self, data: ReplaceUserSequencesInput):
        sequence_id = data.sequence_id
        user_ids = data.users  # Lista de IDs de usuario
        
        # Verificar que el sequence_id existe en la tabla sequence_video
        check_sequence_query = 'SELECT 1 FROM video_training.sequence_video WHERE id = %s'
        sequence_exists = self.db.fetch_one(check_sequence_query, [sequence_id])
        
        if not sequence_exists:
            raise ValueError(f"sequence_id {sequence_id} does not exist in sequence_video table.")
        
        # Primero, borrar los registros existentes para la sequence_id
        delete_query = 'DELETE FROM video_training.user_sequence WHERE sequence_id = %s'
        self.db.execute_query(delete_query, [sequence_id])
        
        # Construir la consulta de inserción para múltiples valores
        if user_ids:
            insert_values = ', '.join(f'(%s, %s)' for _ in user_ids)
            insert_query = f'INSERT INTO video_training.user_sequence (user_id, sequence_id) VALUES {insert_values}'
            
            # Crear una lista de parámetros para la consulta
            params = []
            for user_id in user_ids:
                params.extend([user_id, sequence_id])
            
            # Ejecutar la consulta de inserción con todos los parámetros
            self.db.execute_query(insert_query, params)
 



    def close_connection(self):
        self.db.conn.close()