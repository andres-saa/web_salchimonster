from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.city import citySchema
from schema.inventory.inventory import GroupDailyInventoryItems,DailyInventoryItems
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class Contest:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        
    
    def get_all_contests_with_participation(self, user_id):
        query = f"""
        SELECT 
            c.*, 
            EXISTS (
                SELECT 1 
                FROM contest.contest_entry ce 
                WHERE ce.participant_id = {user_id} AND ce.contest_id = c.id
            ) AS entry_exists
        FROM contest.contest c;
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    def get_all_constests_participate (self,contest_ids,user_id):
        query = f""" SELECT EXISTS (
            SELECT 1 
            FROM contest.contest_entry 
            WHERE participant_id = {user_id} and id in ( {contest_ids})
        ) AS entry_exists;        
                """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    
    def get_all_participation_by_user (self,user_id,contest_id):
        query = f"""SELECT * FROM contest.evidence_full_view WHERE participant_id = {user_id} and contest_id = {contest_id};
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
  
    def close_connection(self):
        self.conn.close()


