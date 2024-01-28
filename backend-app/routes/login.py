from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional

# Importa tu modelo Employer y esquema de validación EmployerSchemaPost
from models.employer import Employer
from schema.employer import EmployerSchemaPost
from auth_utils.Security import Security,authenticate_user,create_access_token
login = APIRouter()

# Configuración de seguridad

security = Security()

# Modelo Pydantic para el inicio de sesión
class LoginSchema(BaseModel):
    dni: str
    password: str


# Ruta para autenticar al usuario y generar un token JWT
@login.post("/token-employer")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Inicio de sesión fallido")
    
    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(
        data={"sub": user['dni'], "rol":user['position'], "dni":user['dni'] ,"id":user['id'] }, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Ruta protegida
@login.get("/profile")
async def read_users_me(current_user: EmployerSchemaPost = Depends(security.oauth2_scheme)):
    return current_user
