
from pydantic import BaseModel
from typing import Optional

class SiteDocumentSchemaPost(BaseModel):
    document_name: str
    document_type:str
    renovation_date:str
    site_id: int
    
    
class SiteFileType(BaseModel):
    type_name: str