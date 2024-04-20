from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
# from schema.adicionales.adicional    import adicionalSchemaPost

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Adicional:
    def __init__(self):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def select_adicionales_for_product_active(self, product_instance_id):
    # Ejecutar la consulta para obtener los detalles adicionales del producto
        select_query = f"SELECT  aditional_item_instance_id,product_category_name, aditional_item_name,aditional_item_price,aditional_item_type_name FROM inventory.product_aditional_details WHERE product_instance_id = {product_instance_id} and status = true;"
        self.cursor.execute(select_query)
        
        # Obtener los nombres de las columnas del resultado
        columns = [desc[0] for desc in self.cursor.description]
        
        additional_details = [dict(zip(columns, row)) for row in self.cursor.fetchall()]

        grouped_details = {}
        for detail in additional_details:
            type_name = detail["aditional_item_type_name"]
            if type_name not in grouped_details:
                grouped_details[type_name] = [detail]
            else:
                grouped_details[type_name].append(detail)
        
        grouped_output = []
        for type_name, items in grouped_details.items():
            category_items = {
                "category": type_name,
                "items": items
            }
            grouped_output.append(category_items)

        return grouped_output

    def select_unique_adicionales_by_site(self, site_id):
        # Consulta SQL para seleccionar adiciones únicas por site_id, corregida para coincidir DISTINCT ON con ORDER BY
        select_query = f"""
        SELECT DISTINCT ON (aditional_item_name, aditional_item_price)
            aditional_item_name, aditional_item_price,aditional_item_instance_id, status, aditional_item_type_name
        FROM inventory.product_aditional_details
        WHERE site_id = {site_id}
        ORDER BY aditional_item_name, aditional_item_price, aditional_item_type_name; 
        """
        self.cursor.execute(select_query)
        

        columns = [desc[0] for desc in self.cursor.description]
        
        rows = self.cursor.fetchall()
        unique_adicionales = [dict(zip(columns, row)) for row in rows]
        
        # Agrupar los resultados por 'aditional_item_type_name'
        grouped_adicionales = {}
        for item in unique_adicionales:
            type_name = item['aditional_item_type_name']
            if type_name not in grouped_adicionales:
                grouped_adicionales[type_name] = []
            grouped_adicionales[type_name].append(item)

        return grouped_adicionales

    

    def toggle_adicionales_status(self, aditional_item_instance_id, status):
        # Primero, obtener el aditional_item_id, el precio y el site_id de la instancia específica
        select_instance_query = f"""
        SELECT aditional_item_id, price, site_id
        FROM orders.aditional_item_instances
        WHERE id = {aditional_item_instance_id};
        """
        self.cursor.execute(select_instance_query)
        instance_details = self.cursor.fetchone()
        if not instance_details:
            return f"No item found with instance ID {aditional_item_instance_id}"

        aditional_item_id, price, site_id = instance_details

        # Luego, obtener el nombre del artículo adicional usando aditional_item_id
        select_name_query = f"""
        SELECT name
        FROM orders.aditional_items
        WHERE id = {aditional_item_id};
        """
        self.cursor.execute(select_name_query)
        item_name = self.cursor.fetchone()
        if not item_name:
            return f"No item found with aditional item ID {aditional_item_id}"

        aditional_item_name = item_name[0]

        # Actualización de todos los registros correspondientes en 'orders.aditional_item_instances'
        update_query = f"""
        UPDATE orders.aditional_item_instances
        SET status = {status}
        WHERE aditional_item_id IN (
            SELECT id FROM orders.aditional_items WHERE name = '{aditional_item_name}' AND price = {price}
        ) AND site_id = {site_id};
        """
        self.cursor.execute(update_query)
        updated_rows = self.cursor.rowcount
        self.conn.commit()

        return f"Updated {updated_rows} items named '{aditional_item_name}' with price {price} at site {site_id} to {'active' if status else 'inactive'}."
    
    
    
    def select_adicionales_for_products(self, product_instance_ids,site_id):
    # Convertir la lista de IDs en una cadena para la consulta SQL
        ids_string = ', '.join(map(str, product_instance_ids))
        
        # Ejecutar la consulta para obtener los detalles adicionales de los productos
        select_query = f"""
        SELECT DISTINCT ON (aditional_item_name, aditional_item_price)
        aditional_item_name,
        aditional_item_instance_id,
        product_category_name,
        aditional_item_price,
        aditional_item_type_name
        FROM inventory.product_aditional_details
        WHERE product_instance_id IN ({ids_string}) and status = true and site_id = {site_id}
        ORDER BY aditional_item_name, aditional_item_price, aditional_item_instance_id;
        """
        self.cursor.execute(select_query)
        
        # Obtener los nombres de las columnas del resultado
        columns = [desc[0] for desc in self.cursor.description]
        
        # Crear un conjunto para eliminar duplicados
        unique_additionals = set()
        additional_details = []
        
        # Recopilar datos únicos
        for row in self.cursor.fetchall():
            # Crear un tuple, que es hashable y se puede añadir a un set
            detail_tuple = tuple(row)
            if detail_tuple not in unique_additionals:
                unique_additionals.add(detail_tuple)
                additional_details.append(dict(zip(columns, row)))

        # Agrupar los detalles adicionales por tipo
        grouped_details = {}
        for detail in additional_details:
            type_name = detail["aditional_item_type_name"]
            if type_name not in grouped_details:
                grouped_details[type_name] = [detail]
            else:
                grouped_details[type_name].append(detail)
        
        # Preparar la salida agrupada
        grouped_output = []
        for type_name, items in grouped_details.items():
            category_items = {
                "category": type_name,
                "items": items
            }
            grouped_output.append(category_items)

        return grouped_output
   

    def select_all_aditional_registered(self):
        # Definimos la consulta que verifica la existencia de instancias activas de productos por cada categoría
        select_query = """
        SELECT * from orders.vw_aditional_items_with_types
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        
        # Convertir filas de la base de datos en diccionarios
        items = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        
        # Agrupar los ítems por el tipo
        grouped_items = {}
        for item in items:
            type_name = item['type_name']
            if type_name not in grouped_items:
                grouped_items[type_name] = []
            grouped_items[type_name].append({
                'item_id': item['item_id'],
                'item_name': item['item_name'],
                'item_price': item['item_price'],
                'type_name':item['type_name']
            })
        
        return grouped_items


    def select_adicionales_for_product(self, product_instance_id):
    # Ejecutar la consulta para obtener los detalles adicionales del producto
        select_query = f"SELECT  aditional_item_instance_id,product_category_name, aditional_item_name,aditional_item_price,aditional_item_type_name FROM inventory.product_aditional_details WHERE product_instance_id = {product_instance_id}"
        self.cursor.execute(select_query)
        
        # Obtener los nombres de las columnas del resultado
        columns = [desc[0] for desc in self.cursor.description]
        
        additional_details = [dict(zip(columns, row)) for row in self.cursor.fetchall()]

        grouped_details = {}
        for detail in additional_details:
            type_name = detail["aditional_item_type_name"]
            if type_name not in grouped_details:
                grouped_details[type_name] = [detail]
            else:
                grouped_details[type_name].append(detail)
        
        grouped_output = []
        for type_name, items in grouped_details.items():
            category_items = {
                "category": type_name,
                "items": items
            }
            grouped_output.append(category_items)

        return grouped_output
 
        
        
     
        
    def close_connection(self):
        self.conn.close()
