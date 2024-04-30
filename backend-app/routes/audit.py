from fastapi import APIRouter, HTTPException
from typing import List
from models.audit import AuditDAO  # Asume que esta es tu clase DAO para Audit
from schema.audit import Audit,CheckGroup,AuditItem,CheckItem,Warning,ChecklistWithGroups,Checklist,AuditItemWithWarning# Asume que este es tu esquema Pydantic para Audit

audit_router = APIRouter()

@audit_router.post("/audits")
def create_audit(audit: Audit):
    audit_dao = AuditDAO()
    audit_id = audit_dao.insert_audit(audit)
    audit_dao.close_connection()
    return audit_id


@audit_router.delete("/checklist/{checklist_id}")
def delete_checklist(checklist_id: int):
    dao = AuditDAO()
    try:
        result = dao.delete_checklist(checklist_id)
        return {"message": f"Checklist {checklist_id} deleted successfully"}
    finally:
        dao.close_connection()

@audit_router.get("/audits")
def get_audits():
    audit_dao = AuditDAO()
    audits = audit_dao.select_all_audits()
    audit_dao.close_connection()
    return audits

@audit_router.get("/audits/{audit_id}")
def get_audit(audit_id: int):
    audit_dao = AuditDAO()
    audit = audit_dao.select_audit_by_id(audit_id)
    audit_dao.close_connection()
    if audit is None:
        raise HTTPException(status_code=404, detail="Audit not found")
    return audit

@audit_router.put("/audits/{audit_id}")
def update_audit(audit_id: int, audit: Audit):
    audit_dao = AuditDAO()
    updated_audit = audit_dao.update_audit(audit_id, audit)
    audit_dao.close_connection()
    if updated_audit is None:
        raise HTTPException(status_code=404, detail="Audit not found")
    return updated_audit

@audit_router.delete("/audits/{audit_id}")
def delete_audit(audit_id: int):
    audit_dao = AuditDAO()
    result = audit_dao.delete_audit(audit_id)
    audit_dao.close_connection()
    if not result:
        raise HTTPException(status_code=404, detail="Audit not found")
    return {"message": f"Audit {audit_id} deleted successfully"}



@audit_router.get("/checklists-with-filters/")
def get_checklists_with_filters(coordinator_id: int, date: str, site_id: int):
    dao = AuditDAO()
    try:
        checklists = dao.get_audit_check_groups_with_filtered_items(coordinator_id, date, site_id)
        if not checklists:
            raise HTTPException(status_code=404, detail="No checklists found with the specified filters")
        return checklists
    finally:
        dao.close_connection()


@audit_router.post("/audit-items")
def create_audit_item(audit_item: AuditItem):
    dao = AuditDAO()
    item_id = dao.insert_audit_item(audit_item)
    dao.close_connection()
    return item_id

@audit_router.get("/audit-items/{item_id}")
def get_audit_item(item_id: int):
    dao = AuditDAO()
    item = dao.select_audit_item_by_id(item_id)
    dao.close_connection()
    if item is None:
        raise HTTPException(status_code=404, detail="Audit item not found")
    return item


@audit_router.get("/audit-items")
def get_audit_items():
    dao = AuditDAO()
    items = dao.select_all_audit_items()  # Ensure this method exists in your DAO
    dao.close_connection()
    return items

@audit_router.put("/audit-items/{item_id}")
def update_audit_item(item_id: int, audit_item: AuditItem):
    dao = AuditDAO()
    updated_item = dao.update_audit_item(item_id, audit_item)
    dao.close_connection()
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Audit item not found")
    return updated_item

@audit_router.delete("/audit-items/{item_id}", response_model=dict)
def delete_audit_item(item_id: int):
    dao = AuditDAO()
    result = dao.delete_audit_item(item_id)
    dao.close_connection()
    if not result:
        raise HTTPException(status_code=404, detail="Audit item not found")
    return {"message": f"Audit item {item_id} deleted successfully"}





@audit_router.post("/check-groups")
def create_check_group(check_group: CheckGroup):
    dao = AuditDAO()
    group_id = dao.insert_check_group(check_group)
    dao.close_connection()
    return group_id

@audit_router.get("/check-groups/{group_id}")
def get_check_group(group_id: int):
    dao = AuditDAO()
    group = dao.select_check_group_by_id(group_id)
    dao.close_connection()
    if group is None:
        raise HTTPException(status_code=404, detail="Check group not found")
    return group

@audit_router.get("/check-groups")
def get_check_groups():
    dao = AuditDAO()
    groups = dao.select_all_check_groups()  # Ensure this method exists in your DAO
    dao.close_connection()
    return groups

@audit_router.put("/check-groups/{group_id}")
def update_check_group(group_id: int, check_group: CheckGroup):
    dao = AuditDAO()
    updated_group = dao.update_check_group(group_id, check_group)
    dao.close_connection()
    if updated_group is None:
        raise HTTPException(status_code=404, detail="Check group not found")
    return updated_group

@audit_router.delete("/check-groups/{group_id}")
def delete_check_group(group_id: int):
    dao = AuditDAO()
    result = dao.delete_check_group(group_id)
    dao.close_connection()
    if not result:
        raise HTTPException(status_code=404, detail="Check group not found")
    return {"message": f"Check group {group_id} deleted successfully"}




