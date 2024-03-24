from fastapi import APIRouter
from models.work_scheduler import WorkShiftCRUD  # Ajusta la ruta del módulo
from models.work_scheduler import WorkRecordCRUD  # Ajusta la ruta del módulo
from schema.work_scheduler import WorkRecord, WorkShift  # Asegúrate de que los esquemas Pydantic sean accesibles
from models.work_scheduler import WorkDayCRUD  # Ajusta la ruta del módulo
from schema.work_scheduler import WorkDay
from fastapi import APIRouter, Depends, Query
from datetime import date  # Importing the date class

work_shift_router = APIRouter()

@work_shift_router.post("/work_shifts")
def create_work_shift(shift: WorkShift):
    shift_instance = WorkShiftCRUD()
    shift_id = shift_instance.create_work_shift(shift)
    shift_instance.close_connection()
    return {"shift_id": shift_id}

@work_shift_router.get("/work_shifts/{shift_id}")
def get_work_shift(shift_id: int):
    shift_instance = WorkShiftCRUD()
    shift = shift_instance.read_work_shift(shift_id)
    shift_instance.close_connection()
    return shift







@work_shift_router.put("/work_shifts/{shift_id}")
def update_work_shift(shift_id: int, shift: WorkShift):
    shift_instance = WorkShiftCRUD()
    updated_shift = shift_instance.update_work_shift(shift_id, shift)
    shift_instance.close_connection()
    return updated_shift

@work_shift_router.delete("/work_shifts/{shift_id}")
def delete_work_shift(shift_id: int):
    shift_instance = WorkShiftCRUD()
    message = shift_instance.delete_work_shift(shift_id)
    shift_instance.close_connection()
    return {"message": message}

work_record_router = APIRouter()

@work_record_router.post("/work_records")
def create_work_record(record: WorkRecord):
    record_instance = WorkRecordCRUD()
    record_id = record_instance.create_work_record(record)
    record_instance.close_connection()
    return {"record_id": record_id}

@work_record_router.get("/work_records/{record_id}")
def get_work_record(record_id: int):
    record_instance = WorkRecordCRUD()
    record = record_instance.read_work_record(record_id)
    record_instance.close_connection()
    return record

@work_record_router.put("/work_records/{record_id}")
def update_work_record(record_id: int, record: WorkRecord):
    record_instance = WorkRecordCRUD()
    updated_record = record_instance.update_work_record(record_id, record)
    record_instance.close_connection()
    return updated_record

@work_record_router.delete("/work_records/{record_id}")
def delete_work_record(record_id: int):
    record_instance = WorkRecordCRUD()
    message = record_instance.delete_work_record(record_id)
    record_instance.close_connection()
    return {"message": message}


@work_shift_router.get("/work_shifts")
def get_all_work_shifts():
    shift_instance = WorkShiftCRUD()
    shifts = shift_instance.select_all_work_shifts()
    shift_instance.close_connection()
    return shifts

@work_record_router.get("/work_records")
def get_all_work_records():
    record_instance = WorkRecordCRUD()
    records = record_instance.select_all_work_records()
    record_instance.close_connection()
    return records









work_day_router = APIRouter()

@work_day_router.post("/work_days", response_model=WorkDay)
def create_work_day(work_day: WorkDay):
    day_instance = WorkDayCRUD()
    try:
        day_id = day_instance.create_work_day(work_day.date,work_day.site_id)
    finally:
        day_instance.close_connection()
    return day_id



@work_day_router.get("/work_days_with_records")
def get_all_work_days_with_records():
    day_instance = WorkDayCRUD()
    work_days_with_records = day_instance.select_all_work_days_with_records()
    day_instance.close_connection()
    return work_days_with_records

@work_day_router.get("/filtered_work_days")
def get_filtered_work_days(
    start_date: date = Query(..., description="The start date for the filter"),
    end_date: date = Query(..., description="The end date for the filter"),
    site_id: int = Query(..., description="The site ID to filter the workdays")
):
    day_instance = WorkDayCRUD()
    try:
        filtered_days = day_instance.select_work_days_with_records_by_date_and_site(start_date, end_date, site_id)
    finally:
        day_instance.close_connection()
    return filtered_days

@work_day_router.get("/work_days/{day_id}")
def get_work_day(day_id: int):
    day_instance = WorkDayCRUD()
    work_day = day_instance.read_work_day(day_id)
    day_instance.close_connection()
    return work_day

@work_day_router.put("/work_days/{day_id}")
def update_work_day(day_id: int, work_day: WorkDay):
    day_instance = WorkDayCRUD()
    updated_day = day_instance.update_work_day(day_id, work_day.date)
    day_instance.close_connection()
    return updated_day

@work_day_router.delete("/work_days/{day_id}")
def delete_work_day(day_id: int):
    day_instance = WorkDayCRUD()
    message = day_instance.delete_work_day(day_id)
    day_instance.close_connection()
    return {"message": message}


@work_day_router.get("/work_days")
def get_all_work_days():
    day_instance = WorkDayCRUD()
    days = day_instance.select_all_work_days()
    day_instance.close_connection()
    return days