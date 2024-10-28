from pydantic import BaseModel
from typing import Optional

class PQRRequest(BaseModel):
    reques_type_id: int
    content: str
    channel_id: int
    rating:Optional[int] = None
    site_id:Optional[int] = None
    network_id:Optional[int] = None
    order_id:Optional[str] = None
    


class PQRStatus(BaseModel):
    name: str
    description: str


class StatusHistory(BaseModel):
    status_id: int
    timestamp: str  # Use the appropriate type based on your application's date handling
    pqr_request_id: int
    responsible_id: int
    notes: str = None
    value: int = None


class PQRRequestType(BaseModel):
    name: str


class PQRFeedback(BaseModel):
    content: str
    pqr_id: int
    rating: int
    timestamp: str  # Adjust the type according to how you handle dates


class PQRChannel(BaseModel):
    name: str
    description: str = None

