
from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    destinatario: EmailStr
    asunto: str
    cuerpo: str