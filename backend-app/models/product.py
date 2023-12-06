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
            name, price, description,
            category_id, porcion, state
        ) VALUES (%s, %s, %s, %s, %s, %s) RETURNING product_id;
        """
        self.cursor.execute(insert_query, (
            product_data.name, product_data.price, product_data.description,
            product_data.category_id, product_data.porcion, product_data.state
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

    def update_product(self, product_id, product_data: ProductSchemaPost):
        update_query = """
        UPDATE products SET
            name = %s,
            price = %s,
            description = %s,
            category_id = %s,
            porcion = %s,
            state = %s
        WHERE product_id = %s;
        """
        self.cursor.execute(update_query, (
            product_data.name, product_data.price, product_data.description,
            product_data.category_id, product_data.porcion, product_data.state,
            product_id
        ))
        self.conn.commit()
 
    def delete_product(self, product_id):
        delete_query = "DELETE FROM products WHERE product_id = %s;"
        self.cursor.execute(delete_query, (product_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

# Ejemplo de uso:
if __name__ == "__main__":
    producto_instance = Product()
    producto_instance.create_table()

    # Insertar un producto
    product_data = ProductSchemaPost(name="Producto1", price=10, description="Descripción del Producto1", porcion="Unit", category_id=1)
    product_id = producto_instance.insert_product(product_data)
    print(f"Producto insertado con ID: {product_id}")

    # Seleccionar todos los productos
    all_products = producto_instance.select_all_products()
    print("Todos los productos:")
    for product in all_products:
        print(product)

    # Seleccionar un producto por ID
    selected_product = producto_instance.select_product_by_id(product_id)
    print(f"Producto seleccionado por ID ({product_id}): {selected_product}")

    # Actualizar un producto
    updated_product_data = ProductSchemaPost(name="Producto1_actualizado", price=15, description="Nueva descripción", porcion="Kg", category_id=2)
    producto_instance.update_product(product_id, updated_product_data)
    print("Producto actualizado")

    # Seleccionar todos los productos después de la actualización
    all_products_after_update = producto_instance.select_all_products()
    print("Todos los productos después de la actualización:")
    for product in all_products_after_update:
        print(product)

    # Eliminar un producto
    producto_instance.delete_product(product_id)
    print("Producto eliminado")

    # Seleccionar todos los productos después de la eliminación
    all_products_after_delete = producto_instance.select_all_products()
    print("Todos los productos después de la eliminación:")
    for product in all_products_after_delete:
        print(product)

    # Cerrar la conexión
    producto_instance.close_connection()
