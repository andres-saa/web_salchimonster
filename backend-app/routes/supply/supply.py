# routers/supply_router.py

from fastapi import APIRouter
from models.supply.supply import Supply  # Asegúrate de que este modelo exista y esté correctamente implementado
from schema.supply import SupplySchema

supply_router = APIRouter()

@supply_router.get("/supplies", )
def get_supplies():
    supply_instance = Supply()
    supplies = supply_instance.select_all_supplies()
    supply_instance.close_connection()
    return supplies

@supply_router.get("/supply/{dotacion_id}", )
def get_supply_by_id(dotacion_id: int):
    supply_instance = Supply()
    supply = supply_instance.select_supply_by_id(dotacion_id)
    supply_instance.close_connection()
    return supply

@supply_router.delete("/supply/{dotacion_id}")
def delete_supply(dotacion_id: int):
    supply_instance = Supply()
    result = supply_instance.delete_supply(dotacion_id)
    supply_instance.close_connection()
    return {"message": result}

@supply_router.post("/supply",)
def create_supply(supply: SupplySchema):
    supply_instance = Supply()
    dotacion_id = supply_instance.insert_supply(supply)
    supply_instance.close_connection()
    return {"dotacion_id": dotacion_id}

@supply_router.put("/supply/{dotacion_id}")
def update_supply(dotacion_id: int, updated_supply: SupplySchema):
    supply_instance = Supply()
    updated_supply_data = supply_instance.update_supply(dotacion_id, updated_supply)
    supply_instance.close_connection()
    return updated_supply_data if updated_supply_data else {"message": "Supply not found"}
