from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
import json
import logging
import requests
from PIL import Image
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.asyncio import AsyncIOScheduler  # <- Úsalo si tu app es async

# Modelos y lógica de negocio (ajusta las importaciones a tu estructura real)
from models.tiendas.Tiendas import Tiendas, Menu

# -----------------------------------------------------
# Configuración de logging
# -----------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------------------------------
# Cargamos el token desde .env
# -----------------------------------------------------
load_dotenv()
TOKEN = os.getenv("API_TOKEN")

# -----------------------------------------------------
# Ajusta tu dominio
# -----------------------------------------------------
DOMAIN_ID = 6149  # Ajustar si es necesario

# -----------------------------------------------------
# Directorios de caché
# -----------------------------------------------------
CACHE_DIR = os.path.join("files", "cache_tiendas")
CACHE_IMAGE_DIR = os.path.join("files", "cache_images_tiendas")

os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(CACHE_IMAGE_DIR, exist_ok=True)

# -----------------------------------------------------
# Lista de locales a refrescar
# -----------------------------------------------------
LOCAL_IDS_TO_CACHE = [8, 6, 2, 9, 4, 5, 1, 11, 3, 13, 7, 16]

# -----------------------------------------------------
# APIRouter
# -----------------------------------------------------
tiendas_router = APIRouter()

# -----------------------------------------------------
# Funciones auxiliares para manejo de imágenes
# -----------------------------------------------------
def download_and_resize_image(image_url: str, image_code: str):
    """
    Descarga y redimensiona la imagen a 600px de ancho.
    Guarda la imagen en CACHE_IMAGE_DIR.
    """
    image_path = os.path.join(CACHE_IMAGE_DIR, image_code)
    if os.path.exists(image_path):
        logger.info(f"Imagen ya existe en caché: {image_code}")
        return

    full_url = f"https://img.restpe.com/{image_url}"
    try:
        response = requests.get(full_url, stream=True)
        response.raise_for_status()
        image = Image.open(response.raw)

        width_percent = (600 / float(image.size[0]))
        new_height = int(float(image.size[1]) * width_percent)
        resized_image = image.resize((600, new_height), Image.LANCZOS)
        resized_image.save(image_path)

        logger.info(f"Imagen descargada y redimensionada: {image_code}")
    except Exception as e:
        logger.error(f"Error al descargar/redimensionar la imagen {image_code}: {e}")

def process_images_from_menu_data(menu_data: Any):
    """
    Recorre la estructura de menú en busca de URLs de imágenes y las guarda en caché.
    """
    image_urls = []

    def extract_images(data):
        if isinstance(data, dict):
            for key, value in data.items():
                # Ajusta si tu JSON de BD guarda la url con otro nombre
                if key.endswith("urlimagen") and isinstance(value, str):
                    image_urls.append(value)
                elif isinstance(value, (dict, list)):
                    extract_images(value)
        elif isinstance(data, list):
            for item in data:
                extract_images(item)

    extract_images(menu_data)

    for image_url in image_urls:
        image_code = image_url.split('/')[-1]
        download_and_resize_image(image_url=image_url, image_code=image_code)

# -----------------------------------------------------
# Funciones para acceso a BD
# -----------------------------------------------------
def get_db_menu_for_local(local_id: int) -> Optional[Any]:
    """
    Obtiene el menú de la BD para un local_id específico.
    Debe retornar la ESTRUCTURA FINAL que se quiera servir al usuario.
    """
    logger.info(f"Buscando en la BD el menú para local_id={local_id}...")
    instance = Tiendas()
    # Ejemplo: tu método podría ser getMenu(local_id), revisa tu implementación
    result = instance.getMenu(local_id=local_id)
    if result and isinstance(result, list) and len(result) > 0:
        return result
    return None

def update_db_menu_data(menu_data: List[Dict[str, Any]], local_id: int) -> dict:
    """
    Guarda o actualiza el menú en la BD.
    Retorna algún dict con el estado de la operación (ajústalo a tu caso).
    """
    logger.info(f"Guardando menú en la BD para local_id={local_id}")
    instance = Tiendas()
    menu = Menu(data=menu_data, local_id=local_id)
    result = instance.updateMenu(menu)
    return result[0] if result else {}

