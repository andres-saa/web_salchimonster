from fastapi import APIRouter


from models.pqrs.pqrs import Pqrs
from schema.pqrs.pqrs import Pqrs as pqrs_schema
import random


Pqrs_router = APIRouter()



@Pqrs_router.get('/get-pqrs-by-place-id/{place_id}', tags=['pqrs'])
def get_qprs_by_place_id(place_id:int):

    pqrs_instance = Pqrs()
    result = pqrs_instance.get_pqrs_by_place_id(place_id)
    pqrs_instance.close_connection()
    return result   


@Pqrs_router.post('/create_pqrs/', tags=['pqrs'])
def get_qprs_by_place_id(data:pqrs_schema):

    pqrs_instance = Pqrs()
    result = pqrs_instance.create_pqrs(data)
    pqrs_instance.close_connection()
    return result   
    









@Pqrs_router.put('/update_pqrs/{id}', tags=['pqrs'])
def get_qprs_by_place_id(data:pqrs_schema, id:int):

    pqrs_instance = Pqrs()
    result = pqrs_instance.update_pqrs(data,id)
    pqrs_instance.close_connection()
    return result   




@Pqrs_router.delete('/delete_pqrs/{id}', tags=['pqrs'])
def get_qprs_by_place_id( id:int):

    pqrs_instance = Pqrs()
    result = pqrs_instance.deactivate_pqrs(id)
    pqrs_instance.close_connection()
    return result   



