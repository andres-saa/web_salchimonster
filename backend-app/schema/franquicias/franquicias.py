from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Franquicias(BaseModel):
    name: str
    phone: str
    email: str
    reason: str
    investment_capacity: str
    zone_of_interest: str
    city: str
    is_in_gastronomic_sector: bool
    will_participate_in_operation: bool
    source_of_income: str
    status:str
