from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date


class GroupmonthlyInventoryItems(BaseModel):
    id:Optional[int] = None
    name: str


class monthlyInventory(BaseModel):
    id:Optional[int] = None
    responsible_id: int
    site_id:int

class monthlyInventoryItem(BaseModel):
    id:Optional[int] = None
    monthly_inventory_item_id: int
    quantity:float
    monthly_inventory_unit_measure_id:int


class monthlyInventoryItems(BaseModel):
    id:Optional[int] = None
    group_monthly_inventory_item_id:int
    monthly_inventory_item_unit_measure_id:int
    name: str

class UnitMeasure (BaseModel):
    id:Optional[int] = None
    name : str

class InventoryComplete(BaseModel):
    monthly_inventory:monthlyInventory
    monthly_inventory_items:list[monthlyInventoryItem] 



