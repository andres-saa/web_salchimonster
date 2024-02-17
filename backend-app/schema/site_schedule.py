from pydantic import BaseModel
from typing import Optional

class site_schedule_schema(BaseModel):
    schedule_id: Optional[int] = None
    site_id: int
    day_of_week:int
    opening_time: str
    closing_time: str

