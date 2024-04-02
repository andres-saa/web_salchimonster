from fastapi import APIRouter, HTTPException, Body
from schema.recipe import RecipeDataSheet  # Asegúrate de que la importación de tu esquema esté correcta
from models.recipe.data_sheet import RecipeDataSheetManager  # Reemplaza 'your_module' con el nombre real de tu módulo
from models.recipe.data_sheet import RecipeDataSheet
recipe_data_sheet_router = APIRouter()
from pydantic import BaseModel
from typing import List
from schema.recipe import RecipeDataSheet, RecipeDataIngredient



manager = RecipeDataSheetManager()

class RecipeDataSheetWithDetails(BaseModel):
    data_sheet: RecipeDataSheet
    ingredient_details: List[RecipeDataIngredient]



@recipe_data_sheet_router.post("/recipe_data_sheet/", tags=['recipe'])
def create_recipe(data: RecipeDataSheetWithDetails = Body(...)):
    result = manager.create_recipe_data_sheet(data.data_sheet, data.ingredient_details)
    if isinstance(result, str):
        raise HTTPException(status_code=500, detail=result)
    return {"id": result, "message": "Data sheet created successfully"}
  
@recipe_data_sheet_router.get("/recipe_data_sheet/{sheet_id}/", tags=['recipe'] )
def get_recipe(sheet_id: int):
    result = manager.get_recipe_data_sheet_by_id(sheet_id)
    if not result:
        raise HTTPException(status_code=404, detail="Data sheet not found")
    return result

@recipe_data_sheet_router.put("/recipe_data_sheet/{sheet_id}/", tags=['recipe'])
def update_recipe(sheet_id: int, data_sheet: RecipeDataSheet = Body(...)):
    result = manager.update_recipe_data_sheet(sheet_id, data_sheet)
    if isinstance(result, str):
        raise HTTPException(status_code=500, detail=result)
    return {"message": "Data sheet updated successfully"}

@recipe_data_sheet_router.delete("/recipe_data_sheet/{sheet_id}/", tags=['recipe'])
def delete_recipe(sheet_id: int):
    result = manager.delete_recipe_data_sheet(sheet_id)
    if isinstance(result, str):
        raise HTTPException(status_code=500, detail=result)
    return {"message": "Data sheet deleted successfully"}

@recipe_data_sheet_router.get("/recipe_data_sheet/", tags=['recipe'])
def list_recipes():
    result = manager.list_recipe_data_sheets()
    if isinstance(result, str):
        raise HTTPException(status_code=500, detail=result)
    return result