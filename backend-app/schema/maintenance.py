from typing import Optional, List
from pydantic import BaseModel
from datetime import date




class MaintenanceSite(BaseModel):
    site_id: int
    scheduled_date: date
    equipment_ids: List[int]


class Maintenance(BaseModel):
    maintenance_id: Optional[int] = None
    frequency: int
    status: str
    completed: bool
    remarks: Optional[str] = None
    sites: List[MaintenanceSite]

class Equipment(BaseModel):
    equipment_id: Optional[int] = None
    name: str
    brand: str
    site_ids: List[int]  # Suponemos que un equipo puede estar en varios sitios
