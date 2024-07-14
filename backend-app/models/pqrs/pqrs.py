from schema.supply import SupplyDeliverySchema
# from schema.site import site_schema_post  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os
from schema.supply import SupplyDeliverySchema, SupplyDeliveryItemSchema
from typing import List, Optional
from psycopg2.extras import RealDictCursor
from schema.pqrs.pqrs import Pqrs

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Pqrs:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()    



    def get_pqrs_by_place_id(self,place_id):
        query = f"""
                SELECT * FROM  pqrs.pqrs_complete_view where place_id = %s order by id
                """
        
        with self.conn.cursor(cursor_factory = RealDictCursor) as cursor:
            cursor.execute(query, (place_id,))
            result = cursor.fetchall()
            return result
        

    def create_pqrs(self,data:Pqrs):
        query = "INSERT INTO pqrs.pqrs (question,answer,place_id) values (%s,%s,%s) returning id;"

        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query,(data.question,data.answer,data.place_id,))
            result  = cursor.fetchone()
            self.conn.commit()
            return result
    
    def update_pqrs(self,data:Pqrs,id):
        query = "UPDATE pqrs.pqrs SET question = %s, answer = %s, place_id = %s where id = %s returning id"
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query,(data.question,data.answer,data.place_id,id))
            result  = cursor.fetchone()
            self.conn.commit()
            return result

    def deactivate_pqrs(self,id):
        query = "UPDATE pqrs.pqrs SET exist = false where id = %s returning id"
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query,(id,))
            result  = cursor.fetchone()
            self.conn.commit()
            return result


    
    def close_connection(self):
        self.conn.close()