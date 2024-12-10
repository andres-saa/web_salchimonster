from fastapi import APIRouter
import requests
from dotenv import load_dotenv
import os


load_dotenv()



integration_router = APIRouter()

TOKEN = os.getenv("API_TOKEN")

@integration_router.get('/get-product-integration/{dominio_id}/{local_id}')
def get_product_integration(dominio_id: int, local_id: int, quipupos: int = 0):
    # Construir la URL dinámica
    url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{dominio_id}/{local_id}"
    
 # Reemplaza con el token correcto
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Token token="{TOKEN}"'
    }
    
    # Parámetros de consulta
    params = {
        "quipupos": quipupos
    }

    # Hacer la solicitud HTTP GET
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        data = response.json()  # Convertir la respuesta en JSON
    except requests.RequestException as e:
        return {"error": str(e)}

    # Retornar la respuesta obtenida
    return data


@integration_router.get('/get-categorized-products/{dominio_id}/{local_id}')
def get_categorized_products(dominio_id: int, local_id: int, quipupos: int = 0):
    # Construir la URL dinámica
    url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{dominio_id}/{local_id}"
    
    # Encabezados necesarios
 # Reemplaza con el token correcto
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Token token="{TOKEN}"'
    }
    
    # Parámetros de consulta
    params = {
        "quipupos": quipupos
    }

    # Hacer la solicitud HTTP GET
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        api_response = response.json()  # Convertir la respuesta en JSON
    except requests.RequestException as e:
        return {"error": str(e)}

    # Extraer categorías y productos
    categorias_raw = api_response['data']['listaCategorias']
    productos_raw = api_response['data']['data']
    # return( productos_raw)
    
    print(productos_raw)

    # Preparar categorías base
    categorias = {cat["categoria_id"]: {
        "categoria_id": cat["categoria_id"],
        "local_id": cat["local_id"],
        "categoria_descripcion": cat["categoria_descripcion"],
        "categoria_estado": cat["categoria_estado"],
        "categoria_padreid": cat["categoria_padreid"],
        "categoria_color": cat["categoria_color"],
        "categoria_delivery": cat["categoria_delivery"],
        "products": []
    } for cat in categorias_raw}

    # Asociar productos completos con categorías
    for producto in productos_raw:
        # Validar que producto sea un diccionario
        if isinstance(producto, dict):
            categoria_id = producto.get("categoria_id")
            if categoria_id in categorias:
                categorias[categoria_id]["products"].append(producto)  # Agregar producto completo
        else:
            # Si no es un diccionario, lo ignoramos o manejamos el error
            continue

    # Convertir categorías a lista
    resultado = list(categorias.values())
    return resultado
