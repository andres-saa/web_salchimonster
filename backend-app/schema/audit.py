from datetime import date
from pydantic import BaseModel, Field
from typing import Optional,List


class Audit(BaseModel):
    # id: Optional[int] = None
    site_id: int
    coordinator_id: int
    audit_date: date
    checklist_id: int
    
    
    



class AuditItemWng(BaseModel):
    audit_id: int
    check_item_id: int
    status: bool
    comments: Optional[str] = ''
    
class CheckGroup(BaseModel):
    name: str
    checklist_id:int
    

class CheckItem(BaseModel):
    description: str 
    group_id:Optional[int] = None



class CheckGroupList(BaseModel):
    name: str
    items:List[CheckItem]
    

class Warning(BaseModel):
    warning_text: str
    resolved: bool 
    date: date



class Checklist(BaseModel):
    name: str
    
    
    
class ChecklistWithGroups(BaseModel):
    name: str
    groups: List[CheckGroupList]
    
    
    
    
class AuditItem(BaseModel):
    check_item_id: int
    status: bool
    comments: Optional[str] = ''

class AuditItemWithWarning(BaseModel):
    audit_item: AuditItem
    warning: Optional[Warning]