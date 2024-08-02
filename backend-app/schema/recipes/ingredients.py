from pydantic import BaseModel
from typing import Optional
from datetime import time, datetime







class IngredientsPost (BaseModel):
    name:str
    purchasing_unit_measure_id:int
    purchasing_price:int
    number_units_purchasing:Optional[int] = None
    purchasing_format_id:Optional[int] = None
    net_gross_weight:float
    shrinkage_persent:Optional[float] = None
   
       

class Ingredients (IngredientsPost):
    id:Optional[int] = None
    exist: bool
    created_at:datetime


class RecipeDataIngredients (IngredientsPost):
    id:Optional[int]
    ingredient_id:int
    recipe_data_sheet_id:int
    unit_measure_id:int
    quantity:int

class RecipeDataIngredientsUpdate (IngredientsPost):
    unit_measure_id:int
    quantity:int



