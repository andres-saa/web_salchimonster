from fastapi import APIRouter, HTTPException

# Importaciones de Adicional (ya incluidas en tu código)
from models.adicionales.adicional import Adicional
from schema.adicionales.adicional import adicionalSchemaPost

# Importaciones de Salsa
from models.adicionales.salsas import Salsas  # Ajusta la ruta según la estructura de tu proyecto
from schema.adicionales.salsas import SalsaSchemaPost

# Importaciones para Toppings (ajusta las rutas según sea necesario)
from models.adicionales.toppings import Toppings    
from schema.adicionales.toppings import ToppingSchemaPost

# Importaciones para Acompañantes (ajusta las rutas según sea necesario)
from models.adicionales.acompanantes import Acompanantes
from schema.adicionales.acompanantes import AcompananteSchemaPost

# Importaciones para Cambios (ajusta las rutas según sea necesario)
from models.adicionales.cambios import Cambios
from schema.adicionales.cambios import CambioSchemaPost






adicional_router = APIRouter()

@adicional_router.get("/adicionales" , tags=['products'])
def get_adicionales():
    adicional_instance = Adicional()
    adicionales = adicional_instance.select_all_adicionales()
    adicional_instance.close_connection()
    return adicionales



@adicional_router.post("/adicionales" , tags=['products'])
def create_adicional(adicional: adicionalSchemaPost):
    adicional_instance = Adicional()
    adicional_id = adicional_instance.insert_adicional(adicional)
    created_adicional = adicional_instance.select_adicional_by_id(adicional_id)
    adicional_instance.close_connection()
    return {"adicional_id": created_adicional[0]}

@adicional_router.put("/adicionales/{adicional_id}" , tags=['products'])
def update_adicional(adicional_id: int, adicional: adicionalSchemaPost):
    adicional_instance = Adicional()
    existing_adicional = adicional_instance.select_adicional_by_id(adicional_id)
    if existing_adicional is None:
        raise HTTPException(status_code=404, detail="Adicional not found")
    
    adicional_instance.update_adicional(adicional_id, adicional)
    updated_adicional = adicional_instance.select_adicional_by_id(adicional_id)
    adicional_instance.close_connection()
    return {"message": "Adicional updated successfully", "adicional_id": adicional_id}

@adicional_router.delete("/adicionales/{adicional_id}" , tags=['products'])
def delete_adicional(adicional_id: int):
    adicional_instance = Adicional()
    existing_adicional = adicional_instance.select_adicional_by_id(adicional_id)
    if existing_adicional is None:
        raise HTTPException(status_code=404, detail="Adicional not found")
    
    adicional_instance.delete_adicional(adicional_id)
    adicional_instance.close_connection()
    return {"message": "Adicional deleted successfully", "deleted_adicional": existing_adicional}

# Agrega más rutas según sea necesario


salsa_router = APIRouter()

@salsa_router.post("/salsas" , tags=['products'])
def create_salsa(salsa: SalsaSchemaPost):
    salsa_instance = Salsas()
    salsa_id = salsa_instance.insert_salsa(salsa)
    salsa_instance.close_connection()
    return {"salsa_id": salsa_id}

@salsa_router.get("/salsas" , tags=['products'])
def get_all_salsas():
    salsa_instance = Salsas()
    salsas = salsa_instance.select_all_salsas()
    salsa_instance.close_connection()
    return salsas

@salsa_router.get("/salsas/{salsa_id}" , tags=['products'])
def get_salsa(salsa_id: int):
    salsa_instance = Salsas()
    salsa = salsa_instance.select_salsa_by_id(salsa_id)
    salsa_instance.close_connection()
    if not salsa:
        raise HTTPException(status_code=404, detail="Salsa not found")
    return salsa

@salsa_router.put("/salsas/{salsa_id}" , tags=['products'])
def update_salsa(salsa_id: int, salsa: SalsaSchemaPost):
    salsa_instance = Salsas()
    salsa_instance.update_salsa(salsa_id, salsa)
    updated_salsa = salsa_instance.select_salsa_by_id(salsa_id)
    salsa_instance.close_connection()
    if not updated_salsa:
        raise HTTPException(status_code=404, detail="Salsa not found")
    return updated_salsa

@salsa_router.delete("/salsas/{salsa_id}" , tags=['products'])
def delete_salsa(salsa_id: int):
    salsa_instance = Salsas()
    salsa_instance.delete_salsa(salsa_id)
    salsa_instance.close_connection()
    return {"message": "Salsa deleted successfully"}



topping_router = APIRouter()

@topping_router.get("/toppings" , tags=['products'])
def get_all_toppings():
    topping_instance = Toppings()
    toppings = topping_instance.select_all_toppings()
    topping_instance.close_connection()
    return toppings

