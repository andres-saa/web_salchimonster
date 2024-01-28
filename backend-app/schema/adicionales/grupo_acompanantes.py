from pydantic import BaseModel, constr
from decimal import Decimal
from typing import List, Optional


class GrupoAcompanantesSchemaPost(BaseModel):
    name: str
    acompanantes: Optional[List[int]] = None
