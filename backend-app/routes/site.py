from fastapi import APIRouter
from models.site import Site
from schema.site import site_schema_post
from models.connectivityLog import ConnectivityLog
from schema.connectivityLog import ConnectivityLogSchema
from datetime import datetime
import pytz
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
    # Asume que esta función ahora también registra un evento de desconexión
    await insert_connectivity_event(sede_id, "Desconexión")
    print(f"Sede {sede_id} ha sido marcada como inactiva.")

from fastapi import FastAPI, BackgroundTasks

tareas_temporizador = {}

# async def verificar_inactividad(sede_id: int, delay: int):
#     await asyncio.sleep(delay)
#     # Tu lógica para manejar la inactividad aquí
#     print(f"Sede {sede_id} ha sido marcada como inactiva.")

# @site_router.post("/asistencia/{sede_id}")
@site_router.post("/asistencia/{sede_id}")
async def asistencia(sede_id: int, background_tasks: BackgroundTasks):
    global tareas_temporizador

    # Comprobar el último estado de conexión de la sede
    connectivity_instance = ConnectivityLog()
    is_online = connectivity_instance.is_site_online(sede_id)
    connectivity_instance.close_connection()

    # Si la sede no está en línea, registrar el evento de conexión
    if not is_online:
        await insert_connectivity_event(sede_id, "Conexión")

        # Cancelar la tarea anterior si existe
        if sede_id in tareas_temporizador:
            tarea_anterior = tareas_temporizador[sede_id]
            tarea_anterior.cancel()
            print(f"Tarea anterior para sede {sede_id} cancelada.")

        # Planificar una nueva tarea de verificación de inactividad
        tarea = asyncio.create_task(verificar_inactividad(sede_id, 60))  # Suponiendo 60 segundos para inactividad
        tareas_temporizador[sede_id] = tarea

        mensaje = "Asistencia registrada y conectividad actualizada para sede " + str(sede_id)
    else:
        # Si la sede ya está en línea, no registrar un nuevo evento de conexión
        mensaje = "La sede " + str(sede_id) + " ya está en línea. No se registra un nuevo evento de conexión."

    return {"mensaje": mensaje}
async def insert_connectivity_event(site_id: int, event_type: str):
    """Función auxiliar para insertar un evento de conectividad."""
    connectivity_instance = ConnectivityLog()
    # Establecer la zona horaria a Colombia
    colombia_zone = pytz.timezone('America/Bogota')
    # Obtener la fecha y hora actuales en la zona horaria de Colombia
    colombia_now = datetime.now(colombia_zone)
    log_data = ConnectivityLogSchema(
        site_id=site_id,
        event_timestamp=colombia_now,
        event_type=event_type
    )
    log_id = connectivity_instance.insert_connectivity_log(log_data)
    connectivity_instance.close_connection()
    return log_id

@site_router.get("/site/{site_id}/online-status", response_model=bool)
def check_site_online_status(site_id: int) -> bool:
    connectivity_instance = ConnectivityLog()
    is_online = connectivity_instance.is_site_online(site_id)
    connectivity_instance.close_connection()
    return is_online


@site_router.get("/sites/online-status")
def get_all_sites_online_status():
    connectivity_instance = ConnectivityLog()
    sites_status = connectivity_instance.get_sites_online_status()
    connectivity_instance.close_connection()
    return sites_status