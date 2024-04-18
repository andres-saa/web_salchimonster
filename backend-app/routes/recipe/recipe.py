from fastapi import APIRouter
from models.recipe.recipe import RecipeManager , Recipe  # Asume que tienes un módulo models con RecipeManager
from schema.recipe import Recipe  # Asume que tienes un módulo schema con Recipe

recipe_router = APIRouter()

@recipe_router.post("/recipe" , tags=['recipe'])
def create_recipe(recipe: Recipe):
    manager = RecipeManager()
    recipe_id = manager.create_recipe(recipe)
    manager.close_connection()
    return {"recipe_id": recipe_id}

@recipe_router.get("/recipe/{recipe_id}" , tags=['recipe'])
def get_recipe(recipe_id: int):
    manager = RecipeManager()
    recipe = manager.get_recipe_by_id(recipe_id)
    manager.close_connection()
    return recipe

@recipe_router.put("/recipe/{recipe_id}" , tags=['recipe'])
def update_recipe(recipe_id: int, updated_recipe: Recipe):
    manager = RecipeManager()
    manager.update_recipe(recipe_id, updated_recipe)
    manager.close_connection()
    return {"message": "Recipe updated" }

@recipe_router.delete("/recipe/{recipe_id}" , tags=['recipe'])
def delete_recipe(recipe_id: int):
    manager = RecipeManager()
    manager.delete_recipe(recipe_id)
    manager.close_connection()
    return {"message": "Recipe deleted"}

@recipe_router.get("/recipes" , tags=['recipe'])
def list_recipes():
    manager = RecipeManager()
    recipes = manager.list_recipes()
    manager.close_connection()
    return recipes


@recipe_router.get("/unit-of-measures" , tags=['recipe'])
def list_measures():
    manager = RecipeManager()
    measures = manager.list_unit_measures()
    manager.close_connection()
    return measures
