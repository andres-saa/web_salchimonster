from fastapi import APIRouter
from schema.order import order_schema_post
from models.order import Order
from fastapi import APIRouter, HTTPException
from datetime import datetime
from pytz import timezone
import pytz 
order_router = APIRouter()

@order_router.get("/orders")
def get_orders():
    order_instance = Order()
    orders = order_instance.select_all_orders()
    order_instance.close_connection()
    return orders

@order_router.get("/order/{order_id}")
def get_order_by_id(order_id: str):
    order_instance = Order()
    order = order_instance.get_order_status_by_order_id(order_id)
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
    orders = order_instance.select_orders_by_site_id(site_id)
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


@order_router.get("/server_time")
def get_server_time():
    # Configura la zona horaria de Colombia
    colombia_tz = pytz.timezone('America/Bogota')

    # Obtiene la hora actual con la zona horaria de Colombia
    now_colombia = datetime.now(colombia_tz)

    # Formatea la fecha y la hora de manera tradicional (YYYY-MM-DD HH:MM)
    fecha_hora_tradicional = now_colombia.strftime("%Y-%m-%d %H:%M")

    return fecha_hora_tradicional


@order_router.get("/sales_report")
def get_sales_report(site_ids: str, status: str, start_date: str, end_date: str):
    # Convertir la cadena de site_ids en una lista de enteros
    site_ids_list = [int(sid) for sid in site_ids.split(",")]

    # Crear una instancia de Order
    order_instance = Order()

    try:
        # Convertir las cadenas de fecha en objetos datetime
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

        # Llamar al método get_sales_report_by_site_and_status
        total_sales = order_instance.get_sales_report_by_site_and_status(
            site_ids=site_ids_list, 
            status=status, 
            start_date=start_date_obj, 
            end_date=end_date_obj
        )

        return {"total_sales": total_sales}

    finally:
        # Asegurarse de cerrar la conexión
        order_instance.close_connection()


@order_router.get("/order_total_price/{order_id}")
def get_order_total_price(order_id: int):
    order_instance = Order()
    try:
        total_price = order_instance.get_order_total_price(order_id)
        if total_price is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return {"order_id": order_id, "total_price": total_price}
    finally:
        order_instance.close_connection()



@order_router.get("/daily_sales")
async def get_daily_sales(site_ids: str, status: str, start_date: str, end_date: str):
    site_ids_list = [int(sid) for sid in site_ids.split(",")]
    order_instance = Order()
    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        daily_sales = order_instance.get_daily_sales_report(
            start_date=start_date_obj, 
            end_date=end_date_obj, 
            site_ids=site_ids_list, 
            status=status
        )
        return daily_sales
    finally:
        order_instance.close_connection()

@order_router.get("/daily_orders")
async def get_daily_orders(site_ids: str, status: str, start_date: str, end_date: str):
    site_ids_list = [int(sid) for sid in site_ids.split(",")]
    order_instance = Order()
    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        daily_orders_report = order_instance.get_daily_orders_report(
            start_date=start_date_obj, 
            end_date=end_date_obj, 
            site_ids=site_ids_list, 
            status=status
        )
        return daily_orders_report
    finally:
        order_instance.close_connection()



@order_router.get("/daily_average_ticket")
async def get_daily_average_ticket(site_ids: str, status: str, start_date: str, end_date: str):
    site_ids_list = [int(sid) for sid in site_ids.split(",")]
    order_instance = Order()
    try:
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        daily_average_ticket = order_instance.get_daily_average_ticket(
            start_date=start_date_obj,
            end_date=end_date_obj,
            site_ids=site_ids_list,
            status=status
        )
        return daily_average_ticket
    finally:
        order_instance.close_connection()
        
        
        
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone=timezone('America/Bogota'))
scheduler.start()

def update_orders_status():
    order_instance = Order()
    order_instance.update_all_orders_status()
    order_instance.close_connection()

# Programa la tarea para que se ejecute todos los días a la 1 AM
scheduler.add_job(update_orders_status, 'cron', hour=23, minute=30)