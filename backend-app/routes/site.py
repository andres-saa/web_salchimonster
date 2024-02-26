from fastapi import APIRouter
from models.site import Site
from schema.site import site_schema_post

site_router = APIRouter()

@site_router.get("/sites")
def get_sites():
    site_instance = Site()
    sites = site_instance.select_all_sites()
    site_instance.close_connection()
    return sites


@site_router.get("/sites/city/{city_id}")
def get_sites_by_city_id(city_id: int):
    site_instance = Site()
    sites = site_instance.select_sites_by_city_id(city_id)
    site_instance.close_connection()
    return sites
    
@site_router.get("/site/{site_id}")
def get_site_by_id(site_id: int):
    site_instance = Site()
    site = site_instance.select_site_by_id(site_id)
    site_instance.close_connection()
    return site

@site_router.delete("/site/{site_id}")
def delete_site(site_id: int):
    site_instance = Site()
    result = site_instance.delete_site(site_id)
    site_instance.close_connection()
    return {"message": result}

@site_router.post("/site")
def create_site(site: site_schema_post):
    site_instance = Site()
    site_id = site_instance.insert_site(site)
    site_instance.close_connection()
    return {"site_id": site_id}

@site_router.put("/site/{site_id}")
def update_site(site_id: int, updated_site: site_schema_post):
    site_instance = Site()
    updated_site_data = site_instance.update_site(site_id, updated_site)

    if updated_site_data:
        site_instance.close_connection()
        return updated_site_data
    else:
        site_instance.close_connection()
        return {"message": "Site not found"}
    


from fastapi import FastAPI, BackgroundTasks
from datetime import datetime, timedelta
import asyncio

# app = FastAPI()

# Este diccionario almacena los temporizadores de asistencia para cada sede
temporizadores_asistencia = {}

async def verificar_inactividad(sede_id: int, delay: int):
    await asyncio.sleep(delay)
    # Lógica para manejar la inactividad, por ejemplo, actualizar el estado en la base de datos
    print(f"Sede {sede_id} inactiva")

from fastapi import FastAPI, BackgroundTasks

tareas_temporizador = {}

async def verificar_inactividad(sede_id: int, delay: int):
    await asyncio.sleep(delay)
    # Tu lógica para manejar la inactividad aquí
    print(f"Sede {sede_id} ha sido marcada como inactiva.")

@site_router.post("/asistencia/{sede_id}")
async def asistencia(sede_id: int, background_tasks: BackgroundTasks):
    global tareas_temporizador
    
    # Cancelar la tarea anterior si existe
    if sede_id in tareas_temporizador:
        tarea_anterior = tareas_temporizador[sede_id]
        tarea_anterior.cancel()
        print(f"Tarea anterior para sede {sede_id} cancelada.")
    
    # Planificar una nueva tarea de verificación de inactividad
    tarea = asyncio.create_task(verificar_inactividad(sede_id, 60))  # Suponiendo 60 segundos para inactividad
    tareas_temporizador[sede_id] = tarea
    
    # Añadir la tarea al background tasks de FastAPI no es necesario aquí,
    # ya que estamos usando asyncio.create_task directamente.
    print(f"Nueva tarea para sede {sede_id} iniciada.")

    return {"mensaje": "Asistencia registrada para sede " + str(sede_id)}