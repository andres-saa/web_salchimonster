from pydantic import BaseModel, constr
from decimal import Decimal
from typing import List, Optional

class GrupoToppingsSchemaPost(BaseModel):
    name: str
    toppings: Optional[List[int]] = None
