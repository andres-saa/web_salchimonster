from models.inventory.daily_inventory import DailyInventory
from fastapi import APIRouter,HTTPException, status
from schema.inventory.inventory import GroupDailyInventoryItems,DailyInventoryItems,InventoryComplete,UnitMeasure



daily_inventory_router = APIRouter()


@daily_inventory_router.get('/all-daily-inventory-report')
def get_inventory_report():
    inventory_report_Instance =  DailyInventory()

    data = inventory_report_Instance.get_all_daily_Inventory_reports()
    inventory_report_Instance.close_connection()
    return data


@daily_inventory_router.get('/all-daily-inventory-report/{responsible_id}')
def get_inventory_report(responsible_id:int):
    inventory_report_Instance =  DailyInventory()

    data = inventory_report_Instance.get_all_daily_Inventory_reports_by_responsible_id(responsible_id)
    inventory_report_Instance.close_connection()
    return data

@daily_inventory_router.get('/all-daily-inventory-report/{responsible_id}/{start_date}/{end_date}')

def get_inventory_report(responsible_id: int, start_date: str, end_date: str):
    inventory_report_instance = DailyInventory()

    try:
        data = inventory_report_instance.get_all_daily_inventory_reports_by_responsible_id_filtered(responsible_id, start_date, end_date)
        return data
    finally:
        inventory_report_instance.close_connection()

@daily_inventory_router.get('/all-daily-inventory-report-filtered/{site_ids}/{start_date}/{end_date}')
def get_filtered_inventory_report(site_ids: str, start_date: str, end_date: str):
    # Convertir la cadena de site_ids en una lista de enteros
    site_ids_list = list(map(int, site_ids.split(',')))

    inventory_report_instance = DailyInventory()
    try:
        data = inventory_report_instance.get_all_daily_inventory_reports_filtered(site_ids_list, start_date, end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        inventory_report_instance.close_connection()

@daily_inventory_router.get('/daily-inventory-entries/{daily_inventory_id}')
def get_inventory_report(daily_inventory_id:int):
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.get_all_daily_Inventory_entries(daily_inventory_id)
    inventory_report_Instance.close_connection()
    return data


@daily_inventory_router.get('/group_daily_inventory_items')
def get_inventory_report():
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.get_all_daily_group_items()
    inventory_report_Instance.close_connection()
    return data


@daily_inventory_router.post('/insert_complete_inventory')
def insert_complete_inventory(complete_inventory_data: InventoryComplete):
    inventory_instance = DailyInventory()
    try:
        inventory_id = inventory_instance.insert_complete_inventory(
            complete_inventory_data.daily_inventory.responsible_id,
            complete_inventory_data.daily_inventory.site_id,
            complete_inventory_data.daily_inventory_items
        )
    except Exception as e:
        inventory_instance.close_connection()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    inventory_instance.close_connection()
    return {"message": "Inventory created successfully", "inventory_id": inventory_id}


@daily_inventory_router.get('/get_groups_with_items')
def get_inventory_report():
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.get_groups_with_items()
    inventory_report_Instance.close_connection()
    return data

@daily_inventory_router.get('/daily_inventory_unit_measures' , tags=['purchase_order'])
def get_inventory_report():
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.get_all_daily_group_unit_measures()
    inventory_report_Instance.close_connection()
    return data

@daily_inventory_router.get('/group_daily_inventory_items/{daily_item_group_name}')
def get_inventory_items_by_group_name(daily_item_group_name: str):
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.get_all_daily_Inventory_item_by_group_name(daily_item_group_name)
    inventory_report_Instance.close_connection()
    return data


@daily_inventory_router.post('/insert_daily_inventory_group')
def insert_daily_inventory_group( daily_group_data :  GroupDailyInventoryItems):
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.insert_daily_inventory_group(daily_group_data)
    inventory_report_Instance.close_connection()
    return data


@daily_inventory_router.post('/insert_daily_inventory_item')
def insert_daily_inventory_item( daily_group_item :  DailyInventoryItems):
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.insert_daily_inventory_item(daily_group_item)
    inventory_report_Instance.close_connection()
    return data


@daily_inventory_router.post('/insert_unit_measure')
def insert_daily_inventory_item( data_unit_measure :  UnitMeasure):
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.insert_unit_measure(data_unit_measure.name)
    inventory_report_Instance.close_connection()
    return data


@daily_inventory_router.put('/disable_daily_inventory_group/{group_id}')
def disable_daily_inventory_group( group_id :  int):
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.disable_daily_inventory_group(group_id)
    inventory_report_Instance.close_connection()
    return data


@daily_inventory_router.put('/disable_unit_measure/{unit_measure_id}')
def disable_daily_inventory_group( unit_measure_id :  int):
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.disable_unit_measure(unit_measure_id)
    inventory_report_Instance.close_connection()
    return data 

@daily_inventory_router.put('/disable_daily_inventory_item/{item_id}')
def disable_daily_inventory_group( item_id :  int):
    inventory_report_Instance =  DailyInventory()
    data = inventory_report_Instance.disable_daily_inventory_item(item_id)
    inventory_report_Instance.close_connection()
    return data