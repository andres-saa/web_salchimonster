from pydantic import BaseModel
from typing import Optional

class ProductSchemaPost(BaseModel):
    name: str
    price: int
    description: str
    category_id: Optional[int] = None
    porcion: int
    state: Optional[str] = None
    grupo_salsa_id: Optional[int] = None
    grupo_topping_id: Optional[int] = None
    grupo_acompanante_id: Optional[int] = None
    grupo_cambio_id: Optional[int] = None
    grupo_adicional_id: Optional[int] = None  # Nueva columna para grupo adicional
    site_id: Optional[int] = None


