from pydantic import BaseModel

class delivery_person_schema(BaseModel):
    delivery_person_name: str
    delivery_person_phone: str