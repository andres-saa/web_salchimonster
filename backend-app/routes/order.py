from fastapi import APIRouter
from schema.order import order_schema_post
from models.order import Order

order_router = APIRouter()

@order_router.get("/orders")
def get_orders():
    order_instance = Order()
    orders = order_instance.select_all_orders()
    order_instance.close_connection()
    return orders

@order_router.get("/order/{order_id}")
def get_order_by_id(order_id: int):
    order_instance = Order()
    order = order_instance.select_order_by_id(order_id)
    order_instance.close_connection()
    return order

@order_router.delete("/order/{order_id}")
def delete_order(order_id: int):
    order_instance = Order()
    order_instance.delete_order(order_id)
    order_instance.close_connection()
    return {"message": "Order deleted successfully"}

@order_router.post("/order")
def create_order(order: order_schema_post):
    order_instance = Order()
    order_id = order_instance.create_order(order)
    order_instance.close_connection()
    return {"order_id": order_id}

@order_router.put("/order/{order_id}")
def update_order(order_id: int, updated_order: order_schema_post):
    order_instance = Order()
    updated_order_data = order_instance.update_order(order_id, updated_order)

    if updated_order_data:
        order_instance.close_connection()
        return updated_order_data
    else:
        order_instance.close_connection()
        return {"message": "Order not found"}
 
@order_router.get("/orders_by_site/{site_id}")
def get_orders_by_site(site_id: int):
    order_instance = Order()
    orders = order_instance.select_orders_by_site(site_id)
    order_instance.close_connection()
    return orders

@order_router.get("/orders/by_delivery_person/{delivery_person_id}")
def get_orders_by_delivery_person(delivery_person_id: int):
    order_instance = Order()
    orders = order_instance.select_orders_by_delivery_person(delivery_person_id)
    order_instance.close_connection()
    return orders

@order_router.get("/orders/by_user/{user_id}")
def get_orders_by_user(user_id: int):
    order_instance = Order()
    orders = order_instance.select_orders_by_user(user_id)
    order_instance.close_connection()
    return orders