from pydantic import BaseModel
from typing import Optional





class Pqrs(BaseModel):
    id : Optional[int] = None
    question:str
    answer:str
    place_id:int

class Place(BaseModel):
    id: Optional[int] = None
    name:str