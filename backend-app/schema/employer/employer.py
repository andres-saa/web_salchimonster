from pydantic import BaseModel, Field
from typing import Optional, List

class EmployerSchemaPost(BaseModel):
    name: str
    dni: str
    address: str
    position: str
    site_id: int
    status: str
    gender: str
    birth_date: str
    password: str
    phone: str
    email:Optional[str] 
    entry_date: str
    exit_date: Optional[str]
    exit_reason: Optional[str]
    comments_notes: str
    authorization_data: Optional[bool]
    birth_country: Optional[str]
    birth_department: Optional[str]
    birth_city: Optional[str]
    blood_type: Optional[str]
    marital_status: Optional[str]
    education_level: Optional[str]
    contract_type: Optional[str]
    eps: Optional[str]
    pension_fund: Optional[str]
    severance_fund: Optional[str]
    has_children: Optional[bool]
    housing_type: Optional[str]
    has_vehicle: Optional[bool]
    vehicle_type: Optional[str]
    household_size: Optional[int]
    emergency_contact: Optional[str]
    shirt_size: Optional[str]
    jeans_sweater_size: Optional[str]
    food_handling_certificate: Optional[bool]
    food_handling_certificate_number: Optional[int] = None
    salary: Optional[int] = None
    boss_id: Optional[int]  # Nuevo campo boss_id

