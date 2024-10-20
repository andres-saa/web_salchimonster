from fastapi import APIRouter, HTTPException,Path,Body,WebSocket,WebSocketDisconnect,websockets,Query
from models.orders.order import Order
from schema.orders.order import Orders,DeliveryPersons,OrderNotes,OrderStatus,OrderStatusHistory,PaymentMethodOptions,Cancellation_request
from typing import List,Dict
from schema.order import OrderSchemaPost
from models.orders.order2 import Order2
from models.payment_method import Pyment_method
order_router = APIRouter()
from pydantic import BaseModel
import schedule
import time
import pytz
from fastapi import APIRouter
from schema.order import order_schema_post
from models.order import Order
from fastapi import APIRouter, HTTPException
from datetime import datetime
from pytz import timezone
import pytz 
from datetime import datetime, timedelta
order_router = APIRouter()
from datetime import datetime, timedelta
from dateutil import parser




connected_clients: Dict[int, List[WebSocket]] = {}

def calcular_total_vendido(data):
    resumen = {}
    for registro in data:
        # Ignorar el registro total
        sitio = registro['site_name'].lower()  # Convertir nombre del sitio a minúsculas
        # Asegurar que total_vendido es tratado como un entero
        total_vendido = int(registro['total_sales_sent'])
        # Formatear total_vendido como string con punto de separación
        resumen[sitio] = f"{total_vendido:,}".replace(",", ".")
    return resumen







class traslate(BaseModel):
    site_id:int
    order_id:str
    
@order_router.put('/traslate-order/')
def traslate(data:traslate):
    order_instance = Order2()
    result = order_instance.traslate_order(data.order_id,data.site_id)
    return result

async def notify_all_clients(site_id: int, message: str, sender: WebSocket):
    for client in connected_clients[site_id]:
        if client != sender:  # Evita enviar el mensaje de vuelta al emisor original
            try:
                await client.send_text(message)
            except WebSocketDisconnect:
                connected_clients[site_id].remove(client)
                if not connected_clients[site_id]:
                    del connected_clients[site_id]
                    




connections: Dict[str, WebSocket] = {}

@order_router.websocket("/ws/orders/{site_id}")
async def websocket_endpoint(websocket: WebSocket, site_id: str):
    await websocket.accept()
    connections[site_id] = websocket
    print(connections)
    await connections[site_id].send_text("Hola")
    try:
        while True:
            data = await websocket.receive_text()
            # Envía el mensaje a todos los clientes conectados
            for connection_site_id, connection in connections.items():
                if connection_site_id != site_id:
                    await connection.send_text(data)
    except WebSocketDisconnect:
        connections.pop(site_id, None)






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


@order_router.get('/order-cancellation-request-categories')
def get_orders_gy_site():
    order_instance = Order2()
    result = order_instance.get_all_cancellation_request_categories()
    order_instance.close_connection()
    return result



class schema (BaseModel):
    order_id:str
    order_code:str

