from pydantic import BaseModel
from typing import Optional
from datetime import time, datetime






class RecipeDataSheetUpdate (BaseModel):
    portion_size:int
    portion_number:int
    preparation_time:time
    cooking_time:time
    service_temperature:int
    selling_price:int
    taxes:int
    presentation:str
    preparation_equipment:str
    elaboration:str



class RecipeDataSheetPost (RecipeDataSheetUpdate):
    product_id:int



class RecipeDataSheet (RecipeDataSheetUpdate):
    id:Optional[int] = None
    exist:bool
    created_at:datetime


class RecipeDataSheetDelete (BaseModel):
    exist:bool = False


