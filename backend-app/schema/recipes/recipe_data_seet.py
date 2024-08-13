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


