from fastapi import APIRouter, HTTPException,Path,Body,WebSocket,WebSocketDisconnect,websockets,Query
from models.orders.order import Order
from schema.orders.order import Orders,DeliveryPersons,OrderNotes,OrderStatus,OrderStatusHistory,PaymentMethodOptions,Cancellation_request
from typing import List,Dict
from schema.order import OrderSchemaPost, OrderSchemaPostDistri
from models.orders.order_distrimonster import Order2
from models.payment_method import Pyment_method
order_distrimonster_router = APIRouter()
from pydantic import BaseModel
from typing import Optional
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
order_distrimonster_router = APIRouter()
from datetime import datetime, timedelta
from dateutil import parser




connected_clients: Dict[int, List[WebSocket]] = {}



@order_distrimonster_router.post("/order-distrimonster")
async def create_order(order_data: OrderSchemaPostDistri):
    order_instance = Order2()
    try:
        result = order_instance.create_order(order_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@order_distrimonster_router.get('/order-to-transfer-distri')
def get_orders_to_transfed():
    order_instance = Order2()
    result = order_instance.get_orders_to_transfer()
    order_instance.close_connection()
    return result



@order_distrimonster_router.get('/get-distrimonster-user-by-dni/{dni}')
def get_orders_to_transfed(dni:str):
    order_instance = Order2()
    result = order_instance.get_distrimonster_user_by_dni(dni)
    order_instance.close_connection()
    return result





class User(BaseModel):
    user_name: str
    user_phone: str
    user_address: str
    site_id :int = 32
    cedula_nit:str
    email: str
    first_last_name:str
    second_last_name:Optional['str']
    second_name: Optional['str']



@order_distrimonster_router.post('/create-distrimonster-user')
def create_distrimonster_user(user_data:User):
    order_instance = Order2()
    result = order_instance.create_distrimonster_usuario(user_data=user_data)
    return result



@order_distrimonster_router.get('/order-to-validate-distri')
def get_orders_to_transfed():
    order_instance = Order2()
    result = order_instance.get_orders_to_validate()
    order_instance.close_connection()
    return result


