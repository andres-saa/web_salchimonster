from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date, datetime


class Contest(BaseModel):
    id: Optional[int] = None
    name:str
    start_date:datetime
    end_date:datetime
    description:str
    evidence_type_id:int
    instructions:str
    contest_winner_type_id:int
    is_site_participation:bool


class Contest_entry(BaseModel):
    id: Optional[int] = None
    participant_id:int
    contest_id:int



class evidence(BaseModel):
    evidence_type_id: int
    evidence_entry:str
    contest_id:int


class evidence_post(BaseModel):
    evidence:evidence
    Contest_entry:Contest_entry


    