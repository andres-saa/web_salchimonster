from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class SupplySchema(BaseModel):
    supply_id: Optional[int] = None
    name: str
    description: Optional[str] = None  # Permite valores nulos para descripción

class SupplyDeliverySchema(BaseModel):
    delivery_id: Optional[int] = None
    delivery_date: date
    user_delivery_id: int
    user_receive_id: int

class SupplyDeliveryItemSchema(BaseModel):
    item_id: Optional[int] = None
    name: str
    quantity: int
    delivery_id: Optional[int] = None  # Clave foránea que relaciona con SupplyDelivery


class SupplyDeliveryWithItemsSchema(BaseModel):
    delivery_data: SupplyDeliverySchema  # Este esquema ahora no incluye user_receive_id
    items_data: List[SupplyDeliveryItemSchema]
    user_receive_ids: List[int]