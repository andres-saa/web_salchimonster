

from models.mail import enviar_correo
from fastapi import APIRouter
from schema.mail import EmailSchema
from fastapi import HTTPException

mail_router = APIRouter()

@mail_router.post("/mail")
def enviar_prueba_email(email_data: EmailSchema):
    try:
        enviar_correo(
            email_data.destinatario, 
            email_data.asunto, 
            email_data.cuerpo
        )
        return {"message": "Correo enviado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))