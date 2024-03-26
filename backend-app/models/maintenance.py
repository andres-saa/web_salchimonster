from schema.maintenance import Maintenance , Equipment # Importa tu esquema Pydantic aquí
import psycopg2
from dotenv import load_dotenv
import os
from typing import List
from datetime import timedelta



load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class EquipmentModel:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_all_equipment(self):
        select_query = "SELECT * FROM equipment;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_equipment_by_id(self, equipment_id):
        select_query = "SELECT * FROM equipment WHERE equipment_id = %s;"
        self.cursor.execute(select_query, (equipment_id,))
        columns = [desc[0] for desc in self.cursor.description]
        equipment_data = self.cursor.fetchone()

        if equipment_data:
            return dict(zip(columns, equipment_data))
        else:
            return None

    def select_equipment_by_site_id(self, site_id):
        select_query = "SELECT * FROM equipment WHERE site_id = %s;"
        self.cursor.execute(select_query, (site_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def insert_equipment(self, equipment_data: Equipment, site_ids: list):
        equipment_ids = []
        for site_id in site_ids:
            insert_query = """
            INSERT INTO equipment (name, brand, site_id) VALUES (%s, %s, %s) RETURNING equipment_id;
            """
            self.cursor.execute(insert_query, (
                equipment_data.name, equipment_data.brand, site_id
            ))
            equipment_id = self.cursor.fetchone()[0]
            self.conn.commit()
            equipment_ids.append(equipment_id)
        return equipment_ids

    def update_equipment(self, equipment_id, updated_data: Equipment):
        update_query = """
        UPDATE equipment
        SET name = %s, brand = %s, site_id = %s
        WHERE equipment_id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.name, updated_data.brand, updated_data.site_id, equipment_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_equipment_data = self.cursor.fetchone()

        if updated_equipment_data:
            self.conn.commit()
            return dict(zip(columns, updated_equipment_data))
        else:
            return None
    
    def select_sites_with_all_equipment_by_names(self, equipment_names: List[str]):
        equipment_count = len(equipment_names)
        if equipment_count == 0:
            return []

        # Creando placeholders para la consulta
        placeholders = ', '.join(['%s'] * equipment_count)

        # Consulta para obtener los site_id que contienen todos los equipos especificados por nombre
        select_query = f"""
        SELECT site_id
        FROM equipment
        WHERE name IN ({placeholders})
        GROUP BY site_id
        HAVING COUNT(DISTINCT name) = %s;
        """

        # Ejecutando la consulta para obtener site_id
        self.cursor.execute(select_query, tuple(equipment_names + [equipment_count]))
        site_ids = [row[0] for row in self.cursor.fetchall()]

        # Si no hay site_ids que coincidan, retorna una lista vacía
        if not site_ids:
            return []

        # Recopilación de información detallada de cada sitio
        sites = []
        for site_id in site_ids:
            # Ajusta esta consulta a tu esquema de base de datos si es necesario
            self.cursor.execute("SELECT * FROM sites WHERE site_id = %s", (site_id,))
            columns = [desc[0] for desc in self.cursor.description]
            site_data = self.cursor.fetchone()
            if site_data:
                sites.append(dict(zip(columns, site_data)))

        return sites

    
    def select_sites_with_all_equipment(self, equipment_ids: List[int]):
        equipment_count = len(equipment_ids)
        if equipment_count == 0:
            return []

        # Creando placeholders para la consulta
        placeholders = ', '.join(['%s'] * equipment_count)

        # Consulta para obtener los site_id que contienen todos los equipos especificados
        select_query = f"""
        SELECT site_id
        FROM equipment
        WHERE equipment_id IN ({placeholders})
        GROUP BY site_id
        HAVING COUNT(DISTINCT equipment_id) = %s;
        """

        # Ejecutando la consulta para obtener site_id
        self.cursor.execute(select_query, tuple(equipment_ids + [equipment_count]))
        site_ids = [row[0] for row in self.cursor.fetchall()]

        # Si no hay site_ids que coincidan, retorna una lista vacía
        if not site_ids:
            return []

        # Recopilación de información detallada de cada sitio
        sites = []
        for site_id in site_ids:
            # Ajusta esta consulta a tu esquema de base de datos
            self.cursor.execute("SELECT * FROM sites WHERE site_id = %s", (site_id,))
            columns = [desc[0] for desc in self.cursor.description]
            site_data = self.cursor.fetchone()
            if site_data:
                sites.append(dict(zip(columns, site_data)))

        return sites
    
    
    def delete_equipment(self, equipment_id):
        delete_query = "DELETE FROM equipment WHERE equipment_id = %s;"
        self.cursor.execute(delete_query, (equipment_id,))
        self.conn.commit()
        return {"message": "Equipment deleted successfully"}

    def close_connection(self):
        self.conn.close()



class MaintenanceModel:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()


    def select_maintenance_by_site_id(self, site_id):
        with self.conn:
            with self.conn.cursor() as cursor:
                select_query = """
                SELECT m.*, e.name as equipment_name, e.brand as equipment_brand
                FROM maintenance m
                LEFT JOIN maintenance_equipment me ON m.maintenance_id = me.maintenance_id
                LEFT JOIN equipment e ON me.equipment_id = e.equipment_id
                WHERE m.site_id = %s;
                """
                cursor.execute(select_query, (site_id,))
                columns = [desc[0] for desc in cursor.description]

                maintenance_records = {}
                for row in cursor.fetchall():
                    maintenance_id = row[columns.index('maintenance_id')]
                    if maintenance_id not in maintenance_records:
                        maintenance_records[maintenance_id] = {col: row[idx] for idx, col in enumerate(columns) if not col.startswith('equipment_')}
                        maintenance_records[maintenance_id]['equipment'] = []

                    if row[columns.index('equipment_name')] and row[columns.index('equipment_brand')]:
                        maintenance_records[maintenance_id]['equipment'].append({
                            'name': row[columns.index('equipment_name')],
                            'brand': row[columns.index('equipment_brand')],
                        })

                return list(maintenance_records.values())


    def select_all_maintenance(self):
        select_query = "SELECT * FROM maintenance;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def select_maintenance_by_id(self, maintenance_id):
        with self.conn:
            with self.conn.cursor() as cursor:
                select_query = """
                SELECT m.*, e.name as equipment_name, e.brand as equipment_brand
                FROM maintenance m
                LEFT JOIN maintenance_equipment me ON m.maintenance_id = me.maintenance_id
                LEFT JOIN equipment e ON me.equipment_id = e.equipment_id
                WHERE m.maintenance_id = %s;
                """
                cursor.execute(select_query, (maintenance_id,))
                columns = [desc[0] for desc in cursor.description]

                result = {}
                for row in cursor.fetchall():
                    if 'equipment' not in result:
                        result = {col: row[idx] for idx, col in enumerate(columns) if not col.startswith('equipment_')}
                        result['equipment'] = []

                    if row[columns.index('equipment_name')] and row[columns.index('equipment_brand')]:
                        result['equipment'].append({
                            'name': row[columns.index('equipment_name')],
                            'brand': row[columns.index('equipment_brand')],
                        })

                return result

    def insert_maintenance(self, maintenance_data: Maintenance):
        maintenance_ids = []
        with self.conn:
            with self.conn.cursor() as cursor:
                for site in maintenance_data.sites:
                    # Calcular las fechas de mantenimiento basadas en la frecuencia
                    maintenance_dates = [site.scheduled_date]
                    for i in range(1, maintenance_data.frequency):
                        next_date = maintenance_dates[-1] + timedelta(days=(365 / maintenance_data.frequency))
                        maintenance_dates.append(next_date)

                    for maintenance_date in maintenance_dates:
                        # Insertar cada mantenimiento programado
                        insert_query = """
                        INSERT INTO maintenance (site_id, scheduled_date, frequency, status, completed, remarks)
                        VALUES (%s, %s, %s, %s, %s, %s) RETURNING maintenance_id;
                        """
                        cursor.execute(insert_query, (
                            site.site_id, maintenance_date, maintenance_data.frequency,
                            maintenance_data.status, maintenance_data.completed, maintenance_data.remarks
                        ))
                        maintenance_id = cursor.fetchone()[0]
                        maintenance_ids.append(maintenance_id)

                        # Inserta las relaciones en maintenance_equipment para cada mantenimiento
                        for equipment_id in site.equipment_ids:
                            relation_insert_query = """
                            INSERT INTO maintenance_equipment (maintenance_id, equipment_id)
                            VALUES (%s, %s);
                            """
                            cursor.execute(relation_insert_query, (maintenance_id, equipment_id))

        return maintenance_ids
    
    
    def complete_maintenance(self, maintenance_id: int, remarks: str):
        update_query = """
        UPDATE maintenance
        SET completed = %s, remarks = %s
        WHERE maintenance_id = %s
        RETURNING *;
        """
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(update_query, (True, remarks, maintenance_id))
                
                columns = [desc[0] for desc in cursor.description]
                updated_maintenance_data = cursor.fetchone()

                if updated_maintenance_data:
                    self.conn.commit()
                    return dict(zip(columns, updated_maintenance_data))
                else:
                    return None
    
    def update_maintenance(self, maintenance_id, updated_data: Maintenance):
        # Permite actualizar site_id
        update_query = """
        UPDATE maintenance
        SET site_id = %s, scheduled_date = %s, frequency = %s, status = %s, completed = %s, remarks = %s
        WHERE maintenance_id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.site_id, updated_data.scheduled_date, updated_data.frequency,
            updated_data.status, updated_data.completed, updated_data.remarks, maintenance_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_maintenance_data = self.cursor.fetchone()

        if updated_maintenance_data:
            self.conn.commit()
            return dict(zip(columns, updated_maintenance_data))
        else:
            return None

    def delete_maintenance(self, maintenance_id):
        delete_query = "DELETE FROM maintenance WHERE maintenance_id = %s;"
        self.cursor.execute(delete_query, (maintenance_id,))
        self.conn.commit()
        return {"message": "Maintenance deleted successfully"}

    def close_connection(self):
        self.conn.close()

