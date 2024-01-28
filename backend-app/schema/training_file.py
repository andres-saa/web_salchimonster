from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class TrainingFile(BaseModel):
    # id: Optional[int]  # Opcional para casos de creación donde aún no se asigna el ID
    training_id: int
    file_name: str
    file_url: str
    file_type: Optional[str] = None
    upload_date: Optional[datetime] = None


