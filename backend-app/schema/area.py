from pydantic import BaseModel
from typing import List, Optional

class NeighborhoodSchema(BaseModel):
    name: str
    delivery_price: float

class AreaSchemaPost(BaseModel):
    name: str
    city_id: int  # Campo añadido
    site_id: int
    wsp: Optional[str]
    neighborhoods: List[NeighborhoodSchema]

class AreaSchemaGet(AreaSchemaPost):
    area_id: int
