from pydantic import BaseModel, constr
from decimal import Decimal

class adicionalSchemaPost(BaseModel):

    name: constr(max_length=255)
    price: Decimal



