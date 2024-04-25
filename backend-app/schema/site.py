from pydantic import BaseModel
from typing import Optional


class site_schema_post(BaseModel):
    site_name: str
    site_address: str
    site_phone: str
    site_business_hours: Optional[str] = ''
    horario_semanal: Optional[dict] =[]  
    wsp_link: Optional[str] = ''
    city_id: Optional[int] = None
    maps: Optional[str] = ''
    show_on_web:  Optional[bool] = False
    email_address:Optional[str] = ''