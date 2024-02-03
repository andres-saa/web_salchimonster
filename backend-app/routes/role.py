from fastapi import APIRouter, HTTPException
from models.role import Role
from models.role import Role,RoleGroup
from typing import List, Dict


from schema.role import RoleGroupSchema, RoleSchema
role_router = APIRouter()








@role_router.get("/roles")
def get_roles():
    role_instance = Role()
    roles = role_instance.select_all_roles()
    role_instance.close_connection()
    return roles

@role_router.get("/role/{role_id}")
def get_role_by_id(role_id: int):
    role_instance = Role()
    role = role_instance.select_role_by_id(role_id)
    role_instance.close_connection()
    return role

@role_router.post("/role")
def create_role(role: RoleSchema):
    role_instance = Role()
    role_id = role_instance.create_role(role)
    role_instance.close_connection()
    return {"role_id": role_id}

@role_router.put("/role/{role_id}")
def update_role(role_id: int, updated_role: RoleSchema):
    role_instance = Role()
    updated_role_data = role_instance.update_role(role_id, updated_role)
    role_instance.close_connection()
    return updated_role_data if updated_role_data else {"message": "Role not found"}




@role_router.delete("/role/{role_id}")
def delete_role(role_id: int):
    role_instance = Role()
    result = role_instance.delete_role(role_id)
    role_instance.close_connection()
    return {"message": result}

rolegroup_router = APIRouter()

@rolegroup_router.get("/rolegroups")
def get_role_groups():
    group_instance = RoleGroup()
    groups = group_instance.select_all_groups()
    group_instance.close_connection()
    return groups






@rolegroup_router.post("/assign-roles-to-group/{group_id}")
def assign_roles_to_group(group_id: int, role_ids: List[int]):
    group_instance = RoleGroup()
    try:
        result = group_instance.assign_roles_to_group(group_id, role_ids)
    except Exception as e:
        group_instance.close_connection()
        raise HTTPException(status_code=400, detail=str(e))
    group_instance.close_connection()
    return result


@rolegroup_router.post("/assign-roles-to-group-delete-olds/{group_id}")
def assign_roles_to_group(group_id: int, role_ids: List[int]):
    group_instance = RoleGroup()
    try:
        result = group_instance.assign_roles_to_group_delete_olds(group_id, role_ids)
    except Exception as e:
        group_instance.close_connection()
        raise HTTPException(status_code=400, detail=str(e))
    group_instance.close_connection()
    return result


@rolegroup_router.get("/formatted-rolegroups", response_model=Dict[str, List[str]])
def get_formatted_roles_by_group():
    group_instance = RoleGroup()
    try:
        # Llama al método get_roles_formatted_by_group para obtener los roles formateados por grupo
        formatted_roles = group_instance.get_roles_formatted_by_group()
        group_instance.close_connection()
        return formatted_roles
    except Exception as e:
        group_instance.close_connection()
        raise HTTPException(status_code=400, detail=str(e))


@rolegroup_router.get("/rolegroup/{group_id}/roles")
def get_roles_by_group(group_id: int):
    group_instance = RoleGroup()
    try:
        roles = group_instance.get_roles_by_group_id(group_id)
        group_instance.close_connection()
        return roles
    except Exception as e:
        group_instance.close_connection()
        raise HTTPException(status_code=400, detail=str(e))



@rolegroup_router.get("/rolegroup/{group_id}")
def get_role_group_by_id(group_id: int):
    group_instance = RoleGroup()
    group = group_instance.select_group_by_id(group_id)
    group_instance.close_connection()
    return group

@rolegroup_router.post("/rolegroup")
def create_role_group(group: RoleGroupSchema):
    group_instance = RoleGroup()
    group_id = group_instance.create_role_group(group)
    group_instance.close_connection()
    return {"group_id": group_id}

@rolegroup_router.put("/rolegroup/{group_id}")
def update_role_group(group_id: int, updated_group: RoleGroupSchema):
    group_instance = RoleGroup()
    updated_group_data = group_instance.update_role_group(group_id, updated_group)
    group_instance.close_connection()
    return updated_group_data if updated_group_data else {"message": "RoleGroup not found"}

@rolegroup_router.delete("/rolegroup/{group_id}")
def delete_role_group(group_id: int):
    group_instance = RoleGroup()
    result = group_instance.delete_role_group(group_id)
    group_instance.close_connection()
    return {"message": result}
