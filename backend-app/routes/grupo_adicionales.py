# routers/grupo_adicionales_router.py
from fastapi import APIRouter, HTTPException
from models.adicionales.grupo_adicionales import GrupoAdicionales
from schema.adicionales.grupo_adicionales import GrupoAdicionalesSchemaPost




# # Importaciones de Salsa
from models.adicionales.grupo_salsas import  GrupoSalsas# Ajusta la ruta según la estructura de tu proyecto
from schema.adicionales.grupo_salsas import GrupoSalsasSchemaPost

# Importaciones para Toppings (ajusta las rutas según sea necesario)
from models.adicionales.grupo_toppings import GrupoToppings    
from schema.adicionales.grupo_toppings import GrupoToppingsSchemaPost

# Importaciones para Acompañantes (ajusta las rutas según sea necesario)
from models.adicionales.grupo_acompanantes import GrupoAcompanantes
from schema.adicionales.grupo_acompanantes import GrupoAcompanantesSchemaPost

# Importaciones para Cambios (ajusta las rutas según sea necesario)
from models.adicionales.grupo_cambios import GrupoCambios
from schema.adicionales.grupo_cambios import GrupoCambiosSchemaPost



grupo_adicionales_router = APIRouter()

@grupo_adicionales_router.post("/grupo-adicionales")
def create_grupo_adicionales(grupo_data: GrupoAdicionalesSchemaPost):
    grupo_instance = GrupoAdicionales()
    grupo_id = grupo_instance.insert_grupo_adicionales(grupo_data)
    grupo_instance.close_connection()
    return {"grupo_id": grupo_id}

@grupo_adicionales_router.get("/grupo-adicionales")
def get_all_grupos():
    grupo_instance = GrupoAdicionales()
    grupos = grupo_instance.select_all_grupos()
    grupo_instance.close_connection()
    return grupos

@grupo_adicionales_router.get("/grupo-adicionales/{grupo_id}")
def get_grupo_by_id(grupo_id: int):
    grupo_instance = GrupoAdicionales()
    grupo = grupo_instance.select_grupo_by_id(grupo_id)
    grupo_instance.close_connection()
    if grupo is None:
        raise HTTPException(status_code=404, detail="Grupo not found")
    return grupo

@grupo_adicionales_router.get("/grupo-adicionales/{grupo_id}/adicionales")
def get_adicionales_by_grupo(grupo_id: int):
    grupo_adicionales_instance = GrupoAdicionales()
    adicionales = grupo_adicionales_instance.get_adicionales_by_grupo_id(grupo_id)
    grupo_adicionales_instance.close_connection()
    if not adicionales:
        raise HTTPException(status_code=404, detail="Grupo Adicionales not found or no adicionales associated")
    return adicionales

@grupo_adicionales_router.put("/grupo-adicionales/{grupo_id}")
def update_grupo(grupo_id: int, grupo_data: GrupoAdicionalesSchemaPost):
    grupo_instance = GrupoAdicionales()
    grupo_instance.update_grupo(grupo_id, grupo_data)
    updated_grupo = grupo_instance.select_grupo_by_id(grupo_id)
    grupo_instance.close_connection()
    if updated_grupo is None:
        raise HTTPException(status_code=404, detail="Grupo not found")
    return {"message": "Grupo updated successfully", "grupo": updated_grupo}

@grupo_adicionales_router.delete("/grupo-adicionales/{grupo_id}")
def delete_grupo(grupo_id: int):
    grupo_instance = GrupoAdicionales()
    grupo_instance.delete_grupo(grupo_id)
    grupo_instance.close_connection()
    return {"message": "Grupo deleted successfully"}


grupo_toppings_router = APIRouter()



@grupo_toppings_router.get("/grupo-toppings/{grupo_topping_id}/toppings")
def get_toppings_by_grupo_id(grupo_topping_id: int):
    grupo_toppings_instance = GrupoToppings()
    toppings = grupo_toppings_instance.get_toppings_by_grupo_id(grupo_topping_id)
    grupo_toppings_instance.close_connection()
    if not toppings:
        raise HTTPException(status_code=404, detail="No toppings found for this grupo_topping_id")
    return toppings

@grupo_toppings_router.post("/grupo-toppings")
def create_grupo_toppings(grupo_data: GrupoToppingsSchemaPost):
    grupo_toppings_instance = GrupoToppings()
    grupo_id = grupo_toppings_instance.insert_grupo_toppings(grupo_data)
    grupo_toppings_instance.close_connection()
    return {"grupo_topping_id": grupo_id}

@grupo_toppings_router.get("/grupo-toppings")
def get_all_grupos_toppings():
    grupo_toppings_instance = GrupoToppings()
    grupos = grupo_toppings_instance.select_all_grupos_toppings()
    grupo_toppings_instance.close_connection()
    return grupos

