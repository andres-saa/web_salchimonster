from pydantic import BaseModel
from typing import Optional
from datetime import time, datetime







class IngredientsPost (BaseModel):
    name:str
    purchasing_unit_measure_id:int
    purchasing_price:float
    number_units_purchasing:Optional[float] = None
    purchasing_format_id:Optional[int] = None
    net_gross_weight:float
    shrinkage_persent:Optional[float] = None
    iva:Optional[float] = None



class cdi_price (BaseModel):
    ingredient_id:int
    last_price_purchase : float
    iva: float
   

class IngredientsUpdate (BaseModel):
    name:str
    purchasing_unit_measure_id:int
    purchasing_price:float
    net_gross_weight:float

   

 

class Ingredients (IngredientsPost):
    id:Optional[int] = None
    exist: bool
    created_at:datetime


class RecipeDataIngredients (BaseModel):
    ingredient_id:int
    recipe_data_sheet_id:int
    unit_measure_id:int
    quantity:float
    quantity_before_shrinkage:float

class RecipeDataIngredientsUpdate (IngredientsPost):
    unit_measure_id:int
    quantity:float



class CdiRecipeDataIngredients (BaseModel):
    ingredient_id:int
    cdi_recipe_data_sheet_id:int
    unit_measure_id:int
    quantity:float



class newRecipeDataIngredients (BaseModel):
    recipe_data_sheet_id:int
    cdi_recipe_data_sheet_id:int
    unit_measure_id:int
    quantity:float
    quantity_before_shrinkage:float



