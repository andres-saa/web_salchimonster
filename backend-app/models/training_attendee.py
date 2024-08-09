from schema.training import TrainingAttendee,TrainingAttendeeList  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os
from typing import List
from datetime import datetime, timedelta
import pytz
from models.training import TrainingModel
from models.mail import enviar_correo
from models.employer import Employer

load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

 # Asegúrate de importar tu esquema Pydantic para trainings
class TrainingAttendeeModel:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_attendees(self):
        select_query = "SELECT * FROM training_attendees;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_attendee_by_id(self, training_id, attendee_id):
        select_query = "SELECT * FROM training_attendees WHERE training_id = %s AND attendee_id = %s;"
        self.cursor.execute(select_query, (training_id, attendee_id))
        columns = [desc[0] for desc in self.cursor.description]
        attendee_data = self.cursor.fetchone()

        if attendee_data:
            return dict(zip(columns, attendee_data))
        else:
            return None



    def select_attendees_with_status(self, training_id):
        select_query = """
        SELECT 
            ta.attendee_id, 
            e.name as attendee_name, 
            ta.assigned
        FROM 
            training_attendees ta
        JOIN 
            employers e 
        ON 
            ta.attendee_id = e.id
        WHERE 
            ta.training_id = %s;
        """
        self.cursor.execute(select_query, (training_id,))
        attendees = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in attendees]

    def select_all_attendees_for_training(self, training_id):
        select_query = "SELECT * FROM training_attendees WHERE training_id = %s;"
        self.cursor.execute(select_query, (training_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def insert_attendees(self, attendees: TrainingAttendeeList):
        if not attendees:
            return  # No hacer nada si la lista está vacía

        training_id = attendees[0].training_id

        # Lista de IDs de asistentes para mantener
        attendee_ids_to_keep = [a.attendee_id for a in attendees]

        # Paso 1: Eliminar los asistentes que no están en la lista proporcionada
        self.cursor.execute("DELETE FROM training_attendees WHERE training_id = %s AND attendee_id NOT IN %s",
                            (training_id, tuple(attendee_ids_to_keep)))

        # Paso 2: Insertar nuevos asistentes, ignorando los conflictos
        insert_query = """
        INSERT INTO training_attendees (training_id, attendee_id, assigned, attendance_time)
        VALUES (%s, %s, %s, %s) ON CONFLICT (training_id, attendee_id) DO NOTHING;
        """
        values_to_insert = [(a.training_id, a.attendee_id, a.assigned, a.attendance_time) for a in attendees]
        self.cursor.executemany(insert_query, values_to_insert)

        self.conn.commit()

        # Enviar invitaciones a los asistentes
        # self.enviar_invitaciones_a_capacitacion(training_id)

    # ... [método enviar_invitaciones_a_capacitacion y otros métodos] ...

    





    def delete_attendee(self, training_id, attendee_id):
        delete_query = "DELETE FROM training_attendees WHERE training_id = %s AND attendee_id = %s RETURNING *;"
        self.cursor.execute(delete_query, (training_id, attendee_id))
        deleted_attendee = self.cursor.fetchone()
        self.conn.commit()
        if deleted_attendee:
            return dict(zip([desc[0] for desc in self.cursor.description], deleted_attendee))
        else:
            return None
        

    def mark_attendance(self, training_id, attendee_id):
        # Get the current UTC time and convert it to Colombian time
        utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
        colombia_time = utc_now.astimezone(pytz.timezone('America/Bogota'))

        # Update the assigned field to True and set the attendance time
        update_query = """
        UPDATE training_attendees
        SET assigned = %s, attendance_time = %s
        WHERE training_id = %s AND attendee_id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (True, colombia_time, training_id, attendee_id))
        updated_attendee = self.cursor.fetchone()
        self.conn.commit()

        if updated_attendee:
            return dict(zip([desc[0] for desc in self.cursor.description], updated_attendee))
        else:
            return None
        




    def select_trainings_invited_to(self, attendee_id):
        select_query = """
        SELECT 
            t.* 
        FROM 
            trainings t
        JOIN 
            training_attendees ta ON t.id = ta.training_id
        WHERE 
            ta.attendee_id = %s;
        """
        self.cursor.execute(select_query, (attendee_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    # ... tus otros métodos ...


 
    def enviar_invitaciones_a_capacitacion(self, training_id):
        # Crear una instancia de TrainingModel para obtener el nombre de la capacitación
        training_model = TrainingModel()
        training_info = training_model.select_training_by_id(training_id)
        training_name = training_info["name"] if training_info else "Capacitación"

        # Obtener todos los asistentes para una capacitación específica
        attendees = self.select_all_attendees_for_training(training_id)

        # Crear una instancia de la clase Employer
        employer_model = Employer()

        # Recorrer la lista de asistentes y enviar correos
        for attendee in attendees:
            # Obtener la información del empleador (asistente) usando su ID
            employer_info = employer_model.select_employer_by_id(attendee["attendee_id"])
            if employer_info and employer_info.get("email"):
                # Preparar el cuerpo del mensaje con el nombre de la capacitación
                cuerpo_mensaje = f"Has sido invitado a la capacitación '{training_name}',en  www.gestion.salchimonster.com/capacitaciones-invitaciones encontrara toda la informacion y archivos que necesite"

                # Enviar correo de invitación
                enviar_correo(
                    destinatario=employer_info["email"],
                    asunto=f"Invitación a la Capacitación: {training_name}",
                    cuerpo=cuerpo_mensaje
                )

        # Cerrar las conexiones
        employer_model.close_connection()
        training_model.close_connection()

    # ... tus otros métodos ...




    def close_connection(self):
        self.conn.close()

