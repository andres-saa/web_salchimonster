from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from typing import Dict, List
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os
import json
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging
from PIL import Image

from models.distrimonster.Distrimonster import Distrimonster  # Ajusta la importación a tu proyecto

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

distrimonster_router = APIRouter()

TOKEN = os.getenv("API_TOKEN")

# Directorios de caché
CACHE_DIR = os.path.join("files", "cache_distrimonster")
CACHE_IMAGE_DIR = os.path.join("files", "cache_images")

os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(CACHE_IMAGE_DIR, exist_ok=True)

# Archivos de caché para el menú
CACHE_FILE_API = os.path.join(CACHE_DIR, "menu_distrimonster.json")         # Cache desde la API
CACHE_FILE_DB  = os.path.join(CACHE_DIR, "menu_distrimonster_db.json")      # Cache desde la BD

# Valores fijos
DOMAIN_ID = 6149
LOCAL_ID = 12

# -----------------------------------------------------
# Clases Pydantic para estructurar datos de entrada/BD
# -----------------------------------------------------
class Menu(BaseModel):
    data: Dict

# -----------------------------------------------------
# Funciones auxiliares para imágenes
# -----------------------------------------------------
def download_and_resize_image(image_url: str, image_code: str):
    """
    Descarga y redimensiona la imagen a 600px de ancho.
    Guarda la imagen en el directorio de cache_images.
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
        image_code = image_url.split('/')[-1]
        download_and_resize_image(image_url=image_url, image_code=image_code)

# -----------------------------------------------------
# Funciones para integración con la API
# -----------------------------------------------------
def fetch_menu_from_api(quipupos: int = 0) -> dict:
    """
    Obtiene el menú del local desde la API (distrimonster).
    Retorna el JSON de la API (en forma de diccionario).
    """
    url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{DOMAIN_ID}/{LOCAL_ID}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Token token="{TOKEN}"'
    }
    params = {"quipupos": quipupos}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return data

def save_to_json_file(data: dict, file_path: str):
    """
    Guarda un diccionario en un archivo JSON con indentación.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# -----------------------------------------------------
# Funciones para integración con la BD (Distrimonster)
# -----------------------------------------------------
def update_db_menu_data(menu_data: dict) -> dict:
    """
    Llama a la función updateMenu(...) para actualizar la BD con los datos.
    Retorna la respuesta de la BD.
    """
    instance = Distrimonster()
    # Notar que se envía un objeto Menu con `data=menu_data`
    result = instance.updateMenu(Menu(data=menu_data))
    return result[0] if result else {}



class Menu(BaseModel):
    data:Dict
    
class Price(BaseModel):
    id:int
    mayor:int
    distribuidor:int
    kilos:float
        
class UpdatePrices(BaseModel):
    prices:List[Price]

    
@distrimonster_router.put('/update-prices/')
def update_prices(data:UpdatePrices):
    instance = Distrimonster()
    result = instance.updatePrices(data=data)
    sync_api_to_db_and_cache(0)
    return result
    
    


def get_db_menu_data() -> dict:
    """
    Llama a la función getMenuDistrimonster() para obtener el menú desde la BD.
    Retorna el menú (diccionario).
    """
    instance = Distrimonster()
    result = instance.getMenuDistrimonster()
    return result[0] if result else {}

# -----------------------------------------------------
# Lógica principal de sincronización API -> BD -> Cache
# -----------------------------------------------------
def filter_and_augment_products(api_data: dict) -> list:
    """
    Filtra los productos cuyo 'categoria_id' sea "107" y agrega un campo 'id' a cada uno:
    - Si el producto tiene una lista 'lista_presentacion' no vacía, se usará el 'producto_id'
      del primer elemento de esa lista.
    - Si no tiene presentaciones, se usará el 'productogeneral_id'.
    Retorna la lista de productos filtrados y modificados.
    """
    # Se asume que la lista de productos está en api_data["data"] o api_data["data"]["data"]
    # Dependiendo de la estructura, ajustar el acceso. Aquí asumimos:
    products = api_data.get("data", [])
    # Si la estructura es: {"data": {"data": [ ... ]}}, descomentar la siguiente línea:
    # products = api_data.get("data", {}).get("data", [])
    
    filtered_products = []

    for product in products:
        # Filtrar por categoría (en este ejemplo se usa el valor "107")
        # Nota: Asegúrate de que el valor a comparar tenga el mismo tipo (str o int)
        if str(product.get("categoria_id")) == "107":
            # Determinar el valor para el nuevo campo "id"
            if product.get("lista_presentacion") and len(product["lista_presentacion"]) > 0:
                new_id = product["lista_presentacion"][0].get("producto_id")
            else:
                new_id = product.get("productogeneral_id")
            # Agregar el campo "id" al producto
            product["id"] = new_id

            filtered_products.append(product)

    print("Productos filtrados:", filtered_products)
    return filtered_products


