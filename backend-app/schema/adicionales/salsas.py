from pydantic import BaseModel, constr
from decimal import Decimal
from typing import List, Optional


class SalsaSchemaPost(BaseModel):
    name: constr(max_length=255)
    price: Decimal