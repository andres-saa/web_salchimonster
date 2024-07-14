from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.city import citySchema
from schema.inventory.cdi_inventory import GroupCdiInventoryItems,CdiInventoryItems,GroupCdiInventoryItems
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class CdiInventory:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        
    
    def get_all_cdi_Inventory_reports (self):
        query = f""" select * from inventory.view_cdi_inventory_details;        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    
    def get_all_cdi_Inventory_reports_by_responsible_id (self, responsible_id:int):
        query = f""" select * from inventory.view_cdi_inventory_details where responsible_id = {responsible_id};        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
     

    def get_all_cdi_inventory_reports_by_responsible_id_filtered(self, responsible_id: int, start_date: str, end_date: str):
        query = f"""
        SELECT * FROM inventory.view_cdi_inventory_details 
        WHERE responsible_id = {responsible_id} 
        AND date >= '{start_date}' 
        AND date <= '{end_date}';
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def get_all_cdi_inventory_reports_filtered(self, site_ids: list, start_date: str, end_date: str):
        if len(site_ids) == 1:
            site_ids_tuple = f"({site_ids[0]})"  # Asegura que se forme una tupla de un solo elemento
        else:
            site_ids_tuple = tuple(site_ids)

        query = f"""
        SELECT * FROM inventory.view_cdi_inventory_details
        WHERE site_id IN {site_ids_tuple}
        AND date >= '{start_date}'
        AND date <= '{end_date}';
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def get_all_cdi_Inventory_entries (self,cdi_inventory_id):
        query = f""" select * from inventory.cdi_detailed_inventory_entries where cdi_inventory_id = {cdi_inventory_id};        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def insert_unit_measure(self, name):
        query = f"""
        INSERT INTO inventory.cdi_inventory_unit_measures (name, status)
        VALUES (%s, true);
        """
        self.cursor.execute(query, (name,))
        self.conn.commit()

    def disable_unit_measure(self, unit_measure_id):
        query = f"""
        UPDATE inventory.cdi_inventory_unit_measures
        SET status = false
        WHERE id = %s;
        """
        self.cursor.execute(query, (unit_measure_id,))
        self.conn.commit()


    def get_all_cdi_Inventory_item_by_group_name (self,cdi_inventory_group):
        query = f""" select * from inventory.complete_cdi_items where group_name = '{cdi_inventory_group}' and status = true ;        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_all_cdi_group_items (self):
        query = f""" select * from inventory.group_cdi_inventory_items where status = true;        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    def get_all_cdi_group_unit_measures (self):
        query = f""" select * from inventory.cdi_inventory_unit_measures where status = true;        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    def insert_cdi_inventory_group(self, group_data: GroupCdiInventoryItems):
        insert_query = """
        INSERT INTO inventory.group_cdi_inventory_items (
            name
        ) VALUES (%s) RETURNING id;
        """
        # Como city_id es generado automáticamente, no necesitamos insertarlo manualmente
        self.cursor.execute(insert_query, (group_data.name,))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id
    
    
    def insert_cdi_inventory_item(self, item_data: CdiInventoryItems):
        insert_query = """
        INSERT INTO inventory.cdi_inventory_items (
            name,group_cdi_inventory_item_id,inventory_item_unit_measure_id
        ) VALUES (%s , %s, %s ) RETURNING id;
        """
        # Como city_id es generado automáticamente, no necesitamos insertarlo manualmente
        self.cursor.execute(insert_query, (item_data.name,item_data.group_cdi_inventory_item_id,item_data.cdi_inventory_item_unit_measure_id))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id




    def disable_cdi_inventory_group(self, group_Id:int):
        insert_query = """
        update inventory.group_cdi_inventory_items set status = false where id = %s RETURNING id;
        """
        self.cursor.execute(insert_query, (group_Id,))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id 
    
    def disable_cdi_inventory_item(self, item_id:int):
        insert_query = """
        update inventory.cdi_inventory_items set status = false where id = %s RETURNING id;
        """
        self.cursor.execute(insert_query, (item_id,))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id 
    

    def get_groups_with_items(self):
        query = """
        SELECT g.id as group_id, g.name as group_name, 
            i.id as item_id, i.name as item_name,
            u.name as unit_measure,
            u.id as unit_measure_id
        FROM inventory.group_cdi_inventory_items g
        INNER JOIN inventory.cdi_inventory_items i ON g.id = i.group_cdi_inventory_item_id
        INNER JOIN inventory.daily_inventory_unit_measures u ON i.inventory_item_unit_measure_id = u.id
        WHERE g.status = true AND i.status = true;
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        
        # Crear una lista para agrupar los ítems por grupo
        groups = []
        group_items = {}
        for row in results:
            group_id = row[0]
            group_name = row[1]
            item_id = row[2]
            item_name = row[3]
            unit_measure = row[4]
            unit_measure_id = row[5]  # Unidad de medida
            
            if group_id not in group_items:
                group_items[group_id] = {
                    'group_id': group_id,
                    'group_name': group_name,
                    'items': []
                }
            group_items[group_id]['items'].append({
                'item_id': item_id, 
                'item_name': item_name,
                'unit_measure': unit_measure,
                'unit_measure_id': unit_measure_id  # Añadir la unidad de medida al ítem
            })
        
        # Agregamos cada grupo y sus ítems a la lista de grupos
        for group in group_items.values():
            groups.append(group)

        return groups


    def insert_complete_inventory(self, responsible_id, site_id, items_data):
        # Insertar el inventario diario usando la hora actual del servidor
        insert_inventory_query = """
        INSERT INTO inventory.cdi_inventory (
            date, responsible_id, site_id
        ) VALUES (CURRENT_TIMESTAMP AT TIME ZONE 'UTC', %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_inventory_query, (responsible_id, site_id))
        inventory_id = self.cursor.fetchone()[0]
      

        # Insertar las entradas del inventario
        insert_entry_query = """
        INSERT INTO inventory.cdi_inventory_entry (
            cdi_inventory_id, cdi_inventory_item_id, quantity, inventory_unit_measure_id
        ) VALUES (%s, %s, %s, %s);
        """
        for item in items_data:
            self.cursor.execute(insert_entry_query, (
                inventory_id,
                item.cdi_inventory_item_id,  # Asumiendo que los datos vienen en un diccionario
                item.quantity,
                item.cdi_inventory_unit_measure_id
            ))
        self.conn.commit()

        return inventory_id
        
    def close_connection(self):
        self.conn.close()


