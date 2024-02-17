from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class Area(BaseModel):
    area_name: str


class DocumentType(BaseModel):
    type_name: str


class ArchivedFile(BaseModel):
    file_name: str
    file_url: str
    file_type: Optional[str] = None
    upload_date: Optional[datetime] = None
    id_area: int
    id_type: int
    file_extension:str

    