from typing import List, Optional
from pydantic import BaseModel

class GrupoAdicionalesSchemaPost(BaseModel):
    name: str
    adicionales: Optional[List[int]] = None