from pydantic import BaseModel
from typing import Optional

class user_schema_post(BaseModel):
    # id:Optional[int]
    user_name:str
    user_phone:str
    user_address:str
    site_id:Optional[int] = None
    


class user_schema(user_schema_post):

    user_id:int

