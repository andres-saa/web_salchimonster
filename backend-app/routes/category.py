from fastapi import APIRouter, HTTPException
from models.category import Category  # Asegúrate de que este importe refleje la ubicación real del módulo de modelo de categoría
from schema.category import CategorySchemaPost  # Asegúrate de que este importe refleje la ubicación real del esquema de categoría

category_router = APIRouter()

@category_router.get("/categories/{site_id}/{restaurant_id}")
def get_categories(site_id:int,restaurant_id:int):
    category_instance = Category()
    categories = category_instance.select_all_categories(site_id,restaurant_id)
    category_instance.close_connection()
    return categories



@category_router.get("/categories_main/{site_id}/{restaurant_id}")
def get_categories(site_id:int,restaurant_id:int):
    category_instance = Category()
    categories = category_instance.select_main_categories(site_id,restaurant_id)
    category_instance.close_connection()
    return categories


@category_router.get("/categories/{site_id}/all/{restaurant_id}")
def get_categories(site_id:int,restaurant_id:int):
    category_instance = Category()
    categories = category_instance.select_all_categories_all(site_id,restaurant_id)
    category_instance.close_connection()
    return categories


@category_router.get("/categories-add-product/{restaurant_id}")
def get_categories(restaurant_id:int):
    category_instance = Category()
    categories = category_instance.select_all_categories_all_add_product(restaurant_id)
    category_instance.close_connection()
    return categories

# @category_router.get("/site/{site_id}/active-categories")
# def get_active_categories_by_site(site_id: int):
#     category_instance = Category()
#     try:
#         active_categories = category_instance.select_all_categories(site_id=)
#     finally:
#         category_instance.close_connection()
#     return active_categories


# @category_router.post("/categories")
# def create_category(category: CategorySchemaPost):
#     category_instance = Category()
#     category_id = category_instance.insert_category(category)
#     created_category = category_instance.select_category_by_id(category_id)
#     category_instance.close_connection()
#     return {"category_id": created_category[0]}

# @category_router.put("/categories/{category_id}")
# def update_category(category_id: int, category: CategorySchemaPost):
#     category_instance = Category()
#     existing_category = category_instance.select_category_by_id(category_id)
#     if existing_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
    
#     category_instance.update_category(category_id, category)
#     updated_category = category_instance.select_category_by_id(category_id)
#     category_instance.close_connection()
#     return {"message": "Category updated successfully", "category_id": category_id}

# @category_router.delete("/categories/{category_id}")
# def delete_category(category_id: int):
#     category_instance = Category()
#     existing_category = category_instance.select_category_by_id(category_id)
#     if existing_category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
    
#     category_instance.delete_category(category_id)
#     category_instance.close_connection()
#     return {"message": "Category deleted successfully", "deleted_category": existing_category}

# # Otras rutas según sea necesario
