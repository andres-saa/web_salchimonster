from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date


class GroupCdiInventoryItems(BaseModel):
    id:Optional[int] = None
    name: str


class CdiInventory(BaseModel):
    id:Optional[int] = None
    responsible_id: int
    site_id:int

class CdiInventoryItem(BaseModel):
    id:Optional[int] = None
    cdi_inventory_item_id: int
    quantity:float
    cdi_inventory_unit_measure_id:int


class CdiInventoryItems(BaseModel):
    id:Optional[int] = None
    group_cdi_inventory_item_id:int
    cdi_inventory_item_unit_measure_id:int
    name: str

class UnitMeasure (BaseModel):
    id:Optional[int] = None
    name : str

class InventoryComplete(BaseModel):
    cdi_inventory:CdiInventory
    cdi_inventory_items:list[CdiInventoryItem] 



