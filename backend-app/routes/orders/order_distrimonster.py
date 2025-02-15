from fastapi import APIRouter, HTTPException,Path,Body,WebSocket,WebSocketDisconnect,websockets,Query
from models.orders.order import Order
from schema.orders.order import Orders,DeliveryPersons,OrderNotes,OrderStatus,OrderStatusHistory,PaymentMethodOptions,Cancellation_request
from typing import List,Dict
from schema.order import OrderSchemaPost
from models.orders.order_distrimonster import Order2
from models.payment_method import Pyment_method
order_distrimonster_router = APIRouter()
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
order_distrimonster_router = APIRouter()
from datetime import datetime, timedelta
from dateutil import parser




connected_clients: Dict[int, List[WebSocket]] = {}



@order_distrimonster_router.post("/order-distrimonster")
async def create_order(order_data: OrderSchemaPost):
    order_instance = Order2()
    try:
        result = order_instance.create_order(order_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


