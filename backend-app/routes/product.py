from fastapi import APIRouter, HTTPException
from models.product import Product
from schema.product import ProductSchemaPost

product_router = APIRouter()

@product_router.get("/products")
def get_products():
    product_instance = Product()
    products = product_instance.select_all_products()
    product_instance.close_connection()
    return products

@product_router.post("/products")
def create_product(product: ProductSchemaPost):
    product_instance = Product()
    product_id = product_instance.insert_product(product)
    created_product = product_instance.select_product_by_id(product_id)
    product_instance.close_connection()
    return {"product_id": created_product[0]}

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