def sync_api_to_db_and_cache(quipupos: int = 0):
    """
    Sincroniza los datos de la API con la BD y la caché, realizando los siguientes pasos:
      1. Descarga el menú completo de la API.
      2. Filtra y modifica los productos cuya categoría sea 107 (usando filter_and_augment_products).
      3. Guarda el JSON modificado (solo con los productos filtrados) en el archivo de caché de la API.
      4. Procesa las imágenes (descarga/redimensiona) de los productos filtrados.
      5. Actualiza la base de datos enviando el JSON modificado.
      6. Lee la data actualizada desde la BD y la guarda en el archivo de caché oficial para el usuario.
    """
    logger.info("Iniciando sincronización API -> DB -> Cache para distrimonster...")

    # 1. Obtener datos de la API (JSON completo)
    try:
        api_data = fetch_menu_from_api(quipupos=quipupos)
    except requests.RequestException as e:
        logger.error(f"Error al obtener menú de la API: {e}")
        raise

    # 2. Filtrar y modificar los productos de la categoría 107
    if isinstance(api_data, dict):
        # Utilizamos la función de filtrado para obtener únicamente los productos que nos interesan
        filtered_products = filter_and_augment_products(api_data)
        # Creamos un nuevo diccionario con los productos filtrados
        modified_api_data = {"data": filtered_products}
    else:
        logger.warning("La respuesta de la API no es un diccionario. No se pudieron modificar los productos.")
        modified_api_data = api_data

    # 3. Guardar el JSON modificado (filtrado) en el archivo de caché de la API
    save_to_json_file(modified_api_data, CACHE_FILE_API)
    logger.info("Menú completo filtrado guardado en caché (API).")

    # 4. Procesar imágenes del menú (usando la data filtrada)
    process_images_from_menu_data(modified_api_data)

    # 5. Actualizar la BD con el JSON modificado (filtrado)
    update_db_menu_data(modified_api_data)
    logger.info("Base de datos actualizada con el menú filtrado.")

    # 6. Leer la data actualizada desde la BD y guardarla en el archivo de caché para el usuario
    db_data = get_db_menu_data()
    logger.info("Datos obtenidos desde la base de datos.")
    save_to_json_file(db_data, CACHE_FILE_DB)
    logger.info("Menú actualizado (DB) guardado en caché.")

    logger.info("Sincronización completada satisfactoriamente.")

# -----------------------------------------------------
# Inicialización y Scheduler para actualización en BG
# -----------------------------------------------------
def initialize_cache(quipupos: int = 0):
    """
    Inicializa (o refresca) la caché y la base de datos
    para la sede distrimonster (local_id=12).
    """
    logger.info("Iniciando actualización de caché y BD para distrimonster...")
    sync_api_to_db_and_cache(quipupos)
    logger.info("Actualización inicial completada.")

    # Programar la tarea cada 30 minutos
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=sync_api_to_db_and_cache,
        trigger=IntervalTrigger(minutes=30),
        args=[0],  # Cambiar si deseas modificar quipupos
        id='cache_updater',
        name='Actualizar caché de distrimonster cada 30 minutos',
        replace_existing=True
    )

# -----------------------------------------------------
# Rutas
# -----------------------------------------------------
@distrimonster_router.post('/refresh-cache-distrimonster')
def refresh_cache_distimonster(quipupos: int = 0):
    """
    Endpoint para refrescar la caché y la base de datos manualmente
    para la sede distrimonster (local_id=12). La respuesta se retorna una vez
    que la sincronización se ha completado.
    """
    logger.info("Solicitud para actualizar caché y BD de distrimonster recibida.")
    sync_api_to_db_and_cache(quipupos)
    return {"message": "Actualización de caché y BD completada para distrimonster (local_id=12)."}

