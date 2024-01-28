from fastapi import APIRouter

# from models.category import category_model
# import json
# from sqlalchemy import select, func
# from config.db import conn
# from models.product_photo import Product_photo_model
# import sqlalchemy
from models.user import User
from schema.user import user_schema_post
user_router = APIRouter()



@user_router.get("/users")
def get_products():
    user_instance = User()
    users = user_instance.select_all_users()
    user_instance.close_connection()
    return users

# @product_router.post("/products")
# def create_product(product: Product_schema_post):
#     user_instance = Product()
#     product_id = user_instance.insert_product(
#         product.product_name,
#         product.product_description,
#         product.product_selling_price,
#         product.product_purchase_price,
#         product.unit_of_measure,
#         product.provider_id,
#         product.category_id,
#     )
#     created_product = user_instance.select_product_by_id(product_id)

#     # Convierte la tupla resultante en un diccionario

#     user_instance.close_connection()
#     return {"product_id": created_product[0]}

@user_router.get("/user/{user_id}",)
def get_user_by_id(user_id: int):
    user_instance = User()
    user = user_instance.select_user_by_id(user_id)
    user_instance.close_connection()
    return user


@user_router.delete("/user/{user_id}",)
def get_user_by_id(user_id: int):
    user_instance = User()
    user = user_instance.delete_user(user_id)
    user_instance.close_connection()
    return user

@user_router.post("/user")
def create_product(user: user_schema_post):
    product_instance = User()
    user_id = product_instance.insert_user(user)
    # created_product = product_instance.select_product_by_id(product_id)

    # Convierte la tupla resultante en un diccionario

    product_instance.close_connection()
    return {"user_id": user_id}

@user_router.put("/user/{user_id}")
def update_user(user_id: int, updated_user: user_schema_post):
    user_instance = User()
    updated_user_data = user_instance.update_user(user_id, updated_user)
    
    if updated_user_data:
        user_instance.close_connection()
        return updated_user_data
    else:
        user_instance.close_connection()
        return {"message": "User not found"}