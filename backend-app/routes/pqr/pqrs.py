from fastapi import APIRouter
from models.pqr.pqr import Pqrs
from schema.pqr import pqrs
from schema.user import user_schema_post
from pydantic import BaseModel

pqr_router = APIRouter()



@pqr_router.post("/create-pqr",tags=["pqr"])
def create_pqrs(data:pqrs.PQRRequest,user:user_schema_post):
    pqr_instance = Pqrs()
    result = pqr_instance.create_pqr(data,user)
    return result



@pqr_router.get("/get-all-pqrs",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_pqrs()
    return result



@pqr_router.get("/get-all-networks",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_networks()
    return result




@pqr_router.get("/get-all-pqr-channel",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_channels()
    return result

@pqr_router.get("/get-all-pqrs-types",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_types()
    return result

@pqr_router.get("/get-all-pqrs-status",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_status()
    return result



from typing import Optional
class ChangeStatusRequest(BaseModel):
    pqr_request_id: int
    status_id: int
    responsible_id: int
    value: Optional[int] = None
    notes: str = ''
    order_id:Optional[str] = None


@pqr_router.post("/change-pqr-status", tags=["pqr"])
def change_pqr_status(data: ChangeStatusRequest):
    pqr_instance = Pqrs()
    result = pqr_instance.update_pqr_status(data)
    return result