from models.inventory.cdi_inventory import CdiInventory
from fastapi import APIRouter,HTTPException, status
from schema.inventory.cdi_inventory import GroupCdiInventoryItems,CdiInventoryItems,InventoryComplete,UnitMeasure



cdi_inventory_router = APIRouter()


@cdi_inventory_router.get('/all-cdi-inventory-report')
def get_inventory_report():
    inventory_report_Instance =  CdiInventory()

    data = inventory_report_Instance.get_all_cdi_Inventory_reports()
    inventory_report_Instance.close_connection()
    return data


@cdi_inventory_router.get('/all-cdi-inventory-report/{responsible_id}')
def get_inventory_report(responsible_id:int):
    inventory_report_Instance =  CdiInventory()

    data = inventory_report_Instance.get_all_cdi_Inventory_reports_by_responsible_id(responsible_id)
    inventory_report_Instance.close_connection()
    return data

@cdi_inventory_router.get('/all-cdi-inventory-report/{responsible_id}/{start_date}/{end_date}')

def get_inventory_report(responsible_id: int, start_date: str, end_date: str):
    inventory_report_instance = CdiInventory()

    try:
        data = inventory_report_instance.get_all_cdi_inventory_reports_by_responsible_id_filtered(responsible_id, start_date, end_date)
        return data
    finally:
        inventory_report_instance.close_connection()

@cdi_inventory_router.get('/all-cdi-inventory-report-filtered/{site_ids}/{start_date}/{end_date}')
def get_filtered_inventory_report(site_ids: str, start_date: str, end_date: str):
    # Convertir la cadena de site_ids en una lista de enteros
    site_ids_list = list(map(int, site_ids.split(',')))

    inventory_report_instance = CdiInventory()
    try:
        data = inventory_report_instance.get_all_cdi_inventory_reports_filtered(site_ids_list, start_date, end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        inventory_report_instance.close_connection()

@cdi_inventory_router.get('/cdi-inventory-entries/{cdi_inventory_id}')
def get_inventory_report(cdi_inventory_id:int):
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.get_all_cdi_Inventory_entries(cdi_inventory_id)
    inventory_report_Instance.close_connection()
    return data


@cdi_inventory_router.get('/group_cdi_inventory_items')
def get_inventory_report():
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.get_all_cdi_group_items()
    inventory_report_Instance.close_connection()
    return data


@cdi_inventory_router.post('/insert_cdi_complete_inventory')
def insert_complete_inventory(complete_inventory_data: InventoryComplete):
    inventory_instance = CdiInventory()
    try:
        inventory_id = inventory_instance.insert_complete_inventory(
            complete_inventory_data.cdi_inventory.responsible_id,
            complete_inventory_data.cdi_inventory.site_id,
            complete_inventory_data.cdi_inventory_items
        )
    except Exception as e:
        inventory_instance.close_connection()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    inventory_instance.close_connection()
    return {"message": "Inventory created successfully", "inventory_id": inventory_id}


@cdi_inventory_router.get('/get_cdi_groups_with_items')
def get_inventory_report():
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.get_groups_with_items()
    inventory_report_Instance.close_connection()
    return data

@cdi_inventory_router.get('/cdi_inventory_unit_measures' , tags=['purchase_order'])
def get_inventory_report():
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.get_all_cdi_group_unit_measures()
    inventory_report_Instance.close_connection()
    return data

@cdi_inventory_router.get('/group_cdi_inventory_items/{cdi_item_group_name}')
def get_inventory_items_by_group_name(cdi_item_group_name: str):
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.get_all_cdi_Inventory_item_by_group_name(cdi_item_group_name)
    inventory_report_Instance.close_connection()
    return data


@cdi_inventory_router.post('/insert_cdi_inventory_group')
def insert_cdi_inventory_group( cdi_group_data :  GroupCdiInventoryItems):
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.insert_cdi_inventory_group(cdi_group_data)
    inventory_report_Instance.close_connection()
    return data


@cdi_inventory_router.post('/insert_cdi_inventory_item')
def insert_cdi_inventory_item( cdi_group_item :  CdiInventoryItems):
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.insert_cdi_inventory_item(cdi_group_item)
    inventory_report_Instance.close_connection()
    return data


@cdi_inventory_router.post('/insert_unit_measure')
def insert_cdi_inventory_item( data_unit_measure :  UnitMeasure):
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.insert_unit_measure(data_unit_measure.name)
    inventory_report_Instance.close_connection()
    return data


@cdi_inventory_router.put('/disable_cdi_inventory_group/{group_id}')
def disable_cdi_inventory_group( group_id :  int):
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.disable_cdi_inventory_group(group_id)
    inventory_report_Instance.close_connection()
    return data


@cdi_inventory_router.put('/disable_unit_measure/{unit_measure_id}')
def disable_cdi_inventory_group( unit_measure_id :  int):
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.disable_unit_measure(unit_measure_id)
    inventory_report_Instance.close_connection()
    return data 

@cdi_inventory_router.put('/disable_cdi_inventory_item/{item_id}')
def disable_cdi_inventory_group( item_id :  int):
    inventory_report_Instance =  CdiInventory()
    data = inventory_report_Instance.disable_cdi_inventory_item(item_id)
    inventory_report_Instance.close_connection()
    return data