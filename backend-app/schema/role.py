from pydantic import BaseModel

class RoleSchema(BaseModel):
    title: str
    description: str = None  # Optional field with a default value of None

class RoleGroupSchema(BaseModel):
    group_name: str
    description: str = None  # Optional field with a default value of None
