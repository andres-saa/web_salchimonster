from pydantic import BaseModel, constr
from decimal import Decimal
from typing import List, Optional

class CambioSchemaPost(BaseModel):
    name: constr(max_length=255)
    price: Decimal