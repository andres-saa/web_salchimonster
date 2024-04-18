from fastapi import APIRouter, HTTPException, Body
from schema.recipe import RecipeDataSheet, RecipeDataIngredient
from models.recipe.data_sheet import RecipeDataSheetManager
from pydantic import BaseModel
from typing import List

recipe_data_sheet_router = APIRouter()

class RecipeDataSheetWithDetails(BaseModel):
    data_sheet: RecipeDataSheet
    ingredient_details: List[RecipeDataIngredient]

@recipe_data_sheet_router.post("/recipe_data_sheet/", tags=['recipe'])
def create_recipe(data: RecipeDataSheetWithDetails = Body(...)):
    manager = RecipeDataSheetManager()
    result = manager.create_recipe_data_sheet(data.data_sheet, data.ingredient_details)
    if isinstance(result, str):
        manager.close_connection()
        raise HTTPException(status_code=500, detail=result)
    manager.close_connection()
    return {"id": result, "message": "Data sheet created successfully"}
  
@recipe_data_sheet_router.get("/recipe_data_sheet/{recipe_id}/", tags=['recipe'])
def get_recipe(recipe_id: int):
    manager = RecipeDataSheetManager()
    result = manager.get_recipe_data_sheet_by_id(recipe_id)
    if not result:
        manager.close_connection()
        raise HTTPException(status_code=404, detail="Data sheet not found")
    manager.close_connection()
    return result

@recipe_data_sheet_router.put("/recipe_data_sheet/{sheet_id}/", tags=['recipe'])
def update_recipe(sheet_id: int, data_sheet: RecipeDataSheet = Body(...)):
    manager = RecipeDataSheetManager()
    result = manager.update_recipe_data_sheet(sheet_id, data_sheet)
    if isinstance(result, str):
        manager.close_connection()
        raise HTTPException(status_code=500, detail=result)
    manager.close_connection()
    return {"message": "Data sheet updated successfully"}

@recipe_data_sheet_router.delete("/recipe_data_sheet/{sheet_id}/", tags=['recipe'])
def delete_recipe(sheet_id: int):
    manager = RecipeDataSheetManager()
    result = manager.delete_recipe_data_sheet(sheet_id)
    if isinstance(result, str):
        manager.close_connection()
        raise HTTPException(status_code=500, detail=result)
    manager.close_connection()
    return {"message": "Data sheet deleted successfully"}

@recipe_data_sheet_router.get("/recipe_data_sheet/", tags=['recipe'])
def list_recipes():
    manager = RecipeDataSheetManager()
    result = manager.list_recipe_data_sheets()
    if isinstance(result, str):
        manager.close_connection()
        raise HTTPException(status_code=500, detail=result)
    manager.close_connection()
    return result

@recipe_data_sheet_router.post("/recipe_data_ingredient/", tags=['recipe'])
def create_recipe_data_ingredient(ingredient_detail: RecipeDataIngredient = Body(...)):
    manager = RecipeDataSheetManager()
    result = manager.create_recipe_data_ingredient(ingredient_detail.recipe_data_sheet_id, ingredient_detail)
    if isinstance(result, str):
        manager.close_connection()
        raise HTTPException(status_code=500, detail=result)
    manager.close_connection()
    return {"message": "Ingredient detail created successfully"}

@recipe_data_sheet_router.delete("/recipe_data_ingredient/{ingredient_detail_id}/", tags=['recipe'])
def delete_recipe_data_ingredient(ingredient_detail_id: int):
    manager = RecipeDataSheetManager()
    result = manager.delete_recipe_data_ingredient(ingredient_detail_id)
    if isinstance(result, str):
        manager.close_connection()
        raise HTTPException(status_code=500, detail=result)
    manager.close_connection()
    return {"message": "Ingredient detail deleted successfully"}
