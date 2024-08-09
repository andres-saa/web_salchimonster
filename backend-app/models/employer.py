import psycopg2
from dotenv import load_dotenv
import os
from schema.employer.employer import EmployerSchemaPost
# Importa aquí tu esquema para employers si lo tienes
# from schema.employer import employer_schema_post
from db.db import Db as dataBase

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Employer:
    def __init__(self):
        self.db = dataBase()
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_employers(self):
    # Consulta SQL que incluye un JOIN para obtener site_name
        query = "SELECT * from hhrr.employers_view;"
        return self.db.fetch_all(query)
    
    def select_employers_basic(self):
    # Consulta SQL que incluye un JOIN para obtener site_name
        select_query = """
        SELECT name, id, gender, dni from employers;
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_employer_basic_by_id(self, employer_id):
        """
        Selecciona información básica de un empleado por su ID.
        """
        select_query = "SELECT id, name, dni, gender FROM employers WHERE id = %s;"
        self.cursor.execute(select_query, (employer_id,))
        columns = [desc[0] for desc in self.cursor.description]
        employer_data = self.cursor.fetchone()

        if employer_data:
            return dict(zip(columns, employer_data))
        else:
            return None


    def select_employer_by_position(self, position):
        select_query = "SELECT * FROM employers WHERE position = %s;"
        self.cursor.execute(select_query, (position,))
        columns = [desc[0] for desc in self.cursor.description]
        employer_data = self.cursor.fetchall()

        if employer_data:
            return [dict(zip(columns, row)) for row in employer_data]
        else:
            return None

    def select_employer_by_id(self, employer_id):
        select_query = "SELECT * FROM employers WHERE id = %s;"
        self.cursor.execute(select_query, (employer_id,))
        columns = [desc[0] for desc in self.cursor.description]
        employer_data = self.cursor.fetchone()

        if employer_data:
            return dict(zip(columns, employer_data))
        else:
            return None

    def insert_employer(self, employer_data):
        existing_employer = self.select_employer_by_dni(employer_data.dni)

        if existing_employer:
            return self.update_employer(existing_employer['id'], employer_data)
        else:
            return self.insert_new_employer(employer_data)

    def insert_new_employer(self, employer_data):
        insert_query = """
        INSERT INTO employers (
            name, dni, address, position, site_id, status, gender, birth_date, phone, email, 
            entry_date, exit_date, exit_reason, comments_notes, authorization_data, birth_country, 
            birth_department, birth_city, blood_type, marital_status, education_level, contract_type, 
            eps, pension_fund, severance_fund, has_children, housing_type, has_vehicle, vehicle_type, 
            household_size, emergency_contact, shirt_size, jeans_sweater_size, food_handling_certificate, 
            food_handling_certificate_number, salary, boss_id, password
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  
        RETURNING id;
        """
        self.cursor.execute(insert_query, (
            employer_data.name, employer_data.dni, employer_data.address, employer_data.position, employer_data.site_id, 
            employer_data.status, employer_data.gender, employer_data.birth_date, employer_data.phone, employer_data.email,
            employer_data.entry_date, employer_data.exit_date, employer_data.exit_reason, employer_data.comments_notes, 
            employer_data.authorization_data, employer_data.birth_country, employer_data.birth_department, employer_data.birth_city, 
            employer_data.blood_type, employer_data.marital_status, employer_data.education_level, employer_data.contract_type, 
            employer_data.eps, employer_data.pension_fund, employer_data.severance_fund, employer_data.has_children, employer_data.housing_type, 
            employer_data.has_vehicle, employer_data.vehicle_type, employer_data.household_size, employer_data.emergency_contact, 
            employer_data.shirt_size, employer_data.jeans_sweater_size, employer_data.food_handling_certificate, 
            employer_data.food_handling_certificate_number, employer_data.salary, employer_data.boss_id,
            employer_data.password  
        ))
        employer_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return employer_id

    
    
    def select_employer_by_dni(self, dni):
        select_query = """
        SELECT * from permission.permission_employer_complete
        WHERE dni = %s;
        """
        self.cursor.execute(select_query, (dni,))
        columns = [desc[0] for desc in self.cursor.description]
        employer_data = self.cursor.fetchone()

        if employer_data:
            return dict(zip(columns, employer_data))
        else:
            return None
        

    def select_employers_grouped_by_site(self):
        select_query = """
        SELECT s.site_name, array_agg(json_build_object('id', e.id, 'name', e.name)) AS employers
        FROM sites s
        JOIN employers e ON s.site_id = e.site_id
        GROUP BY s.site_name;
        """
        self.cursor.execute(select_query)
        grouped_employers = self.cursor.fetchall()

        result = []
        for site_name, employers in grouped_employers:
            # Convertir la representación en texto de los empleadores a una lista de diccionarios
            employers_list = []
            for employer in employers:
                # Aquí se asume que employer ya es un diccionario
                employers_list.append(employer)
            result.append({
                'site_name': site_name,
                'employers': employers_list
            })

        return result

    def update_employer(self, employer_id, updated_data):
        update_query = """
        UPDATE employers
        SET name = %s, dni = %s, address = %s, position = %s, site_id = %s, status = %s, gender = %s, birth_date = %s, 
            phone = %s, email = %s, entry_date = %s, exit_date = %s, exit_reason = %s, comments_notes = %s, 
            authorization_data = %s, birth_country = %s, birth_department = %s, birth_city = %s, blood_type = %s, 
            marital_status = %s, education_level = %s, contract_type = %s, eps = %s, pension_fund = %s, severance_fund = %s, 
            has_children = %s, housing_type = %s, has_vehicle = %s, vehicle_type = %s, household_size = %s, 
            emergency_contact = %s, shirt_size = %s, jeans_sweater_size = %s, food_handling_certificate = %s, 
            food_handling_certificate_number = %s, salary = %s, boss_id = %s, password = %s  -- Aquí se actualiza la contraseña
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.name, updated_data.dni, updated_data.address, updated_data.position, updated_data.site_id, 
            updated_data.status, updated_data.gender, updated_data.birth_date, updated_data.phone, updated_data.email, 
            updated_data.entry_date, updated_data.exit_date, updated_data.exit_reason, updated_data.comments_notes, 
            updated_data.authorization_data, updated_data.birth_country, updated_data.birth_department, updated_data.birth_city, 
            updated_data.blood_type, updated_data.marital_status, updated_data.education_level, updated_data.contract_type, 
            updated_data.eps, updated_data.pension_fund, updated_data.severance_fund, updated_data.has_children, updated_data.housing_type, 
            updated_data.has_vehicle, updated_data.vehicle_type, updated_data.household_size, updated_data.emergency_contact, 
            updated_data.shirt_size, updated_data.jeans_sweater_size, updated_data.food_handling_certificate, 
            updated_data.food_handling_certificate_number, updated_data.salary, updated_data.boss_id, 
            updated_data.password,  # Asegúrate de que updated_data incluye la contraseña
            employer_id  # ID del empleador que se está actualizando
        ))

        updated_employer_data = self.cursor.fetchone()

        self.conn.commit()

        if updated_employer_data:
            return dict(zip([desc[0] for desc in self.cursor.description], updated_employer_data))
        else:
            return None

    def select_employers_by_site_id(self, site_id):
        try:
            # Utiliza UNION para garantizar que el usuario con ID 1132 esté incluido sin duplicados
            select_query = """
            SELECT * FROM employers WHERE site_id = %s
            UNION
            SELECT * FROM employers WHERE id = 1132;
            """
            self.cursor.execute(select_query, (site_id,))
            columns = [desc[0] for desc in self.cursor.description]
            employers_data = self.cursor.fetchall()

            return [dict(zip(columns, row)) for row in employers_data]
        except Exception as e:
            print(f"Ocurrió un error al obtener los datos: {e}")
            return []

   
    def delete_employer(self, employer_id):
        delete_query = "DELETE FROM employers WHERE id = %s;"
        self.cursor.execute(delete_query, (employer_id,))
        self.conn.commit()
        return 'Employer deleted'

    def select_employers_grouped_by_position(self):
        select_query = """
        SELECT e.position, array_agg(json_build_object('id', e.id, 'name', e.name)) AS employers
        FROM employers e
        GROUP BY e.position;
        """
        self.cursor.execute(select_query)
        grouped_employers = self.cursor.fetchall()

        result = []
        for position, employers in grouped_employers:
            # Convertir la representación en texto de los empleadores a una lista de diccionarios
            employers_list = []
            for employer in employers:
                # Aquí se asume que employer ya es un diccionario
                employers_list.append(employer)
            result.append({
                'position': position,
                'employers': employers_list
            })

        return result


    def close_connection(self):
        self.conn.close()
