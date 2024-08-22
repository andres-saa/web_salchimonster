from fastapi import APIRouter,Depends
from fastapi import APIRouter, HTTPException
from models.permission import Permission  # Asume que tienes una clase Permission en models
from schema.permission import PermissionSchemaPost  # Asume que tienes un esquema PermissionSchemaPost
from auth_utils.Security import Security,authenticate_user,create_access_token

permission_employer_router = APIRouter()

@permission_employer_router.get("/permissions")
def get_permissions():
    permission_instance = Permission()
    permissions = permission_instance.select_all_permissions()
    permission_instance.close_connection()
    return permissions

@permission_employer_router.get("/permission/{permission_id}")
def get_permission_by_id(permission_id: int):
    permission_instance = Permission()
    permission = permission_instance.select_permission_by_id(permission_id)
    permission_instance.close_connection()
    return permission

@permission_employer_router.get("/permissions/user/{user_id}")
def get_permissions_by_user_id(user_id: int):
    permission_instance = Permission()
    permissions = permission_instance.select_permissions_by_user_id(user_id)
    permission_instance.close_connection()

    if permissions:
        return permissions
    else:
        return [] 
@permission_employer_router.post("/permission")
def create_permission(permission: PermissionSchemaPost):
    permission_instance = Permission()
    permission_id = permission_instance.insert_permission(permission)
    permission_instance.close_connection()
    return {"permission_id": permission_id}

@permission_employer_router.put("/permission/{permission_id}")
def update_permission(permission_id: int, updated_permission: PermissionSchemaPost):
    permission_instance = Permission()
    updated_permission_data = permission_instance.update_permission(permission_id, updated_permission)
    permission_instance.close_connection()
    
    if updated_permission_data:
        return updated_permission_data
    else:
        raise HTTPException(status_code=404, detail="Permission not found")


@permission_employer_router.get("/permission/user/{user_id}/status/{status}")
def get_permissions_by_user_id_and_status(user_id: int, status: str):
    permission_instance = Permission()
    permissions = permission_instance.select_permissions_by_user_id_and_status(user_id, status)
    permission_instance.close_connection()

    if permissions:
        return permissions
    else:
        return []


@permission_employer_router.get("/permissions/user/{user_id}/status/{status}/type/{tipo}")
def get_permissions_by_status_userid_and_tipo(user_id: int, status: str, tipo: str):
    permission_instance = Permission()
    permissions = permission_instance.select_permissions_by_status_userid_and_type(status, user_id, tipo)
    permission_instance.close_connection()

    if permissions:
        return permissions
    else:
        return []
        

@permission_employer_router.get("/permissions/status/{status}")
def get_permissions_by_status(status: str):
    permission_instance = Permission()
    permissions = permission_instance.select_permissions_by_status(status)
    permission_instance.close_connection()
    return permissions

@permission_employer_router.get("/permissions/status/{status}/type/{tipo}")
def get_permissions_by_status_and_tipo(status: str, tipo: str):
    permission_instance = Permission()
    permissions = permission_instance.select_permissions_by_status_and_tipo(status, tipo)
    permission_instance.close_connection()
    return permissions

@permission_employer_router.delete("/permission/{permission_id}")
def delete_permission(permission_id: int):
    permission_instance = Permission()
    result = permission_instance.delete_permission(permission_id)
    permission_instance.close_connection()
    return result
