from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
import psycopg2
from dotenv import load_dotenv
import os
from typing import List

from schema.audit import Audit,CheckGroup,AuditItem,CheckItem,Warning,Checklist,ChecklistWithGroups,AuditItemWithWarning


load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class AuditDAO:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    


    def get_all_checklists(self):
        query = """
        SELECT 
            cl.id as checklist_id,
            cl.name as checklist_name,
            cg.id as group_id,
            cg.name as group_name
        FROM 
            checklists cl
            LEFT JOIN checkgroup cg ON cl.id = cg.checklist_id
        ORDER BY 
            cl.name, cg.name;
        """
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Initialize a dictionary to keep track of checklists and their groups
        checklists = {}

        # Iterate over each row in the query result
        for row in rows:
            checklist_id, checklist_name, group_id, group_name = row

            # Check if the checklist is already added
            if checklist_id not in checklists:
                checklists[checklist_id] = {
                    'checklist_id': checklist_id,
                    'checklist_name': checklist_name,
                    'groups': []
                }

            # Add the group to the checklist if it exists
            if group_id:
                checklists[checklist_id]['groups'].append({
                    'group_id': group_id,
                    'group_name': group_name
                })

        # Return a list of checklists with their groups
        return list(checklists.values())







    def get_audit_check_groups_with_items(self, audit_id):
        # Primero, obtenemos el ID del checklist asociado con la auditoría
        self.cursor.execute("SELECT checklist_id FROM audits WHERE id = %s;", (audit_id,))
        checklist_id_row = self.cursor.fetchone()
        if checklist_id_row is None:
            return [], []
        checklist_id = checklist_id_row[0]

        # Ahora ajustamos la consulta para filtrar por el checklist_id obtenido
        query = """
        SELECT 
            cg.name as group_name, 
            ci.description as item_description, 
            CASE 
                WHEN ai.status IS NULL THEN false
                ELSE ai.status
            END as item_status,
            w.warning_text,
            w.date as warning_date
        FROM 
            checkgroup cg
            INNER JOIN check_item ci ON cg.id = ci.group_id
            INNER JOIN checklists cl ON cg.checklist_id = cl.id
            LEFT JOIN audit_items ai ON ci.id = ai.check_item_id AND ai.audit_id = %s
            LEFT JOIN warnings w ON ai.id = w.audit_item_id
        WHERE 
            cl.id = %s
        ORDER BY 
            cg.name, ci.description;
        """
        self.cursor.execute(query, (audit_id, checklist_id))
        rows = self.cursor.fetchall()

        groups_with_items = []
        temp_groups = {}
        for row in rows:
            group_name, item_description, item_status, warning_text, warning_date = row
            if group_name not in temp_groups:
                temp_groups[group_name] = {'items': []}
            temp_groups[group_name]['items'].append({
                'description': item_description, 
                'status': item_status, 
                'warning_text': warning_text, 
                'warning_date': warning_date
            })

        for group_name, group_data in temp_groups.items():
            groups_with_items.append({'group_name': group_name, 'items': group_data['items']})

        warnings = [
            {'audit_id': audit_id, 'group_name': group['group_name'], 'item_description': item['description'], 'warning_text': item['warning_text'], 'warning_date': item['warning_date']} 
            for group in groups_with_items for item in group['items'] if item['warning_text']
        ]

        return groups_with_items, warnings




    def get_audit_check_groups_with_filtered_items(self, coordinator_id, date, site_id):
        # Filtramos las auditorías por ID del coordinador, fecha y site_id
        self.cursor.execute("""
            SELECT id FROM audits 
            WHERE coordinator_id = %s AND audit_date = %s AND site_id = %s;
        """, (coordinator_id, date, site_id))
        audit_ids = [row[0] for row in self.cursor.fetchall()]
        if not audit_ids:
            return [], []

        # Preparamos para buscar en todas las auditorías encontradas
        checklist_ids_query = """
            SELECT DISTINCT cl.id 
            FROM audits a
            INNER JOIN checklists cl ON a.checklist_id = cl.id
            WHERE a.id = ANY(%s);
        """
        self.cursor.execute(checklist_ids_query, (audit_ids,))
        checklist_ids = [row[0] for row in self.cursor.fetchall()]
        if not checklist_ids:
            return [], []

        # Ajustamos la consulta para incluir múltiples checklist_ids
        query = """
        SELECT 
            cg.name as group_name, 
            ci.description as item_description, 
            ai.status as item_status,
            w.warning_text,
            w.date as warning_date
        FROM 
            checkgroup cg
            INNER JOIN check_item ci ON cg.id = ci.group_id
            INNER JOIN checklists cl ON cg.checklist_id = cl.id
            LEFT JOIN audit_items ai ON ci.id = ai.check_item_id AND ai.audit_id = ANY(%s)
            LEFT JOIN warnings w ON ai.id = w.audit_item_id
        WHERE 
            cl.id = ANY(%s)
        ORDER BY 
            cg.name, ci.description;
        """
        self.cursor.execute(query, (audit_ids, checklist_ids))
        rows = self.cursor.fetchall()

        groups_with_items = []
        temp_groups = {}
        for row in rows:
            group_name, item_description, item_status, warning_text, warning_date = row
            if group_name not in temp_groups:
                temp_groups[group_name] = {'items': []}
            temp_groups[group_name]['items'].append({
                'description': item_description, 
                'status': item_status, 
                'warning_text': warning_text, 
                'warning_date': warning_date
            })

        for group_name, group_data in temp_groups.items():
            groups_with_items.append({'group_name': group_name, 'items': group_data['items']})

        warnings = [
            {'group_name': group['group_name'], 'item_description': item['description'], 'warning_text': item['warning_text'], 'warning_date': item['warning_date']} 
            for group in groups_with_items for item in group['items'] if item['warning_text']
        ]

        return groups_with_items, warnings

    




        
    def select_all_audits(self):
        select_query = """
        SELECT 
            a.*, 
            s.site_name, 
            e.name as coordinator_name,
            cl.name as checklist_name,
            COUNT(ai.id) FILTER (WHERE ai.status = true) as true_items,
            COUNT(ai.id) as total_items
        FROM 
            audits a
            INNER JOIN sites s ON a.site_id = s.site_id
            INNER JOIN employers e ON a.coordinator_id = e.id
            INNER JOIN checklists cl ON a.checklist_id = cl.id
            LEFT JOIN audit_items ai ON a.id = ai.audit_id
        GROUP BY 
            a.id, s.site_name, e.name, cl.name;
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        audits = self.cursor.fetchall()

        audit_list = []
        for audit in audits:
            audit_dict = dict(zip(columns, audit))
            total_items = audit_dict['total_items']
            true_items = audit_dict['true_items']
            # Calculate the score
            audit_dict['score'] = (5 / total_items) * true_items if total_items > 0 else 0
            audit_list.append(audit_dict)

        return audit_list



    def select_audit_by_id(self, audit_id):
        select_query = "SELECT * FROM audits WHERE id = %s;"
        self.cursor.execute(select_query, (audit_id,))
        columns = [desc[0] for desc in self.cursor.description]
        audit_data = self.cursor.fetchone()

        if audit_data:
            return dict(zip(columns, audit_data))
        else:
            return None



    def select_unique_coordinators(self):
        select_query = "SELECT * FROM unique_coordinator_audits;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        items_data = self.cursor.fetchall()

        if items_data:
            return [dict(zip(columns, item_data)) for item_data in items_data]
        else:
            return []



    def insert_checklist_with_groups_and_items(self, checklist_data: Checklist):
            
            # Insertar el checklist y obtener su ID
            checklist_id = self.insert_checklist(checklist_data)

            # Insertar los grupos con sus elementos asociados
            for group_data in checklist_data.groups:
                # Asignar el ID del checklist al grupo
                group_data.checklist_id = checklist_id
                # Insertar el grupo
                group_id = self.insert_check_group(group_data)
                
                # Insertar los elementos del grupo
                for item_data in group_data.items:
                    # Asignar el ID del grupo al elemento
                    item_data.group_id = group_id
                    # Insertar el elemento
                    self.insert_check_item(item_data)

            return checklist_id



    def insert_audit(self, audit_data: Audit):
        insert_query = """
        INSERT INTO audits (
             site_id, coordinator_id, audit_date, checklist_id
        ) VALUES ( %s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (
            audit_data.site_id, audit_data.coordinator_id, audit_data.audit_date, audit_data.checklist_id
        ))
        audit_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return audit_id

    def update_audit(self, audit_id, updated_data: Audit):
        update_query = """
        UPDATE audits
        SET site_id = %s, coordinator_id = %s, audit_date = %s, checklist_id = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.site_id, updated_data.coordinator_id, updated_data.audit_date, updated_data.checklist_id, audit_id
        ))
        self.conn.commit()
        

        columns = [desc[0] for desc in self.cursor.description]
        updated_audit_data = self.cursor.fetchone()

        

        if updated_audit_data:
            return dict(zip(columns, updated_audit_data))
        else:
            return None
    
    def delete_audit(self, audit_id):
        # Retrieve all audit item IDs associated with the audit
        self.cursor.execute("SELECT id FROM audit_items WHERE audit_id = %s;", (audit_id,))
        audit_item_ids = self.cursor.fetchall()

        # Delete warnings associated with each audit item
        for item_id in audit_item_ids:
            self.cursor.execute("DELETE FROM warnings WHERE audit_item_id = %s;", (item_id[0],))

        # Delete audit items associated with the audit
        delete_items_query = "DELETE FROM audit_items WHERE audit_id = %s;"
        self.cursor.execute(delete_items_query, (audit_id,))

        # Delete the audit itself
        delete_audit_query = "DELETE FROM audits WHERE id = %s;"
        self.cursor.execute(delete_audit_query, (audit_id,))

        self.conn.commit()

        return f"Audit with id {audit_id} was deleted along with its related audit items and warnings."




    def create_audit_with_items_and_warnings(self, audit_data: Audit, items_with_warnings: List[AuditItemWithWarning]):
        # 1. Crear la auditoría y obtener el ID
        
        
        self.cursor.execute("""
        SELECT id FROM audits 
        WHERE coordinator_id = %s AND site_id = %s AND audit_date = %s AND checklist_id = %s;
        """, 
        (audit_data.coordinator_id, audit_data.site_id, audit_data.audit_date, audit_data.checklist_id))
        existing_audit = self.cursor.fetchone()
        
        if existing_audit:
            audit_id = existing_audit[0]
            # Update the existing audit rather than creating a new one
            return audit_id
      

        audit_id = self.insert_audit(audit_data)
        
        
        

        # 2. Obtener todos los ítems del checklist asociado
        self.cursor.execute("SELECT id FROM check_item WHERE group_id IN (SELECT id FROM checkgroup WHERE checklist_id = %s)", (audit_data.checklist_id,))
        all_checklist_items = {item[0] for item in self.cursor.fetchall()}

        # 3. Insertar los ítems de la auditoría y manejar los warnings
        for check_item_id in all_checklist_items:
            item_with_warning = next((item for item in items_with_warnings if item.audit_item.check_item_id == check_item_id), None)

            # Insertar el ítem de la auditoría y obtener su ID
            audit_item = item_with_warning.audit_item if item_with_warning else AuditItem(check_item_id=check_item_id, status=True, comments="")
            audit_item_id = self.insert_audit_item(audit_id, audit_item)

            if item_with_warning:
                # Si el ítem tiene un warning y está marcado como false, insertar el warning
                if not item_with_warning.audit_item.status and item_with_warning.warning:
                    self.insert_warning(audit_item_id, item_with_warning.warning)
                elif item_with_warning.audit_item.status:
                    # Si el ítem está marcado como true, actualizar cualquier warning existente a resolved = true
                    self.resolve_warnings_for_audit_item(audit_item_id)
            else:
                # Si el ítem está marcado como true y no está en items_with_warnings, asegurar que sus warnings estén resueltos
                self.resolve_warnings_for_audit_item(audit_item_id)
            
        return audit_id


    def update_audit_item(self, item_id, updated_data: AuditItem):
        # Actualizar el audit_item
        update_query = """
        UPDATE audit_items
        SET audit_id = %s, check_item_id = %s, status = ture, comments = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.audit_id, updated_data.check_item_id,
            updated_data.status, updated_data.comments, item_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_item_data = self.cursor.fetchone()

        # Si el estado se actualiza a True, actualizar todas las advertencias asociadas como resueltas
        if updated_data.status:
            self.resolve_warnings_for_audit_item(item_id)

        self.conn.commit()

        if updated_item_data:
            return dict(zip(columns, updated_item_data))
        else:
            return None

    def resolve_audit_items_by_check_item_description(self, audit_id, description, new_status):
        """
        Resuelve los audit_items de una auditoría específica, basándose en la descripción del check_item asociado.

        :param audit_id: El ID de la auditoría cuyos items se actualizarán.
        :param description: La descripción del check_item que se busca.
        :param new_status: El nuevo estado para los audit_items encontrados.
        """
        # Encontrar el ID del check_item basado en la descripción
        self.cursor.execute("SELECT id FROM check_item WHERE description = %s;", (description,))
        check_item_id = self.cursor.fetchone()

        if check_item_id:
            # Actualizar los audit_items que están asociados con el check_item encontrado
            update_query = """
            UPDATE audit_items
            SET status = %s
            WHERE audit_id = %s AND check_item_id = %s;
            """
            self.cursor.execute(update_query, (new_status, audit_id, check_item_id[0]))
            self.conn.commit()
            return f"audit_items updated for check_item with description '{description}' in audit_id {audit_id}."
        else:
            return "No check_item found with the given description."

    def insert_audit_item(self, audit_id, audit_item: AuditItem):
        insert_query = """
        INSERT INTO audit_items (audit_id, check_item_id, status, comments)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (
            audit_id, 
            audit_item.check_item_id, 
            audit_item.status, 
            audit_item.comments
        ))
        item_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return item_id


    def select_audit_item_by_id(self, item_id):
        select_query = "SELECT * FROM audit_items WHERE id = %s;"
        self.cursor.execute(select_query, (item_id,))
        columns = [desc[0] for desc in self.cursor.description]
        item_data = self.cursor.fetchone()

        if item_data:
            return dict(zip(columns, item_data))
        else:
            return None
        
        
    def select_all_audit_items(self):
        select_query = "SELECT * FROM audit_items ;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        items_data = self.cursor.fetchall()

        if items_data:
            return [dict(zip(columns, item_data)) for item_data in items_data]
        else:
            return []

    def update_audit_item(self, item_id, updated_data: AuditItem):
        update_query = """
        UPDATE audit_items
        SET audit_id = %s, check_item_id = %s, status = %s, comments = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.audit_id, updated_data.check_item_id,
            updated_data.status, updated_data.comments, item_id
        ))

        columns = [desc[0] for desc in self.cursor.description]
        updated_item_data = self.cursor.fetchone()

        if updated_item_data:
            return dict(zip(columns, updated_item_data))
        else:
            return None

    def delete_audit_item(self, item_id):
        delete_query = "DELETE FROM audit_items WHERE id = %s;"
        self.cursor.execute(delete_query, (item_id,))
        self.conn.commit()
        return f"Audit item with id {item_id} was deleted."


    def delete_warnings_for_audit_item(self, audit_item_id):
        delete_query = "DELETE FROM warnings WHERE audit_item_id = %s;"
        self.cursor.execute(delete_query, (audit_item_id,))
        self.conn.commit()


    def insert_check_group(self, check_group: CheckGroup):
        insert_query = """
        INSERT INTO checkgroup (name)
        VALUES (%s) RETURNING id;
        """
        self.cursor.execute(insert_query, (check_group.name,))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id



    def select_check_group_by_id(self, group_id):
        select_query = "SELECT * FROM checkgroup WHERE id = %s;"
        self.cursor.execute(select_query, (group_id,))
        columns = [desc[0] for desc in self.cursor.description]
        group_data = self.cursor.fetchone()

        if group_data:
            return dict(zip(columns, group_data))
        else:
            return None

    def update_check_group(self, group_id, updated_data: CheckGroup):
        update_query = """
        UPDATE checkgroup
        SET name = %s, checklist_id = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (updated_data.name, updated_data.checklist_id, group_id))
        columns = [desc[0] for desc in self.cursor.description]
        updated_group_data = self.cursor.fetchone()
        self.conn.commit()  # Aquí se agrega el commit
        return dict(zip(columns, updated_group_data)) if updated_group_data else None


    def delete_checklist(self, checklist_id):
        # First, delete check items associated with the checklist
        delete_items_query = """
        DELETE FROM check_item
        WHERE group_id IN (
            SELECT id FROM checkgroup WHERE checklist_id = %s
        );
        """
        self.cursor.execute(delete_items_query, (checklist_id,))
        
        # Then, delete the check groups associated with the checklist
        delete_groups_query = "DELETE FROM checkgroup WHERE checklist_id = %s;"
        self.cursor.execute(delete_groups_query, (checklist_id,))

        # Finally, delete the checklist itself
        delete_checklist_query = "DELETE FROM checklists WHERE id = %s;"
        self.cursor.execute(delete_checklist_query, (checklist_id,))
        
        self.conn.commit()
        return f"Checklist with id {checklist_id} was deleted along with its related groups and items."



    def delete_check_group(self, group_id):
        delete_query = "DELETE FROM checkgroup WHERE id = %s;"
        self.cursor.execute(delete_query, (group_id,))
        self.conn.commit()
        return f"Check group with id {group_id} was deleted."
    
    
    def select_all_check_groups(self):
        select_query = "SELECT * FROM checkgroup;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        all_groups = self.cursor.fetchall()

        return [dict(zip(columns, group_data)) for group_data in all_groups]



    def insert_check_item(self, check_item: CheckItem):
        insert_query = """
        INSERT INTO check_item (description, group_id)
        VALUES (%s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (check_item.description, check_item.group_id))
        item_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return item_id
    
    def select_all_check_items(self):
        select_query = "SELECT * FROM check_item;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        items_data = self.cursor.fetchall()
        return [dict(zip(columns, item)) for item in items_data] if items_data else []
    
    
    def select_all_warnings(self):
        select_query = "SELECT * FROM warnings;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        warnings_data = self.cursor.fetchall()
        return [dict(zip(columns, warning)) for warning in warnings_data] if warnings_data else []
        
    def select_check_item_by_id(self, item_id):
        select_query = "SELECT * FROM check_item WHERE id = %s;"
        self.cursor.execute(select_query, (item_id,))
        columns = [desc[0] for desc in self.cursor.description]
        item_data = self.cursor.fetchone()
        return dict(zip(columns, item_data)) if item_data else None
    
    
    def update_check_item(self, item_id, updated_data: CheckItem):
        update_query = """
        UPDATE check_item
        SET description = %s, group_id = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (updated_data.description, updated_data.group_id, item_id))
        columns = [desc[0] for desc in self.cursor.description]
        updated_item_data = self.cursor.fetchone()
        return dict(zip(columns, updated_item_data)) if updated_item_data else None
    
    def delete_check_item(self, item_id):
        delete_query = "DELETE FROM check_item WHERE id = %s;"
        self.cursor.execute(delete_query, (item_id,))
        self.conn.commit()
        return f"Check item with id {item_id} was deleted."
    
    
    def insert_warning(self, audit_item_id, warning: Warning):
        insert_query = """
        INSERT INTO warnings (audit_item_id, warning_text, resolved, date)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (
            audit_item_id,
            warning.warning_text,
            warning.resolved,
            warning.date
        ))
        warning_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return warning_id
    
    def update_warning(self, warning_id, updated_data: Warning):
        update_query = """
        UPDATE warnings
        SET audit_item_id = %s, warning_text = %s, resolved = %s, date = %s
        WHERE id = %s
        RETURNING *;
        """
        self.cursor.execute(update_query, (
            updated_data.audit_item_id, updated_data.warning_text, updated_data.resolved, updated_data.date, warning_id
        ))
        columns = [desc[0] for desc in self.cursor.description]
        updated_warning_data = self.cursor.fetchone()
        return dict(zip(columns, updated_warning_data)) if updated_warning_data else None

    def select_warning_by_id(self, warning_id):
        select_query = "SELECT * FROM warnings WHERE id = %s;"
        self.cursor.execute(select_query, (warning_id,))
        columns = [desc[0] for desc in self.cursor.description]
        warning_data = self.cursor.fetchone()
        return dict(zip(columns, warning_data)) if warning_data else None
    
    
    def delete_warning(self, warning_id):
        delete_query = "DELETE FROM warnings WHERE id = %s;"
        self.cursor.execute(delete_query, (warning_id,))
        self.conn.commit()
        return f"Warning with id {warning_id} was deleted."
    
    
    def get_all_checklists_with_groups_and_items(self):
        query = """
        SELECT 
            cl.id as checklist_id,
            cl.name as checklist_name,
            cg.id as group_id,
            cg.name as group_name,
            ci.id as item_id,
            ci.description as item_description
        FROM 
            checklists cl
            LEFT JOIN checkgroup cg ON cl.id = cg.checklist_id
            LEFT JOIN check_item ci ON cg.id = ci.group_id
        ORDER BY 
            cl.name, cg.name, ci.description;
        """
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        # Inicializamos una lista para almacenar los checklists
        checklists = []

        # Iteramos sobre los resultados de la consulta
        for row in rows:
            checklist_id, checklist_name, group_id, group_name, item_id, item_description = row

            # Verificamos si el checklist ya existe en la lista
            checklist_exists = False
            for checklist in checklists:
                if checklist['checklist_id'] == checklist_id:
                    checklist_exists = True
                    # Verificamos si el grupo ya existe en el checklist
                    group_exists = False
                    for group in checklist['groups']:
                        if group['group_id'] == group_id:
                            group_exists = True
                            # Agregamos el item al grupo existente
                            group['items'].append({'item_id': item_id, 'item_description': item_description})
                            break
                    # Si el grupo no existe, lo agregamos al checklist
                    if not group_exists:
                        checklist['groups'].append({'group_id': group_id, 'group_name': group_name, 'items': [{'item_id': item_id, 'item_description': item_description}]})
                    break

            # Si el checklist no existe, lo agregamos a la lista
            if not checklist_exists:
                checklists.append({'checklist_id': checklist_id, 'checklist_name': checklist_name, 'groups': [{'group_id': group_id, 'group_name': group_name, 'items': [{'item_id': item_id, 'item_description': item_description}]}]})

        return checklists

    
    
    def get_checklist_by_id_with_groups_and_items(self, checklist_id):
        query = """
        SELECT 
            cl.id as checklist_id,
            cl.name as checklist_name,
            cg.id as group_id,
            cg.name as group_name,
            ci.id as item_id,
            ci.description as item_description
        FROM 
            checklists cl
            LEFT JOIN checkgroup cg ON cl.id = cg.checklist_id
            LEFT JOIN check_item ci ON cg.id = ci.group_id
        WHERE
            cl.id = %s
        ORDER BY 
            cl.name, cg.name, ci.description;
        """
        self.cursor.execute(query, (checklist_id,))
        rows = self.cursor.fetchall()

        # Inicializamos un diccionario para almacenar el checklist
        checklist = {'checklist_id': None, 'checklist_name': None, 'groups': []}

        # Iteramos sobre los resultados de la consulta
        for row in rows:
            _, checklist_name, group_id, group_name, item_id, item_description = row

            # Si el checklist no tiene valores asignados, los asignamos
            if not checklist['checklist_id']:
                checklist['checklist_id'] = checklist_id
                checklist['checklist_name'] = checklist_name

            # Verificamos si el grupo ya existe en el checklist
            group_exists = False
            for group in checklist['groups']:
                if group['group_id'] == group_id:
                    group_exists = True
                    # Agregamos el item al grupo existente
                    group['items'].append({'item_id': item_id, 'item_description': item_description})
                    break

            # Si el grupo no existe, lo agregamos al checklist
            if not group_exists:
                checklist['groups'].append({'group_id': group_id, 'group_name': group_name, 'items': [{'item_id': item_id, 'item_description': item_description}]})

        return checklist

    
    
    
    
    
    def insert_checklist_with_groups_and_items(self, checklist_data: ChecklistWithGroups):
        # Insertar el checklist y obtener su ID
        insert_checklist_query = """
        INSERT INTO checklists (name)
        VALUES (%s) RETURNING id;
        """
        self.cursor.execute(insert_checklist_query, (checklist_data.name,))
        checklist_id = self.cursor.fetchone()[0]
        self.conn.commit()

        # Iterar sobre los grupos del checklist
        for group in checklist_data.groups:
            # Insertar el grupo y obtener su ID
            insert_group_query = """
            INSERT INTO checkgroup (name, checklist_id)
            VALUES (%s, %s) RETURNING id;
            """
            self.cursor.execute(insert_group_query, (group.name, checklist_id))
            group_id = self.cursor.fetchone()[0]
            self.conn.commit()

            # Iterar sobre los ítems del grupo
            for item in group.items:
                # Insertar el ítem en la base de datos
                insert_item_query = """
                INSERT INTO check_item (description, group_id)
                VALUES (%s, %s) RETURNING id;
                """
                self.cursor.execute(insert_item_query, (item.description, group_id))
                self.conn.commit()

        return checklist_id
    
    
    
    def resolve_warnings_for_audit_item(self, audit_item_id):
        update_query = "UPDATE warnings SET resolved = TRUE WHERE audit_item_id = %s;"
        self.cursor.execute(update_query, (audit_item_id,))
        self.conn.commit()
    
    
    
    
    
    def close_connection(self):
        self.conn.close()
        
        