@grupo_toppings_router.get("/grupo-toppings/{grupo_topping_id}")
def get_grupo_toppings(grupo_topping_id: int):
    grupo_toppings_instance = GrupoToppings()
    grupo = grupo_toppings_instance.select_grupo_toppings_by_id(grupo_topping_id)
    grupo_toppings_instance.close_connection()
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo Toppings not found")
    return grupo

@grupo_toppings_router.put("/grupo-toppings/{grupo_topping_id}")
def update_grupo_toppings(grupo_topping_id: int, grupo_data: GrupoToppingsSchemaPost):
    grupo_toppings_instance = GrupoToppings()
    grupo_toppings_instance.update_grupo_toppings(grupo_topping_id, grupo_data)
    updated_grupo = grupo_toppings_instance.select_grupo_toppings_by_id(grupo_topping_id)
    grupo_toppings_instance.close_connection()
    if not updated_grupo:
        raise HTTPException(status_code=404, detail="Grupo Toppings not found")
    return {"message": "Grupo Toppings updated successfully"}

@grupo_toppings_router.delete("/grupo-toppings/{grupo_topping_id}")
def delete_grupo_toppings(grupo_topping_id: int):
    grupo_toppings_instance = GrupoToppings()
    grupo_toppings_instance.delete_grupo_toppings(grupo_topping_id)
    grupo_toppings_instance.close_connection()
    return {"message": "Grupo Toppings deleted successfully"}


    

grupo_salsas_router = APIRouter()


@grupo_salsas_router.post("/grupo-salsas")
def create_grupo_salsas(grupo_data: GrupoSalsasSchemaPost):
    grupo_salsas_instance = GrupoSalsas()
    grupo_id = grupo_salsas_instance.insert_grupo_salsas(grupo_data)
    grupo_salsas_instance.close_connection()
    return {"grupo_salsa_id": grupo_id}

@grupo_salsas_router.get("/grupo-salsas/{grupo_salsa_id}/salsas")
def get_salsas_by_grupo_id(grupo_salsa_id: int):
    grupo_salsas_instance = GrupoSalsas()
    salsas = grupo_salsas_instance.get_salsas_by_grupo_id(grupo_salsa_id)
    grupo_salsas_instance.close_connection()
    if not salsas:
        raise HTTPException(status_code=404, detail="No salsas found for this grupo_salsa_id")
    return salsas
@grupo_salsas_router.get("/grupo-salsas")
def get_all_grupos_salsas():
    grupo_salsas_instance = GrupoSalsas()
    grupos = grupo_salsas_instance.select_all_grupos_salsas()
    grupo_salsas_instance.close_connection()
    return grupos

@grupo_salsas_router.get("/grupo-salsas/{grupo_salsa_id}")
def get_grupo_salsas(grupo_salsa_id: int):
    grupo_salsas_instance = GrupoSalsas()
    grupo = grupo_salsas_instance.select_grupo_salsas_by_id(grupo_salsa_id)
    grupo_salsas_instance.close_connection()
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo Salsas not found")
    return grupo

@grupo_salsas_router.put("/grupo-salsas/{grupo_salsa_id}")
def update_grupo_salsas(grupo_salsa_id: int, grupo_data: GrupoSalsasSchemaPost):
    grupo_salsas_instance = GrupoSalsas()
    grupo_salsas_instance.update_grupo_salsas(grupo_salsa_id, grupo_data)
    updated_grupo = grupo_salsas_instance.select_grupo_salsas_by_id(grupo_salsa_id)
    grupo_salsas_instance.close_connection()
    if not updated_grupo:
        raise HTTPException(status_code=404, detail="Grupo Salsas not found")
    return {"message": "Grupo Salsas updated successfully"}

@grupo_salsas_router.delete("/grupo-salsas/{grupo_salsa_id}")
def delete_grupo_salsas(grupo_salsa_id: int):
    grupo_salsas_instance = GrupoSalsas()
    grupo_salsas_instance.delete_grupo_salsas(grupo_salsa_id)
    grupo_salsas_instance.close_connection()
    return {"message": "Grupo Salsas deleted successfully"}




grupo_acompanantes_router = APIRouter()
@grupo_acompanantes_router.get("/grupo-acompanantes/{grupo_acompanante_id}/acompanantes")
def get_acompanantes_by_grupo_id(grupo_acompanante_id: int):
    grupo_acompanantes_instance = GrupoAcompanantes()
    acompanantes = grupo_acompanantes_instance.get_acompanantes_by_grupo_id(grupo_acompanante_id)
    grupo_acompanantes_instance.close_connection()

    if not acompanantes:
        raise HTTPException(status_code=404, detail="No acompañantes found for this grupo_acompanante_id")
    return acompanantes

