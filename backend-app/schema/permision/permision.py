from pydantic import BaseModel
from typing import Optional





class RolPost (BaseModel):
    name:str
    created_by:int

class Rol (RolPost):
    id:int




class toggle_permision(BaseModel):
    rol_id:int
    permission_id:int

