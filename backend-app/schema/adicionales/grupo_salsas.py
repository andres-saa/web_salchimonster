from pydantic import BaseModel, constr
from decimal import Decimal
from typing import List, Optional


class GrupoSalsasSchemaPost(BaseModel):
    name: str
    salsas: Optional[List[int]] = None