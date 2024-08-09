from fastapi import APIRouter
from models.permissions.permission import Permission



permission_router = APIRouter()





@permission_router.get('/get-all-rol', tags=['permisions'])
def get_all_rol():
    permission_instance = Permission()
    data = permission_instance.get_all_rol()
    return data


@permission_router.get('/get-all-permission', tags=['permisions'])
def get_all_rol():
    permission_instance = Permission()
    data = permission_instance.get_all_permission()
    return data


@permission_router.get('/get_all-permission-group-by-group', tags=['permisions'])
def get_all_rol():
    permission_instance = Permission()
    data = permission_instance.get_all_permission_group_by_group()
    return data



@permission_router.get('/get_all-permission-by-employer-id/{employer_id}', tags=['permisions'])
def get_all_rol(employer_id:int):
    permission_instance = Permission()
    data = permission_instance.get_all_permission_by_employer_id(employer_id)
    return data