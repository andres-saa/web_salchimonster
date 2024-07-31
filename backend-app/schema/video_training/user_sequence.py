from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from typing import List



class UserSecuence(BaseModel):
    id:Optional[int] = None
    exist:bool
    index:int
    user_id:int
    sequence_id:int




class ReplaceUserSequencesInput(BaseModel):
    sequence_id: int
    users: List[int]