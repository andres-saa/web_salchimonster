from models.inventory.purchase_order import PurchaseOrder
from fastapi import APIRouter,HTTPException, status
from schema.inventory.inventory import GroupDailyInventoryItems,DailyInventoryItems,InventoryComplete
from schema.inventory.purchase_order import GroupPurchaseItems,PurchaseOrderItem,OrderComplete,PurchaseOrderStatus

order_purchase_router = APIRouter()


@order_purchase_router.get('/all-purchase_orders',tags=['purchase_order'])
def get_inventory_report():
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.get_all_purchase_orders()
    order_purchase_instance.close_connection()
    return data


@order_purchase_router.get('/all-purchase_orders_by_responsible_id/{responsible_id}', tags=['purchase_order'])
def get_inventory_report(responsible_id:int):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.get_all_purchase_orders_by_responsible_id(responsible_id)
    order_purchase_instance.close_connection()
    return data


@order_purchase_router.get('/all-purchase_orders_by_lap_id/{lap_id}', tags=['purchase_order'])
def get_inventory_report(lap_id:int):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.get_all_purchase_orders_by_lap_id(lap_id)
    order_purchase_instance.close_connection()
    return data




@order_purchase_router.get('/all-purchase-orders-filtered/{responsible_id}/{start_date}/{end_date}', tags=['purchase_order'])

def get_inventory_report(responsible_id: int, start_date: str, end_date: str):
    order_purchase_instance = PurchaseOrder()

    try:
        data = order_purchase_instance.get_all_purchase_order_by_responsible_id_filtered(responsible_id, start_date, end_date)
        return data
    finally:
        order_purchase_instance.close_connection()



@order_purchase_router.get('/all-purchase-orders-by-site-filtered/{site_ids}/{start_date}/{end_date}' , tags=['purchase_order'])
def get_filtered_inventory_report(site_ids: str, start_date: str, end_date: str):
    # Convertir la cadena de site_ids en una lista de enteros
    site_ids_list = list(map(int, site_ids.split(',')))
    order_purchase_instance = PurchaseOrder()
    try:
        data = order_purchase_instance.get_all_purchase_order_by_sites_filtered(site_ids_list, start_date, end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        order_purchase_instance.close_connection()



@order_purchase_router.get('/purchase-order-entries-by-purchase-id/{daily_inventory_id}', tags=['purchase_order'] )
def get_inventory_report(daily_inventory_id:int):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.get_purchase_order_entries_by_order_purchase_id(daily_inventory_id)
    order_purchase_instance.close_connection()
    return data


@order_purchase_router.get('/get_purchase_item_groups_with_items', tags=['purchase_order'] )
def get_inventory_report():
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.get_purchase_item_groups_with_items()
    order_purchase_instance.close_connection()
    return data


@order_purchase_router.post('/insert_complete_order')
def insert_complete_inventory(complete_order_data: OrderComplete):
    inventory_instance = PurchaseOrder()
    try:
        inventory_id = inventory_instance.insert_complete_order(
            complete_order_data.order_purchase.responsible_id,
            complete_order_data.order_purchase.site_id,
            complete_order_data.order_purchase_items
        )
    except Exception as e:
        inventory_instance.close_connection()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    inventory_instance.close_connection()
    return {"message": "Inventory created successfully", "inventory_id": inventory_id}




@order_purchase_router.post('/prepare-purchase-order')
def insert_complete_inventory(prepare_order_data: PurchaseOrderStatus):
    inventory_instance = PurchaseOrder()
    try:
        inventory_id = inventory_instance.chage_order_purchase_status(prepare_order_data
        )
    except Exception as e:  
        inventory_instance.close_connection()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    inventory_instance.close_connection()
    return {"message": "Inventory created successfully", "inventory_id": inventory_id}







@order_purchase_router.get('/group-purchase-items-by-group-name/{daily_item_group_name}' , tags=['purchase_order'])
def get_inventory_items_by_group_name(daily_item_group_name: str):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.get_all_purchase_order_item_by_group_name(daily_item_group_name)
    order_purchase_instance.close_connection()
    return data




@order_purchase_router.get('/purchase-order-history/{purchase_order_id}' , tags=['purchase_order'])
def get_inventory_items_by_group_name(purchase_order_id: str):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.get_all_purchase_order_history(purchase_order_id)
    order_purchase_instance.close_connection()
    return data



@order_purchase_router.get('/all_purchase_order_group_items' , tags=['purchase_order'])
def get_inventory_report():
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.get_all_purchase_order_group_items()
    order_purchase_instance.close_connection()
    return data

@order_purchase_router.post('/insert_purchase_items_group')
def insert_daily_inventory_group( daily_group_data :  GroupPurchaseItems):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.insert_purchase_items_group(daily_group_data)
    order_purchase_instance.close_connection()
    return data


@order_purchase_router.post('/insert_purchase_order_item')
def insert_daily_inventory_item( purchase_order_item :  PurchaseOrderItem):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.insert_purchase_group_item(purchase_order_item)
    order_purchase_instance.close_connection()
    return data



@order_purchase_router.put('/disable_purchase_order_group/{group_id}')
def disable_daily_inventory_group( group_id :  int):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.disable_purchase_order_group(group_id)
    order_purchase_instance.close_connection()
    return data


@order_purchase_router.put('/disable_order_purchase_item/{item_id}')
def disable_daily_inventory_group( item_id :  int):
    order_purchase_instance =  PurchaseOrder()
    data = order_purchase_instance.disable_order_purchase_item(item_id)
    order_purchase_instance.close_connection()
    return data