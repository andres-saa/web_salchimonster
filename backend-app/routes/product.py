from fastapi import APIRouter, HTTPException,Body
from models.product import Product
from schema.product import ProductSchemaPost
from schema.product import Product as Product_schema
from typing import List
from pydantic import BaseModel


product_router = APIRouter()

@product_router.get("/products")
def get_products():
    product_instance = Product()
    products = product_instance.select_all_products()
    product_instance.close_connection()
    return products

@product_router.post("/products")
def create_product(product: Product_schema):
    product_instance = Product()
    product_id = product_instance.insert_product(product)
    created_product = product_instance.select_product_by_id(product_id)
    product_instance.close_connection()
    return {"product_id": product_id}



@product_router.put("/deactivate-product/{product_id}")
def deactivate_product(product_id:int):
    product_instance = Product()
    product_id = product_instance.deactivate_product(product_id)
    return {"product_id": product_id}



@product_router.get("/products-active/category-id/{category_id}/site/{site_id}/{restaurant_id}")
def get_products_by_category_name_and_site(category_id: str, site_id: int, restaurant_id):
    product_instance = Product()
    try:
        products = product_instance.select_products_by_site_and_category_active(site_id,category_id,restaurant_id)
        if not products:
            raise HTTPException(status_code=404, detail="No products found for the given category name and site")
        return products
    finally:
        product_instance.close_connection()



class aditionals(BaseModel):
    ids:list[int]


@product_router.put("/products/update/{product_instance_id}")
def update_product_and_instances(product_instance_id: int, product: ProductSchemaPost, additional_item_ids:list[int]):
    product_instance = Product()
    try:
        existing_product = product_instance.select_product_by_id(product_instance_id)
        if existing_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        
        # print(existing_product)

        # Convertir el esquema de entrada en un diccionario o manejarlo directamente si el método acepta un objeto del esquema
        product_info = {
            
            "product_instance_id": product.product_id,
            "product_id":existing_product[0]['product_id'],
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "category_id": product.category_id,
            "status": True
        }
        
        
        print(product_info)

        # Llama al método de actualización que maneja tanto el producto como sus instancias y adicionales
        update_result = product_instance.update_product_and_its_instances(product_info, additional_item_ids)
        return {"message": update_result}

    finally:
        product_instance.close_connection()


@product_router.get("/products-all/category-id/{category_id}/site/{site_id}/{restaurant_id}")
def get_products_by_category_name_and_site(category_id: str, site_id: int,restaurant_id:int):
    product_instance = Product()
    try:
        products = product_instance.select_products_by_site_and_category_all(site_id,category_id,restaurant_id)
        if not products:
            raise HTTPException(status_code=404, detail="No products found for the given category name and site")
        return products
    finally:
        product_instance.close_connection()


@product_router.get("/products/category/{category_id}")
def get_products_by_category(category_id: int):
    product_instance = Product()
    try:
        products = product_instance.select_products_by_category(category_id)
        if not products:
            raise HTTPException(status_code=404, detail="No products found for the given category")
        return products
    finally:
        product_instance.close_connection()


@product_router.get("/products/category/name/{category_name}")
def get_products_by_category_name(category_name: str):
    product_instance = Product()
    try:
        products = product_instance.select_products_by_category_name(category_name)
        if not products:
            raise HTTPException(status_code=404, detail="No products found for the given category name")
        return products
    finally:
        product_instance.close_connection()




@product_router.put("/products/{product_id}")
def update_product(product_id: int, product: ProductSchemaPost):
    product_instance = Product()
    existing_product = product_instance.select_product_by_id(product_id)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_instance.update_product(product_id, product)
    updated_product = product_instance.select_product_by_id(product_id)
    product_instance.close_connection()
    return {"message": "Product updated successfully", "product_id": product_id}




@product_router.get("/product/{product_id}")
def update_product(product_id: int):
    product_instance = Product()

    product = product_instance.select_product_by_id(product_id)
    product_instance.close_connection()
    return product








@product_router.get("/products/name/{product_name}/sites")
def get_sites_by_product_name(product_name: str):
    product_instance = Product()
    try:
        sites = product_instance.select_sites_by_product_name(product_name)
        if not sites:
            raise HTTPException(status_code=404, detail="No sites found for the given product name")
        return sites
    finally:
        product_instance.close_connection()

@product_router.get("/products/name/{name}")
def get_products_by_name(name: str):
    product_instance = Product()
    try:
        products = product_instance.select_products_by_name(name)
        if not products:
            raise HTTPException(status_code=404, detail="No products found with given name")
        return products
    finally:
        product_instance.close_connection()

@product_router.delete("/products/{product_id}")
def delete_product(product_id: int):
    product_instance = Product()
    existing_product = product_instance.select_product_by_id(product_id)
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_instance.delete_product(product_id)
    product_instance.close_connection()
    return {"message": "Product deleted successfully", "deleted_product": existing_product}

# Otras rutas según sea necesario
