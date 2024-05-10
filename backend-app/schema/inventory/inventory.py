from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date


class GroupDailyInventoryItems(BaseModel):
    id:Optional[int] = None
    name: str


class DailyInventory(BaseModel):
    id:Optional[int] = None
    responsible_id: int
    site_id:int

class DailyInventoryItem(BaseModel):
    id:Optional[int] = None
    daily_inventory_item_id: int
    quantity:float
    daily_inventory_unit_measure_id:int


class DailyInventoryItems(BaseModel):
    id:Optional[int] = None
    group_daily_inventory_item_id:int
    daily_inventory_item_unit_measure_id:int
    name: str

class UnitMeasure (BaseModel):
    id:Optional[int] = None
    name : str

class InventoryComplete(BaseModel):
    daily_inventory:DailyInventory
    daily_inventory_items:list[DailyInventoryItem] 



