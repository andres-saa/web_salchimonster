from fastapi import APIRouter, HTTPException,Path,Body,WebSocket,WebSocketDisconnect,websockets,Query
from models.app.salchigets import salchigest

salchigest_router = APIRouter()


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




@salchigest_router.get('/get-salchigest-version/',tags=['app'])
def get_orders_gy_site():
    contest_instance = salchigest()
    result = contest_instance.get_version()
    contest_instance.close_connection()
    return result