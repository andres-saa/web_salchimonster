from schema.training import AssignedAttendee  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class AssignedAttendeeModel:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_assigned_attendees(self):
        select_query = "SELECT * FROM assigned_attendees;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_assigned_attendee_by_id(self, training_id, attendee_id):
        select_query = "SELECT * FROM assigned_attendees WHERE training_id = %s AND attendee_id = %s;"
        self.cursor.execute(select_query, (training_id, attendee_id))
        columns = [desc[0] for desc in self.cursor.description]
        attendee_data = self.cursor.fetchone()

        if attendee_data:
            return dict(zip(columns, attendee_data))
        else:
            return None

    def select_all_assigned_for_training(self, training_id):
        select_query = "SELECT * FROM assigned_attendees WHERE training_id = %s;"
        self.cursor.execute(select_query, (training_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]



    def insert_assigned_attendee(self, attendee_data: AssignedAttendee):
        insert_query = """
        INSERT INTO assigned_attendees (training_id, attendee_id, assigned_time)
        VALUES (%s, %s, %s) RETURNING training_id, attendee_id, assigned_time;
        """
        self.cursor.execute(insert_query, (
            attendee_data.training_id, attendee_data.attendee_id, attendee_data.assigned_time
        ))
        self.conn.commit()
        
        # Obtener los valores insertados desde la base de datos y devolverlos como un diccionario
        inserted_values = self.cursor.fetchone()
        
        return {
            "training_id": inserted_values[0],
            "attendee_id": inserted_values[1],
            "assigned_time": inserted_values[2]
        }


    def delete_assigned_attendee(self, training_id, attendee_id):
        delete_query = "DELETE FROM assigned_attendees WHERE training_id = %s AND attendee_id = %s RETURNING *;"
        self.cursor.execute(delete_query, (training_id, attendee_id))
        deleted_attendee = self.cursor.fetchone()
        self.conn.commit()
        if deleted_attendee:
            return dict(zip([desc[0] for desc in self.cursor.description], deleted_attendee))
        else:
            return None

    def close_connection(self):
        self.conn.close()
