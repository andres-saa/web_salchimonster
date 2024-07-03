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
            (c.start_date AT TIME ZONE 'America/Bogota') AS start_date_bogota,
            (c.end_date AT TIME ZONE 'America/Bogota') AS end_date_bogota,
            EXISTS (
                SELECT 1 
                FROM contest.contest_entry ce 
                WHERE ce.participant_id = {user_id} AND ce.contest_id = c.id
            ) AS entry_exists,
            json_agg(
                json_build_object(
                    'employer_id', rbq.employer_id,
                    'name', rbq.name,
                    'dni', rbq.dni,
                    'site_id', rbq.site_id,
                    'contest_id', rbq.contest_id,
                    'total_entries', rbq.total_entries
                ) ORDER BY rbq.total_entries DESC
            ) AS rbq,
            MAX(rbq.total_entries) AS max_entries
        FROM contest.contest c
        LEFT JOIN (
            SELECT 
                rq.employer_id,
                rq.name,
                rq.dni,
                rq.site_id,
                rq.contest_id,
                CASE
                    WHEN c.contest_winner_type_id = 2 THEN rv.total_value
                    ELSE rq.total_entries
                END AS total_entries
            FROM contest.rank_by_quantity rq
            FULL OUTER JOIN contest.rank_by_total_value rv ON rq.employer_id = rv.employer_id AND rq.contest_id = rv.contest_id
            JOIN contest.contest c ON c.id = rq.contest_id OR c.id = rv.contest_id
        ) rbq ON c.id = rbq.contest_id
        GROUP BY c.id 
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        return results


    

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
        query = f"""SELECT *, (timestamp at time zone 'America/Bogota') as timestamp FROM contest.evidence_full_view WHERE participant_id = {user_id} and contest_id = {contest_id};
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    


    def create_participation(self, evidence, evidence_entry):

        query_insert_evidence = f"""INSERT INTO contest.evidence ( evidence_type_id, evidence_entry, contest_id)  VALUES ({evidence.evidence_type_id},'{evidence.evidence_entry}',{evidence.contest_id})  RETURNING id"""


        self.cursor.execute(query_insert_evidence)
        evidence_id = self.cursor.fetchone()[0]

        query_insert_contest_entry = f"""INSERT INTO contest.contest_entry (participant_id, contest_id, evidence_id,timestamp) values ({evidence_entry.participant_id}, {evidence_entry.contest_id}, {evidence_id}, NOW()) RETURNING id"""

        self.cursor.execute(query_insert_contest_entry)
        contest_entry_id = self.cursor.fetchone()[0]
        self.conn.commit()

        return evidence_id
    


    def updateEntryImageUrl(self,evidence_id,url):
        query = f"""UPDATE contest.evidence  SET  evidence_entry = '{url}' where id = {evidence_id};"""
        self.cursor.execute(query)
        self.conn.commit()

    
    def deleteEvidenceByImageError(self, evidence_id):
        query = f"""DELETE FROM contest.contest_entry where evidence_id = {evidence_id}; DELETE FROM contest.evidence where id = {evidence_id} """
        self.cursor.execute(query)
        self.conn.commit()

    
  
    def close_connection(self):
        self.conn.close()


