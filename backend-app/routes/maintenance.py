from fastapi import APIRouter
from models.maintenance import EquipmentModel,MaintenanceModel  # Asume que este es tu modelo
from schema.maintenance import Maintenance,Equipment  # Asume que este es tu esquema Pydantic
from fastapi import APIRouter, HTTPException
from typing import List
equipment_router = APIRouter()

@equipment_router.get("/equipment")
def get_all_equipment():
    equipment_instance = EquipmentModel()
    equipment_list = equipment_instance.select_all_equipment()
    equipment_instance.close_connection()
    return equipment_list

@equipment_router.get("/equipment/{equipment_id}")
def get_equipment_by_id(equipment_id: int):
    equipment_instance = EquipmentModel()
    equipment = equipment_instance.select_equipment_by_id(equipment_id)
    equipment_instance.close_connection()
    return equipment


@equipment_router.get("/equipment/site/{site_id}")
def get_equipment_by_site(site_id: int):
    equipment_instance = EquipmentModel()
    equipment_list = equipment_instance.select_equipment_by_site_id(site_id)
    equipment_instance.close_connection()
    return equipment_list

@equipment_router.post("/equipment/sites-with-all")
def get_sites_with_all_equipment(equipment_ids: List[int]):
    equipment_instance = EquipmentModel()
    sites = equipment_instance.select_sites_with_all_equipment(equipment_ids)
    equipment_instance.close_connection()
    if not sites:
        raise HTTPException(status_code=404, detail="No sites found containing all specified equipment")
    return sites


@equipment_router.post("/equipment")
def create_equipment(equipment: Equipment):
    equipment_instance = EquipmentModel()
    equipment_ids = equipment_instance.insert_equipment(equipment, equipment.site_ids)
    equipment_instance.close_connection()
    return {"equipment_ids": equipment_ids}

@equipment_router.put("/equipment/{equipment_id}")
def update_equipment(equipment_id: int, equipment_data: Equipment):
    equipment_instance = EquipmentModel()
    updated_equipment = equipment_instance.update_equipment(equipment_id, equipment_data)
    equipment_instance.close_connection()
    return updated_equipment

@equipment_router.delete("/equipment/{equipment_id}")
def delete_equipment(equipment_id: int):
    equipment_instance = EquipmentModel()
    message = equipment_instance.delete_equipment(equipment_id)
    equipment_instance.close_connection()
    return {"message": message}



maintenance_router = APIRouter()



@maintenance_router.post("/maintenance")
def create_maintenance_record(maintenance: Maintenance):
    maintenance_instance = MaintenanceModel()
    maintenance_ids = maintenance_instance.insert_maintenance(maintenance)
    maintenance_instance.close_connection()
    if not maintenance_ids:
        raise HTTPException(status_code=400, detail="Error creating maintenance records")
    return {"maintenance_ids": maintenance_ids}


@maintenance_router.get("/maintenance")
def get_all_maintenance_records():
    maintenance_instance = MaintenanceModel()
    maintenance_list = maintenance_instance.select_all_maintenance()
    maintenance_instance.close_connection()
    return maintenance_list


@maintenance_router.get("/maintenance/site/{site_id}")
def get_maintenance_by_site(site_id: int):
    maintenance_instance = MaintenanceModel()
    maintenance_records = maintenance_instance.select_maintenance_by_site_id(site_id)
    maintenance_instance.close_connection()
    return maintenance_records

@maintenance_router.get("/maintenance/{maintenance_id}")
def get_maintenance_by_id(maintenance_id: int):
    maintenance_instance = MaintenanceModel()
    maintenance = maintenance_instance.select_maintenance_by_id(maintenance_id)
    maintenance_instance.close_connection()
    return maintenance



@maintenance_router.put("/maintenance/{maintenance_id}")
def update_maintenance_record(maintenance_id: int, maintenance_data: Maintenance):
    maintenance_instance = MaintenanceModel()
    updated_maintenance = maintenance_instance.update_maintenance(maintenance_id, maintenance_data)
    maintenance_instance.close_connection()
    return updated_maintenance

@maintenance_router.delete("/maintenance/{maintenance_id}")
def delete_maintenance_record(maintenance_id: int):
    maintenance_instance = MaintenanceModel()
    message = maintenance_instance.delete_maintenance(maintenance_id)
    maintenance_instance.close_connection()
    return {"message": message}






@maintenance_router.put("/maintenance/{maintenance_id}/complete")
def complete_maintenance_record(maintenance_id: int, remarks: str):
    maintenance_instance = MaintenanceModel()
    updated_maintenance = maintenance_instance.complete_maintenance(maintenance_id, remarks)
    maintenance_instance.close_connection()
    if updated_maintenance:
        return updated_maintenance
    else:
        raise HTTPException(status_code=404, detail="Maintenance record not found or could not be updated")
    
    
    

@equipment_router.post("/equipment/sites-with-all-by-names")
def get_sites_with_all_equipment_by_names(equipment_names: List[str]):
    equipment_instance = EquipmentModel()
    sites = equipment_instance.select_sites_with_all_equipment_by_names(equipment_names)
    equipment_instance.close_connection()
    if not sites:
       return [
           
       ]
    return sites