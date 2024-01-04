from pydantic import BaseModel, Json
from datetime import date
from typing import Optional, Any, List

class PermissionSchemaPost(BaseModel):
    employer_id: int
    start_date: date
    end_date: date
    observations: Optional[str] = None
    status: dict  # Representa un campo JSON
    history: List[dict]  # Historial de cambios como lista de objetos JSON
