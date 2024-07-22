from typing import Optional
from pydantic import BaseModel
from datetime import datetime



class Sesion(BaseModel):
    id:Optional[int] = None
    name:str
    exist:Optional[bool] = True
    index:Optional[int] = 0
    created_at:Optional[datetime] = None
    created_by:int
    description:str


class SesionUpdate(BaseModel):
    name:str
    description:str