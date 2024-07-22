from typing import Optional
from pydantic import BaseModel
from datetime import datetime



class SequenceVideo(BaseModel):
    id:Optional[int] = None
    name:str
    exist:bool
    index:int
    created_at:datetime
    created_by:int
    sesion_id:int


class SequenceVideoPost(BaseModel):
    name:str
    created_by:int
    sesion_id:int
    description:str


class SequenceVideoUpdate(BaseModel):
    name:str
    description:str
