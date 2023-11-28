from fastapi import APIRouter

# from models.category import category_model
# import json
# from sqlalchemy import select, func
# from config.db import conn
# from models.product_photo import Product_photo_model
# import sqlalchemy
from models.product import Product
from schema.product import Product_schema_post
product_router = APIRouter()



@product_router.get("/products")
def get_products():
    product_instance = Product()
    products = product_instance.select_all_products()
    product_instance.close_connection()
    return products

@product_router.post("/products")
def create_product(product: Product_schema_post):
    product_instance = Product()
    product_id = product_instance.insert_product(
        product.product_name,
        product.product_description,
        product.product_selling_price,
        product.product_purchase_price,
        product.unit_of_measure,
        product.provider_id,
        product.category_id,
    )
    created_product = product_instance.select_product_by_id(product_id)

    # Convierte la tupla resultante en un diccionario

    product_instance.close_connection()
    return {"product_id": created_product[0]}

@product_router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    product_instance = Product()
    product_instance.delete_product(product_id)
    product_instance.close_connection()
    return {"message": "Product deleted successfully"}