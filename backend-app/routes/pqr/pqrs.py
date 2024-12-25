from fastapi import APIRouter
from models.pqr.pqr import Pqrs
from schema.pqr import pqrs as pqr_schema
from schema.user import user_schema_post
from pydantic import BaseModel
from fastapi import Query

pqr_router = APIRouter()



@pqr_router.post("/create-pqr",tags=["pqr"])
def create_pqrs(data:pqr_schema.PQRRequest,user:user_schema_post):
    pqr_instance = Pqrs()
    result = pqr_instance.create_pqr(data,user)
    return result



@pqr_router.get("/get-all-pqrs",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_pqrs()
    return result



@pqr_router.get('/recent-pqr' ,tags=["pqr"])
def recent():
    pqr_instance = Pqrs()
    result = pqr_instance.is_recent_pqr_generated()
    return result





@pqr_router.get("/get-all-networks",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_networks()
    return result




@pqr_router.get("/get-all-pqr-tags",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_tags()
    return result

@pqr_router.get("/get-pqrs-by-date-range/{fecha_inicio}/{fecha_fin}", tags=["pqr"])
def get_pqrs_by_date_range(fecha_inicio:str, fecha_fin:str):
    """
    Obtiene las PQRs cuyo estado actual esté entre las fechas proporcionadas.
    :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD)
    :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD)
    :return: Lista de PQRs agrupadas por sede y estados en JSON.
    """
    pqr_instance = Pqrs()
    result = pqr_instance.get_pqrs_by_date_range(fecha_inicio, fecha_fin)
    return result




@pqr_router.get("/get-pqrs-by-date-range-types/{fecha_inicio}/{fecha_fin}", tags=["pqr"])
def get_pqrs_by_date_range(fecha_inicio:str, fecha_fin:str):
    """
    Obtiene las PQRs cuyo estado actual esté entre las fechas proporcionadas.
    :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD)
    :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD)
    :return: Lista de PQRs agrupadas por sede y estados en JSON.
    """
    pqr_instance = Pqrs()
    result = pqr_instance.get_pqrs_by_date_range_and_type(fecha_inicio, fecha_fin)
    return result





@pqr_router.get("/get_pqrs_by_responsible_and_state/{fecha_inicio}/{fecha_fin}", tags=["pqr"])
def get_pqrs_by_date_range(fecha_inicio:str, fecha_fin:str):
    """
    Obtiene las PQRs cuyo estado actual esté entre las fechas proporcionadas.
    :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD)
    :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD)
    :return: Lista de PQRs agrupadas por sede y estados en JSON.
    """
    pqr_instance = Pqrs()
    result = pqr_instance.get_pqrs_by_responsible_and_state(fecha_inicio, fecha_fin)
    return result



class sites(BaseModel):
    ids:list[int]

@pqr_router.post("/get_daily_pqrs_report/{fecha_inicio}/{fecha_fin}", tags=["pqr"])
def get_pqrs_by_date_range(fecha_inicio:str, fecha_fin:str, site_ids:sites):
    """
    Obtiene las PQRs cuyo estado actual esté entre las fechas proporcionadas.
    :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD)
    :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD)
    :return: Lista de PQRs agrupadas por sede y estados en JSON.
    """
    pqr_instance = Pqrs()
    result = pqr_instance.get_daily_pqrs_report( site_ids.ids,fecha_inicio, fecha_fin )
    return result





@pqr_router.get("/get-all-pqr-channel",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_channels()
    return result

@pqr_router.get("/get-all-pqrs-types",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_types()
    return result

@pqr_router.get("/get-all-pqrs-status",tags=["pqr"])
def create_pqrs():
    pqr_instance = Pqrs()
    result = pqr_instance.get_all_status()
    return result



from typing import Optional
class ChangeStatusRequest(BaseModel):
    pqr_request_id: int
    status_id: int
    responsible_id: int
    value: Optional[int] = None
    notes: str = ''
    order_id:Optional[str] = None


@pqr_router.post("/change-pqr-status", tags=["pqr"])
def change_pqr_status(data: ChangeStatusRequest):
    pqr_instance = Pqrs()
    result = pqr_instance.update_pqr_status(data)
    return result