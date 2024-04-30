from schema.site import site_schema_post  # Asegúrate de importar tu esquema de sitio adecuado
import psycopg2
from dotenv import load_dotenv
import os
from schema.directory import *
load_dotenv()
import json
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Site:
    def __init__(self, site_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.site_id = site_id

    def select_all_sites(self):
        select_query = "SELECT * FROM sites;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def select_sites_by_city_id(self, city_id):
        select_query = "SELECT * FROM sites WHERE city_id = %s;"
        self.cursor.execute(select_query, (city_id,))
        columns = [desc[0] for desc in self.cursor.description]
        sites_data = self.cursor.fetchall()

        if sites_data:
            return [dict(zip(columns, row)) for row in sites_data]
        else:
            return []


    def select_site_by_id(self, site_id):
        select_query = "SELECT * FROM sites WHERE site_id = %s;"
        self.cursor.execute(select_query, (site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        site_data = self.cursor.fetchone()

        if site_data:
            return dict(zip(columns, site_data))
        else:
            return None

    def insert_site(self, site_data: site_schema_post):
        insert_query = """
        INSERT INTO sites (
            site_name, site_address, site_phone
        ) VALUES (%s, %s, %s) RETURNING site_id;
        """
        self.cursor.execute(insert_query, (
            site_data.site_name, site_data.site_address, site_data.site_phone
        ))
        site_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return site_id

    def delete_site(self, site_id):
        # Puedes implementar la lógica de desactivación o eliminación según tus requisitos.
        return 'solo desactiva el sitio'

    def update_site(self, site_id, updated_data: site_schema_post):
        update_query = """
        UPDATE sites SET
            site_name = %s,
            site_address = %s,
            site_phone = %s,
            site_business_hours = %s,
            horario_semanal = %s::json,
            wsp_link = %s,
            city_id = %s,
            maps = %s,
            show_on_web = %s,
            email_address = %s
        WHERE site_id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.site_name,
            updated_data.site_address,
            updated_data.site_phone,
            updated_data.site_business_hours,
            json.dumps(updated_data.horario_semanal),
            updated_data.wsp_link,
            updated_data.city_id,
            updated_data.maps,
            updated_data.show_on_web,
            updated_data.email_address,
            site_id
        ))
        columns = [desc[0] for desc in self.cursor.description]
        updated_site_data = self.cursor.fetchone()
        if updated_site_data:
            return dict(zip(columns, updated_site_data))
        else:
            return None
            
            
            
            
        
        
        
        
        
    def get_all_safe_boxes(self):
        select_query = "SELECT * FROM directory.dir_safe_boxes WHERE site_id = %s;"
        self.cursor.execute(select_query, (self.site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_all_cameras(self):
        select_query = "SELECT * FROM directory.dir_cameras WHERE site_id = %s;"
        self.cursor.execute(select_query, (self.site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_all_wifi_networks(self):
        select_query = "SELECT * FROM directory.dir_wifi WHERE site_id = %s;"
        self.cursor.execute(select_query, (self.site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_all_dataphones(self):
        select_query = "SELECT * FROM directory.dir_dataphones WHERE site_id = %s;"
        self.cursor.execute(select_query, (self.site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_all_web_pages(self):
        select_query = "SELECT * FROM directory.dir_web_pages WHERE site_id = %s;"
        self.cursor.execute(select_query, (self.site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_all_applications(self):
        select_query = "SELECT * FROM directory.dir_applications WHERE site_id = %s;"
        self.cursor.execute(select_query, (self.site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_all_general_emails(self):
        # Suponiendo que necesitas obtener los correos relacionados con una sede, pero esta relación no está directamente definida en tu esquema
        # Deberías ajustar esta función según tu diseño de base de datos y necesidades.
        select_query = "SELECT * FROM directory.dir_general_emails;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]



        
    def get_all_site_data(self):
        site_data = {
            "site_info": self.select_site_by_id(self.site_id),
            "safe_boxes": self.get_all_safe_boxes(),
            "cameras": self.get_all_cameras(),
            "wifi_networks": self.get_all_wifi_networks(),
            "dataphones": self.get_all_dataphones(),
            "web_pages": self.get_all_web_pages(),
            "applications": self.get_all_applications(),
            # "general_emails": self.get_all_general_emails(),  # Inclúyelo si los emails están relacionados con las sedes
        }
        return site_data




    def create_safe_box(self, safe_box: DirSafeBoxes):
        insert_query = "INSERT INTO directory.dir_safe_boxes (site_id,box_name,password) VALUES (%s,%s,%s);"
        self.cursor.execute(insert_query, (safe_box.site_id,safe_box.box_name,safe_box.password))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_safe_box(self, safe_box: DirSafeBoxes):
        update_query = "UPDATE directory.dir_safe_boxes SET site_id = %s WHERE safe_box_id = %s;"
        self.cursor.execute(update_query, (safe_box.site_id, safe_box.safe_box_id))
        self.conn.commit()

    def create_camera(self, camera: DirCameras):
        insert_query = "INSERT INTO directory.dir_cameras (site_id, username, password) VALUES (%s, %s, %s);"
        self.cursor.execute(insert_query, (camera.site_id, camera.username, camera.password))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_camera(self, camera: DirCameras):
        update_query = "UPDATE directory.dir_cameras SET site_id = %s, username = %s, password = %s WHERE camera_id = %s;"
        self.cursor.execute(update_query, (camera.site_id, camera.username, camera.password, camera.camera_id))
        self.conn.commit()

    # Repite un patrón similar para los métodos create y update de las demás entidades...

    def create_wifi_network(self, wifi: DirWifi):
        insert_query = "INSERT INTO directory.dir_wifi (site_id, username, password) VALUES (%s, %s, %s);"
        self.cursor.execute(insert_query, (wifi.site_id, wifi.username, wifi.password))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_wifi_network(self, wifi: DirWifi):
        update_query = "UPDATE directory.dir_wifi SET site_id = %s, username = %s, password = %s WHERE wifi_id = %s;"
        self.cursor.execute(update_query, (wifi.site_id, wifi.username, wifi.password, wifi.wifi_id))
        self.conn.commit()
        
        
    def create_dataphone(self, dataphone: DirDataphones):
        insert_query = "INSERT INTO directory.dir_dataphones (site_id, unique_code, external_code) VALUES (%s, %s, %s);"
        self.cursor.execute(insert_query, (dataphone.site_id, dataphone.unique_code, dataphone.external_code))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_dataphone(self, dataphone: DirDataphones):
        update_query = "UPDATE directory.dir_dataphones SET site_id = %s, unique_code = %s, external_code = %s WHERE dataphone_id = %s;"
        self.cursor.execute(update_query, (dataphone.site_id, dataphone.unique_code, dataphone.external_code, dataphone.dataphone_id))
        self.conn.commit()

    def create_web_page(self, web_page: DirWebPages):
        insert_query = "INSERT INTO directory.dir_web_pages (site_id, page, username, password) VALUES (%s, %s, %s, %s);"
        self.cursor.execute(insert_query, (web_page.site_id, web_page.page, web_page.username, web_page.password))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_web_page(self, web_page: DirWebPages):
        update_query = "UPDATE directory.dir_web_pages SET site_id = %s, page = %s, username = %s, password = %s WHERE web_page_id = %s;"
        self.cursor.execute(update_query, (web_page.site_id, web_page.page, web_page.username, web_page.password, web_page.web_page_id))
        self.conn.commit()

    def create_application(self, application: DirApplications):
        insert_query = "INSERT INTO directory.dir_applications (site_id, name, username, password) VALUES (%s, %s, %s, %s);"
        self.cursor.execute(insert_query, (application.site_id, application.name, application.username, application.password))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_application(self, application: DirApplications):
        update_query = "UPDATE directory.dir_applications SET site_id = %s, name = %s, username = %s, password = %s WHERE application_id = %s;"
        self.cursor.execute(update_query, (application.site_id, application.name, application.username, application.password, application.application_id))
        self.conn.commit()

    def create_general_email(self, email: DirGeneralEmails):
        insert_query = "INSERT INTO directory.dir_general_emails (description, email) VALUES (%s, %s);"
        self.cursor.execute(insert_query, (email.description, email.email))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_general_email(self, email: DirGeneralEmails):
        update_query = "UPDATE directory.dir_general_emails SET description = %s, email = %s WHERE email_id = %s;"
        self.cursor.execute(update_query, (email.description, email.email, email.email_id))
        self.conn.commit()

    def delete_safe_box(self, safe_box_id: int):
        delete_query = "DELETE FROM directory.dir_safe_boxes WHERE safe_box_id = %s;"
        self.cursor.execute(delete_query, (safe_box_id,))
        self.conn.commit()

    def delete_camera(self, camera_id: int):
        delete_query = "DELETE FROM directory.dir_cameras WHERE camera_id = %s;"
        self.cursor.execute(delete_query, (camera_id,))
        self.conn.commit()

    def delete_wifi_network(self, wifi_id: int):
        delete_query = "DELETE FROM directory.dir_wifi WHERE wifi_id = %s;"
        self.cursor.execute(delete_query, (wifi_id,))
        self.conn.commit()

    def delete_dataphone(self, dataphone_id: int):
        delete_query = "DELETE FROM directory.dir_dataphones WHERE dataphone_id = %s;"
        self.cursor.execute(delete_query, (dataphone_id,))
        self.conn.commit()

    def delete_web_page(self, web_page_id: int):
        delete_query = "DELETE FROM directory.dir_web_pages WHERE web_page_id = %s;"
        self.cursor.execute(delete_query, (web_page_id,))
        self.conn.commit()

    def delete_application(self, application_id: int):
        delete_query = "DELETE FROM directory.dir_applications WHERE application_id = %s;"
        self.cursor.execute(delete_query, (application_id,))
        self.conn.commit()

    def delete_general_email(self, email_id: int):
        delete_query = "DELETE FROM directory.dir_general_emails WHERE email_id = %s;"
        self.cursor.execute(delete_query, (email_id,))
        self.conn.commit()



    

    def close_connection(self):
        self.conn.close()
        