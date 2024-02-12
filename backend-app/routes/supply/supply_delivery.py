# routers/supply_delivery_router.py

from fastapi import APIRouter, HTTPException
from models.supply.supply_delivery import SupplyDelivery  # Asegúrate de que este modelo exista y esté correctamente implementado
from schema.supply import SupplyDeliverySchema,SupplyDeliveryWithItemsSchema

supply_delivery_router = APIRouter()

@supply_delivery_router.get("/supply-deliveries")
def get_supply_deliveries():
    supply_delivery_instance = SupplyDelivery()
    deliveries = supply_delivery_instance.select_all_deliveries()
    supply_delivery_instance.close_connection()
    return deliveries

@supply_delivery_router.get("/supply-elivery/{delivery_id}")
def get_supply_delivery_by_id(delivery_id: int):
    supply_delivery_instance = SupplyDelivery()
    delivery = supply_delivery_instance.select_delivery_by_id(delivery_id)
    supply_delivery_instance.close_connection()
    return delivery





@supply_delivery_router.post("/supply-delivery/{delivery_id}/sign-sent")
def sign_delivery_as_sent(delivery_id: int):
    supply_delivery_instance = SupplyDelivery()
    try:
        success = supply_delivery_instance.sign_delivery_sent(delivery_id)
        supply_delivery_instance.close_connection()
        if success:
            return {"message": "Delivery signed as sent successfully"}
        else:
            raise HTTPException(status_code=404, detail="Supply delivery not found or already signed")
    except Exception as e:
        supply_delivery_instance.close_connection()
        raise HTTPException(status_code=400, detail=str(e))





@supply_delivery_router.post("/supply-delivery/{delivery_id}/sign-received")
def sign_delivery_as_received(delivery_id: int):
    supply_delivery_instance = SupplyDelivery()
    try:
        success = supply_delivery_instance.sign_delivery_received(delivery_id)
        supply_delivery_instance.close_connection()
        if success:
            return {"message": "Delivery signed as received successfully"}
        else:
            raise HTTPException(status_code=404, detail="Supply delivery not found or already signed")
    except Exception as e:
        supply_delivery_instance.close_connection()
        raise HTTPException(status_code=400, detail=str(e))

























@supply_delivery_router.post("/supply-delivery-with-items")
async def create_supply_delivery_with_items(delivery_with_items: SupplyDeliveryWithItemsSchema):
    supply_delivery_instance = SupplyDelivery()
    try:
        # Usando el nuevo método que maneja múltiples receptores
        delivery_ids = supply_delivery_instance.insert_delivery_with_items_for_multiple_receivers(
            delivery_data=delivery_with_items.delivery_data, 
            items_data=delivery_with_items.items_data, 
            user_receive_ids=delivery_with_items.user_receive_ids
        )
        supply_delivery_instance.close_connection()
        return {"delivery_ids": delivery_ids}
    except Exception as e:
        supply_delivery_instance.close_connection()
        raise HTTPException(status_code=400, detail=str(e))

@supply_delivery_router.delete("/supply-delivery/{delivery_id}")
def delete_supply_delivery(delivery_id: int):
    supply_delivery_instance = SupplyDelivery()
    result = supply_delivery_instance.delete_delivery(delivery_id)
    supply_delivery_instance.close_connection()
    return {"message": result}

@supply_delivery_router.post("/supply-delivery")
def create_supply_delivery(delivery: SupplyDeliverySchema):
    supply_delivery_instance = SupplyDelivery()
    delivery_id = supply_delivery_instance.insert_delivery(delivery)
    supply_delivery_instance.close_connection()
    return {"delivery_id": delivery_id}

@supply_delivery_router.put("/supply-delivery/{delivery_id}",)
def update_supply_delivery(delivery_id: int, updated_delivery: SupplyDeliverySchema):
    supply_delivery_instance = SupplyDelivery()
    updated_delivery_data = supply_delivery_instance.update_delivery(delivery_id, updated_delivery)
    supply_delivery_instance.close_connection()
    return updated_delivery_data if updated_delivery_data else {"message": "Supply delivery not found"}



@supply_delivery_router.get("/user/{user_id}/supply-deliveries")
def get_supply_deliveries_by_user_id(user_id: int):
    supply_delivery_instance = SupplyDelivery()
    try:
        deliveries = supply_delivery_instance.get_deliveries_by_user_id(user_id)
        if deliveries:
            return deliveries
        else:
            raise HTTPException(status_code=404, detail="No supply deliveries found for the given user ID")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        supply_delivery_instance.close_connection()
