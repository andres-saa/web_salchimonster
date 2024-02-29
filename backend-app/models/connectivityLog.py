import psycopg2
from dotenv import load_dotenv
import os
from datetime import datetime
from pydantic import BaseModel
import pytz
from datetime import datetime, timedelta

from schema.connectivityLog import ConnectivityLogSchema




load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class ConnectivityLog:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def insert_connectivity_log(self, log_data: ConnectivityLogSchema):
        insert_query = """
        INSERT INTO connectivity_logs (
            site_id,  event_type
        ) VALUES (%s, %s) RETURNING log_id;
        """
        self.cursor.execute(insert_query, (
            log_data.site_id,  log_data.event_type
        ))
        log_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return log_id

    def select_connectivity_logs_by_site_id(self, site_id):
        select_query = "SELECT * FROM connectivity_logs WHERE site_id = %s;"
        self.cursor.execute(select_query, (site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        logs_data = self.cursor.fetchall()

        if logs_data:
            return [dict(zip(columns, row)) for row in logs_data]
        else:
            return []
        
    def is_site_online(self, site_id):
        colombia_timezone = pytz.timezone('America/Bogota')
        current_time_colombia = datetime.now(colombia_timezone)

        # Asumiendo que quieres comparar usando UTC
        current_time_utc = current_time_colombia.astimezone(pytz.utc)

        # Restamos 5 minutos a la hora actual UTC para determinar el umbral de inactividad
        threshold_time = current_time_utc - timedelta(minutes=5)

        # Consulta para obtener el último evento
        self.cursor.execute("""
            SELECT event_type, event_timestamp FROM connectivity_logs
            WHERE site_id = %s
            ORDER BY event_timestamp DESC
            LIMIT 1;
        """, (site_id,))

        last_event = self.cursor.fetchone()

        if not last_event:
            return False

        # # Hacer que last_event[1] sea consciente de la zona horaria
        # last_event_timestamp_aware = last_event[1].replace(tzinfo=pytz.utc)

        if last_event[0] == 'Desconexión':
            return False

        return True
    
    def get_sites_online_status(self):
        # Consulta para obtener todos los site_id y site_name
        self.cursor.execute("SELECT site_id, site_name FROM sites order by site_id;")
        sites_data = self.cursor.fetchall()

        # Lista para almacenar el estado en línea de cada sede
        sites_online_status = []

        for site in sites_data:
            site_id, site_name = site
            is_online = self.is_site_online(site_id)
            sites_online_status.append({"id":site_id,"site_name": site_name, "online_status": is_online})

        return sites_online_status
    
    def close_connection(self):
        self.conn.close()
