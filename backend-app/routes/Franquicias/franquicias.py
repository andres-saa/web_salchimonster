from fastapi import APIRouter
from schema.franquicias.franquicias import Franquicias
from models.Franquicias.franquicias import Franquis




franquis_router = APIRouter()



@franquis_router.post('/create_franquicia_request',tags=["franquicias"])
def create_franquicias(data:Franquicias):
    Franquis_instance = Franquis()
    result = Franquis_instance.create_franquicia_request(data=data)
    return result


@franquis_router.get('/get_franquicia_request',tags=["franquicias"])
def get_franquicias():
    Franquis_instance = Franquis()
    result = Franquis_instance.get_franquicia_request()
    return result


@franquis_router.put('/update_franquicia_request/{id}',tags=["franquicias"])
def get_franquicias(data:Franquicias,id:int):
    Franquis_instance = Franquis()
    result = Franquis_instance.change_status(data,id)
    return result