from pydantic import BaseModel
from typing import Optional
from datetime import time, datetime






class PurchasingFormat (BaseModel):
    id:Optional[int] = None
    name:str
    exist:bool
    created_at:datetime
