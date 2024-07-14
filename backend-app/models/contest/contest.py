from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.city import citySchema
from schema.inventory.inventory import GroupDailyInventoryItems,DailyInventoryItems
from schema.contests.contest import Contest
load_dotenv()
from psycopg2.extras import DictCursor,RealDictCursor
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
            cv.*,
            EXISTS (
                SELECT 1 
                FROM contest.contest_entry ce 
                WHERE ce.participant_id = %s AND ce.contest_id = cv.id
            ) AS entry_exists
        FROM contest.contest_view cv where exist = true
        """
        self.cursor.execute(query, (user_id,))
        columns = [desc[0] for desc in self.cursor.description]
        results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        return results


    def get_all_contests_with_participation_visible(self, user_id):
        query = """
        SELECT 
            cv.*,
            EXISTS (
                SELECT 1 
                FROM contest.contest_entry ce 
                WHERE ce.participant_id = %s AND ce.contest_id = cv.id
            ) AS entry_exists
        FROM contest.contest_view cv 
        WHERE visible = true and exist = true
        """
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (user_id,))
            results = cursor.fetchall()
        return results
    


    def get_all_contest_entry_options(self):
        query = """
        SELECT * from contest.evidence_type
        """

        query2 = """
        SELECT * from contest.contest_winner_type
        """

        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query)
            results = cursor.fetchall()

        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query2)
            results2 = cursor.fetchall()


        return {"evidences":results, "winner_type":results2}
    

    def toggle_constest_visible(self, status:bool, id:int):
        query = f"""UPDATE contest.contest set visible = {status} where id = {id}   RETURNING id"""
        self.cursor.execute(query)
        id = self.cursor.fetchone()[0]
        self.conn.commit()
        return id
    

    def delete_contest(self, id:int):
        query = f"""UPDATE contest.contest set exist = false where id = {id}  RETURNING id"""
        self.cursor.execute(query)
        id = self.cursor.fetchone()[0]
        self.conn.commit()
        return id


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
    

    def create_contest(self,Contest):
        if Contest.contest_winner_type_id == 2:
            Contest.evidence_type_id = 4

        query_insert_contest = f"""INSERT INTO contest.contest( name, start_date, end_date, evidence_type_id, description, instructions, contest_winner_type_id , is_site_participation)
                                VALUES ('{ Contest.name }', '{ Contest.start_date }', '{ Contest.end_date }', {Contest.evidence_type_id}, '{Contest.description}', '{Contest.instructions}',{Contest.contest_winner_type_id}, {Contest.is_site_participation}) RETURNING id;"""
        self.cursor.execute(query_insert_contest)
        contest_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return contest_id
    
    def update_contest(self, Contest):

        if Contest.contest_winner_type_id == 2:
            Contest.evidence_type_id = 4
        query_update_contest = f"""
            UPDATE contest.contest
            SET 
                name = '{Contest.name}',
                start_date = '{Contest.start_date}',
                end_date = '{Contest.end_date}',
                evidence_type_id = {Contest.evidence_type_id},
                description = '{Contest.description}',
                instructions = '{Contest.instructions}',
                contest_winner_type_id = {Contest.contest_winner_type_id},
                is_site_participation = {Contest.is_site_participation}
            WHERE id = {Contest.id}
            RETURNING id;
        """
        self.cursor.execute(query_update_contest)
        updated_contest_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return updated_contest_id


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


