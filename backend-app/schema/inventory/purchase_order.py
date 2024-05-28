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



class PurchaseOrderAdjust(BaseModel):
    order_purchase_entry_id:int
    quantity_adjusted:float

class PurchaseOrderStatus(BaseModel):
    id:Optional[int] = None
    purchase_order_id:int
    lap_id:int
    responsible_id:int
    receiver_id:Optional[int] = None
    ajusts:list[PurchaseOrderAdjust]
    order_purchase_notes:Optional[str] = ''



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




