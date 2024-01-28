from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime
from typing import List

class Training(BaseModel):
    id: Optional[int] = None
    creator_id: int
    name: str
    topic: str
    material_url: Optional[HttpUrl] = None
    scheduled_time: datetime
    created_at: Optional[datetime] = None
    status: Optional[str] = 'Scheduled'
    location: Optional[str] = None

class TrainingAttendee(BaseModel):
    training_id: int
    attendee_id: int
    assigned: Optional[bool] = False
    attendance_time: Optional[datetime] = None

class AssignedAttendee(BaseModel):
    training_id: int
    attendee_id: int
    assigned_time: Optional[datetime] = None



class TrainingAttendeeList(BaseModel):
    attendees: List[TrainingAttendee]