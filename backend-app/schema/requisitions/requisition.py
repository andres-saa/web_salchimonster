from pydantic import BaseModel
from typing import Optional

class Requisition(BaseModel):

    area_id: int
    requester_id:int
    requisition_lap_id:Optional[int] = 1 
    created_by:int
    description:str
    site_id:int


class Applicant(BaseModel):
    name:str
    email:str
    phone:str
    cv_file_id:int
    vacancy_id:int
    lap_id:Optional[int] = 1 
    
    


class Vacancy(BaseModel):
    requisition_id:int
    created_by:int
    title:str
    description:str
    image_identifier:str



class LapHistory(BaseModel):

    requisition_lap_id:int
    requisition_id:int
    responsible_id:int


class cvFile(BaseModel):
    url_file:str