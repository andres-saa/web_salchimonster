from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time
from decimal import Decimal

class Recipe(BaseModel):
    id: Optional[int] = None
    product_id: int

class RecipeDataSheet(BaseModel):
    id: Optional[int] = None
    date: date
    portion_size: int
    portion_number: int
    preparation_time: time
    cooking_time: time
    service_temperature: int
    selling_price: Decimal
    taxes: Decimal
    presentation: str
    preparation_equipment: str
    recipe_id:Optional[int] = None

class Ingredient(BaseModel):
    id: Optional[int] = None
    name: str
    unit_of_measure_id: int
    purchasing_price: Decimal
    number_units_purchasing: int
    purchasing_format: str
    net_gross_weight: int
    shrinkage_percent: int

class Allergen(BaseModel):
    id: Optional[int] = None
    name: str

class RecipeDataAllergens(BaseModel):
    id: Optional[int] = None
    recipe_data_id: int
    allergen_id: int

class RecipeDataIngredient(BaseModel):
    id: Optional[int] = None
    ingredient_id: int
    recipe_data_sheet_id: Optional[int] = None
    unit_measure_id:int
    quantity: int

class Unit_of_measures (BaseModel):
    id: Optional[int] = None
    name: str
