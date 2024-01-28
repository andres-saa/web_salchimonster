from pydantic import BaseModel, Json
from datetime import date
from typing import Optional, Any, List

class PermissionSchemaPost(BaseModel):
    employer_id: int
    start_date: date
    end_date: date
    observations: Optional[str] = None
    status: dict  # Represents a JSON field
    history: List[dict]  # History of changes as a list of JSON objects
    tipo: str  # New field  # Historial de cambios como lista de objetos JSON
