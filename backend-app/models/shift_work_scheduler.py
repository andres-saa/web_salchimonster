import psycopg2
from dotenv import load_dotenv
import os
# from schema.work_scheduler import ShiftWorkRecord, ShiftWorkShift
from schema.shift_work_scheduler import ShiftWorkDay, ShiftWorkRecord, ShiftWorkShift
# Cargar las variables de entorno desde .env
from datetime import date, time
from fastapi import HTTPException
from datetime import date, timedelta


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



class ShiftWorkShiftCRUD:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_ShiftWorkShift(self):
            self.cursor.execute("SELECT * FROM ShiftWorkShift;")
            shifts = self.cursor.fetchall()
            columns = [desc[0] for desc in self.cursor.description]
            return [dict(zip(columns, shift)) for shift in shifts]
        
    def create_work_shift(self, shift_data: ShiftWorkShift):
        insert_query = """
        INSERT INTO ShiftWorkShift (start_time, end_time, description)
        VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (shift_data.start_time, shift_data.end_time, shift_data.description))
        shift_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return shift_id

    def read_work_shift(self, shift_id: int):
        select_query = "SELECT * FROM ShiftWorkShift WHERE id = %s;"
        self.cursor.execute(select_query, (shift_id,))
        shift = self.cursor.fetchone()
        return shift

    def update_work_shift(self, shift_id: int, new_data: ShiftWorkShift):
        update_query = """
        UPDATE ShiftWorkShift
        SET start_time = %s, end_time = %s, description = %s
        WHERE id = %s RETURNING *;
        """
        self.cursor.execute(update_query, (new_data.start_time, new_data.end_time, new_data.description, shift_id))
        self.conn.commit()
        return self.cursor.fetchone()

    def delete_work_shift(self, shift_id: int):
        delete_query = "DELETE FROM ShiftWorkShift WHERE id = %s;"
        self.cursor.execute(delete_query, (shift_id,))
        self.conn.commit()
        return f"Work shift {shift_id} deleted successfully."

    def close_connection(self):
        self.conn.close()

class ShiftWorkRecordCRUD:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_ShiftWorkRecord(self):
        self.cursor.execute("SELECT * FROM ShiftWorkRecord;")
        records = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, record)) for record in records]
    
    def create_work_record(self, record_data: ShiftWorkRecord):
        insert_query = """
        INSERT INTO ShiftWorkRecord (employer_id, work_day_id, start_time, end_time, comments, rest)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
        """
        # Nota que se elimina record_data.date de los parámetros
        self.cursor.execute(insert_query, (record_data.employer_id, record_data.work_day_id, record_data.start_time, record_data.end_time, record_data.comments or None, record_data.rest or False))
        record_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return record_id

    def read_work_record(self, record_id: int):
        select_query = "SELECT * FROM ShiftWorkRecord WHERE id = %s;"
        self.cursor.execute(select_query, (record_id,))
        record = self.cursor.fetchone()
        return record

    def update_work_record(self, record_id: int, new_data: ShiftWorkRecord):
        update_query = """
        UPDATE ShiftWorkRecord
        SET employer_id = %s, work_day_id = %s, date = %s, start_time = %s, end_time = %s, comments = %s
        WHERE id = %s RETURNING *;
        """
        self.cursor.execute(update_query, (new_data.employer_id, new_data.work_day_id, new_data.date, new_data.start_time, new_data.end_time, new_data.comments, record_id))
        self.conn.commit()
        return self.cursor.fetchone()

    def delete_work_record(self, record_id: int):
        delete_query = "DELETE FROM ShiftWorkRecord WHERE employer_id = %s;"
        self.cursor.execute(delete_query, (record_id,))
        self.conn.commit()
        return f"Work record {record_id} deleted successfully."

    def close_connection(self):
        self.conn.close()
    
    
class ShiftWorkDayCRUD:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()


    def create_work_week(self, work_day_date: date, site_id: int):
        # Calcular el inicio y el fin de la semana (asumiendo que la semana comienza el lunes)
        start_of_week = work_day_date - timedelta(days=work_day_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        created_days = []

        for single_date in (start_of_week + timedelta(n) for n in range(7)):
            check_query = "SELECT * FROM ShiftWorkDay WHERE date = %s AND site_id = %s;"
            self.cursor.execute(check_query, (single_date, site_id))
            existing_day = self.cursor.fetchone()

            if existing_day:
                print(f"El día {single_date} con el mismo site_id ya está registrado.")
                continue  # Continuar con el siguiente día si este ya existe

            insert_query = "INSERT INTO ShiftWorkDay (date, site_id) VALUES (%s, %s) RETURNING id, date, site_id;"
            self.cursor.execute(insert_query, (single_date, site_id))
            new_day = self.cursor.fetchone()
            self.conn.commit()

            # Verificar que la fecha se haya insertado correctamente
            self.cursor.execute("SELECT date FROM ShiftWorkDay WHERE id = %s;", (new_day[0],))
            inserted_date = self.cursor.fetchone()[0]
            print(f"Inserted date: {inserted_date}")

            created_days.append({'id': new_day[0], 'date': new_day[1], 'site_id': new_day[2]})

        return created_days

    
    def select_work_days_with_records_by_date_and_site(self, start_date: date, end_date: date, site_id: int):
        self.cursor.execute("""
            SELECT wd.id as work_day_id, wd.date, wd.site_id, wr.id as record_id, wr.employer_id, (wr.start_time at time zone 'America/Bogota') as start_time, (wr.end_time at time zone 'America/Bogota') as end_time, wr.rest
            FROM ShiftWorkDay wd
            LEFT JOIN ShiftWorkRecord wr ON wd.id = wr.work_day_id
            WHERE wd.date BETWEEN %s AND %s AND wd.site_id = %s;
        """, (start_date, end_date, site_id))
        results = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]

        work_days = {}
        for row in results:
            work_day_id = row[columns.index('work_day_id')]
            if work_day_id not in work_days:
                work_days[work_day_id] = {
                    'id': work_day_id,
                    'date': row[columns.index('date')],
                    'site_id': row[columns.index('site_id')],
                    'records': []
                }

            if row[columns.index('record_id')]:
                work_days[work_day_id]['records'].append({
                    'record_id': row[columns.index('record_id')],
                    'employer_id': row[columns.index('employer_id')],
                    'start_time': row[columns.index('start_time')],
                    'end_time': row[columns.index('end_time')],
                    'rest': row[columns.index('rest')]
                    
                })

        # Ordenar los work_days por fecha de menor a mayor
        sorted_work_days = sorted(work_days.values(), key=lambda x: x['date'])

        return sorted_work_days

    
    
    
    def select_all_work_days_with_records(self):
        self.cursor.execute("""
            SELECT wd.id as work_day_id, wd.date, wr.id as record_id, wr.employer_id, wr.start_time, wr.end_time
            FROM ShiftWorkDay wd
            LEFT JOIN ShiftWorkRecord wr ON wd.id = wr.work_day_id;
        """)
        results = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]

        # Transformar los resultados en una estructura más útil
        work_days = {}
        for row in results:
            work_day_id = row[columns.index('work_day_id')]
            if work_day_id not in work_days:
                work_days[work_day_id] = {
                    'id': work_day_id,
                    'date': row[columns.index('date')],
                    'records': []
                }

            if row[columns.index('record_id')]:
                work_days[work_day_id]['records'].append({
                    'record_id': row[columns.index('record_id')],
                    'employer_id': row[columns.index('employer_id')],
                    'start_time': row[columns.index('start_time')],
                    'end_time': row[columns.index('end_time')]
                })

        return list(work_days.values())

    def read_work_day(self, work_day_id: int):
        select_query = "SELECT * FROM ShiftWorkDay WHERE id = %s;"
        self.cursor.execute(select_query, (work_day_id,))
        return self.cursor.fetchone()

    def update_work_day(self, work_day_id: int, new_date: date):
        update_query = "UPDATE ShiftWorkDay SET date = %s WHERE id = %s RETURNING *;"
        self.cursor.execute(update_query, (new_date, work_day_id))
        self.conn.commit()
        return self.cursor.fetchone()

    def delete_work_day(self, work_day_id: int):
        # Primero, eliminar todos los registros de trabajo asociados con este día de trabajo
        delete_records_query = "DELETE FROM ShiftWorkRecord WHERE work_day_id = %s;"
        self.cursor.execute(delete_records_query, (work_day_id,))
        self.conn.commit()

        # Luego, eliminar el día de trabajo
        delete_day_query = "DELETE FROM ShiftWorkDay WHERE id = %s;"
        self.cursor.execute(delete_day_query, (work_day_id,))
        self.conn.commit()
        
        return f"Work day {work_day_id} and all associated work records deleted successfully."

    def select_all_work_days(self):
        self.cursor.execute("SELECT * FROM ShiftWorkDay;")
        work_days = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, work_day)) for work_day in work_days]

    def close_connection(self):
        self.conn.close()