@grupo_acompanantes_router.post("/grupo-acompanantes")
def create_grupo_acompanantes(grupo_data: GrupoAcompanantesSchemaPost):
    grupo_acompanantes_instance = GrupoAcompanantes()
    grupo_id = grupo_acompanantes_instance.insert_grupo_acompanantes(grupo_data)
    grupo_acompanantes_instance.close_connection()
    return {"grupo_acompanante_id": grupo_id}

@grupo_acompanantes_router.get("/grupo-acompanantes")
def get_all_grupos_acompanantes():
    grupo_acompanantes_instance = GrupoAcompanantes()
    grupos = grupo_acompanantes_instance.select_all_grupos_acompanantes()
    grupo_acompanantes_instance.close_connection()
    return grupos

@grupo_acompanantes_router.get("/grupo-acompanantes/{grupo_acompanante_id}")
def get_grupo_acompanantes(grupo_acompanante_id: int):
    grupo_acompanantes_instance = GrupoAcompanantes()
    grupo = grupo_acompanantes_instance.select_grupo_acompanantes_by_id(grupo_acompanante_id)
    grupo_acompanantes_instance.close_connection()
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo Acompanantes not found")
    return grupo

@grupo_acompanantes_router.put("/grupo-acompanantes/{grupo_acompanante_id}")
def update_grupo_acompanantes(grupo_acompanante_id: int, grupo_data: GrupoAcompanantesSchemaPost):
    grupo_acompanantes_instance = GrupoAcompanantes()
    grupo_acompanantes_instance.update_grupo_acompanantes(grupo_acompanante_id, grupo_data)
    updated_grupo = grupo_acompanantes_instance.select_grupo_acompanantes_by_id(grupo_acompanante_id)
    grupo_acompanantes_instance.close_connection()
    if not updated_grupo:
        raise HTTPException(status_code=404, detail="Grupo Acompanantes not found")
    return {"message": "Grupo Acompanantes updated successfully"}

@grupo_acompanantes_router.delete("/grupo-acompanantes/{grupo_acompanante_id}")
def delete_grupo_acompanantes(grupo_acompanante_id: int):
    grupo_acompanantes_instance = GrupoAcompanantes()
    grupo_acompanantes_instance.delete_grupo_acompanantes(grupo_acompanante_id)
    grupo_acompanantes_instance.close_connection()
    return {"message": "Grupo Acompanantes deleted successfully"}




grupo_cambios_router = APIRouter()

@grupo_cambios_router.get("/grupo-cambios/{grupo_cambio_id}/cambios")
def get_cambios_by_grupo_id(grupo_cambio_id: int):
    grupo_cambios_instance = GrupoCambios()
    cambios = grupo_cambios_instance.get_cambios_by_grupo_id(grupo_cambio_id)
    grupo_cambios_instance.close_connection()

    if not cambios:
        raise HTTPException(status_code=404, detail="No cambios found for this grupo_cambio_id")

    return cambios


@grupo_cambios_router.post("/grupo-cambios")
def create_grupo_cambios(grupo_data: GrupoCambiosSchemaPost):
    grupo_cambios_instance = GrupoCambios()
    grupo_id = grupo_cambios_instance.insert_grupo_cambios(grupo_data)
    grupo_cambios_instance.close_connection()
    return {"grupo_cambio_id": grupo_id}

@grupo_cambios_router.get("/grupo-cambios")
def get_all_grupos_cambios():
    grupo_cambios_instance = GrupoCambios()
    grupos = grupo_cambios_instance.select_all_grupos_cambios()
    grupo_cambios_instance.close_connection()
    return grupos

@grupo_cambios_router.get("/grupo-cambios/{grupo_cambio_id}")
def get_grupo_cambios(grupo_cambio_id: int):
    grupo_cambios_instance = GrupoCambios()
    grupo = grupo_cambios_instance.select_grupo_cambios_by_id(grupo_cambio_id)
    grupo_cambios_instance.close_connection()
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo Cambios not found")
    return grupo

@grupo_cambios_router.put("/grupo-cambios/{grupo_cambio_id}")
def update_grupo_cambios(grupo_cambio_id: int, grupo_data: GrupoCambiosSchemaPost):
    grupo_cambios_instance = GrupoCambios()
    grupo_cambios_instance.update_grupo_cambios(grupo_cambio_id, grupo_data)
    updated_grupo = grupo_cambios_instance.select_grupo_cambios_by_id(grupo_cambio_id)
    grupo_cambios_instance.close_connection()
    if not updated_grupo:
        raise HTTPException(status_code=404, detail="Grupo Cambios not found")
    return {"message": "Grupo Cambios updated successfully"}

@grupo_cambios_router.delete("/grupo-cambios/{grupo_cambio_id}")
def delete_grupo_cambios(grupo_cambio_id: int):
    grupo_cambios_instance = GrupoCambios()
    grupo_cambios_instance.delete_grupo_cambios(grupo_cambio_id)
    grupo_cambios_instance.close_connection()
    return {"message": "Grupo Cambios deleted successfully"}
