from fastapi import APIRouter, HTTPException
from models.adicionales_new import Adicional
from typing import List
from pydantic import BaseModel



class InstanceProductIDs(BaseModel):
    instance_product_ids: List[int]
    site_id : int

class ToggleStatus(BaseModel):
    status: bool

adicional_new_router = APIRouter()
    
@adicional_new_router.get("/adicionales-new-active/{instance_product_id}" , tags=['products'])
def get_adicionales_new_active(instance_product_id:int):
    adicional_instance = Adicional()
    adicionales = adicional_instance.select_adicionales_for_product_active(instance_product_id)
    adicional_instance.close_connection()
    return adicionales

@adicional_new_router.get("/adicionales-new/{instance_product_id}" , tags=['products'])
def get_adicionales_new(instance_product_id:int):
    adicional_instance = Adicional()
    adicionales = adicional_instance.select_adicionales_for_product(instance_product_id)
    adicional_instance.close_connection()
    return adicionales


@adicional_new_router.get("/all-aditional-registered" , tags=['products'])
def get_adicionales_new():
    adicional_instance = Adicional()
    adicionales = adicional_instance.select_all_aditional_registered()
    adicional_instance.close_connection()
    return adicionales

@adicional_new_router.get("/adicionales-unique-site/{site_id}" , tags=['products'])
def get_adicionales_new(site_id:int):
    adicional_instance = Adicional()
    adicionales = adicional_instance.select_unique_adicionales_by_site(site_id)
    adicional_instance.close_connection()
    return adicionales



class ToggleStatusRequest(BaseModel):
    status: bool

@adicional_new_router.put("/toggle-adicionales/{aditional_item_instance_id}", tags=['activation'])
def toggle_adicionales(aditional_item_instance_id: int, request: ToggleStatusRequest):
    adicional_instance = Adicional()
    try:
        result = adicional_instance.toggle_adicionales_status(aditional_item_instance_id, request.status)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        adicional_instance.close_connection()
        
        
        
@adicional_new_router.post("/adicionales-new-group-active/", tags=['products'])
def get_adicionales_new(request_body: InstanceProductIDs):
    adicional_instance = Adicional()
    try:
        # Access the list of IDs with request_body.instance_product_ids
        adicionales = adicional_instance.select_adicionales_for_products(request_body.instance_product_ids,request_body.site_id)
    finally:
        adicional_instance.close_connection()
    return adicionales