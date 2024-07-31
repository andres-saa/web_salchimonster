from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sequence_video import SequenceVideoPost as sechence_schema, SequenceVideoUpdate as sequence_update_schema



class SequenceVideo:
    def __init__(self):
        self.db = DataBase()

    def get_all_sequence_video(self):
        query = 'SELECT * FROM video_training.sequence_view'
        result = self.db.fetch_all(query)
        return result
    
    def get_sequence_video_by_sesion_id(self, sesion_id:int):
        query = 'SELECT * FROM video_training.sequence_view where sesion_id = %s;'
        result = self.db.execute_query(query, [sesion_id],fetch=True)
        return result
    

    def get_sequence_video_by_student_id(self, student_id:int):
        query = 'SELECT * FROM video_training.sequence_view_student where student_id = %s;'
        result = self.db.execute_query(query, [student_id],fetch=True)
        return result

    def insert_sequence_video(self, data:sechence_schema,):
        query= 'INSERT INTO video_training.sequence_video (name, created_by, description, sesion_id) values (%s, %s, %s, %s) returning id'
        sequence_video_id = self.db.execute_query(query,[ data.name, data.created_by, data.description, data.sesion_id],fetch=True)
        return sequence_video_id
    
    def delete_sequence_video(self, sequence_video_id):
        query= 'UPDATE  video_training.sequence_video SET exist = false where id = %s RETURNING id'
        sequence_video_id = self.db.execute_query(query,[ sequence_video_id],fetch=True)
        return sequence_video_id
    
    def update_sequence_video(self,sequence_video_id, data:sequence_update_schema):
        query= 'UPDATE  video_training.sequence_video SET name = %s, description = %s where id = %s RETURNING id'
        sequence_video_id = self.db.execute_query(query,[data.name,data.description, sequence_video_id],fetch=True)
        return sequence_video_id

    def close_connection(self):
        self.db.conn.close()