@distrimonster_router.get('/get-product-integration-distrimonster')
def get_product_integration_distimonster():
    """
    Retorna el contenido (JSON) proveniente de la base de datos,
    usando el archivo de caché `menu_distrimonster_db.json`.
    Si no existe el archivo, intenta sincronizar nuevamente.
    """
    if os.path.exists(CACHE_FILE_DB):
        try:
            with open(CACHE_FILE_DB, 'r', encoding='utf-8') as f:
                data_db = json.load(f)
            return data_db
        except (FileNotFoundError, json.JSONDecodeError):
            logger.error("El archivo de caché de BD está corrupto o no existe. Se reintenta la sincronización.")
    else:
        logger.warning("No existe archivo de caché de BD. Se hará sincronización inmediata.")

    # Si no existe o está corrupto, sincronizamos
    try:
        sync_api_to_db_and_cache()
        # Luego de sincronizar, leemos de nuevo
        with open(CACHE_FILE_DB, 'r', encoding='utf-8') as f:
            data_db = json.load(f)
        return data_db
    except Exception as e:
        logger.error(f"Error al sincronizar: {e}")
        raise HTTPException(status_code=500, detail="No se pudo obtener datos actualizados.")

@distrimonster_router.get('/get-categorized-products-distrimonster')
def get_categorized_products_distimonster():
    """
    Similar a /get-product-integration-distrimonster, pero procesando
    la estructura de categorías y productos desde el JSON de BD.
    """
    # Verificar caché de la BD
    if not os.path.exists(CACHE_FILE_DB):
        logger.warning("No existe archivo de caché de BD. Se hará sincronización inmediata.")
        try:
            sync_api_to_db_and_cache()
        except Exception as e:
            logger.error(f"Error al sincronizar: {e}")
            raise HTTPException(status_code=500, detail="No se pudo obtener datos actualizados.")

    # Intentar leer el JSON de la BD
    try:
        with open(CACHE_FILE_DB, 'r', encoding='utf-8') as f:
            db_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("El archivo de caché de BD está corrupto o no existe. Se reintenta la sincronización.")
        try:
            sync_api_to_db_and_cache()
            with open(CACHE_FILE_DB, 'r', encoding='utf-8') as f:
                db_data = json.load(f)
        except Exception as e:
            logger.error(f"Error al sincronizar: {e}")
            raise HTTPException(status_code=500, detail="No se pudo obtener datos actualizados.")

    # Procesar la estructura de categorías y productos
    categorias_raw = db_data.get('data', {}).get('listaCategorias', [])
    productos_raw = db_data.get('data', {}).get('data', [])

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

    return list(categorias.values())

@distrimonster_router.get('/get-image-distrimonster')
def get_image_distimonster(image_url: str):
    """
    Retorna una imagen (redimensionada a 600px de ancho) desde la caché si existe;
    si no, la descarga, la redimensiona y luego la almacena en caché.

    Parámetro:
    - image_url (str): Ruta parcial (sin https://img.restpe.com/) de la imagen.
    """
    image_code = image_url.split('/')[-1]
    image_path = os.path.join(CACHE_IMAGE_DIR, image_code)

    if not os.path.exists(image_path):
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

# -----------------------------------------------------
# Rutas de DB directas (si quieres exponerlas)
# -----------------------------------------------------
@distrimonster_router.get('/get-db-menu')
def get_db_menu():
    """
    Retorna el menú directamente desde la BD (use con precaución).
    """
    data_db = get_db_menu_data()
    return data_db

@distrimonster_router.put('/update-db-menu')
def update_db_menu():
    """
    Ejemplo de actualización manual de la BD, simplemente hardcodeado.
    """
    result = update_db_menu_data({"algo": "otra cosa"})
    return result


# -----------------------------------------------------
# (Opcional) Llamada inicial para iniciar el scheduler
# -----------------------------------------------------
# Normalmente, esto lo ejecutarías al iniciar tu aplicación (startup event).
# Aquí lo dejamos comentado para que lo llames en tu main:
#
# initialize_cache(quipupos=0)
