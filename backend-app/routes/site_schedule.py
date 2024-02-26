from fastapi import APIRouter,HTTPException
from models.site import Site
from schema.site import site_schema_post
from schema.site_schedule import site_schedule_schema
from models.site_schedule import site_schedule
site_schedule_router = APIRouter()
from fastapi import APIRouter, Depends
from typing import List


@site_schedule_router.post("/site-schedule")
def insert_site_schedule(schedule_data:site_schedule_schema):
    site_schedule_instance = site_schedule()
    site_schedule_id = site_schedule_instance.create_schedule(schedule_data)
    site_schedule_instance.close_connection()

    return {"site_schedule_id":site_schedule_id} 

@site_schedule_router.put("/site-schedule/")
def update_site_schedule( schedule_data:List[site_schedule_schema] ):
    site_schedule_instance = site_schedule()
    site_schedule_instance.update_schedules_all( schedule_data)
    site_schedule_instance.close_connection()
    return {"message": "Schedule updated successfully"}

@site_schedule_router.get("/site-schedule/{site_id}")

def get_schedule_by_site_id(site_id: int):
    site_schedule_instance = site_schedule()
    schedule_data = site_schedule_instance.get_schedule_by_site_id(site_id)
    if not schedule_data:
        raise HTTPException(status_code=404, detail="No se encontraron horarios para el sitio especificado")
    return schedule_data


@site_schedule_router.get("/site/{site_id}/status")
def get_site_status(site_id: int, schedule_instance: site_schedule = Depends()):
    is_open, next_opening_time = schedule_instance.is_site_open(site_id)
    if is_open:
        return {"status": "open"}
    else:
        if next_opening_time:
            return {"status": "closed", "next_opening_time": next_opening_time}
        else:
            return {"status": "closed", "message": "No schedule found for the site."}
        


# @site_schedule_router.put("/site-schedule/update")
# def update_multiple_schedules_all(schedule_data_list: List[site_schedule_schema]):
#     site_schedule_instance = site_schedule()
#     site_schedule_instance.update_schedules_all(schedule_data_list)
#     site_schedule_instance.close_connection()
#     return {"message": "Schedules updated successfully"}