@audit_router.post("/check-items")
def create_check_item(check_item: CheckItem):
    dao = AuditDAO()
    item_id = dao.insert_check_item(check_item)
    dao.close_connection()
    return item_id

@audit_router.get("/check-items")
def get_check_items():
    dao = AuditDAO()
    items = dao.select_all_check_items()  # Ensure this method exists in your DAO
    dao.close_connection()
    return items

@audit_router.get("/check-items/{item_id}")
def get_check_item(item_id: int):
    dao = AuditDAO()
    item = dao.select_check_item_by_id(item_id)
    dao.close_connection()
    if item is None:
        raise HTTPException(status_code=404, detail="Check item not found")
    return item

@audit_router.put("/check-items/{item_id}")
def update_check_item(item_id: int, check_item: CheckItem):
    dao = AuditDAO()
    updated_item = dao.update_check_item(item_id, check_item)
    dao.close_connection()
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Check item not found")
    return updated_item

@audit_router.delete("/check-items/{item_id}")
def delete_check_item(item_id: int):
    dao = AuditDAO()
    result = dao.delete_check_item(item_id)
    dao.close_connection()
    if not result:
        raise HTTPException(status_code=404, detail="Check item not found")
    return {"message": f"Check item {item_id} deleted successfully"}


@audit_router.post("/warnings")
def create_warning(warning: Warning):
    dao = AuditDAO()
    warning_id = dao.insert_warning(warning)
    dao.close_connection()
    return warning_id

@audit_router.get("/warnings")
def get_warnings():
    dao = AuditDAO()
    warnings = dao.select_all_warnings()  # Ensure this method exists in your DAO
    dao.close_connection()
    return warnings

@audit_router.get("/warnings/{warning_id}")
def get_warning(warning_id: int):
    dao = AuditDAO()
    warning = dao.select_warning_by_id(warning_id)
    dao.close_connection()
    if warning is None:
        raise HTTPException(status_code=404, detail="Warning not found")
    return warning

@audit_router.put("/warnings/{warning_id}")
def update_warning(warning_id: int, warning: Warning):
    dao = AuditDAO()
    updated_warning = dao.update_warning(warning_id, warning)
    dao.close_connection()
    if updated_warning is None:
        raise HTTPException(status_code=404, detail="Warning not found")
    return updated_warning

@audit_router.delete("/warnings/{warning_id}")
def delete_warning(warning_id: int):
    dao = AuditDAO()
    result = dao.delete_warning(warning_id)
    dao.close_connection()
    if not result:
        raise HTTPException(status_code=404, detail="Warning not found")
    return {"message": f"Warning {warning_id} deleted successfully"}


@audit_router.get("/audits/{audit_id}/check-groups-with-items")
def get_audit_check_groups_with_items(audit_id: int):
    dao = AuditDAO()
    try:
        audit_check_groups = dao.get_audit_check_groups_with_items(audit_id)
        if not audit_check_groups:
            raise HTTPException(status_code=404, detail="No data found for the specified audit")
        return audit_check_groups
    finally:
        dao.close_connection()
        
        
        
# @audit_router.get("/checklists")
# def get_checklists():
#     dao = AuditDAO()
#     try:
#         checklists = dao.get_all_checklists()
#         if not checklists:
#             raise HTTPException(status_code=404, detail="No checklists found")
#         return checklists
#     finally:
#         dao.close_connection()
        
        


@audit_router.get("/checklists")
def get_checklists():
    dao = AuditDAO()
    try:
        checklists = dao.get_all_checklists_with_groups_and_items()
        if not checklists:
            raise HTTPException(status_code=404, detail="No checklists found")
        return checklists
    finally:
        dao.close_connection()
        
        
@audit_router.get("/checklists/{checklist_id}")
def get_checklist_id(checklist_id: int):
    dao = AuditDAO()
    try:
        checklist = dao.get_checklist_by_id_with_groups_and_items(checklist_id)
        if not checklist:
            raise HTTPException(status_code=404, detail="Checklist not found")
        return checklist
    finally:
        dao.close_connection()
        
        
@audit_router.post("/checklists-with-groups-and-items")
def create_checklist_with_groups_and_items(checklist_data: ChecklistWithGroups):
    dao = AuditDAO()
    try:
        checklist_id = dao.insert_checklist_with_groups_and_items(checklist_data)
        return {"checklist_id": checklist_id}
    finally:
        dao.close_connection()
        
        
@audit_router.post("/audits-with-items-and-warnings")
def create_audit_with_items_and_warnings(audit: Audit, items_with_warnings: List[AuditItemWithWarning]):
    dao = AuditDAO()
    try:
        audit_id = dao.create_audit_with_items_and_warnings(audit, items_with_warnings)
        return {"audit_id": audit_id}
    finally:
        dao.close_connection()
        
        
@audit_router.get("/audits-coordinators")
def create_audit_with_items_and_warnings():
    dao = AuditDAO()
    try:
        acoordinators = dao.select_unique_coordinators()
        return acoordinators
    finally:
        dao.close_connection()