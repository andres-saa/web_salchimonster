from fastapi import APIRouter
from models.pqr.pqr import Pqrs
from schema.pqr import pqrs as pqr_schema
from schema.user import user_schema_post
from pydantic import BaseModel
from fastapi import Query
from models.users.users import Users

user_router = APIRouter()





class sites(BaseModel):
    ids:list[int]



class report(BaseModel):
    start_date:str
    end_date:str
    sites:list[int]



@user_router.post("/get_user_report/", tags=["users"])
def get_pqrs_by_date_range(data:report):
    """
    Obtiene las PQRs cuyo estado actual esté entre las fechas proporcionadas.
    :param fecha_inicio: Fecha de inicio (formato: YYYY-MM-DD)
    :param fecha_fin: Fecha de fin (formato: YYYY-MM-DD)
    :return: Lista de PQRs agrupadas por sede y estados en JSON.
    """
    user_instance = Users()
    result = user_instance.get_user_report(data.sites,data.start_date, data.end_date )
    return result