# -----------------------------------------------------
# Lógica principal: buscar en caché, BD, o API
# -----------------------------------------------------
def fetch_and_cache_categorized_products(dominio_id: int, local_id: int, quipupos: int = 0) -> Any:
    """
    1. Revisa si existe un archivo de caché en disco (JSON).
    2. Si no hay caché, se consulta la BD.
    3. Si tampoco hay en BD, se llama a la API -> se guarda en BD -> se vuelve a leer la BD -> se guarda en caché.
    """
    cache_file = os.path.join(CACHE_DIR, f"menu_{local_id}.json")

    # 1. Verificar archivo de caché
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                final_data = json.load(f)
            logger.info(f"Menú de local_id={local_id} obtenido desde caché de archivos.")
            return final_data
        except json.JSONDecodeError:
            logger.warning(f"El archivo de caché local_id={local_id} está dañado. Se eliminará.")
            os.remove(cache_file)

    # 2. Verificar en la BD
    db_data = get_db_menu_for_local(local_id)
    if db_data:
        logger.info(f"Menú de local_id={local_id} encontrado en la BD. Guardando en caché...")
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(db_data, f, ensure_ascii=False, indent=4)

        # Procesar imágenes
        process_images_from_menu_data(db_data)
        return db_data

    # 3. Ni caché ni BD: Llamar a la API y luego a la BD para la versión final
    logger.info(f"No hay menú para local_id={local_id} en caché ni en BD. Descargando de la API...")

    try:
        url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{dominio_id}/{local_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Token token="{TOKEN}"'
        }
        params = {"quipupos": quipupos}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        api_response = response.json()
    except requests.RequestException as e:
        logger.error(f"Error al obtener datos de la API para local_id={local_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    categorias_raw = api_response.get("listaCategorias", [])
    productos_raw = api_response.get("data", [])

    categorias = {
        cat["categoria_id"]: {
            "categoria_id": cat["categoria_id"],
            "local_id": cat["local_id"],
            "categoria_descripcion": cat["categoria_descripcion"],
            "categoria_estado": cat["categoria_estado"],
            "categoria_padreid": cat["categoria_padreid"],
            "categoria_color": cat["categoria_color"],
            "categoria_delivery": cat["categoria_delivery"],
            "products": []
        }
        for cat in categorias_raw
    }

    for producto in productos_raw:
        if isinstance(producto, dict):
            cid = producto.get("categoria_id")
            if cid in categorias:
                categorias[cid]["products"].append(producto)

    api_categorized_data = list(categorias.values())

    # Guardar PRIMERO en la BD
    update_db_menu_data(api_categorized_data, local_id)

    # Leer nuevamente la BD para obtener la versión final
    final_db_data = get_db_menu_for_local(local_id)
    if not final_db_data:
        logger.warning("La BD no devolvió datos tras update. Devolviendo data categorizada.")
        final_db_data = api_categorized_data

    # Guardar en caché
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(final_db_data, f, ensure_ascii=False, indent=4)

    # Procesar imágenes
    process_images_from_menu_data(final_db_data)

    logger.info(f"Menú de local_id={local_id} listo (API -> BD -> caché).")
    return final_db_data

# -----------------------------------------------------
# Endpoints
# -----------------------------------------------------
@tiendas_router.get("/tiendas/{local_id}/products")
def get_products_for_tienda(local_id: int, quipupos: int = 0):
    """
    Devuelve el menú categorizado para un local.
    """
    return fetch_and_cache_categorized_products(DOMAIN_ID, local_id, quipupos)

@tiendas_router.get("/tiendas/get-image")
def get_image_tienda(image_url: str):
    """
    Devuelve una imagen redimensionada (ya en caché).
    Si no está, intenta descargar en ese momento.
    """
    image_code = image_url.split('/')[-1]
    image_path = os.path.join(CACHE_IMAGE_DIR, image_code)

    if not os.path.exists(image_path):
        # No está en caché, descargar
        full_url = f"https://img.restpe.com/{image_url}"
        try:
            response = requests.get(full_url, stream=True)
            response.raise_for_status()
            image = Image.open(response.raw)

            width_percent = (600 / float(image.size[0]))
            new_height = int(float(image.size[1]) * width_percent)
            resized_image = image.resize((600, new_height), Image.LANCZOS)
            resized_image.save(image_path)

            logger.info(f"Imagen descargada y redimensionada: {image_code}")
        except requests.RequestException as e:
            logger.error(f"Error al descargar la imagen {image_code}: {e}")
            raise HTTPException(status_code=404, detail="Imagen no encontrada o error al descargarla.")
        except Exception as e:
            logger.error(f"Error al procesar la imagen {image_code}: {e}")
            raise HTTPException(status_code=500, detail="Error al procesar la imagen.")

    return FileResponse(image_path, media_type="image/jpeg", filename=image_code)

@tiendas_router.get("/tiendas/{local_id}/refresh")
def refresh_menu_for_tienda(local_id: int, quipupos: int = 0):
    """
    Fuerza la descarga desde la API, ignorando caché/BD, y luego usa la misma
    lógica de 'guardar en BD -> leer BD -> guardar en caché'.
    """
    logger.info(f"Forzando refresco de menú para local_id={local_id}...")

    # Descargamos directamente de la API
    try:
        url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{DOMAIN_ID}/{local_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Token token="{TOKEN}"'
        }
        params = {"quipupos": quipupos}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        api_response = response.json()
    except requests.RequestException as e:
        logger.error(f"Error al refrescar datos de la API para local_id={local_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    categorias_raw = api_response.get("listaCategorias", [])
    productos_raw = api_response.get("data", [])

    categorias = {
        cat["categoria_id"]: {
            "categoria_id": cat["categoria_id"],
            "local_id": cat["local_id"],
            "categoria_descripcion": cat["categoria_descripcion"],
            "categoria_estado": cat["categoria_estado"],
            "categoria_padreid": cat["categoria_padreid"],
            "categoria_color": cat["categoria_color"],
            "categoria_delivery": cat["categoria_delivery"],
            "products": []
        }
        for cat in categorias_raw
    }

    for producto in productos_raw:
        if isinstance(producto, dict):
            cid = producto.get("categoria_id")
            if cid in categorias:
                categorias[cid]["products"].append(producto)

    api_categorized_data = list(categorias.values())

    # Guardar en BD
    db_result = update_db_menu_data(api_categorized_data, local_id)

    # Leer la versión definitiva desde la BD
    final_db_data = get_db_menu_for_local(local_id)
    if not final_db_data:
        logger.warning("La BD no devolvió nada tras el refresco. Usando data categorizada sin procesar.")
        final_db_data = api_categorized_data

    # Guardar en caché
    cache_file = os.path.join(CACHE_DIR, f"menu_{local_id}.json")
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(final_db_data, f, ensure_ascii=False, indent=4)

    # Procesar imágenes
    process_images_from_menu_data(final_db_data)

    return {
        "message": f"Menú del local {local_id} refrescado exitosamente.",
        "db_update_result": db_result,
        "menu_data": final_db_data
    }

@tiendas_router.get("/tiendas/refresh_all")
def refresh_all_tiendas(quipupos: int = 0):
    """
    Para cada local en LOCAL_IDS_TO_CACHE, ejecuta la lógica fetch_and_cache_categorized_products
    y actualiza la BD. Retorna un estado de cada uno.
    """
    results = []
    logger.info("Refrescando menú para TODOS los locales en LOCAL_IDS_TO_CACHE...")
    for l_id in LOCAL_IDS_TO_CACHE:
        try:
            new_data = fetch_and_cache_categorized_products(DOMAIN_ID, l_id, quipupos)
            # new_data aquí ya es la data final de la BD
            db_result = update_db_menu_data(new_data, l_id)
            results.append({
                "local_id": l_id,
                "status": "ok",
                "db_update_result": db_result
            })
        except Exception as e:
            logger.error(f"Error refrescando local_id={l_id}: {e}")
            results.append({
                "local_id": l_id,
                "status": "error",
                "error_detail": str(e)
            })

    return {
        "message": "Menú de todos los locales refrescado",
        "results": results
    }

# -----------------------------------------------------
# Scheduler
# -----------------------------------------------------
scheduler = BackgroundScheduler()

def scheduled_job():
    """
    Cada X tiempo se actualiza la caché (y la BD) de todos los locales.
    """
    logger.info("=== Tarea programada: actualizando todos los locales ===")
    try:
        for local_id in LOCAL_IDS_TO_CACHE:
            try:
                fetch_and_cache_categorized_products(DOMAIN_ID, local_id, quipupos=0)
            except Exception as e:
                logger.error(f"Error actualizando local_id={local_id}: {e}")
    except Exception as e:
        logger.error(f"Error global en la tarea programada: {e}")
    finally:
        logger.info("=== Tarea programada finalizada ===")

# Configuramos la tarea cada 30 minutos (ajusta el intervalo según requieras)
scheduler.add_job(scheduled_job, "interval", minutes=30)

# -----------------------------------------------------
# Crear la app FastAPI
# -----------------------------------------------------
app = FastAPI()

@app.on_event("startup")
def on_startup():
    logger.info("Iniciando aplicación FastAPI...")
    # Iniciar scheduler si está detenido (por ejemplo, en modo reload)
    if scheduler.state == 0:  # 0 = STATE_STOPPED
        logger.info("Iniciando APScheduler (BackgroundScheduler)...")
        scheduler.start()

@app.on_event("shutdown")
def on_shutdown():
    if scheduler.state == 1:  # 1 = STATE_RUNNING
        scheduler.shutdown()
    logger.info("Cerrando aplicación FastAPI... (scheduler off)")

app.include_router(tiendas_router)
