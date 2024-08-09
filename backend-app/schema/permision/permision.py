from pydantic import BaseModel





class RolPost (BaseModel):
    name:str
    created_by:int

class Rol (RolPost):
    id:int


