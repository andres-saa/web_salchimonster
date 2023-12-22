from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal

class order_schema_post(BaseModel):
    order_products: List[dict]
    user_id: int
    site_id: int
    order_status: dict
    payment_method: str
    delivery_person_id: int
    status_history: List[dict]
    delivery_price: Decimal
    order_notes:str
    user_data: dict