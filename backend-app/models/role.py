import psycopg2
from dotenv import load_dotenv
import os
from schema.role import RoleGroupSchema , RoleSchema
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')



class Role:
    def __init__(self):
        self.conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}")
        self.cursor = self.conn.cursor()

    def create_role(self, role_data: RoleSchema):
        insert_query = "INSERT INTO job_roles (title, description) VALUES (%s, %s) RETURNING id;"
        self.cursor.execute(insert_query, (role_data.title, role_data.description))
        role_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return role_id
    
    def select_all_roles(self):
        select_query = "SELECT * FROM job_roles order by title;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def read_role(self, role_id: int):
        select_query = "SELECT * FROM job_roles WHERE id = %s;"
        self.cursor.execute(select_query, (role_id,))
        columns = [desc[0] for desc in self.cursor.description]
        role = self.cursor.fetchone()
        return dict(zip(columns, role)) if role else None


    def update_role(self, role_id: int, updated_data: RoleSchema):
        update_query = "UPDATE job_roles SET title = %s, description = %s WHERE id = %s;"
        self.cursor.execute(update_query, (updated_data.title, updated_data.description, role_id))
        self.conn.commit()
        return self.read_role(role_id)
    


    # Dentro de la clase RoleGroup




    def delete_role(self, role_id: int):
        delete_query = "DELETE FROM job_roles WHERE id = %s;"
        self.cursor.execute(delete_query, (role_id,))
        self.conn.commit()
        return {"message": "Role deleted successfully"}
    
    def select_role_by_id(self, role_id: int):
        select_query = "SELECT * FROM job_roles WHERE id = %s;"
        self.cursor.execute(select_query, (role_id,))
        role = self.cursor.fetchone()
        return role

    def close_connection(self):
        self.conn.close()




class RoleGroup:
    def __init__(self):
        self.conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}")

        self.cursor = self.conn.cursor()

    def create_role_group(self, group_data: RoleGroupSchema):
        insert_query = "INSERT INTO role_groups (group_name, description) VALUES (%s, %s) RETURNING id;"
        self.cursor.execute(insert_query, (group_data.group_name, group_data.description))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id
    
    


    def get_roles_by_group_id(self, group_id: int):
        # Asegúrate de ajustar los nombres de las tablas y columnas según tu esquema de base de datos.
        select_query = """
        SELECT jr.*
        FROM job_roles jr
        JOIN role_group_memberships gm ON jr.id = gm.role_id
        WHERE gm.group_id = %s;
        """
        self.cursor.execute(select_query, (group_id,))
        roles = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, role)) for role in roles] if roles else []
    

    def select_group_by_id(self, group_id: int):
        select_query = "SELECT * FROM role_groups WHERE id = %s;"
        self.cursor.execute(select_query, (group_id,))
        columns = [desc[0] for desc in self.cursor.description]
        group = self.cursor.fetchone()
        return dict(zip(columns, group)) if group else None

    def read_role_group(self, group_id: int):
        select_query = "SELECT * FROM role_groups WHERE id = %s;"
        self.cursor.execute(select_query, (group_id,))
        group = self.cursor.fetchone()
        return group

    def update_role_group(self, group_id: int, updated_data: RoleGroupSchema):
        update_query = "UPDATE role_groups SET group_name = %s, description = %s WHERE id = %s;"
        self.cursor.execute(update_query, (updated_data.group_name, updated_data.description, group_id))
        self.conn.commit()
        return self.read_role_group(group_id)
    
    def select_all_groups(self):
        select_query = "SELECT * FROM role_groups;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def delete_role_group(self, group_id: int):
        delete_query = "DELETE FROM role_groups WHERE id = %s;"
        self.cursor.execute(delete_query, (group_id,))
        self.conn.commit()
        return {"message": "Role group deleted successfully"}
    

    def get_roles_formatted_by_group(self):
        # Consulta para obtener los grupos con sus roles
        query = """
        SELECT rg.group_name, array_agg(jr.title) AS roles
        FROM role_groups rg
        LEFT JOIN role_group_memberships rgm ON rg.id = rgm.group_id
        LEFT JOIN job_roles jr ON rgm.role_id = jr.id
        GROUP BY rg.group_name;
        """
        self.cursor.execute(query)
        groups_with_roles = self.cursor.fetchall()

        # Formatear el resultado en un diccionario, asegurándose de que todos los elementos son strings
        formatted_roles_by_group = {}
        for group_name, roles in groups_with_roles:
            # Filtrar cualquier valor que no sea una cadena de texto
            roles_list = [role for role in roles if isinstance(role, str)]
            formatted_roles_by_group[group_name] = roles_list

        return formatted_roles_by_group






    def assign_roles_to_group(self, group_id: int, role_ids: list[int]):
        # Verificar las asignaciones existentes para este grupo
        select_query = "SELECT role_id FROM role_group_memberships WHERE group_id = %s;"
        self.cursor.execute(select_query, (group_id,))
        existing_roles = [row[0] for row in self.cursor.fetchall()]

        # Filtrar role_ids para incluir solo los nuevos roles que no están ya asignados
        new_role_ids = [role_id for role_id in role_ids if role_id not in existing_roles]

        # Insertar solo los nuevos roles para este grupo
        insert_query = "INSERT INTO role_group_memberships (role_id, group_id) VALUES (%s, %s);"
        for role_id in new_role_ids:
            self.cursor.execute(insert_query, (role_id, group_id))

        if new_role_ids:  # Solo hacer commit si hay nuevos roles para asignar
            self.conn.commit()
            return {"message": "New roles assigned to group successfully", "assigned_roles": new_role_ids}
        else:
            return {"message": "No new roles to assign, all provided roles already exist in group"}



    def assign_roles_to_group_delete_olds(self, group_id: int, role_ids: list[int]):
    # Primero, borrar todas las asignaciones existentes de roles para este grupo
        delete_query = "DELETE FROM role_group_memberships WHERE group_id = %s;"
        self.cursor.execute(delete_query, (group_id,))
        
        # Ahora, insertar los nuevos roles para este grupo
        insert_query = "INSERT INTO role_group_memberships (role_id, group_id) VALUES (%s, %s);"
        for role_id in role_ids:
            self.cursor.execute(insert_query, (role_id, group_id))

        if role_ids:  # Solo hacer commit si hay roles para asignar
            self.conn.commit()
            return {"message": "Roles assigned to group successfully", "assigned_roles": role_ids}
        else:
            return {"message": "No roles to assign"}




    def close_connection(self):
        self.conn.close()