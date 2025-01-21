from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

import requests
from dotenv import load_dotenv
import os
import json
from typing import List
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging
from PIL import Image

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
LOCAL_IDS_TO_CACHE = [8, 6, 2, 9, 4, 5, 1, 11, 3, 13, 7]  # Ejemplo de IDs de locales

def download_and_resize_image(image_url: str, image_code: str):
    """
    Descarga y redimensiona la imagen a 600px de ancho.
    Guarda la imagen en el directorio de cache_images.
    """
    image_path = os.path.join(CACHE_IMAGE_DIR, image_code)
    if os.path.exists(image_path):
        logger.info(f"Imagen ya existe: {image_code}")
        return
    # Construir la URL completa
    full_url = f"https://img.restpe.com/{image_url}"
    try:
        response = requests.get(full_url, stream=True)
        response.raise_for_status()
        # Abrir la imagen con Pillow
        image = Image.open(response.raw)
        # Calcular la nueva altura manteniendo el aspecto
        width_percent = (600 / float(image.size[0]))
        new_height = int((float(image.size[1]) * float(width_percent)))
        resized_image = image.resize((600, new_height))
        # Guardar la imagen
        resized_image.save(image_path)
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
        # Extraer el código de la imagen
        # Asumiendo que el código de la imagen es la parte después del último '/'
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

def initialize_cache(dominio_id: int, quipupos: int = 0):
    """
    Inicializa la caché para todos los locales en la lista.
    """
    logger.info(f"Iniciando actualización de caché para dominio_id: {dominio_id}...")
    for local_id in LOCAL_IDS_TO_CACHE:
        fetch_and_cache_menu(dominio_id=dominio_id, local_id=local_id, quipupos=quipupos)
    logger.info(f"Actualización de caché completada para dominio_id: {dominio_id}.")

    # Programador de tareas para actualizar la caché cada 30 minutos
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=initialize_cache,
        trigger=IntervalTrigger(minutes=30),
        args=[6149],  # Reemplaza 6149 con el dominio_id adecuado
        id='cache_updater',
        name='Actualizar caché cada 30 minutos',
        replace_existing=True
    )

# Nota: No inicializar la caché al iniciar
# initialize_cache()

@integration_router.post('/refresh-cache/{dominio_id}')
def refresh_cache(
    dominio_id: int,
    background_tasks: BackgroundTasks,
    quipupos: int = 0
):
    """
    Endpoint para refrescar la caché manualmente.
    """
    background_tasks.add_task(initialize_cache, dominio_id=dominio_id, quipupos=quipupos)
    logger.info(f"Solicitud para actualizar caché recibida para dominio_id: {dominio_id}")
    return {"message": "Actualización de caché iniciada."}

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
        # Si hay un error y hay caché disponible (aunque corrupta), retornar un error
        if os.path.exists(cache_file):
            return {"error": "Error al actualizar el caché, utilizando datos antiguos si están disponibles."}
        else:
            raise HTTPException(status_code=500, detail=str(e))

@integration_router.get('/get-categorized-products/{dominio_id}/{local_id}')
def get_categorized_products(dominio_id: int, local_id: int, quipupos: int = 0):
    """
    Ruta existente para obtener productos categorizados. Utiliza caché si está disponible.
    """
    cache_file = os.path.join(CACHE_DIR, f"menu_{local_id}.json")
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                api_response = json.load(f)
        except json.JSONDecodeError:
            logger.error(f"Error al leer el caché para local_id {local_id}")
            # Si el caché está corrupto, obtener de la API
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
    else:
        # Si no existe el caché, intentar obtener y almacenar
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

    categorias_raw = api_response.get('data', {}).get('listaCategorias', [])
    productos_raw = api_response.get('data', {}).get('data', [])

    logger.debug(productos_raw)

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
        } for cat in categorias_raw
    }

    for producto in productos_raw:
        if isinstance(producto, dict):
            categoria_id = producto.get("categoria_id")
            if categoria_id in categorias:
                categorias[categoria_id]["products"].append(producto)
        else:
            continue

    resultado = list(categorias.values())
    return resultado


@integration_router.get('/get-image')
def get_image(image_url: str):
    """
    Endpoint para obtener una imagen por su URL.
    - Verifica si la imagen está en la caché.
    - Si no está, la descarga, redimensiona y la guarda en la caché.
    - Retorna la imagen desde la caché.
    
    Parámetros:
    - image_url: URL parcial de la imagen (ejemplo: "salchimonsterrestaurantpe/productogeneral/22428b7d-57e1-4f94-ac44-d4ecbe36d4a4.jpg")
    
    Ejemplo de Uso:
    GET /integration/get-image?image_url=salchimonsterrestaurantpe/productogeneral/22428b7d-57e1-4f94-ac44-d4ecbe36d4a4.jpg
    """
    # Extraer el código de la imagen (parte después del último '/')
    image_code = image_url.split('/')[-1]
    image_path = os.path.join(CACHE_IMAGE_DIR, image_code)
    
    # Verificar si la imagen ya está en la caché
    if not os.path.exists(image_path):
        # Descargar y redimensionar la imagen
        full_url = f"https://img.restpe.com/{image_url}"
        try:
            response = requests.get(full_url, stream=True)
            response.raise_for_status()
            # Abrir la imagen con Pillow
            image = Image.open(response.raw)
            # Calcular la nueva altura manteniendo el aspecto
            width_percent = (600 / float(image.size[0]))
            new_height = int((float(image.size[1]) * float(width_percent)))
            resized_image = image.resize((600, new_height), Resampling.LANCZOS)
            # Guardar la imagen en la caché
            resized_image.save(image_path)
            logger.info(f"Imagen descargada y redimensionada: {image_code}")
        except requests.RequestException as e:
            logger.error(f"Error al descargar la imagen {image_code}: {e}")
            raise HTTPException(status_code=404, detail="Imagen no encontrada o error al descargarla.")
        except Exception as e:
            logger.error(f"Error al procesar la imagen {image_code}: {e}")
            raise HTTPException(status_code=500, detail="Error al procesar la imagen.")
    
    # Retornar la imagen desde la caché
    return FileResponse(image_path, media_type="image/jpeg", filename=image_code)