@topping_router.post("/toppings" , tags=['products'])
def create_topping(topping: ToppingSchemaPost):
    topping_instance = Toppings()
    topping_id = topping_instance.insert_topping(topping)
    topping_instance.close_connection()
    return {"topping_id": topping_id}

@topping_router.get("/toppings/{topping_id}" , tags=['products'])
def get_topping(topping_id: int):
    topping_instance = Toppings()
    topping = topping_instance.select_topping_by_id(topping_id)
    topping_instance.close_connection()
    if not topping:
        raise HTTPException(status_code=404, detail="Topping not found")
    return topping

@topping_router.put("/toppings/{topping_id}" , tags=['products'])
def update_topping(topping_id: int, topping_data: ToppingSchemaPost):
    topping_instance = Toppings()
    topping_instance.update_topping(topping_id, topping_data)
    updated_topping = topping_instance.select_topping_by_id(topping_id)
    topping_instance.close_connection()
    if not updated_topping:
        raise HTTPException(status_code=404, detail="Topping not found")
    return updated_topping

@topping_router.delete("/toppings/{topping_id}" , tags=['products'])
def delete_toppings(topping_id: int):
    topping_instance = Topping()
    topping_instance.delete_topping(topping_id)
    topping_instance.close_connection()
    return {"message": "Topping deleted successfully"}

acompanante_router = APIRouter()

@acompanante_router.post("/acompanantes" , tags=['products'])
def create_acompanante(acompanante: AcompananteSchemaPost):
    acompanante_instance = Acompanantes()
    acompanante_id = acompanante_instance.insert_acompanante(acompanante)
    acompanante_instance.close_connection()
    return {"acompanante_id": acompanante_id}

@acompanante_router.get("/acompanantes" , tags=['products'])
def get_all_acompanantes():
    acompanante_instance = Acompanantes()
    acompanantes = acompanante_instance.select_all_acompanantes()
    acompanante_instance.close_connection()
    return acompanantes

@acompanante_router.get("/acompanantes/{acompanante_id}" , tags=['products'])
def get_acompanante(acompanante_id: int):
    acompanante_instance = Acompanantes()
    acompanante = acompanante_instance.select_acompanante_by_id(acompanante_id)
    acompanante_instance.close_connection()
    if not acompanante:
        raise HTTPException(status_code=404, detail="Acompanante not found")
    return acompanante

@acompanante_router.put("/acompanantes/{acompanante_id}" , tags=['products'])
def update_acompanante(acompanante_id: int, acompanante_data: AcompananteSchemaPost):
    acompanante_instance = Acompanantes()
    acompanante_instance.update_acompanante(acompanante_id, acompanante_data)
    updated_acompanante = acompanante_instance.select_acompanante_by_id(acompanante_id)
    acompanante_instance.close_connection()
    if not updated_acompanante:
        raise HTTPException(status_code=404, detail="Acompanante not found")
    return updated_acompanante

@acompanante_router.delete("/acompanantes/{acompanante_id}" , tags=['products'])
def delete_acompanante(acompanante_id: int):
    acompanante_instance = Acompanantes()
    acompanante_instance.delete_acompanante(acompanante_id)
    acompanante_instance.close_connection()
    return {"message": "Acompanante deleted successfully"}


cambio_router = APIRouter()

@cambio_router.post("/cambios" , tags=['products'])
def create_cambio(cambio: CambioSchemaPost):
    cambio_instance = Cambios()
    cambio_id = cambio_instance.insert_cambio(cambio)
    cambio_instance.close_connection()
    return {"cambio_id": cambio_id}

@cambio_router.get("/cambios/{cambio_id}" , tags=['products'])
def get_cambio(cambio_id: int):
    cambio_instance = Cambios()
    cambio = cambio_instance.select_cambio_by_id(cambio_id)
    cambio_instance.close_connection()
    if not cambio:
        raise HTTPException(status_code=404, detail="Cambio not found")
    return cambio

@cambio_router.put("/cambios/{cambio_id}" , tags=['products'])
def update_cambio(cambio_id: int, cambio_data: CambioSchemaPost):
    cambio_instance = Cambios()
    cambio_instance.update_cambio(cambio_id, cambio_data)
    updated_cambio = cambio_instance.select_cambio_by_id(cambio_id)
    cambio_instance.close_connection()
    if not updated_cambio:
        raise HTTPException(status_code=404, detail="Cambio not found")
    return updated_cambio

@cambio_router.delete("/cambios/{cambio_id}" , tags=['products'])
def delete_cambio(cambio_id: int):
    cambio_instance = Cambios()
    cambio_instance.delete_cambio(cambio_id)
    cambio_instance.close_connection()
    return {"message": "Cambio deleted successfully"}


@cambio_router.get("/cambios" , tags=['products'])
def get_all_cambios():
    cambio_instance = Cambios()
    cambios = cambio_instance.select_all_cambios()
    cambio_instance.close_connection()
    return cambios