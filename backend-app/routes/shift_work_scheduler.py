from fastapi import APIRouter
# from models.shift_work_scheduler import   # Ajusta la ruta del módulo
from models.shift_work_scheduler import ShiftWorkDay, ShiftWorkDayCRUD,ShiftWorkRecord,ShiftWorkRecordCRUD,ShiftWorkShift,ShiftWorkShiftCRUD  # Ajusta la ruta del módulo

# from schema.shift_work_scheduler import ShiftWorkDay, ShiftWorkRecord, ShiftWorkShift

# Asegúrate de que los esquemas Pydantic sean accesibles
from models.work_scheduler import WorkDayCRUD  # Ajusta la ruta del módulo
from schema.work_scheduler import WorkDay
from fastapi import APIRouter, Depends, Query
from datetime import date  # Importing the date class

shift_work_shift_router = APIRouter()

@shift_work_shift_router.post("/shift_work_shifts")
def create_work_shift(shift: ShiftWorkShift):
    shift_instance = ShiftWorkShiftCRUD()
    shift_id = shift_instance.create_work_shift(shift)
    shift_instance.close_connection()
    return {"shift_id": shift_id}

@shift_work_shift_router.get("/shift_work_shifts/{shift_id}")
def get_work_shift(shift_id: int):
    shift_instance = ShiftWorkShiftCRUD()
    shift = shift_instance.read_work_shift(shift_id)
    shift_instance.close_connection()
    return shift






@shift_work_shift_router.put("/shift_work_shifts/{shift_id}")
def update_work_shift(shift_id: int, shift: ShiftWorkShift):
    shift_instance = ShiftWorkShiftCRUD()
    updated_shift = shift_instance.update_work_shift(shift_id, shift)
    shift_instance.close_connection()
    return updated_shift

@shift_work_shift_router.delete("/shift_work_shifts/{shift_id}")
def delete_work_shift(shift_id: int):
    shift_instance = ShiftWorkShiftCRUD()
    message = shift_instance.delete_work_shift(shift_id)
    shift_instance.close_connection()
    return {"message": message}

shift_work_record_router = APIRouter()

@shift_work_record_router.post("/shift_work_records")
def create_work_record(record: ShiftWorkRecord):
    record_instance = ShiftWorkRecordCRUD()
    record_id = record_instance.create_work_record(record)
    record_instance.close_connection()
    return {"record_id": record_id}

@shift_work_record_router.get("/shift_work_records/{record_id}")
def get_work_record(record_id: int):
    record_instance = ShiftWorkRecordCRUD()
    record = record_instance.read_work_record(record_id)
    record_instance.close_connection()
    return record

@shift_work_record_router.put("/shift_work_records/{record_id}")
def update_work_record(record_id: int, record: ShiftWorkRecord):
    record_instance = ShiftWorkRecordCRUD()
    updated_record = record_instance.update_work_record(record_id, record)
    record_instance.close_connection()
    return updated_record

@shift_work_record_router.delete("/shift_work_records/{record_id}")
def delete_work_record(record_id: int):
    record_instance = ShiftWorkRecordCRUD()
    message = record_instance.delete_work_record(record_id)
    record_instance.close_connection()
    return {"message": message}


@shift_work_shift_router.get("/shift_work_shifts")
def get_all_work_shifts():
    shift_instance = ShiftWorkShiftCRUD()
    shifts = shift_instance.select_all_work_shifts()
    shift_instance.close_connection()
    return shifts

@shift_work_record_router.get("/shift_work_records")
def get_all_work_records():
    record_instance = ShiftWorkRecordCRUD()
    records = record_instance.select_all_work_records()
    record_instance.close_connection()
    return records









shift_work_day_router = APIRouter()

@shift_work_day_router.post("/shift_work_days")
def create_work_week(work_day: ShiftWorkDay):
    day_instance = ShiftWorkDayCRUD()
    try:
        day_id = day_instance.create_work_week(work_day.date,work_day.site_id)
    finally:
        day_instance.close_connection()
    return day_id



@shift_work_day_router.get("/shift_work_days_with_records")
def get_all_work_days_with_records():
    day_instance = ShiftWorkDayCRUD()
    work_days_with_records = day_instance.select_all_work_days_with_records()
    day_instance.close_connection()
    return work_days_with_records

@shift_work_day_router.get("/shift_filtered_work_days")
def get_shift_filtered_work_days(
    start_date: date = Query(..., description="The start date for the filter"),
    end_date: date = Query(..., description="The end date for the filter"),
    site_id: int = Query(..., description="The site ID to filter the workdays")
):
    day_instance = ShiftWorkDayCRUD()
    try:
        filtered_days = day_instance.select_work_days_with_records_by_date_and_site(start_date, end_date, site_id)
    finally:
        day_instance.close_connection()
    return filtered_days

# @shift_work_day_router.post("/shift_work_days")
# def create_work_week(work_day: ShiftWorkDay):
#     day_instance = ShiftWorkDayCRUD()
#     try:
#         # Assuming create_work_week returns a list of WorkDay objects
#         created_days = day_instance.create_work_week(work_day.date, work_day.site_id)
#     finally:
#         day_instance.close_connection()
#     return created_days

@shift_work_day_router.put("/shift_work_days/{day_id}")
def update_work_day(day_id: int, work_day: ShiftWorkDay):
    day_instance = ShiftWorkDayCRUD()
    updated_day = day_instance.update_work_day(day_id, work_day.date)
    day_instance.close_connection()
    return updated_day

@shift_work_day_router.delete("/shift_work_days/{day_id}")
def delete_work_day(day_id: int):
    day_instance = ShiftWorkDayCRUD()
    message = day_instance.delete_work_day(day_id)
    day_instance.close_connection()
    return {"message": message}


@shift_work_day_router.get("/shift_work_days")
def get_all_work_days():
    day_instance = ShiftWorkDayCRUD()
    days = day_instance.select_all_work_days()
    day_instance.close_connection()
    return days