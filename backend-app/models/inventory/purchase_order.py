from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.city import citySchema
from schema.inventory.inventory import GroupDailyInventoryItems,DailyInventoryItems
from schema.inventory.purchase_order import GroupPurchaseItems,PurchaseOrderItem,PurchaseOrderStatus
load_dotenv()
import pytz

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


class PurchaseOrder:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        
    
    def get_all_purchase_orders(self):
        query = "SELECT * FROM purchase.view_purchase_details2;"
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        
        # Crear una lista para almacenar los registros con la fecha convertida
        converted_records = []
        
        # Zona horaria de Colombia
        tz_colombia = pytz.timezone('America/Bogota')
        
        for row in results:
            record = dict(zip(columns, row))
            # Suponiendo que 'expedition_date' es el nombre de la columna de la fecha
            utc_date = record['expedition_date']
            # Convertir la fecha de UTC a hora de Colombia
            local_date = utc_date.replace(tzinfo=pytz.utc).astimezone(tz_colombia)
            # Actualizar el registro con la nueva fecha
            record['expedition_date'] = local_date.strftime('%d-%m-%YT%H:%M:%S')
            converted_records.append(record)
        
        return converted_records



    def get_all_purchase_order_history(self,purchase_order_id):
        query = f"SELECT * FROM purchase.view_purchase_history where purchase_order_id = {purchase_order_id}"
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        
        # Crear una lista para almacenar los registros con la fecha convertida
        converted_records = []
        
        # Zona horaria de Colombia
        tz_colombia = pytz.timezone('America/Bogota')
        
        for row in results:
            record = dict(zip(columns, row))
            # Suponiendo que 'expedition_date' es el nombre de la columna de la fecha
            utc_date = record['status_timestamp']
            # Convertir la fecha de UTC a hora de Colombia
            local_date = utc_date.replace(tzinfo=pytz.utc).astimezone(tz_colombia)
            # Actualizar el registro con la nueva fecha
            record['status_timestamp'] = local_date.strftime('%d-%m-%YT%H:%M:%S')
            converted_records.append(record)
        
        return converted_records


    def get_all_purchase_orders_by_lap_id(self, lap_id):
        query = f"SELECT * FROM purchase.view_purchase_details_complete where lap_id = {lap_id};"
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        
        # Crear una lista para almacenar los registros con la fecha convertida
        converted_records = []
        
        # Zona horaria de Colombia
        tz_colombia = pytz.timezone('America/Bogota')
        
        for row in results:
            record = dict(zip(columns, row))
            # Suponiendo que 'expedition_date' es el nombre de la columna de la fecha
            utc_date = record['expedition_date']
            # Convertir la fecha de UTC a hora de Colombia
            local_date = utc_date.replace(tzinfo=pytz.utc).astimezone(tz_colombia)
            # Actualizar el registro con la nueva fecha
            record['expedition_date'] = local_date.strftime('%d-%m-%YT%H:%M:%S')
            converted_records.append(record)


            utc_status_timestamp = record['status_timestamp']
            local_status_timestamp = utc_status_timestamp.replace(tzinfo=pytz.utc).astimezone(tz_colombia)
            record['status_timestamp'] = local_status_timestamp.strftime('%d-%m-%YT%H:%M:%S')
        
        return converted_records
    

    
    def get_all_purchase_orders_by_responsible_id (self, responsible_id:int):
        query = f""" select * from purchase.view_purchase_details where responsible_id = {responsible_id};        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        
        # Crear una lista para almacenar los registros con la fecha convertida
        converted_records = []
        
        # Zona horaria de Colombia
        tz_colombia = pytz.timezone('America/Bogota')
        
        for row in results:
            record = dict(zip(columns, row))
            # Suponiendo que 'expedition_date' es el nombre de la columna de la fecha
            utc_date = record['expedition_date']
            # Convertir la fecha de UTC a hora de Colombia
            local_date = utc_date.replace(tzinfo=pytz.utc).astimezone(tz_colombia)
            # Actualizar el registro con la nueva fecha
            record['expedition_date'] = local_date.strftime('%d-%m-%YT%H:%M:%S')
            converted_records.append(record)
        
        return converted_records
    

    # def get_all_purchase_orders_by_lap_id (self, lap_id:int):
    #     query = f""" select * from purchase.view_purchase_details where lap_id = {lap_id};        
    #     """
    #     self.cursor.execute(query)
    #     columns = [desc[0] for desc in self.cursor.description]
    #     return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    



    def get_all_purchase_order_by_responsible_id_filtered(self, responsible_id: int, start_date: str, end_date: str):
        query = f"""
        SELECT * FROM purchase.view_purchase_details
        WHERE responsible_id = {responsible_id} 
        AND status_timestamp >= '{start_date}' 
        AND status_timestamp <= '{end_date}';
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]



    def get_all_purchase_order_by_sites_filtered(self, site_ids: list, start_date: str, end_date: str):
        if len(site_ids) == 1:
            site_ids_tuple = f"({site_ids[0]})"  # Asegura que se forme una tupla de un solo elemento
        else:
            site_ids_tuple = tuple(site_ids)
        
        

        query = f"""
        SELECT * FROM purchase.view_purchase_details
        WHERE site_id IN {site_ids_tuple}
        AND status_timestamp >= '{start_date}'
        AND status_timestamp <= '{end_date}';
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()

       # Crear una lista para almacenar los registros con la fecha convertida
        converted_records = []
        
        # Zona horaria de Colombia
        tz_colombia = pytz.timezone('America/Bogota')
        
        for row in results:
            record = dict(zip(columns, row))
            # Suponiendo que 'expedition_date' es el nombre de la columna de la fecha
            utc_date = record['expedition_date']
            # Convertir la fecha de UTC a hora de Colombia
            local_date = utc_date.replace(tzinfo=pytz.utc).astimezone(tz_colombia)
            # Actualizar el registro con la nueva fecha
            record['expedition_date'] = local_date.strftime('%d-%m-%YT%H:%M:%S')
            converted_records.append(record)
        
        return converted_records




     

    def get_all_purchase_order_by_responsible_id_filtered(self, responsible_id: int, start_date: str, end_date: str):
        query = f"""
        SELECT * FROM purchase.view_purchase_details 
        WHERE responsible_id = {responsible_id} 
        AND status_timestamp >= '{start_date}' 
        AND status_timestamp <= '{end_date}';
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        
        # Crear una lista para almacenar los registros con la fecha convertida
        converted_records = []
        
        # Zona horaria de Colombia
        tz_colombia = pytz.timezone('America/Bogota')
        
        for row in results:
            record = dict(zip(columns, row))
            # Suponiendo que 'expedition_date' es el nombre de la columna de la fecha
            utc_date = record['expedition_date']
            # Convertir la fecha de UTC a hora de Colombia
            local_date = utc_date.replace(tzinfo=pytz.utc).astimezone(tz_colombia)
            # Actualizar el registro con la nueva fecha
            record['expedition_date'] = local_date.strftime('%d-%m-%YT%H:%M:%S')
            converted_records.append(record)
        
        return converted_records


    # def get_all_daily_inventory_reports_filtered(self, site_ids: list, start_date: str, end_date: str):
    #     if len(site_ids) == 1:
    #         site_ids_tuple = f"({site_ids[0]})"  # Asegura que se forme una tupla de un solo elemento
    #     else:
    #         site_ids_tuple = tuple(site_ids)

    #     query = f"""
    #     SELECT * FROM inventory.view_daily_inventory_details
    #     WHERE site_id IN {site_ids_tuple}
    #     AND date >= '{start_date}'
    #     AND date <= '{end_date}';
    #     """
    #     self.cursor.execute(query)
    #     columns = [desc[0] for desc in self.cursor.description]
    #     return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def get_purchase_item_groups_with_items(self):
        query = """
        SELECT g.id as group_id, g.name as group_name, 
            i.id as item_id, i.name as item_name,
            u.name as unit_measure,
            u.id as unit_measure_id
        FROM purchase.order_purchase_item_groups g
        INNER JOIN purchase.order_purchase_item i ON g.id = i.order_purchase_item_group_id
        INNER JOIN inventory.daily_inventory_unit_measures u ON i.unit_measure_id = u.id
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


    def get_all_purchase_order_group_items (self):
        query = f""" select * from purchase.order_purchase_item_groups where status = true;        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def get_purchase_order_entries_by_order_purchase_id (self,order_purchase_id):
        query = f""" select * from purchase.detailed_purchase_entries5 where purchase_order_id = {order_purchase_id};        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        
        # Crear una lista para almacenar los registros con la fecha convertida
        converted_records = []
        
        # Zona horaria de Colombia
        tz_colombia = pytz.timezone('America/Bogota')
        
        for row in results:
            record = dict(zip(columns, row))
            # Suponiendo que 'expedition_date' es el nombre de la columna de la fecha
            utc_date = record['date']
            # Convertir la fecha de UTC a hora de Colombia
            local_date = utc_date.replace(tzinfo=pytz.utc).astimezone(tz_colombia)
            # Actualizar el registro con la nueva fecha
            record['date'] = local_date.strftime('%d-%m-%YT%H:%M:%S')
            converted_records.append(record)
        
        return converted_records




    def get_all_purchase_order_item_by_group_name (self,order_purchase_group_name):
        query = f""" select * from purchase.complete_purchase_items where group_name = '{order_purchase_group_name}' and status = true ;        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    def get_all_purchase_items (self):
        query = f""" select * from purchase.complete_purchase_items where status = true;        
        """
        self.cursor.execute(query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    
    # def get_all_daily_group_unit_measures (self):
    #     query = f""" select * from inventory.daily_inventory_unit_measures;        
    #     """
    #     self.cursor.execute(query)
    #     columns = [desc[0] for desc in self.cursor.description]
    #     return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    def insert_purchase_items_group(self, group_data: PurchaseOrderItem):
        insert_query = """
        INSERT INTO purchase.order_purchase_item_groups (
            name
        ) VALUES (%s) RETURNING id;
        """
        # Como city_id es generado automáticamente, no necesitamos insertarlo manualmente
        self.cursor.execute(insert_query, (group_data.name,))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id
    
    
    def insert_purchase_group_item(self, item_data: DailyInventoryItems):
        insert_query = """
        INSERT INTO  purchase.order_purchase_item (
            name,order_purchase_item_group_id,unit_measure_id
        ) VALUES (%s , %s, %s ) RETURNING id;
        """
        # Como city_id es generado automáticamente, no necesitamos insertarlo manualmente
        self.cursor.execute(insert_query, (item_data.name,item_data.order_purchase_item_group_id,item_data.unit_measure_id))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id




    def disable_purchase_order_group(self, group_Id:int):
        insert_query = """
        update purchase.order_purchase_item_groups set status = false where id = %s RETURNING id;
        """
        self.cursor.execute(insert_query, (group_Id,))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id 
    
    def disable_order_purchase_item(self, item_id:int):
        insert_query = """
        update purchase.order_purchase_item set status = false where id = %s RETURNING id;
        """
        self.cursor.execute(insert_query, (item_id,))
        group_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return group_id 
    



    def chage_order_purchase_status(self, purchase_order_status: PurchaseOrderStatus):
        # Construir la parte del receiver_id opcionalmente
        receiver_id_value = 'NULL' if purchase_order_status.receiver_id is None else purchase_order_status.receiver_id
        
        insert_query = f"""
        INSERT INTO purchase.purchase_order_status(
        purchase_order_id, lap_id, responsible_id, status_timestamp, receiver_id)
        VALUES (
            {purchase_order_status.purchase_order_id}, 
            {purchase_order_status.lap_id+1}, 
            {purchase_order_status.responsible_id},
            CURRENT_TIMESTAMP AT TIME ZONE 'UTC',
            {receiver_id_value}) RETURNING id;
        """
        self.cursor.execute(insert_query)
        group_id = self.cursor.fetchone()[0]

        for item in purchase_order_status.ajusts:
            insert_query_ajust = f"""
            INSERT INTO purchase.order_purchase_entry_quantity_adjust(
                order_purchase_entry_id, responsible_id, lap_id, quantity_adjusted)
                VALUES ( {item.order_purchase_entry_id}, {purchase_order_status.responsible_id}, {purchase_order_status.lap_id}, {item.quantity_adjusted});
                """
            self.cursor.execute(insert_query_ajust)


        insert_query_note = f"""
            INSERT INTO purchase.purchase_order_status_notes(
            purchase_order_status_id, note)
            VALUES ({group_id}, '{purchase_order_status.order_purchase_notes}');
                """
        self.cursor.execute(insert_query_note)

        self.conn.commit()
        return group_id
        

    
    # def get_groups_with_items(self):
    #     query = """
    #     SELECT g.id as group_id, g.name as group_name, 
    #         i.id as item_id, i.name as item_name,
    #         u.name as unit_measure,
    #         u.id as unit_measure_id
    #     FROM inventory.group_daily_inventory_items g
    #     INNER JOIN inventory.daily_inventory_items i ON g.id = i.group_daily_inventory_item_id
    #     INNER JOIN inventory.daily_inventory_unit_measures u ON i.daily_inventory_item_unit_measure_id = u.id
    #     WHERE g.status = true AND i.status = true;
    #     """
    #     self.cursor.execute(query)
    #     columns = [desc[0] for desc in self.cursor.description]
    #     results = self.cursor.fetchall()
        
    #     # Crear una lista para agrupar los ítems por grupo
    #     groups = []
    #     group_items = {}
    #     for row in results:
    #         group_id = row[0]
    #         group_name = row[1]
    #         item_id = row[2]
    #         item_name = row[3]
    #         unit_measure = row[4]
    #         unit_measure_id = row[5]  # Unidad de medida
            
    #         if group_id not in group_items:
    #             group_items[group_id] = {
    #                 'group_id': group_id,
    #                 'group_name': group_name,
    #                 'items': []
    #             }
    #         group_items[group_id]['items'].append({
    #             'item_id': item_id, 
    #             'item_name': item_name,
    #             'unit_measure': unit_measure,
    #             'unit_measure_id':unit_measure_id  # Añadir la unidad de medida al ítem
    #         })
        
    #     # Agregamos cada grupo y sus ítems a la lista de grupos
    #     for group in group_items.values():
    #         groups.append(group)

    #     return groups



    def insert_complete_order(self, responsible_id, site_id, items_data, initial_lap_id=1):
        # Insertar la orden de compra usando la hora actual del servidor con zona horaria UTC
        insert_order_query = """
        INSERT INTO purchase.purchase_orders (
            expedition_date, responsible_id, site_id
        ) VALUES (CURRENT_TIMESTAMP AT TIME ZONE 'UTC', %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_order_query, (responsible_id, site_id))
        order_id = self.cursor.fetchone()[0]
        self.conn.commit()

        # Insertar el estado inicial de la orden con el lap id 1
        insert_status_query = """
        INSERT INTO purchase.purchase_order_status (
            purchase_order_id, lap_id, responsible_id, status_timestamp
        ) VALUES (%s, %s, %s, CURRENT_TIMESTAMP AT TIME ZONE 'UTC');
        """
        self.cursor.execute(insert_status_query, (order_id, initial_lap_id, responsible_id))
        self.conn.commit()

        # Insertar los ítems de la orden de compra
        insert_item_query = """
        INSERT INTO purchase.order_purchase_entry (
            order_purchase_id, order_purchase_item_id, quantity, unit_measure_id
        ) VALUES (%s, %s, %s, %s);
        """
        for item in items_data:
            # Asumiendo que item es un diccionario con claves que contienen los datos necesarios
            self.cursor.execute(insert_item_query, (
                order_id,
                item.order_purchase_item_id,
                item.quantity,
                item.unit_measure_id
            ))
        self.conn.commit()

        return order_id


        
    def close_connection(self):
        self.conn.close()


