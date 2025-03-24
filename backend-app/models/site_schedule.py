import psycopg2
from dotenv import load_dotenv
import os
# from schema.role import RoleGroupSchema , RoleSchema
from schema.site_schedule import site_schedule_schema
from datetime import datetime
import pytz
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



class site_schedule:
    def __init__(self):
        self.conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}")
        self.cursor = self.conn.cursor()

    def create_schedule(self,schedule_data:site_schedule_schema ):
        site_id = schedule_data.site_id
        day_of_week = schedule_data.day_of_week
        opening_time = schedule_data.opening_time
        closing_time = schedule_data.closing_time

        # print(site_id,opening_time,closing_time)

        insert_query = f"""INSERT INTO site_schedule 
        (site_id, day_of_week, opening_time, closing_time) 
        values (
            {day_of_week}, 
            {site_id},
            '{opening_time}',
            '{closing_time}') 
            returning schedule_id"""
        
        self.cursor.execute(insert_query)
        schedule_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return schedule_id

    def get_schedule_by_site_id(self, site_id: int):
        query = f"""
        SELECT schedule_id, site_id, day_of_week, opening_time, closing_time
        FROM site_schedule
        WHERE site_id = {site_id}
        ORDER BY day_of_week;
        """
        self.cursor.execute(query)
        schedule_data = self.cursor.fetchall()
        schedule_list = []
        for schedule_id, site_id, day_of_week, opening_time, closing_time in schedule_data:
            schedule_list.append({"schedule_id": schedule_id, "site_id": site_id, "day_of_week": day_of_week, "opening_time": opening_time, "closing_time": closing_time})
        return schedule_list


    def is_site_open(self, site_id: int):
        # Configurar la zona horaria de Colombia

        query = f"""
        SELECT status_json from public.v_site_status
        WHERE site_id = {site_id}
        """
        
        self.cursor.execute(query)
        schedule_data = self.cursor.fetchone()

        
        return schedule_data[0]  # No se encontró ningún horario para el sitio y el día dados   

    def update_schedule(self, schedule_id, schedule_data: site_schedule_schema):
        site_id = schedule_data.site_id
        day_of_week = schedule_data.day_of_week
        opening_time = schedule_data.opening_time
        closing_time = schedule_data.closing_time

        update_query = f"""UPDATE site_schedule 
        SET site_id = {site_id}, 
            day_of_week = {day_of_week},
            opening_time = '{opening_time}',
            closing_time = '{closing_time}'
        WHERE schedule_id = {schedule_id}"""
        
        self.cursor.execute(update_query)
        self.conn.commit()

        if current_time is None:
            current_time = datetime.now().strftime("%H:%M:%S")

        current_time = datetime.strptime(current_time, "%H:%M:%S").time()  # Convertir la cadena a datetime.time
        
        # Mapear el nombre del día de la semana a un número
        current_day_of_week = datetime.now().strftime("%w")  # %w devuelve el día de la semana como número (0 para domingo, 1 para lunes, etc.)
        
        query = f"""
        SELECT opening_time, closing_time
        FROM site_schedule
        WHERE site_id = {site_id}
        AND day_of_week = '{current_day_of_week}';
        """
        
        self.cursor.execute(query)
        schedule_data = self.cursor.fetchone()

        if schedule_data:
            opening_time, closing_time = schedule_data
            if opening_time <= current_time < closing_time:
                return True, None  # El sitio está abierto
            else:
                return False, opening_time  # El sitio está cerrado, devolver la hora de apertura
        else:
            return False, None  # No se encontró ningún horario para el sitio y el día dados   

    def update_schedules_all(self, schedules_data):
        for schedule in schedules_data:
            site_id = schedule.site_id
            day_of_week = schedule.day_of_week
            opening_time = schedule.opening_time
            closing_time = schedule.closing_time

            update_query = f"""UPDATE site_schedule 
            SET opening_time = '{opening_time}',
                closing_time = '{closing_time}'
            WHERE site_id = {site_id}
            AND day_of_week = {day_of_week};"""

            self.cursor.execute(update_query)
        
        self.conn.commit()
        
        
        
    def update_sites_open_status(self, status:bool,site_id:int):
        
        update_query = f"""UPDATE sites 
        SET open = {status}  
        WHERE site_id = {site_id} returning status;"""

        result = self.cursor.execute(update_query)
        self.conn.commit()
        return self.cursor.fetchall()[0][0]
    
    
    def get_site_open_status(self, site_id: int) -> bool:
        query = f"""SELECT open FROM sites 
                    WHERE site_id = {site_id};"""
        
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        
        if result is not None:
            return bool(result[0])  # Convert to boolean if not None
        else:
            return None  # or raise an exception if the site_id does not exist




    def get_site_open_status(self, site_id: int):
        query = f"""SELECT open FROM sites 
                    WHERE site_id = {site_id};"""
        
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        
        if result is not None:
            return bool(result[0])  # Convert to boolean if not None
        else:
            return None  # or raise an exception if the site_id does not exist

    def close_connection(self):
        self.conn.close()