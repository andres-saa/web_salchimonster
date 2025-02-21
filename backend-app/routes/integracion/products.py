from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

import requests
from dotenv import load_dotenv
import os
import json
from typing import List
import logging
from PIL import Image
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

integration_router = APIRouter()

TOKEN = os.getenv("API_TOKEN")
CACHE_DIR = os.path.join("files", "cache_menu")
CACHE_IMAGE_DIR = os.path.join("files", "cache_images")

# Asegurarse de que los directorios de caché existan
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(CACHE_IMAGE_DIR, exist_ok=True)

# Lista de locales a cachear (puedes ajustar esta lista según tus necesidades)
LOCAL_IDS_TO_CACHE = [8, 6, 2, 9, 4, 5, 1, 11, 3, 13, 7, 16]  # Ejemplo de IDs de locales

# ---------------------------------------------------
# Configuración de Scheduler Global (evita múltiples instancias)
# ---------------------------------------------------
scheduler = BackgroundScheduler()
scheduler.start()

def download_and_resize_image(image_url: str, image_code: str):
    """
    Descarga y redimensiona la imagen a 600px de ancho.
    Guarda la imagen en el directorio de cache_images en formato JPEG,
    sin importar si el image_code no tiene extensión.
    """
    image_path = os.path.join(CACHE_IMAGE_DIR, image_code)

    # Si ya existe un archivo con este nombre, no volvemos a descargar.
    if os.path.exists(image_path):
        logger.info(f"Imagen ya existe en caché: {image_code}")
        return

    # Construir la URL completa
    full_url = f"https://img.restpe.com/{image_url}"
    try:
        response = requests.get(full_url, stream=True)
        response.raise_for_status()

        # Abrir la imagen con Pillow
        image = Image.open(response.raw)
        
        # Calcular la nueva altura manteniendo la relación de aspecto
        width_percent = (600 / float(image.size[0]))
        new_height = int((float(image.size[1]) * float(width_percent)))

        # Redimensionar la imagen
        resized_image = image.resize((600, new_height), Image.Resampling.LANCZOS)

        # Guardar como JPEG (aunque no tenga extensión, se fuerza JPEG)
        resized_image.save(image_path, "JPEG")
        logger.info(f"Imagen descargada y redimensionada: {image_code}")
    except Exception as e:
        logger.error(f"Error al descargar o redimensionar la imagen {image_code}: {e}")

