from typing import List, Optional
from pydantic import BaseModel
from datetime import time, date

class WorkShift(BaseModel):
    id: Optional[int] = None
    start_time: time
    end_time: time
    description: Optional[str] = None

class WorkRecord(BaseModel):
    id: Optional[int] = None
    employer_id: int
    shift_id: Optional[int] = None  # Referencia al ID de WorkShift
    start_time: time
    end_time: time
    comments: Optional[str] = None
    work_day_id: int

class WorkDay(BaseModel):
    date: date  # The specific date for the workday.
    records: List[WorkRecord] = []  # A list of work records associated with the workday.
    site_id: int  # The identifier linking to the site.