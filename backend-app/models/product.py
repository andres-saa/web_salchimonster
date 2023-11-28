# producto.py

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class Product:
    def __init__(self, product_id=None):
        self.conn_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}"
        self.conn = psycopg2.connect(self.conn_str)
        self.cursor = self.conn.cursor()
        self.product_id = product_id

    def create_table(self):
        create_table_script = """
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(255),
            product_description VARCHAR(255),
            product_selling_price FLOAT,
            product_purchase_price FLOAT,
            unit_of_measure VARCHAR(50),
            provider_id INTEGER REFERENCES providers(provider_id),
            category_id INTEGER REFERENCES categories(category_id)
        );
        """
        self.cursor.execute(create_table_script)
        self.conn.commit()

    def insert_product(self, product_name, product_description, product_selling_price,
                       product_purchase_price, unit_of_measure, provider_id, category_id):
        insert_query = """
        INSERT INTO products (
            product_name, product_description, product_selling_price,
            product_purchase_price, unit_of_measure, provider_id, category_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING product_id;
        """
        self.cursor.execute(insert_query, (
            product_name, product_description, product_selling_price,
            product_purchase_price, unit_of_measure, provider_id, category_id
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

    def update_product(self, product_id, new_product_name, new_product_description,
                       new_product_selling_price, new_product_purchase_price,
                       new_unit_of_measure, new_provider_id, new_category_id):
        update_query = """
        UPDATE products SET
            product_name = %s,
            product_description = %s,
            product_selling_price = %s,
            product_purchase_price = %s,
            unit_of_measure = %s,
            provider_id = %s,
            category_id = %s
        WHERE product_id = %s;
        """
        self.cursor.execute(update_query, (
            new_product_name, new_product_description,
            new_product_selling_price, new_product_purchase_price,
            new_unit_of_measure, new_provider_id, new_category_id,
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
    producto_instance = Producto()
    producto_instance.create_table()

    # Insertar un producto
    product_id = producto_instance.insert_product(
        "Producto1", "Descripción del Producto1", 10.99, 5.99, "Unit",
        1, 1
    )
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
    producto_instance.update_product(
        product_id, "Producto1_actualizado", "Nueva descripción", 15.99, 8.99, "Kg", 2, 2
    )
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
