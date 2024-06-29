from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date


class Contest(BaseModel):
    id: Optional[int] = None
    name:str
    type_id:int
    start_date:date
    end_date:date
    evidence_type_id:int


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


    