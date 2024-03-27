from pydantic import BaseModel, Field
from typing import Optional,List
from datetime import time, date

class ShiftWorkShift(BaseModel):
    id: Optional[int] = None
    start_time: time 
    end_time: time 
    description: Optional[str] = None
  



class ShiftWorkRecord(BaseModel):
    id: Optional[int] = None
    employer_id: int
    shift_id: Optional[int] = None  # Reference to WorkShift ID
    start_time: time
    end_time: time
    comments: Optional[str] = None
    work_day_id: int
    rest: bool = Field(default=False, description="Indicates if the employee is resting during this shift")

  
class ShiftWorkDay(BaseModel):
    date: date  # The specific date for the workday.
    records: List[ShiftWorkRecord] = []  # A list of work records associated with the workday.
    site_id: int  # The identifier linking to the site.
    