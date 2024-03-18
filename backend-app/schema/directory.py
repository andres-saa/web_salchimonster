from pydantic import BaseModel
from typing import Optional

class DirSafeBoxes(BaseModel):
    safe_box_id: Optional[int] = None
    site_id: int
    box_name: str  # Asumiendo que el nombre es obligatorio
    password: Optional[str] = None  # Asumiendo que la clave puede ser opcional


class DirCameras(BaseModel):
    camera_id: Optional[int]  = None
    site_id: int
    username: Optional[str]  = None
    password: Optional[str]  = None

class DirWifi(BaseModel):
    wifi_id: Optional[int]  = None
    site_id: int
    username: Optional[str]  = None
    password: Optional[str]  = None

class DirDataphones(BaseModel):
    dataphone_id: Optional[int]  = None
    site_id: int
    unique_code: Optional[str]  = None
    external_code: Optional[str]  = None

class DirWebPages(BaseModel):
    web_page_id: Optional[int]  = None
    site_id: int
    page: Optional[str]  = None
    username: Optional[str]  = None
    password: Optional[str]  = None

class DirApplications(BaseModel):
    application_id: Optional[int]  = None
    site_id: int
    name: Optional[str]  = None
    username: Optional[str]  = None
    password: Optional[str]  = None

class DirGeneralEmails(BaseModel):
    email_id: Optional[int]  = None
    description: Optional[str] = None
    email: Optional[str] = None
