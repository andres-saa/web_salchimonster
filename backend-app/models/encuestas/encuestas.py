from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
from schema.city import citySchema
# from schema.order import OrderSchemaPost
from schema.order import OrderSchemaPost
from models.user import User
from schema.user import user_schema_post
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from datetime import datetime, time
from config.wsp import enviar_mensaje_whatsapp
import pytz
from psycopg2.extras import Json
from dateutil import parser  # Asegúrate de tener python-dateutil instalado
from db.db import Db as DataBase
from typing import List, Optional
from schema.user import user_schema_post

from models.user import User



class Votacion(BaseModel):
    question_id:int
    option_id:Optional[int] = None
    text:Optional[str] = None
    question:Optional[str] = None


class EncuestaVotar(BaseModel):
    encuesta_id:int
    user:user_schema_post
    select:List[Votacion]


class Encuesta:
    def __init__(self):
        self.db = DataBase()
        
    def get_encuesta(self):
        query = 'SELECT * FROM encuesta.encuesta_view'
        result = self.db.fetch_one(query)
        return result
    
    
    def get_encuesta_by_id(self,id:int):
        query = 'SELECT * FROM encuesta.encuesta_view where id = %s'
        
        result = self.db.fetch_one(query=query,params=[id])
        return result

    
    def get_encuestas(self):
        query = 'SELECT * FROM encuesta.encuesta_view'
        result = self.db.fetch_all(query)
        return result
    
    def get_encuesta_users(self,encuesta_id:int ): 
        query = f'SELECT * FROM encuesta.results_view_people where encuesta_id = {encuesta_id}'
        result = self.db.fetch_all(query)
        return result
    
    def get_encuesta_results(self,encuesta_id:int):
        query = f'SELECT * FROM encuesta.results_summary_view where encuesta_id = {encuesta_id}'
        result = self.db.fetch_all(query)
        return result

    def votar(self,response:EncuestaVotar):
        code, user_id = self.create_user(response.user)
        for r in response.select:
            query =  """ INSERT INTO encuesta.response(
                           question_id, option_id, user_id, text)
                            VALUES (%s, %s, %s, %s);
                    """
            params = [r.question_id,r.option_id,user_id,r.text ]
            self.db.execute_query(query=query, params=params)
        return code
    
    
    def votar_encuesta(self,response:EncuestaVotar):
        code, user_id = self.create_user(response.user)
        for r in response.select:
            query =  """ INSERT INTO encuesta.satisfaccion_response (data) values (%s);
                    """
            params = [response ]
            self.db.execute_query_model(query=query, params=params)
        return code
        
    
    def close_connection(self):
        self.conn.close()

    def create_user(self, user_data):
        code, user_id = User().insert_user_code2(user_data)
        return code, user_id
        
