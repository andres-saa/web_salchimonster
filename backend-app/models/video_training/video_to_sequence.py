from typing import Optional
from pydantic import BaseModel
from datetime import datetime



class Sesion(BaseModel):
    id:Optional[int] = None
    video_id:int
    sequence_id:int
    exist:bool
    index:int
    sesion_id: int
    created_at:datetime
    created_by:int