from pydantic import BaseModel
from typing import Optional

class NeighborhoodSchema(BaseModel):
    neighborhood_id: Optional[int] = None
    name: str
    delivery_price: float
    site_id: int
    city_id: int


    