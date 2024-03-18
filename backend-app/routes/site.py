from fastapi import APIRouter
from models.site import Site
from schema.site import site_schema_post
from models.connectivityLog import ConnectivityLog
from schema.connectivityLog import ConnectivityLogSchema
from datetime import datetime
import pytz
from schema.directory import *

def obtener_hora_colombia():
    zona_horaria_colombia = pytz.timezone('America/Bogota')
    hora_actual_colombia = datetime.now(zona_horaria_colombia)
    return hora_actual_colombia


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

async def verificar_inactividad(sede_id: int, tiempo_espera: int):
    await asyncio.sleep(tiempo_espera)  # Espera el tiempo definido antes de verificar nuevamente
    connectivity_instance = ConnectivityLog()
    is_online = connectivity_instance.is_site_online(sede_id)
    connectivity_instance.close_connection()
    # Solo registra el evento de desconexión si el sitio sigue desconectado y el último evento no es una desconexión
    if not is_online and not connectivity_instance.last_event_is_disconnection(sede_id):
        await insert_connectivity_event(sede_id, "Desconexión")
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

    connectivity_instance = ConnectivityLog()
    is_online = connectivity_instance.is_site_online(sede_id)
    connectivity_instance.close_connection()

    # No registra inmediatamente un evento de desconexión para evitar duplicados
    if not is_online:
        print(f"Sede {sede_id} detectada como desconectada, esperando para verificar inactividad.")
    
    if sede_id in tareas_temporizador:
        tarea_anterior = tareas_temporizador.get(sede_id)
        if tarea_anterior and not tarea_anterior.done():
            tarea_anterior.cancel()
        print(f"Tarea anterior para sede {sede_id} cancelada.")
    
    tarea = asyncio.create_task(verificar_inactividad(sede_id, 60))
    tareas_temporizador[sede_id] = tarea

    mensaje = f"Asistencia registrada. Verificación de conectividad pendiente para sede {sede_id}."
    return {"mensaje": mensaje}

async def insert_connectivity_event(site_id: int, event_type: str):
    connectivity_instance = ConnectivityLog()
    colombia_now = obtener_hora_colombia()  # Usar la función para obtener la hora
    log_data = ConnectivityLogSchema(site_id=site_id, event_type=event_type, timestamp=colombia_now)
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




@site_router.get("/site/{site_id}/safe-boxes")
def get_safe_boxes(site_id: int):
    site_instance = Site(site_id=site_id)
    safe_boxes = site_instance.get_all_safe_boxes()
    site_instance.close_connection()
    return safe_boxes

@site_router.get("/site/{site_id}/cameras")
def get_cameras(site_id: int):
    site_instance = Site(site_id=site_id)
    cameras = site_instance.get_all_cameras()
    site_instance.close_connection()
    return cameras

@site_router.get("/site/{site_id}/wifi-networks")
def get_wifi_networks(site_id: int):
    site_instance = Site(site_id=site_id)
    wifi_networks = site_instance.get_all_wifi_networks()
    site_instance.close_connection()
    return wifi_networks

@site_router.get("/site/{site_id}/dataphones")
def get_dataphones(site_id: int):
    site_instance = Site(site_id=site_id)
    dataphones = site_instance.get_all_dataphones()
    site_instance.close_connection()
    return dataphones

@site_router.get("/site/{site_id}/web-pages")
def get_web_pages(site_id: int):
    site_instance = Site(site_id=site_id)
    web_pages = site_instance.get_all_web_pages()
    site_instance.close_connection()
    return web_pages

@site_router.get("/site/{site_id}/applications")
def get_applications(site_id: int):
    site_instance = Site(site_id=site_id)
    applications = site_instance.get_all_applications()
    site_instance.close_connection()
    return applications

# Consider adding an endpoint for general emails if needed and if they are associated with sites.

# You can also consider adding an endpoint that aggregates all these details for a site
@site_router.get("/site/{site_id}/all-details")
def get_all_site_details(site_id: int):
    site_instance = Site(site_id=site_id)
    site_details = site_instance.get_all_site_data()
    site_instance.close_connection()
    return site_details





@site_router.post("/site/safe-box")
def create_safe_box( safe_box: DirSafeBoxes):
    site_instance = Site()
    safe_box_id = site_instance.create_safe_box(safe_box)
    site_instance.close_connection()
    return {"safe_box_id": safe_box_id}

@site_router.put("/site/{site_id}/safe-box/{safe_box_id}")
def update_safe_box(site_id: int, safe_box_id: int, safe_box: DirSafeBoxes):
    site_instance = Site(site_id=site_id)
    site_instance.update_safe_box(safe_box_id, safe_box)
    site_instance.close_connection()
    return {"message": "Safe box updated"}