@order_router.post('/validate-order-code')
def validate_order_code(order_data:schema):
    order_instance = Order2()
    try:
        result = order_instance.validate_order_code(order_data.order_id, order_data.order_code)
        return {"valid": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        order_instance.close_connection()

@order_router.get('/order/{order_id}')
def get_orders_gy_site(order_id:str):
    order_instance = Order2()
    result = order_instance.get_order_status_by_order_id(order_id)
    order_instance.close_connection()
    return result


@order_router.get('/order-by-id/{order_id}')
def get_orders_gy_site(order_id:str):
    order_instance = Order2()
    result = order_instance.get_order_by_id(order_id)
    order_instance.close_connection()
    return result



@order_router.get('/order-to-transfer')
def get_orders_to_transfer():
    order_instance = Order2()
    result = order_instance.get_orders_to_transfer()
    order_instance.close_connection()
    return result


@order_router.get('/order-by-phone/{user_phone}')
def get_orders_gy_site(user_phone:str):
    order_instance = Order2()
    result = order_instance.get_order_by_user_phone(user_phone)
    order_instance.close_connection()
    return result

@order_router.get('/get_order_count_by_site_id/{site_id}')
def get_order_count_by_site_id(site_id:int):
    order_instance = Order2()
    result = order_instance.get_order_count_by_site_id(site_id)
    order_instance.close_connection()
    return result


@order_router.get('/get_all_cancellation_request')
def get_all_cancellation_request():
    order_instance = Order2()
    result = order_instance.get_all_cancellation_request()
    order_instance.close_connection()
    return result

@order_router.get('/get_all_cancellation_request_acepted')
def get_all_cancellation_request():
    order_instance = Order2()
    result = order_instance.get_all_cancellation_request_solved_acepted()
    order_instance.close_connection()
    return result


@order_router.get('/get_all_cancellation_request_acepted')
def get_all_cancellation_request():
    order_instance = Order2()
    result = order_instance.get_all_cancellation_request_solved_acepted()
    order_instance.close_connection()
    return result


@order_router.get('/get_all_cancellation_request_pendients')
def get_all_cancellation_request():
    order_instance = Order2()
    result = order_instance.get_all_cancellation_request_pendients()
    order_instance.close_connection()
    return result

@order_router.get('/get_all_cancellation_request_rejected')
def get_all_cancellation_request():
    order_instance = Order2()
    result = order_instance.get_all_cancellation_request_solved_rejected()
    order_instance.close_connection()
    return result

@order_router.post('/insert-cancellation-order')
def get_order_count_by_site_id(calncelation:Cancellation_request):
    order_instance = Order2()
    result = order_instance.insert_cancellation_request(
        calncelation.order_id,
        calncelation.responsible,
        calncelation.reason
    )
    order_instance.close_connection()
    return result




@order_router.put('/delivery_zero/{order_id}')
def get_order_count_by_site_id(order_id:str):
    order_instance = Order2()
    result = order_instance.DelivZero(order_id)
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


@order_router.put("/resolve-cancellation/{cancellation_request_id}")
def resolve_cancellation_request_endpoint(
    
    cancellation_request_id: int, 
    authorized: bool = Body(..., embed=True),
    responsible_id: int = Body(..., embed=True),
    responsible_observation:str = Body(..., embed=True), category_id:int = Body(..., embed=True) ):
    
    order_instance = Order2()
    try:
        order_instance.resolve_cancellation_request(cancellation_request_id, authorized, responsible_id,responsible_observation,category_id)
        return {"message": "Cancellation request resolved successfully", "cancellation_request_id": cancellation_request_id, "authorized": authorized}
    except Exception as e:
        order_instance.close_connection()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        order_instance.close_connection()


@order_router.get('/recent-order/{site_id}')
def get_orders (site_id:int):
    order_instance = Order2()
    response = order_instance.is_recent_order_generated(site_id)
    order_instance.close_connection()
    return response



@order_router.get('/recent-cancellation')
def get_orders ():
    order_instance = Order2()
    response = order_instance.is_recent_cancellation_generated()
    order_instance.close_connection()
    return response



@order_router.get('/recent-pendient-transfer')
def get_orders ():
    order_instance = Order2()
    response = order_instance.is_recent_pendient_transfers()
    order_instance.close_connection()
    return response







@order_router.put("/authorize_order/{order_id}")
async def authorize_order(order_id: str, responsible_id: int = Body(..., embed=True)):
    order_instance = Order2()
    try:
        result = order_instance.authorize_order(order_id, responsible_id)
        return result
    except Exception as e:
        order_instance.close_connection()
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
    print('start',start_date)
    print('end',end_date)

    # Crear una instancia de Order
    order_instance = Order()

    try:
        # Convertir las cadenas de fecha en objetos datetime
        start_date_obj = start_date
        end_date_obj = end_date

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



@order_router.get("/sales_report_sumary")
def get_sales_report(site_ids: str, start_date: str, end_date: str):
    # Convertir la cadena de site_ids en una lista de enteros
    site_ids_list = [int(sid) for sid in site_ids.split(",")]

    # Crear una instancia de Order
    order_instance = Order()

    try:
        # Convertir las cadenas de fecha en objetos datetime
        start_date_obj = start_date
        end_date_obj = end_date

        # Llamar al método get_sales_report_by_site_and_status
        total_sales = order_instance.get_sales_report_by_site(
            site_ids=site_ids_list, 
            start_date=start_date_obj, 
            end_date=end_date_obj
        )

        return total_sales

    finally:
        # Asegurarse de cerrar la conexión
        order_instance.close_connection()







def get_sales_report(start_date: str, end_date: str):
    order_instance = Order()
    try:
        # Configurar la zona horaria de Colombia
        colombia_tz = pytz.timezone('America/Bogota')

        # Convertir strings a objetos datetime en UTC
        start_date_utc = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")  # Ajustado para incluir hora
        end_date_utc = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")  # Ajustado para incluir hora

        # Convertir de UTC a hora de Colombia
        start_date_col = start_date_utc.astimezone(colombia_tz)
        end_date_col = end_date_utc.astimezone(colombia_tz)

        # Formatear fechas para la consulta y para el mensaje
        formatted_start_date = start_date_col.strftime("%A %d de %B de %Y")
        formatted_msg_date = start_date_col.strftime("%d de %B de %Y")

        total_sales = order_instance.get_sales_report_by_site(
            site_ids=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            start_date=start_date,
            end_date=end_date
        )
        sales_data = calcular_total_vendido(total_sales)
        msj = Order2().enviar_mensaje_template(
            '573216252922',
            sales_data.get("bretaña", 0),
            sales_data.get("flora", 0),
            sales_data.get("montes", 0),
            sales_data.get("caney", 0),
            sales_data.get("jamundi", 0),
            sales_data.get("palmira", 0),
            sales_data.get("modelia", 0),
            sales_data.get("suba", 0),
            sales_data.get("kennedy", 0),
            sales_data.get("laureles", 0),
            formatted_msg_date,
            sales_data.get("total", 0)
        )

        print(msj)
        return {"total_sales": total_sales}
    finally:
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
     # Convertir IDs de sitios de string a lista de enteros
    site_ids_list = [int(sid) for sid in site_ids.split(",")]

    # Crear instancia de la clase Order
    order_instance = Order()

    try:
        # Convertir strings de fechas ISO 8601 a objetos datetime
        start_date_obj = parser.isoparse(start_date)
        end_date_obj = parser.isoparse(end_date)

        # Calcular el número de días del periodo actual
        period_length = (end_date_obj - start_date_obj).days

        # Calcular fechas para el periodo anterior
        previous_start_date_obj = start_date_obj - timedelta(days=period_length)
        previous_end_date_obj = end_date_obj - timedelta(days=period_length)

        # Obtener reportes para el periodo actual y el periodo anterior
        current_period_orders = order_instance.get_daily_sales_report(
            start_date=start_date_obj,
            end_date=end_date_obj,
            site_ids=site_ids_list,
            status=status
        )
        previous_period_orders = order_instance.get_daily_sales_report(
            start_date=previous_start_date_obj,
            end_date=previous_end_date_obj,
            site_ids=site_ids_list,
            status=status
        )

        # Combinar los datos en un diccionario para la respuesta
        response = {
            "current_period": current_period_orders,
            "previous_period": previous_period_orders
        }

        return response
    finally:
        order_instance.close_connection()

@order_router.get("/daily_orders")
async def get_daily_orders(site_ids: str, status: str, start_date: str, end_date: str):
    # Convertir IDs de sitios de string a lista de enteros
    site_ids_list = [int(sid) for sid in site_ids.split(",")]

    # Crear instancia de la clase Order
    order_instance = Order()

    try:
        # Convertir strings de fechas ISO 8601 a objetos datetime
        start_date_obj = parser.isoparse(start_date)
        end_date_obj = parser.isoparse(end_date)

        # Calcular el número de días del periodo actual
        period_length = (end_date_obj - start_date_obj).days

        # Calcular fechas para el periodo anterior
        previous_start_date_obj = start_date_obj - timedelta(days=period_length)
        previous_end_date_obj = end_date_obj - timedelta(days=period_length)

        # Obtener reportes para el periodo actual y el periodo anterior
        current_period_orders = order_instance.get_daily_orders_report(
            start_date=start_date_obj,
            end_date=end_date_obj,
            site_ids=site_ids_list,
            status=status
        )
        previous_period_orders = order_instance.get_daily_orders_report(
            start_date=previous_start_date_obj,
            end_date=previous_end_date_obj,
            site_ids=site_ids_list,
            status=status
        )

        # Combinar los datos en un diccionario para la respuesta
        response = {
            "current_period": current_period_orders,
            "previous_period": previous_period_orders
        }

        return response
    finally:
        # Cerrar la conexión a la base de datos
        order_instance.close_connection()

@order_router.get("/daily_average_ticket")
async def get_daily_average_ticket(site_ids: str, status: str, start_date: str, end_date: str):
    # Convertir IDs de sitios de string a lista de enteros
    site_ids_list = [int(sid) for sid in site_ids.split(",")]

    # Crear instancia de la clase Order
    order_instance = Order()

    try:
        # Convertir strings de fechas ISO 8601 a objetos datetime
        start_date_obj = parser.isoparse(start_date)
        end_date_obj = parser.isoparse(end_date)

        # Calcular el número de días del periodo actual
        period_length = (end_date_obj - start_date_obj).days

        # Calcular fechas para el periodo anterior
        previous_start_date_obj = start_date_obj - timedelta(days=period_length)
        previous_end_date_obj = end_date_obj - timedelta(days=period_length)

        # Obtener reportes para el periodo actual y el periodo anterior
        current_period_orders = order_instance.get_daily_average_ticket(
            start_date=start_date_obj,
            end_date=end_date_obj,
            site_ids=site_ids_list,
            status=status
        )
        previous_period_orders = order_instance.get_daily_average_ticket(
            start_date=previous_start_date_obj,
            end_date=previous_end_date_obj,
            site_ids=site_ids_list,
            status=status
        )

        # Combinar los datos en un diccionario para la respuesta
        response = {
            "current_period": current_period_orders,
            "previous_period": previous_period_orders
        }

        return response
    finally:
        order_instance.close_connection()




from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone=timezone('America/Bogota'))
scheduler.start()

def scheduled_job():
    tz = pytz.timezone('America/Bogota')
    current_time = datetime.now(tz)
    # Ajusta el 'start_date' para que comience a las 10 AM del día anterior
    start_date = current_time.replace(hour=10, minute=0, second=0, microsecond=0) - timedelta(days=1)
    # Ajusta el 'end_date' para que termine a las 4 AM del día actual
    end_date = current_time.replace(hour=4, minute=0, second=0, microsecond=0)
    if current_time.hour < 4:
        # Si la hora actual es menor a las 4 AM, ajusta el 'end_date' al día anterior
        end_date -= timedelta(days=1)
    
    # Convertir a UTC y formatear de acuerdo a lo que la función espera
    start_date_utc = start_date.astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')
    end_date_utc = end_date.astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')
    
    get_sales_report(start_date_utc, end_date_utc)

# Asegúrate de que el cron job está configurado para la hora correcta


# Programa la tarea para que se ejecute todos los días a la 1 AM
scheduler.add_job(scheduled_job, 'cron', hour=5, minute=0)