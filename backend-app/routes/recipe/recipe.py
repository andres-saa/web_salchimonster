from fastapi import APIRouter
from models.recipes.recipes import Recipe # Asume que tienes un módulo models con RecipeManager
# from schema.recipes.re import Recipe  # Asume que tienes un módulo schema con Recipe
from schema.recipes.recipe_data_seet import RecipeDataSheet,RecipeDataSheetPost,RecipeDataSheetUpdate
from schema.recipes.ingredients import IngredientsPost,IngredientsUpdate
from schema.recipes.ingredients import RecipeDataIngredients
recipe_router = APIRouter()
from pydantic import BaseModel
from models.recipes.ingredients import Ingredient


@recipe_router.get("/list-recipes" , tags=['recipe'])
def get_all_recipes():
    recipe_instance = Recipe()
    result = recipe_instance.get_all_recipes()
    return result



@recipe_router.get("/list-recipes-enabled" , tags=['recipe'])
def get_all_recipes():
    recipe_instance = Recipe()
    result = recipe_instance.get_all_recipes_enabled()
    return result



@recipe_router.get("/list-ingredients" , tags=['recipe'])
def get_all_recipes():

   

    recipe_instance = Ingredient()
    result = recipe_instance.get_all_ingredients()
    return result





class update (BaseModel):
    status:bool

@recipe_router.put("/toggle_product_to_recipe/{id}" , tags=['recipe'])
def get_all_recipes(id:int, data:update):
    recipe_instance = Recipe()
    result = recipe_instance.toggle_product_to_recipe(status=data.status, id=id)
    return result


@recipe_router.get("/list-recipe-by-product-id/{product_id}" , tags=['recipe'])
def get_all_recipes(product_id:int):
    recipe_instance = Recipe()
    result = recipe_instance.get_recipe_data_sheet_by_product_id(product_id)
    return result

@recipe_router.get("/get-recipe-summary-benefit" , tags=['recipe'])
def get_all_recipes():
    recipe_instance = Recipe()
    result = recipe_instance.get_all_get_summary_benefit()
    return result


@recipe_router.post("/create-recipe-data-sheet" , tags=['recipe'])
def get_all_recipes(data:RecipeDataSheetPost):
    recipe_instance = Recipe()
    result = recipe_instance.create_recipe_data_sheet(data)
    return result


@recipe_router.post("/create-recipe-data-ingredient" , tags=['recipe'])
def get_all_recipes(data:RecipeDataIngredients):
    recipe_instance = Recipe()
    result = recipe_instance.create_recipe_data_ingredient(data)
    return result


@recipe_router.delete("/delete-recipe-data-ingredient/{id}" , tags=['recipe'])
def get_all_recipes(id:int):
    recipe_instance = Recipe()
    result = recipe_instance.delete_recipe_data_ingredient(id)
    return result

@recipe_router.put("/update-recipe-data-ingredient/{id}" , tags=['recipe'])
def get_all_recipes(id:int,data:RecipeDataIngredients):
    recipe_instance = Recipe()
    result = recipe_instance.update_recipe_data_ingredient(id,data)
    return result

@recipe_router.post("/create-ingredient" , tags=['recipe'])
def get_all_recipes(data:IngredientsPost):
    recipe_instance = Ingredient()
    result = recipe_instance.create_ingredient(data)
    return result


@recipe_router.post("/update-ingredient/{id}" , tags=['recipe'])
def get_all_recipes(data:IngredientsUpdate,id:int):
    recipe_instance = Ingredient()
    result = recipe_instance.update_ingredient(id,data)
    return result


@recipe_router.delete("/delete-ingredient/{id}" , tags=['recipe'])
def get_all_recipes(id:int):
    recipe_instance = Ingredient()
    result = recipe_instance.delete_ingredient(id)
    return result


@recipe_router.put("/update-recipe-data-sheet/{id}" , tags=['recipe'])
def get_all_recipes(id:int,data:RecipeDataSheetUpdate):
    recipe_instance = Recipe()
    result = recipe_instance.update_recipe_data_sheet(id,data)
    return result






# @recipe_router.get("/recipe/{recipe_id}" , tags=['recipe'])
# def get_recipe(recipe_id: int):
#     manager = RecipeManager()
#     recipe = manager.get_recipe_by_id(recipe_id)
#     manager.close_connection()
#     return recipe

# @recipe_router.put("/recipe/{recipe_id}" , tags=['recipe'])
# def update_recipe(recipe_id: int, updated_recipe: Recipe):
#     manager = RecipeManager()
#     manager.update_recipe(recipe_id, updated_recipe)
#     manager.close_connection()
#     return {"message": "Recipe updated" }

# @recipe_router.delete("/recipe/{recipe_id}" , tags=['recipe'])
# def delete_recipe(recipe_id: int):
#     manager = RecipeManager()
#     manager.delete_recipe(recipe_id)
#     manager.close_connection()
#     return {"message": "Recipe deleted"}

# @recipe_router.get("/recipes" , tags=['recipe'])
# def list_recipes():
#     manager = RecipeManager()
#     recipes = manager.list_recipes()
#     manager.close_connection()
#     return recipes


# @recipe_router.get("/unit-of-measures" , tags=['recipe'])
# def list_measures():
#     manager = RecipeManager()
#     measures = manager.list_unit_measures()
#     manager.close_connection()
#     return measures
