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


@product_router.get("/products/category/name/{category_name}/site/{site_id}")
def get_products_by_category_name_and_site(category_name: str, site_id: int):
    product_instance = Product()
    try:
        products = product_instance.select_products_by_category_name_and_site(category_name, site_id)
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
