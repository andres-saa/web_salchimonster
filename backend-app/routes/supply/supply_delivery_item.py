# routers/supply_delivery_item_router.py

# routers/supply_delivery_router.py

from fastapi import APIRouter
from models.supply.supply_delivery_item import SupplyDeliveryItem  # Asegúrate de que este modelo exista y esté correctamente implementado
from schema.supply import SupplyDeliveryItemSchema
supply_delivery_item_router = APIRouter()

@supply_delivery_item_router.get("/supply_delivery_items" )
def get_supply_delivery_items():
    supply_delivery_item_instance = SupplyDeliveryItem()
    items = supply_delivery_item_instance.select_all_items()
    supply_delivery_item_instance.close_connection()
    return items

@supply_delivery_item_router.get("/supply_delivery_item/{item_id}")
def get_supply_delivery_item_by_id(item_id: int):
    supply_delivery_item_instance = SupplyDeliveryItem()
    item = supply_delivery_item_instance.select_item_by_id(item_id)
    supply_delivery_item_instance.close_connection()
    return item

@supply_delivery_item_router.delete("/supply_delivery_item/{item_id}")
def delete_supply_delivery_item(item_id: int):
    supply_delivery_item_instance = SupplyDeliveryItem()
    result = supply_delivery_item_instance.delete_item(item_id)
    supply_delivery_item_instance.close_connection()
    return {"message": result}

@supply_delivery_item_router.get("/supply_delivery_items/delivery/{delivery_id}")
def get_supply_delivery_items_by_delivery_id(delivery_id: int):
    supply_delivery_item_instance = SupplyDeliveryItem()
    items = supply_delivery_item_instance.select_items_by_delivery_id(delivery_id)
    supply_delivery_item_instance.close_connection()
    if items:
        return items
    else:
        return {"message": "No items found for this delivery ID"}


@supply_delivery_item_router.post("/supply_delivery_item",)
def create_supply_delivery_item(item: SupplyDeliveryItemSchema):
    supply_delivery_item_instance = SupplyDeliveryItem()
    item_id = supply_delivery_item_instance.insert_item(item)
    supply_delivery_item_instance.close_connection()
    return {"item_id": item_id}

@supply_delivery_item_router.put("/supply_delivery_item/{item_id}")
def update_supply_delivery_item(item_id: int, updated_item: SupplyDeliveryItemSchema):
    supply_delivery_item_instance = SupplyDeliveryItem()
    updated_item_data = supply_delivery_item_instance.update_item(item_id, updated_item)
    supply_delivery_item_instance.close_connection()
    return updated_item_data if updated_item_data else {"message": "Supply delivery item not found"}
