from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sesion import Sesion as sesion_schema, SesionUpdate as sesion_update_schema




class Sesion:
    def __init__(self):
        self.db = DataBase()

    def get_all_sesion(self):
        query = 'SELECT * FROM video_training.sesion_view'
        result = self.db.fetch_all(query)
        return result
    
    def insert_sesion(self, data:sesion_schema,):
        query= 'INSERT INTO video_training.sesion (name, created_by, description) values (%s, %s,%s) returning id'
        sesion_id = self.db.execute_query(query,[ data.name, data.created_by, data.description],fetch=True)
        return sesion_id
    
    def delete_sesion(self, sesion_id):
        query= 'UPDATE  video_training.sesion SET exist = false where id = %s RETURNING id'
        sesion_id = self.db.execute_query(query,[ sesion_id],fetch=True)
        return sesion_id
    
    def update_sesion(self,sesion_id, data:sesion_update_schema):
        query= 'UPDATE  video_training.sesion SET name = %s, description = %s where id = %s RETURNING id'
        sesion_id = self.db.execute_query( query , [ data.name, data.description, sesion_id ], fetch=True )
        return sesion_id
    
    def close_connection(self):
        self.db.conn.close()