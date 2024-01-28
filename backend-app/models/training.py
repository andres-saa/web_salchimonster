from schema.training import Training  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

 # Asegúrate de importar tu esquema Pydantic para trainings

class TrainingModel:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_trainings(self):
        select_query = "SELECT * FROM trainings;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_training_by_id(self, training_id):
        select_query = "SELECT * FROM trainings WHERE id = %s;"
        self.cursor.execute(select_query, (training_id,))
        columns = [desc[0] for desc in self.cursor.description]
        training_data = self.cursor.fetchone()

        if training_data:
            return dict(zip(columns, training_data))
        else:
            return None

    def insert_training(self, training_data: Training):
        insert_query = """
        INSERT INTO trainings (
            creator_id, name, topic, material_url, scheduled_time, status, location
        ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;
        """
        # Convert URL object to a string
        material_url_str = str(training_data.material_url) if training_data.material_url else None

        self.cursor.execute(insert_query, (
            training_data.creator_id, training_data.name, training_data.topic, 
            material_url_str, training_data.scheduled_time, 
            training_data.status, training_data.location
        ))
        training_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return training_id



    def update_training(self, training_id, updated_data: Training):
        try:
            # Convertir Url a str
            material_url = str(updated_data.material_url) if updated_data.material_url else None

            update_query = """
            UPDATE trainings
            SET creator_id = %s, name = %s, topic = %s, material_url = %s, 
            scheduled_time = %s, status = %s, location = %s
            WHERE id = %s
            RETURNING *;
            """

            self.cursor.execute(update_query, (
                updated_data.creator_id, updated_data.name, updated_data.topic, 
                material_url, updated_data.scheduled_time, 
                updated_data.status, updated_data.location, training_id
            ))

            updated_training_data = self.cursor.fetchone()
            self.conn.commit()

            if updated_training_data:
                columns = [desc[0] for desc in self.cursor.description]
                return dict(zip(columns, updated_training_data))
            else:
                return None
        except Exception as e:
            self.conn.rollback()
            print(f"Error updating training: {e}")
            return None

    def delete_training(self, training_id):
        delete_query = "DELETE FROM trainings WHERE id = %s RETURNING *;"
        self.cursor.execute(delete_query, (training_id,))
        deleted_training = self.cursor.fetchone()
        self.conn.commit()
        if deleted_training:
            return dict(zip([desc[0] for desc in self.cursor.description], deleted_training))
        else:
            return None


    def select_trainings_by_creator_id(self, creator_id):
        select_query = "SELECT * FROM trainings WHERE creator_id = %s;"
        self.cursor.execute(select_query, (creator_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def close_connection(self):
        self.conn.close()
