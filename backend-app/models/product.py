
from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os
from schema.product import Product as Product_schema
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class ProductSchemaPost(BaseModel):
    name: str
    price: int
    description: str
    category_id: Optional[int] = None
    porcion: str
    


class Product:
    def __init__(self, product_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.product_id = product_id

    # def create_table(self):
    #     create_table_script = """
    #     CREATE TABLE IF NOT EXISTS products (
    #         product_id SERIAL PRIMARY KEY,
    #         name VARCHAR(255),
    #         price INT,
    #         description VARCHAR(255),
    #         category_id INTEGER,
    #         porcion VARCHAR(50)
    #     );
    #     """
        # self.cursor.execute(create_table_script)
        # self.conn.commit()

    def insert_product(self, product_data: Product_schema):
        insert_query = """
        INSERT INTO inventory.products (
            name, description, category_id
        ) VALUES (%s, %s, %s) RETURNING id;
        """
        self.cursor.execute(insert_query, (
            product_data.name,
            product_data.description,
            product_data.category_id # Incluir los nuevos campos
        ))
        product_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return product_id


    def select_products_by_site_and_category_active(self, site_id: int, category_id: int):
        select_query = f"""
        select * from inventory.complete_product_instances
        WHERE site_id = {site_id} AND category_id = {category_id} AND status = true order by price;
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        products = self.cursor.fetchall()
        return [dict(zip(columns, row)) for row in products]
    


    def deactivate_product(self, product_id):
        update_query = f"""
        UPDATE inventory.products SET visible = false WHERE id = {product_id}
        """
        self.cursor.execute(update_query)
        self.conn.commit()
        return 'ok'

        
    
    def select_products_by_site_and_category_all(self, site_id: int, category_id: int):
        select_query = f"""
        select * from inventory.complete_product_instances
        WHERE site_id = {site_id} AND category_id = {category_id} order by price;
        """
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        products = self.cursor.fetchall()
        return [dict(zip(columns, row)) for row in products]


    def select_all_products(self):
        select_query = "SELECT * FROM inventory.products;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]
    

    def select_product_by_id(self, product_id):
        select_query = "SELECT * FROM inventory.product_full_view WHERE product_instance_id = %s;"
        self.cursor.execute(select_query, (product_id,))
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        return [dict(zip(columns, row)) for row in results] if results else []


    def select_products_by_name(self, name: str):
        select_query = "SELECT * FROM inventory.product_full_view; WHERE name = %s;"
        self.cursor.execute(select_query, (name,))
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        return [dict(zip(columns, row)) for row in results] if results else []
    

    def select_product_by_name(self, name: str):
        select_query = "SELECT * FROM products WHERE name = %s;"
        self.cursor.execute(select_query, (name,))
        columns = [desc[0] for desc in self.cursor.description]
        result = self.cursor.fetchone()
        if result:
            return dict(zip(columns, result))
        else:
            return None


    def select_products_by_category_name(self, category_name: str):
            select_query = """
            SELECT p.* FROM products p
            JOIN categories c ON p.category_id = c.category_id
            WHERE c.category_name = %s;
            """
            self.cursor.execute(select_query, (category_name,))
            columns = [desc[0] for desc in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def select_products_by_category_id_and_site(self, category_id: int, site_id: int):
        select_query = """
        SELECT * FROM inventory.product_full_view 
        WHERE category_id = %s AND site_id = %s AND status; 
        """
        self.cursor.execute(select_query, (category_id, site_id))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    
    def update_product_and_its_instances(self, product_info, additional_item_ids):
        try:
            # Inicia una transacción
            self.cursor.execute("BEGIN;")

            # Actualiza la información del producto principal
            update_product_query = """
            UPDATE inventory.products
            SET name = %s, description = %s
            WHERE id = %s;
            """
            self.cursor.execute(update_product_query, (
                product_info['name'],
                product_info['description'],
                product_info['product_id']
            ))

            # Recupera todos los site_id disponibles
            self.cursor.execute("SELECT site_id FROM public.sites where show_on_web = true;")
            all_sites = self.cursor.fetchall()

            # Actualiza o inserta las instancias del producto en todas las sedes
            for site in all_sites:
                site_id = site[0]
                update_or_insert_product_instance_query = f"""
                update  inventory.product_instances set price = {product_info['price']} where product_id = {product_info['product_id']}
                
                """
                self.cursor.execute(update_or_insert_product_instance_query)
                

            # Elimina las asociaciones de productos con adicionales
            delete_product_additional_associations_query = """
            DELETE FROM orders.product_aditional_item_instances
            WHERE product_instance_id IN (
                SELECT id FROM inventory.product_instances WHERE product_id = %s
            );
            


            """
            self.cursor.execute(delete_product_additional_associations_query, (product_info['product_id'],))

            
            delete_additionals_query = """
            DELETE FROM orders.aditional_item_instances
            WHERE id IN (
                SELECT aditional_item_instance_id FROM orders.product_aditional_item_instances WHERE product_instance_id IN (
                    SELECT id FROM inventory.product_instances WHERE product_id = %s
                )
            );
            """
            
            self.cursor.execute(delete_additionals_query, (product_info['product_id'],))

            # Inserta nuevas instancias de adicionales y crea relaciones con el producto
            for additional_id in additional_item_ids:
                print("este es ek aducuibak",additional_id)
                for site in all_sites:
                    site_id = site[0]
                    
                    self.cursor.execute(f"SELECT price from orders.aditional_items where id = {additional_id}")
                    aditiona_price = self.cursor.fetchone()[0]
                    
                    insert_additional_query = """
                    INSERT INTO orders.aditional_item_instances (price, status, aditional_item_id, site_id, category_id)
                    VALUES (%s, %s, %s, %s, %s) RETURNING id;
                    """
                    print("site",site_id)
                    self.cursor.execute(insert_additional_query, (
                        aditiona_price,
                        True,# Aquí puedes ajustar si cada sitio podría tener un precio diferente
                        additional_id,
                        site_id,
                        product_info['category_id']
                    ))
                    additional_instance_id = self.cursor.fetchone()[0]

                    print("adicional", additional_instance_id)
                    
                    
                    
                    insert_product_additional_relation_query = """
                        INSERT INTO orders.product_aditional_item_instances (aditional_item_instance_id, product_instance_id)
                        SELECT %s, id FROM inventory.product_instances WHERE product_id = %s AND site_id = %s;
                    """
                    self.cursor.execute(insert_product_additional_relation_query, (
                        additional_instance_id,
                        product_info['product_id'],  # Usamos product_id para aplicarlo a todas las instancias de este producto
                        site_id
                    ))

            # Confirma los cambios
            self.cursor.execute("COMMIT;")
            return "Producto y sus instancias actualizados con éxito en todas las sedes."

        except Exception as e:
            # Si algo falla, revierte la transacción
            self.cursor.execute("ROLLBACK;")
            return f"Error al actualizar: {str(e)}"




    def close_connection(self):
        self.conn.close()

