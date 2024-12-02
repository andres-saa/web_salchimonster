from fastapi import APIRouter
import requests

integration_router = APIRouter()

@integration_router.get('/get-product-integration/{dominio_id}/{local_id}')
def get_inventory_report(dominio_id: int, local_id: int, quipupos: int = 0):
    # Construir la URL dinámica
    url = f"https://api.restaurant.pe/restaurant/readonly/rest/delivery/obtenerCartaPorLocal/{dominio_id}/{local_id}"
    
    # Encabezados necesarios
    token = '898f626c749eea07442da4fccffe2e86'  # Reemplaza con el token correcto
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Token token="{token}"'
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



from pydantic import BaseModel
from typing import List

class PolygonData(BaseModel):
    name: str
    coordinates: List[List[float]]  # Lista de coordenadas [[lat, lng], ...]
    delivery_price: float
    
    