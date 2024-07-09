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

from schema.contests.contest import Contest as contest_schema,evidence,Contest_entry 
from models.contest.contest import Contest
from schema.contests.contest import evidence_post


contest_router = APIRouter()


# @contest_router.post("/order")
# async def create_order(order_data: OrderSchemaPost):
#     contest_instance = Order2()
#     try:
#         result = contest_instance.create_order(order_data)
#         # Notify the site associated with the order
#         await notify_sites(order_data.site_id, "Order processed")
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))




@contest_router.get('/contests_all/{participant_id}')
def get_orders_gy_site(participant_id:int):
    contest_instance = Contest()
    result = contest_instance.get_all_contests_with_participation(participant_id)
    contest_instance.close_connection()
    return result


@contest_router.get('/contests/{participant_id}')
def get_orders_gy_site(participant_id:int):
    contest_instance = Contest()
    result = contest_instance.get_all_contests_with_participation_visible(participant_id)
    contest_instance.close_connection()
    return result


@contest_router.post('/contest-entry/')
def create_contest_entry(evidence:evidence_post):
    contest_instance = Contest()
    result = contest_instance.create_participation(evidence.evidence,evidence.Contest_entry)
    contest_instance.close_connection()
    return result



@contest_router.post('/contest/')
def create_contest(contest:contest_schema):
    contest_instance = Contest()
    result = contest_instance.create_contest(contest)
    contest_instance.close_connection()
    return result

@contest_router.put('/contest/')
def create_contest(contest:contest_schema):
    contest_instance = Contest()
    result = contest_instance.update_contest(contest)
    contest_instance.close_connection()
    return result


@contest_router.get('/contest_entry_option/')
def create_contest():
    contest_instance = Contest()
    result = contest_instance.get_all_contest_entry_options()
    contest_instance.close_connection()
    return result


@contest_router.put('/contest_toggle_visible/status/{status}/id/{id}')
def toggle_contest_visible(status,id):
    contest_instance = Contest()
    result = contest_instance.toggle_constest_visible(status, id)
    contest_instance.close_connection()
    return result


@contest_router.delete('/delete-contest/{id}')
def toggle_contest_visible(id):
    contest_instance = Contest()
    result = contest_instance.delete_contest( id)
    contest_instance.close_connection()
    return result


@contest_router.get('/user-contest-participation/{participant_id}/{contest_id}')
def get_all_participation_by_user(participant_id:int,contest_id:int):
    contest_instance = Contest()
    result = contest_instance.get_all_participation_by_user(participant_id,contest_id)
    contest_instance.close_connection()
    return result