@site_router.post("/site/camera")
def create_camera( camera: DirCameras):
    site_instance = Site()
    camera_id = site_instance.create_camera(camera)
    site_instance.close_connection()
    return {"camera_id": camera_id}

@site_router.put("/site/{site_id}/camera/{camera_id}")
def update_camera(site_id: int, camera_id: int, camera: DirCameras):
    site_instance = Site(site_id=site_id)
    site_instance.update_camera(camera_id, camera)
    site_instance.close_connection()
    return {"message": "Camera updated"}

@site_router.post("/site/wifi-network")
def create_wifi_network( wifi_network: DirWifi):
    site_instance = Site()
    wifi_id = site_instance.create_wifi_network(wifi_network)
    site_instance.close_connection()
    return {"wifi_id": wifi_id}

@site_router.put("/site/{site_id}/wifi-network/{wifi_id}")
def update_wifi_network(site_id: int, wifi_id: int, wifi_network: DirWifi):
    site_instance = Site(site_id=site_id)
    site_instance.update_wifi_network(wifi_id, wifi_network)
    site_instance.close_connection()
    return {"message": "WiFi network updated"}

@site_router.post("/site/dataphone")
def create_dataphone(dataphone: DirDataphones):
    site_instance = Site()
    dataphone_id = site_instance.create_dataphone(dataphone)
    site_instance.close_connection()
    return {"dataphone_id": dataphone_id}

@site_router.put("/site/{site_id}/dataphone/{dataphone_id}")
def update_dataphone(site_id: int, dataphone_id: int, dataphone: DirDataphones):
    site_instance = Site(site_id=site_id)
    site_instance.update_dataphone(dataphone_id, dataphone)
    site_instance.close_connection()
    return {"message": "Dataphone updated"}

@site_router.post("/siteweb-page")
def create_web_page( web_page: DirWebPages):
    site_instance = Site()
    web_page_id = site_instance.create_web_page(web_page)
    site_instance.close_connection()
    return {"web_page_id": web_page_id}

@site_router.put("/site/{site_id}/web-page/{web_page_id}")
def update_web_page(site_id: int, web_page_id: int, web_page: DirWebPages):
    site_instance = Site(site_id=site_id)
    site_instance.update_web_page(web_page_id, web_page)
    site_instance.close_connection()
    return {"message": "Web page updated"}

@site_router.post("/site/application")
def create_application( application: DirApplications):
    site_instance = Site()
    application_id = site_instance.create_application(application)
    site_instance.close_connection()
    return {"application_id": application_id}

@site_router.put("/site/{site_id}/application/{application_id}")
def update_application(site_id: int, application_id: int, application: DirApplications):
    site_instance = Site(site_id=site_id)
    site_instance.update_application(application_id, application)
    site_instance.close_connection()
    return {"message": "Application updated"}




@site_router.delete("/site/{site_id}/safe-box/{safe_box_id}")
def delete_safe_box(site_id: int, safe_box_id: int):
    site_instance = Site(site_id=site_id)
    site_instance.delete_safe_box(safe_box_id)
    site_instance.close_connection()
    return {"message": "Safe box deleted"}

@site_router.delete("/site/{site_id}/camera/{camera_id}")
def delete_camera(site_id: int, camera_id: int):
    site_instance = Site(site_id=site_id)
    site_instance.delete_camera(camera_id)
    site_instance.close_connection()
    return {"message": "Camera deleted"}

@site_router.delete("/site/{site_id}/wifi-network/{wifi_id}")
def delete_wifi_network(site_id: int, wifi_id: int):
    site_instance = Site(site_id=site_id)
    site_instance.delete_wifi_network(wifi_id)
    site_instance.close_connection()
    return {"message": "WiFi network deleted"}

@site_router.delete("/site/{site_id}/dataphone/{dataphone_id}")
def delete_dataphone(site_id: int, dataphone_id: int):
    site_instance = Site(site_id=site_id)
    site_instance.delete_dataphone(dataphone_id)
    site_instance.close_connection()
    return {"message": "Dataphone deleted"}

@site_router.delete("/site/{site_id}/web-page/{web_page_id}")
def delete_web_page(site_id: int, web_page_id: int):
    site_instance = Site(site_id=site_id)
    site_instance.delete_web_page(web_page_id)
    site_instance.close_connection()
    return {"message": "Web page deleted"}

@site_router.delete("/site/{site_id}/application/{application_id}")
def delete_application(site_id: int, application_id: int):
    site_instance = Site(site_id=site_id)
    site_instance.delete_application(application_id)
    site_instance.close_connection()
    return {"message": "Application deleted"}
