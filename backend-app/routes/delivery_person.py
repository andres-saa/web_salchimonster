from fastapi import APIRouter
from schema.delivery_person import delivery_person_schema
from models.delivery_person import DeliveryPerson

delivery_person_router = APIRouter()

@delivery_person_router.get("/deliverypersons")
def get_delivery_persons():
    delivery_person_instance = DeliveryPerson()
    delivery_persons = delivery_person_instance.select_all_delivery_persons()
    delivery_person_instance.close_connection()
    return delivery_persons

@delivery_person_router.get("/deliveryperson/{delivery_person_id}")
def get_delivery_person_by_id(delivery_person_id: int):
    delivery_person_instance = DeliveryPerson()
    delivery_person = delivery_person_instance.select_delivery_person_by_id(delivery_person_id)
    delivery_person_instance.close_connection()
    return delivery_person

@delivery_person_router.delete("/deliveryperson/{delivery_person_id}")
def delete_delivery_person(delivery_person_id: int):
    delivery_person_instance = DeliveryPerson()
    delivery_person_instance.delete_delivery_person(delivery_person_id)
    delivery_person_instance.close_connection()
    return {"message": "Delivery person deleted successfully"}

@delivery_person_router.post("/deliveryperson")
def create_delivery_person(delivery_person: delivery_person_schema):
    delivery_person_instance = DeliveryPerson()
    delivery_person_id = delivery_person_instance.insert_delivery_person(delivery_person)
    delivery_person_instance.close_connection()
    return {"delivery_person_id": delivery_person_id}

@delivery_person_router.put("/deliveryperson/{delivery_person_id}")
def update_delivery_person(delivery_person_id: int, updated_delivery_person: delivery_person_schema):
    delivery_person_instance = DeliveryPerson()
    updated_delivery_person_data = delivery_person_instance.update_delivery_person(delivery_person_id, updated_delivery_person)

    if updated_delivery_person_data:
        delivery_person_instance.close_connection()
        return updated_delivery_person_data
    else:
        delivery_person_instance.close_connection()
        return {"message": "Delivery person not found"}
