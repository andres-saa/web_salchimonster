from fastapi import APIRouter, HTTPException,Path,Body,WebSocket,WebSocketDisconnect,websockets,Query
from models.orders.order import Order
from schema.orders.order import Orders,DeliveryPersons,OrderNotes,OrderStatus,OrderStatusHistory,PaymentMethodOptions,Cancellation_request
from typing import List,Dict
from schema.order import OrderSchemaPost
from models.orders.order2 import Order2
from models.payment_method import Pyment_method
contest_router = APIRouter()
from pydantic import BaseModel

from fastapi import APIRouter
from schema.order import order_schema_post
from models.order import Order
from fastapi import APIRouter, HTTPException
from datetime import datetime
from pytz import timezone
import pytz 

from schema.contests.contest import Contest,evidence,Contest_entry 
from models.contest.contest import Contest



contest_router = APIRouter()


# @contest_router.post("/order")
# async def create_order(order_data: OrderSchemaPost):
#     order_instance = Order2()
#     try:
#         result = order_instance.create_order(order_data)
#         # Notify the site associated with the order
#         await notify_sites(order_data.site_id, "Order processed")
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))




@contest_router.get('/contests/{participant_id}')
def get_orders_gy_site(participant_id:int):
    order_instance = Contest()
    result = order_instance.get_all_contests_with_participation(participant_id)
    order_instance.close_connection()
    return result


