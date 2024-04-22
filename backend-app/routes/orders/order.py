from fastapi import APIRouter, HTTPException,Path,Body,WebSocket,WebSocketDisconnect,websockets,Query
from models.orders.order import Order
from schema.orders.order import Orders,DeliveryPersons,OrderNotes,OrderStatus,OrderStatusHistory,PaymentMethodOptions
from typing import List,Dict
from schema.order import OrderSchemaPost
from models.orders.order2 import Order2
from models.payment_method import Pyment_method
order_router = APIRouter()
from pydantic import BaseModel

from fastapi import APIRouter
from schema.order import order_schema_post
from models.order import Order
from fastapi import APIRouter, HTTPException
from datetime import datetime

order_router = APIRouter()





connected_clients: Dict[int, List[WebSocket]] = {}



async def notify_all_clients(site_id: int, message: str, sender: WebSocket):
    for client in connected_clients[site_id]:
        if client != sender:  # Evita enviar el mensaje de vuelta al emisor original
            try:
                await client.send_text(message)
            except WebSocketDisconnect:
                connected_clients[site_id].remove(client)
                if not connected_clients[site_id]:
                    del connected_clients[site_id]
                    

@order_router.websocket("/ws/{site_id}")
async def websocket_endpoint(websocket: WebSocket, site_id: int):
    site_id = int(site_id)  # Ensure site_id is converted to integer, if not already
    await websocket.accept()
    if site_id not in connected_clients:
        connected_clients[site_id] = []
    connected_clients[site_id].append(websocket)
    
    try:
        while True:
            # This can be a place to handle incoming messages or just keep the connection alive
            await websocket.receive_text()
            await notify_sites(site_id, 'hola')
    except WebSocketDisconnect:
        # Properly handle disconnections
        connected_clients[site_id].remove(websocket)
        if not connected_clients[site_id]:
            del connected_clients[site_id]
        print(f"Disconnected: {site_id}")


async def notify_sites(site_id: int, message: str):
    if site_id in connected_clients:
        clients_to_remove = []
        for websocket in connected_clients[site_id]:
            try:
                await websocket.send_text(message)
            except WebSocketDisconnect:
                clients_to_remove.append(websocket)
        for websocket in clients_to_remove:
            connected_clients[site_id].remove(websocket)



@order_router.post("/order")
async def create_order(order_data: OrderSchemaPost):
    order_instance = Order2()
    try:
        result = order_instance.create_order(order_data)
        # Notify the site associated with the order
        await notify_sites(order_data.site_id, "Order processed")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@order_router.get('/order-by-site/{site_id}')
def get_orders_gy_site(site_id:int):
    order_instance = Order2()
    result = order_instance.get_orders_by_site_id_for_today(site_id)
    order_instance.close_connection()
    return result



@order_router.get('/get_order_count_by_site_id/{site_id}')
def get_order_count_by_site_id(site_id:int):
    order_instance = Order2()
    result = order_instance.get_order_count_by_site_id(site_id)
    order_instance.close_connection()
    return result





class updateProduct (BaseModel):
    new_status:bool
@order_router.put('/product-instance/{product_instance_id}/status')
def update_product_instance_status_endpoint(product_instance_id: int, new_status:updateProduct):
    order_instance = Order2()
    try:
        order_instance.update_product_instance_status(product_instance_id, new_status.new_status)
        return {"message": "Product instance status updated successfully", "product_instance_id": product_instance_id, "new_status": new_status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        order_instance.close_connection()



@order_router.get('/payment_methods/')
def get_orders ():
    order_instance = Pyment_method()
    response = order_instance.get_all_payment_methods()
    order_instance.close_connection()
    return response


@order_router.post('/order/{order_id}/prepare')
def prepare_order(order_id: str):
    order_instance = Order2()
    try:
        order_instance.prepare_order(order_id)
    except Exception as e:
        order_instance.close_connection()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        order_instance.close_connection()
    return {"message": "Order is being prepared", "order_id": order_id}


@order_router.post('/order/{order_id}/cancel')
def cancel_order(order_id: str, reason: str = Body(...), responsible: str = Body(...)):
    order_instance = Order2()
    try:
        order_instance.cancel_order(order_id, responsible, reason)
    except Exception as e:
        order_instance.close_connection()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        order_instance.close_connection()
    return {"message": "Order has been cancelled", "order_id": order_id, "reason": reason, "responsible": responsible}


@order_router.post('/order/{order_id}/send')
def send_order(order_id: str = Path(..., description="The ID of the order to be sent")):
    order_instance = Order2()
    try:
        order_instance.send_order(order_id)
    except Exception as e:
        order_instance.close_connection()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        order_instance.close_connection()
    return {"message": "Order has been sent", "order_id": order_id}



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
        