def process_images_from_menu_data(menu_data: dict):
    """
    Extrae las URLs de las imágenes del menú y las procesa (descarga y redimensiona).
    """
    image_urls = []

    def extract_images(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key.endswith("urlimagen") and isinstance(value, str):
                    image_urls.append(value)
                elif isinstance(value, (dict, list)):
                    extract_images(value)
        elif isinstance(data, list):
            for item in data:
                extract_images(item)

    extract_images(menu_data)

    for image_url in image_urls:
        # Extraer el código de la imagen de la parte final de la URL
        image_code = image_url.split('/')[-1]
        download_and_resize_image(image_url=image_url, image_code=image_code)

def fetch_and_cache_menu(dominio_id: int, local_id: int, quipupos: int = 0):
    """
    Función para obtener el menú de un local y almacenarlo en el caché.
    Además, procesa las imágenes del menú.
    """
    url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{dominio_id}/{local_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Token token="{TOKEN}"'
    }
    params = {
        "quipupos": quipupos
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Escribir en el archivo de caché
        cache_file = os.path.join(CACHE_DIR, f"menu_{local_id}.json")
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        logger.info(f"Caché actualizada para local_id: {local_id}")

        # Procesar imágenes del menú
        process_images_from_menu_data(data)

    except requests.RequestException as e:
        logger.error(f"Error al actualizar caché para local_id {local_id}: {e}")

def initialize_cache(dominio_id: int = 6149, quipupos: int = 0):
    """
    Inicializa o refresca la caché para todos los locales en la lista.
    """
    logger.info(f"Iniciando actualización de caché para dominio_id: {dominio_id}...")
    for local_id in LOCAL_IDS_TO_CACHE:
        fetch_and_cache_menu(dominio_id=dominio_id, local_id=local_id, quipupos=quipupos)
    logger.info(f"Actualización de caché completada para dominio_id: {dominio_id}.")

    # Programar la actualización de la caché cada 30 minutos sólo si no existe ya un job
    job_id = 'cache_updater'
    existing_job = scheduler.get_job(job_id)
    if not existing_job:
        scheduler.add_job(
            func=initialize_cache,
            trigger=IntervalTrigger(minutes=30),
            args=[6149],  # Cambia 6149 si necesitas otro valor por defecto
            id=job_id,
            name='Actualizar caché cada 30 minutos',
            replace_existing=True
        )
        logger.info("Programada la actualización automática cada 30 minutos.")

# ---------------------------------------------------
# Endpoint para refrescar la caché en segundo plano
# ---------------------------------------------------
@integration_router.post('/refresh-cache')
def refresh_cache(
    background_tasks: BackgroundTasks,
    dominio_id: int = 6149, 
    quipupos: int = 0
):
    """
    Endpoint para refrescar manualmente la caché en segundo plano.
    - dominio_id (opcional, por defecto 6149).
    - quipupos (opcional, por defecto 0).
    """
    # Lanza la tarea de actualización en segundo plano
    background_tasks.add_task(initialize_cache, dominio_id, quipupos)
    logger.info(f"Se ha enviado la tarea de refrescar la caché para dominio_id={dominio_id} en segundo plano.")

    return {"message": f"Refresco de caché iniciado en segundo plano para dominio_id={dominio_id}."}

# ---------------------------------------------------
# Endpoint para obtener productos (con caché)
# ---------------------------------------------------
@integration_router.get('/get-product-integration/{dominio_id}/{local_id}')
def get_product_integration(
    dominio_id: int,
    local_id: int,
    quipupos: int = 0
):
    """
    Endpoint para obtener la integración de productos para un local utilizando caché.
    """
    cache_file = os.path.join(CACHE_DIR, f"menu_{local_id}.json")
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError:
            logger.error(f"Error al leer el caché para local_id {local_id}")
            # Si el caché está corrupto, intentar obtener de la API

    # Si no existe el caché o está corrupto, intentar obtener y almacenar
    try:
        url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{dominio_id}/{local_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Token token="{TOKEN}"'
        }
        params = {
            "quipupos": quipupos
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Escribir en el caché
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logger.info(f"Caché creado para local_id: {local_id}")

        # Procesar imágenes del menú
        process_images_from_menu_data(data)

        return data
    except requests.RequestException as e:
        logger.error(f"Error al obtener datos para local_id {local_id}: {e}")
        # Si hay un error y existía caché corrupta, retornar un error.
        if os.path.exists(cache_file):
            return {
                "error": "Error al actualizar el caché, utilizando datos antiguos si están disponibles."
            }
        else:
            raise HTTPException(status_code=500, detail=str(e))

# ---------------------------------------------------
# Endpoint para obtener productos categorizados (con caché)
# ---------------------------------------------------
@integration_router.get('/get-categorized-products/{dominio_id}/{local_id}')
def get_categorized_products(dominio_id: int, local_id: int, quipupos: int = 0):
    """
    Ruta para obtener productos categorizados. Utiliza caché si está disponible.
    """
    cache_file = os.path.join(CACHE_DIR, f"menu_{local_id}.json")
    
    # Intentar leer de caché
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                api_response = json.load(f)
        except json.JSONDecodeError:
            logger.error(f"Error al leer el caché para local_id {local_id}")
            # Si el caché está corrupto, obtener de la API y volver a guardar
            try:
                url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{dominio_id}/{local_id}"
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f'Token token="{TOKEN}"'
                }
                params = {
                    "quipupos": quipupos
                }
                response = requests.get(url, headers=headers, params=params)
                response.raise_for_status()
                api_response = response.json()

                # Escribir en el caché
                with open(cache_file, 'w', encoding='utf-8') as f:
                    json.dump(api_response, f, ensure_ascii=False, indent=4)
                logger.info(f"Caché creado (actualizado) para local_id: {local_id}")

                # Procesar imágenes
                process_images_from_menu_data(api_response)
            except requests.RequestException as e:
                logger.error(f"Error al obtener datos para local_id {local_id}: {e}")
                raise HTTPException(status_code=500, detail=str(e))
    else:
        # Si no existe el caché, obtener y almacenar
        try:
            url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{dominio_id}/{local_id}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f'Token token="{TOKEN}"'
            }
            params = {
                "quipupos": quipupos
            }
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            api_response = response.json()

            # Escribir en el caché
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(api_response, f, ensure_ascii=False, indent=4)
            logger.info(f"Caché creado para local_id: {local_id}")

            # Procesar imágenes del menú
            process_images_from_menu_data(api_response)
        except requests.RequestException as e:
            logger.error(f"Error al obtener datos para local_id {local_id}: {e}")
            raise HTTPException(status_code=500, detail=str(e))

    # A partir de este punto, api_response debería existir
    categorias_raw = api_response.get('listaCategorias', [])
    productos_raw = api_response.get('data', [])

    # Crear estructura de categorías
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

    # Asignar productos a sus categorías correspondientes
    for producto in productos_raw:
        if isinstance(producto, dict):
            categoria_id = producto.get("categoria_id")
            if categoria_id in categorias:
                categorias[categoria_id]["products"].append(producto)
        else:
            continue

    # Convertir el diccionario en lista
    resultado = list(categorias.values())
    return resultado

# ---------------------------------------------------
# Endpoint para obtener una imagen
# ---------------------------------------------------
@integration_router.get('/get-image')
def get_image(image_url: str):
    """
    Endpoint para obtener una imagen por su URL (parcial).
    Si la imagen no está en caché, la descarga y la redimensiona a 600px de ancho
    y se guarda como JPEG, incluso si no tiene extensión.
    
    Parámetros:
    - image_url: URL parcial de la imagen (por ej: "mi_restaurante/productogeneral/imagen_12345")
    """
    # Extraer el código de la imagen (sin asumir extensión)
    image_code = image_url.split('/')[-1]
    image_path = os.path.join(CACHE_IMAGE_DIR, image_code)
    
    # Verificar si la imagen ya está en caché
    if not os.path.exists(image_path):
        # Descargar y redimensionar la imagen
        full_url = f"https://img.restpe.com/{image_url}"
        try:
            response = requests.get(full_url, stream=True)
            response.raise_for_status()

            image = Image.open(response.raw)
            width_percent = (600 / float(image.size[0]))
            new_height = int((float(image.size[1]) * float(width_percent)))
            resized_image = image.resize((600, new_height), Image.Resampling.LANCZOS)
            
            # Forzamos guardado en JPEG
            resized_image.save(image_path, "JPEG")

            logger.info(f"Imagen descargada y redimensionada: {image_code}")
        except requests.RequestException as e:
            logger.error(f"Error al descargar la imagen {image_code}: {e}")
            raise HTTPException(status_code=404, detail="Imagen no encontrada o error al descargarla.")
        except Exception as e:
            logger.error(f"Error al procesar la imagen {image_code}: {e}")
            raise HTTPException(status_code=500, detail="Error al procesar la imagen.")
    
    # Retornar la imagen desde la caché, siempre como JPEG
    return FileResponse(
        image_path,
        media_type="image/jpeg",
        filename=image_code  # Se devuelve el código como nombre, sin extensión
    )
