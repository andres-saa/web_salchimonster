from fastapi import APIRouter
from models.recipe.ingredient import Ingredient as ingredient_model  # Asume que tienes un módulo models con Ingredient
from schema.recipe import Ingredient  # Asume que tienes un módulo schema con Ingredient
# from db.db import engine,conn
ingredient_router = APIRouter()

@ingredient_router.post("/ingredient" , tags=['recipe'])
def create_ingredient(ingredient: Ingredient):
    manager = ingredient_model()
    ingredient_id = manager.create_ingredient(ingredient)
    manager.close_connection()
    return {"ingredient_id": ingredient_id}

@ingredient_router.get("/ingredient/{ingredient_id}" , tags=['recipe'])
def get_ingredient(ingredient_id: int):
    manager = ingredient_model()
    ingredient = manager.get_ingredient_by_id(ingredient_id)
    manager.close_connection()
    return ingredient

@ingredient_router.put("/ingredient/{ingredient_id}" , tags=['recipe'])
def update_ingredient(ingredient_id: int, updated_ingredient: Ingredient):
    manager = ingredient_model()
    manager.update_ingredient(ingredient_id, updated_ingredient)
    manager.close_connection()
    return {"message": "Ingredient updated"}

@ingredient_router.delete("/ingredient/{ingredient_id}" , tags=['recipe'])
def delete_ingredient(ingredient_id: int):
    manager = ingredient_model()
    manager.delete_ingredient(ingredient_id)
    manager.close_connection()
    return {"message": "Ingredient deleted"}

@ingredient_router.get("/ingredients" , tags=['recipe'])
def list_ingredients():
    manager = ingredient_model()
    ingredients = manager.list_ingredients()
    manager.close_connection()
    return ingredients



