from pydantic import BaseModel, constr
from decimal import Decimal
from typing import List, Optional

class GrupoCambiosSchemaPost(BaseModel):
    name: str
    cambios: Optional[List[int]] = None