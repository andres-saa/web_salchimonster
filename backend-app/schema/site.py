from pydantic import BaseModel

class site_schema_post(BaseModel):
    site_name: str
    site_address: str
    site_phone: str
    site_business_hours: str

