from fastapi import APIRouter, Response,UploadFile,File,HTTPException
from fastapi.responses import StreamingResponse
from models.neigborhoods.neigborhoods import Neigborhoods
import requests
from io import BytesIO
from pydantic import BaseModel

from typing import List

neiborhoods_route = APIRouter()


class get_neiborghoo(BaseModel):
    site_ids:list[int]


@neiborhoods_route.post('/get-neigborhoods-report/', tags=['neigborhoods'])
def get_neigborhoods(data:get_neiborghoo):
    
    
    neigborhood_instance = Neigborhoods()
    result = neigborhood_instance.get_neiborhoods_report(data)

    if not result:
        return []

    # En este ejemplo asumimos que `result[0]` es el objeto/datos que se necesitan
    data_to_send = result[0]

    # Enviamos la data al endpoint que genera el Excel
    excel_response = requests.post(
        "https://excel-creator.salchimonster.com/crear-excel",
        json=data_to_send
    )

    # Verificamos que la respuesta sea exitosa
    if excel_response.status_code != 200:
        return {
            "error": "No se pudo generar el archivo Excel",
            "status_code": excel_response.status_code,
            "detalle": excel_response.text
        }

    # Convertimos el contenido binario a un archivo en memoria
    excel_file = BytesIO(excel_response.content)

    # Retornamos el archivo en un StreamingResponse para que se descargue
    headers = {
        "Content-Disposition": 'attachment; filename="report.xlsx"'
    }
    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers=headers
    )



@neiborhoods_route.post("/update-neigborhoods", tags=['neigborhoods'])
async def excel_to_json(file: UploadFile = File(...)):
    """
    Recibe un archivo Excel y lo reenvía a localhost:8000/excel-a-json.
    Luego retorna el JSON que devuelva ese endpoint.
    """
    # Leemos el contenido del archivo en memoria
    file_bytes = await file.read()

    # Realizamos la petición POST al otro servicio
    # Ajusta el nombre del campo (clave de 'files'), según lo que tu servicio en /excel-a-json espere.
    response = requests.post(
        "https://excel-creator.salchimonster.com/excel-a-json",
        files={"file": (file.filename, file_bytes, file.content_type)}
    )
    
    data = []

    # Validamos la respuesta
    if response.status_code == 200:
        # Retornamos directamente el JSON que nos haya devuelto /excel-a-json
        # return response.json()
    
    
        data = response.json()
    
    neigborhood_instance = Neigborhoods()
    result = neigborhood_instance.update_neigborhoods(data=data)
    # return data