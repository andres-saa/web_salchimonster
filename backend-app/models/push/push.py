from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from db.db import Db as DataBase
from schema.video_training.sesion import Sesion as sesion_schema, SesionUpdate as sesion_update_schema
from schema.recipes.recipe_data_seet import RecipeDataSheet,RecipeDataSheetPost,RecipeDataSheetUpdate
from schema.video_training.user_sequence import ReplaceUserSequencesInput
from schema.video_training.video import markVideo
from schema.recipes.ingredients import IngredientsPost,IngredientsUpdate
from schema.permision.permision import toggle_permision
from datetime import time
from typing import Dict, List
import json


class SiteSubscription(BaseModel):
    site_id: int
    endpoint: str
    keys: Dict


class Push:
    def __init__(self):
        self.db = DataBase()
        
    
    
    
    def create_push(self, data:SiteSubscription):
        query = """INSERT INTO push.site_push_subscriptions(
        site_id, endpoint, keys)
        VALUES (%s, %s, %s);"""
        
        result = self.db.execute_query(query=query,params=[data.site_id,data.endpoint,json.dumps(data.keys) ])
        return result
    
    
    def get_push(self, site_id:int):
        query = "select endpoint, keys from push.site_push_subscriptions where site_id = %s"
        result = self.db.fetch_all(query=query, params=[site_id])

        return result
        
        
            


    def close_connection(self):
        self.db.conn.close()