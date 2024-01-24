
from typing import Optional
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv
import os

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

    def insert_product(self, product_data: ProductSchemaPost):
        insert_query = """
        INSERT INTO products (
            name, price, description, category_id, porcion, state, 
            grupo_salsa_id, grupo_topping_id, grupo_acompanante_id, 
            grupo_cambio_id, grupo_adicional_id, site_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING product_id;
        """
        self.cursor.execute(insert_query, (
            product_data.name, product_data.price, product_data.description,
            product_data.category_id, product_data.porcion, product_data.state,
            product_data.grupo_salsa_id, product_data.grupo_topping_id,
            product_data.grupo_acompanante_id, product_data.grupo_cambio_id,
            product_data.grupo_adicional_id, product_data.site_id  # Incluir los nuevos campos
        ))
        product_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return product_id

    def select_all_products(self):
        select_query = "SELECT * FROM products;"
        self.cursor.execute(select_query)
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    def select_product_by_id(self, product_id):
        select_query = "SELECT * FROM products WHERE product_id = %s;"
        self.cursor.execute(select_query, (product_id,))
        return self.cursor.fetchone()

    def select_products_by_name(self, name: str):
        select_query = "SELECT * FROM products WHERE name = %s;"
        self.cursor.execute(select_query, (name,))
        columns = [desc[0] for desc in self.cursor.description]
        results = self.cursor.fetchall()
        return [dict(zip(columns, row)) for row in results] if results else []

    def select_sites_by_product_name(self, product_name: str):
        select_query = """
        SELECT p.product_id, p.site_id, s.site_name
        FROM products p
        JOIN sites s ON p.site_id = s.site_id
        WHERE p.name = %s;
        """
        self.cursor.execute(select_query, (product_name,))
        columns = ['product_id', 'site_id', 'site_name']
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def select_product_by_name(self, name: str):
        select_query = "SELECT * FROM products WHERE name = %s;"
        self.cursor.execute(select_query, (name,))
        columns = [desc[0] for desc in self.cursor.description]
        result = self.cursor.fetchone()
        if result:
            return dict(zip(columns, result))
        else:
            return None

    def update_product(self, product_id, product_data: ProductSchemaPost):
        try:
            update_query = """
            UPDATE products SET
                name = %s, price = %s, description = %s, category_id = %s,
                porcion = %s, state = %s, grupo_salsa_id = %s, grupo_topping_id = %s,
                grupo_acompanante_id = %s, grupo_cambio_id = %s,
                grupo_adicional_id = %s, site_id = %s
            WHERE product_id = %s;
            """
            self.cursor.execute(update_query, (
                product_data.name, product_data.price, product_data.description,
                product_data.category_id, product_data.porcion, product_data.state,
                product_data.grupo_salsa_id, product_data.grupo_topping_id,
                product_data.grupo_acompanante_id, product_data.grupo_cambio_id,
                product_data.grupo_adicional_id, product_data.site_id,
                product_id
            ))
            self.conn.commit()
        except psycopg2.Error as e:
            print("Error updating product:", e)
            self.conn.rollback()



    def select_products_by_category_name(self, category_name: str):
            select_query = """
            SELECT p.* FROM products p
            JOIN categories c ON p.category_id = c.category_id
            WHERE c.category_name = %s;
            """
            self.cursor.execute(select_query, (category_name,))
            columns = [desc[0] for desc in self.cursor.description]
            return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def select_products_by_category_name_and_site(self, category_name: str, site_id: int):
        select_query = """
        SELECT p.* FROM products p
        JOIN categories c ON p.category_id = c.category_id
        WHERE c.category_name = %s AND p.site_id = %s;
        """
        self.cursor.execute(select_query, (category_name, site_id))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

        

    def select_products_by_category_and_state(self, category_id: int, state: str):
        select_query = """
        SELECT * FROM products WHERE category_id = %s AND state = %s;
        """
        self.cursor.execute(select_query, (category_id, state))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]


    def select_products_by_category(self, category_id: int):
        select_query = """
        SELECT * FROM products WHERE category_id = %s;
        """
        self.cursor.execute(select_query, (category_id,))
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

 
    def delete_product(self, product_id):
        delete_query = "DELETE FROM products WHERE product_id = %s;"
        self.cursor.execute(delete_query, (product_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

