from fastapi import APIRouter
from models.cachier_money.cachier_money import CachierMoney
from schema.pqr import pqrs
from schema.user import user_schema_post
from pydantic import BaseModel
from datetime import date
cachier_money_router = APIRouter()



@cachier_money_router.get("/get-all-cachier-money",tags=["cachier_money"])
def create_pqrs():
    pqr_instance = CachierMoney()
    result = pqr_instance.get_all_cachier_money()
    return result



@cachier_money_router.get("/get-all-cachier-money-by-site-id/{site-id}",tags=["cachier_money"])
def create_pqrs(site_id:int):
    pqr_instance = CachierMoney()
    result = pqr_instance.get_cachier_money_by_site_id(site_id)
    return result



@cachier_money_router.get("/get-work-schedule",tags=["cachier_money"])
def create_pqrs():
    pqr_instance = CachierMoney()
    result = pqr_instance.get_call_work_schedule()
    return result


@cachier_money_router.get("/get-output-types",tags=["cachier_money"])
def create_pqrs():
    pqr_instance = CachierMoney()
    result = pqr_instance.get_call_output_types()
    return result


class filtered_schema(BaseModel):
    sites:list[int]
    start_date:str
    end_date:str



class cachier_money_entry(BaseModel):
    cachier_id:int
    work_schedule_id:int
    value:int
    site_id:int
    date:str



class Output(BaseModel):
    date: date
    content: str
    value: int
    output_type_id: int
    responsible_id: int
    work_schedule_id:int




@cachier_money_router.post("/create-output-cachier-money/{site_id}",tags=["cachier_money"])
def get_filtered_cachiers_money(data:Output,site_id:int):
    pqr_instance = CachierMoney()
    result = pqr_instance.create_output(data,site_id)
    return result



@cachier_money_router.post("/create-cachier-entry/",tags=["cachier_money"])
def get_filtered_cachiers_money(data:cachier_money_entry):
    pqr_instance = CachierMoney()
    result = pqr_instance.create_cachier_money_entry(data)
    return result



@cachier_money_router.post("/get-all-cachier-money-by-filtered/",tags=["cachier_money"])
def get_filtered_cachiers_money(data:filtered_schema):
    pqr_instance = CachierMoney()
    result = pqr_instance.get_cachier_money_filtered(data)
    return result

