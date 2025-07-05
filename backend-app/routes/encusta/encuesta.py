from fastapi import APIRouter
from models.encuestas.encuestas import Encuesta
from typing import List,Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

encuesta_router = APIRouter()
from schema.user import user_schema_post

class Votacion(BaseModel):
    question_id:int
    option_id:Optional[int] = None
    text:Optional[str] = None
    question:Optional[str] = None
    
class EncuestaVotar(BaseModel):
    encuesta_id:int
    user:user_schema_post
    select:List[Votacion]
    

@encuesta_router.get('/encuestas')
def get_encustas():
    encusta_instance = Encuesta()
    result = encusta_instance.get_encuesta()
    return result


@encuesta_router.get('/encuesta/{id}')
def get_encustas(id:int):
    encusta_instance = Encuesta()
    result = encusta_instance.get_encuesta_by_id(id)
    return result

@encuesta_router.get('/encuestas_results/{encuenta_id}')
def get_encustas(encuesta_id:int):
    encusta_instance = Encuesta()
    result = encusta_instance.get_encuesta_results(encuesta_id=encuesta_id)
    return result

@encuesta_router.get('/encuestas_results_text/{encuesta_id}')
def get_encustas(encuesta_id:int):
    encusta_instance = Encuesta()
    result = encusta_instance.get_encuesta_results(encuesta_id=encuesta_id)
    
    respuesta1 = result[0]['questions_summary'][0]["responses"]['Belleville\n500 Cortlandt St NJ']
    respuesta2 = result[0]['questions_summary'][0]["responses"]['Union city\n2100 Kerrigan Ave NJ']
    
    return {"message": f"""Claro, asi va la cosa para Belleville tenemos *{respuesta1}* votos \n y para Union city llevamos *{respuesta2}* votos """}




@encuesta_router.get('/encuestas_results_text_html/{encuesta_id}', response_class=HTMLResponse)
def get_encustas(encuesta_id: int):
    encusta_instance = Encuesta()
    result = encusta_instance.get_encuesta_results(encuesta_id=encuesta_id)
    
    respuesta1 = result[0]['questions_summary'][0]["responses"]['Belleville\n500 Cortlandt St NJ']
    respuesta2 = result[0]['questions_summary'][0]["responses"]['Union city\n2100 Kerrigan Ave NJ']

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resultados de la Encuesta</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #fafafa;
                margin: 0;
                padding: 1rem;
                color: #222;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }}
            .card {{
                background-color: #fff;
                border-radius: 16px;
                padding: 2rem;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                max-width: 90%;
                width: 400px;
                text-align: center;
            }}
            h2 {{
                font-size: 2rem;
                color: #4CAF50;
                margin-bottom: 1.5rem;
            }}
            .result {{
                font-size: 1.5rem;
                margin-bottom: 1rem;
            }}
            .thanks {{
                font-size: 1.2rem;
                margin-top: 1.5rem;
                color: #555;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>📊 Resultados de la Encuesta</h2>
            <p class="result">📍 Belleville:<br><strong>{respuesta1}</strong> votos</p>
            <p class="result">📍 Union City:<br><strong>{respuesta2}</strong> votos</p>
            <p class="thanks">¡Gracias por participar! 🎉</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)




@encuesta_router.get('/encuestas_users/{encuesta_id}')
def get_encustas(encuesta_id:int):
    encusta_instance = Encuesta()
    result = encusta_instance.get_encuesta_users(encuesta_id=encuesta_id)
    return result




@encuesta_router.get('/encuestas_all')
def get_encustas():
    encusta_instance = Encuesta()
    result = encusta_instance.get_encuestas()
    return result



@encuesta_router.post('/votar')
def votar (data:EncuestaVotar):

    encusta_instance = Encuesta()
    result = encusta_instance.votar(data)
    return result



@encuesta_router.post('/votar-encuesta')
def votar (data:EncuestaVotar):

    encusta_instance = Encuesta()
    result = encusta_instance.votar_encuesta(data)
    return result