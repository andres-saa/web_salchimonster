from pydantic import BaseModel
from typing import Optional
from datetime import time, datetime






class RecipeDataSheetUpdate (BaseModel):
    portion_size:int
    portion_number:int
    preparation_time:str
    cooking_time:str
    service_temperature:float
    selling_price:float
    taxes:float
    presentation:str
    preparation_equipment:str
    elaboration:str




# class updateBulkPurchasePrace(BaseModel):


class updateLastPurchasePrice(BaseModel):
    name:str
    ingredient_id:int
    last_price_purchase:float
    iva:float

class cdi_percent(BaseModel):
    percent:int

class update_cdi_percent(BaseModel):
    main:bool

class RecipeDataSheetPost (RecipeDataSheetUpdate):
    product_id:int


class RecipeDataSheet (RecipeDataSheetUpdate):
    id:Optional[int] = None
    exist:bool
    created_at:datetime


class RecipeDataSheetDelete (BaseModel):
    exist:bool = False


class CdiRecipeDataSheet (BaseModel):
    ingredient_id:Optional[int] = None
    name:str
    iva:float
    pasamanos:bool


class cdi_recipe_data_sheet_on_ingredient (BaseModel):
    unit_measure_id:int
    convert_value:float
    cdi_recipe_data_sheet_id:Optional[int] = None


class CdiRecipeDataIngredients (BaseModel):
    ingredient_id:int
    cdi_recipe_data_sheet_id:int
    unit_measure_id:int
    quantity:float

class post_cdi_recipe_data_sheet (BaseModel):
    cdi_recipe_data_sheet:CdiRecipeDataSheet
    cdi_recipe_data_sheet_on_ingredient:cdi_recipe_data_sheet_on_ingredient



class post_cdi_recipe_data_sheet_pasamanos (BaseModel):
    cdi_recipe_data_sheet:CdiRecipeDataSheet
    cdi_recipe_data_sheet_on_ingredient:cdi_recipe_data_sheet_on_ingredient
    cdi_recipe_data_Ingredient: CdiRecipeDataIngredients