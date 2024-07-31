from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.video import Video as video_schema, VideoPost as video_post_schema, VideoUpdate as video_update_schema


class Video:
    def __init__(self):
        self.db = DataBase()


    def get_all_video(self):
        query = 'SELECT * FROM video_training.video_view;'
        result = self.db.fetch_all(query)
        return result
    
    def get_video_by_sequence_id(self, sequence_id:int):
        query = 'SELECT * FROM video_training.sequence_videos_view where sequence_id = %s;'
        result = self.db.execute_query(query, [sequence_id],fetch=True)
        return result
    

        
    def get_video_by_sequence_id_and_student_id(self, sequence_id:int, student_id:int):
        query = 'SELECT * FROM video_training.sequence_videos_view_student where sequence_id = %s and student_id =%s;'
        result = self.db.execute_query(query, [sequence_id, student_id],fetch=True)
        return result

    def insert_video(self, data:video_post_schema,):
        query= 'INSERT INTO video_training.video (name, created_by, description, link) values (%s, %s, %s, %s) returning id'
        video_id = self.db.execute_query(query,[ data.name, data.created_by, data.description, data.link],fetch=True)

        query_add_to_sequence = 'INSERT INTO video_training.video_to_sequence(video_id, sequence_id, created_by) VALUES ( %s, %s, %s);'
        self.db.execute_query(query_add_to_sequence,[video_id[0]["id"], data.sequence_id,data.created_by ])
        return video_id
    
    def delete_video(self, video_id):
        query= 'UPDATE  video_training.video SET exist = false where id = %s RETURNING id'
        video_id = self.db.execute_query(query,[ video_id],fetch=True)
        return video_id
    
    def update_video(self,video_id, data:video_update_schema):
        query= 'UPDATE  video_training.video SET name = %s, description = %s, link = %s  where id = %s RETURNING id'
        video_id = self.db.execute_query( query ,[ data.name , data.description , data.link , video_id ] , fetch=True )
        return video_id

    def close_connection(self):
        self.db.conn.close()