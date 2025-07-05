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

@user_router.get("/users-distri")
def get_products():
    user_instance = User()
    users = user_instance.select_all_users_distri   ()
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
    
    
    


@user_router.post("/insert-user-to-email/")
def create_product(user: user_schema_post):
    product_instance = User()
    user_id = product_instance.insert_user_code(user)
    # created_product = product_instance.select_product_by_id(product_id)

    # Convierte la tupla resultante en un diccionario

    product_instance.close_connection()
    return user_id






@user_router.get("/get-user-by-code/{user_code}")
def get_user_by_id(user_code: str):
    user_instance = User()
    user = user_instance.get_user_by_code(user_code)
    user_instance.close_connection()
    return user

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
import requests, io



@user_router.get(
    "/get-users-code",
    response_class=StreamingResponse,
    summary="Descarga un Excel con los códigos de usuarios"
)
def get_user_code():
    # 1. Traemos los datos de la BD
    user_instance = User()
    users = user_instance.get_users_code()
    user_instance.close_connection()

    # 2. Convertimos la lista al formato que requiere el generador de Excel
    excel_payload = {
        "hojas": [
            {
                "hoja": "Usuarios",
                "title": "Códigos de Usuarios",
                "column_widths": {          # opcional; ajusta o elimina si no lo necesitas
                    "Código": 15,
                    "Redimido": 10,
                    "Nombre": 25,
                    "Teléfono": 15,
                    "Dirección": 50,
                    "Email": 50
                },
                "data": [
                    {
                        "Código":     u["code"],
                        "Redimido":   "Sí" if u["redimido"] else "No",
                        "Nombre":     u["user_name"],
                        "Teléfono":   u["user_phone"],
                        "Dirección":  u["user_address"],
                        "Email":      u["email"],
                    }
                    for u in users
                ],
            }
        ]
    }

    # 3. Solicitamos el archivo al micro-servicio de Excel
    res = requests.post(
        "https://excel-creator.salchimonster.com/crear-excel",
        json=excel_payload,
        timeout=30,
    )

    if res.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"Error generando Excel: {res.status_code} – {res.text}",
        )

    # 4. Devolvemos el Excel como streaming
    excel_bytes = io.BytesIO(res.content)
    headers = {
        "Content-Disposition": 'attachment; filename="usuarios.xlsx"'
    }

    return StreamingResponse(
        excel_bytes,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers=headers,
    )




@user_router.get("/get-users-code-plain")
def get_user_code():
    user_instance = User()
    users = user_instance.get_users_code()
    user_instance.close_connection()
    return users




@user_router.post("/redeem-code-email/{code}/")
def create_product(code:str):
    product_instance = User()
    user_id = product_instance.redeem_code(code)
    product_instance.close_connection()
    return user_id



