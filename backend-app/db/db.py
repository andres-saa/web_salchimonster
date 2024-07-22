
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import os
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



class Db:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)

    def close_connection(self):
        self.conn.close()

    def execute_query(self, query, params=None, fetch=False):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                self.conn.commit()
                if fetch:
                    return cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")


    def fetch_one(self, query, params=None):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")


    def fetch_all(self, query, params=None):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
       
        self.close_connection()