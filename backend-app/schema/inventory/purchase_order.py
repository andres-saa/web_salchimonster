from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date


class GroupPurchaseItems(BaseModel):
    id:Optional[int] = None
    name: str


class PurchaseOrder(BaseModel):
    id:Optional[int] = None
    responsible_id:int
    site_id:int

class OrderPurchaseEntry(BaseModel):
    id:Optional[int] = None
    quantity:float
    order_purchase_item_id:int
    unit_measure_id:int


class PurchaseOrderItem(BaseModel):
    id:Optional[int] = None
    order_purchase_item_group_id:int
    unit_measure_id:int
    name: str


class OrderComplete(BaseModel):
    order_purchase:PurchaseOrder
    order_purchase_items:list[OrderPurchaseEntry] 



