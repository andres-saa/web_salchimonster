from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional

# Importa tu modelo Employer y esquema de validación EmployerSchemaPost
from models.employer import Employer
from schema.employer.employer import EmployerSchemaPost
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
    
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": user['dni'], "rol":user['position'],"name":user["name"],"permissions":user["permissions"], "site_name":user["site_name"], "dni":user['dni'] ,"id":user['id'],"site_id":user["site_id"] }, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer",}

# Ruta protegida
@login.get("/profile")
async def read_users_me(current_user: EmployerSchemaPost = Depends(security.oauth2_scheme)):
    return current_user

@login.get("/validate-token")
async def validate_and_renew_token(token: str = Depends(security.oauth2_scheme)):
    try:
        # Decodificar el token para verificar su validez y expiración
        payload = jwt.decode(token, security.secret_key, algorithms=[security.algorithm])
        # Si el token es válido, crear un nuevo token con la misma información pero con una nueva expiración
        access_token_expires = timedelta(minutes=60)  # O el tiempo de expiración que prefieras
        new_access_token = create_access_token(
            data={"sub": payload["sub"], "rol": payload["rol"], "name":payload["name"],"permissions":payload["permissions"],"site_name":payload["site_name"], "dni": payload["dni"], "id": payload["id"], "site_id": payload["site_id"]},
            expires_delta=access_token_expires
        )
        return {"access_token": new_access_token, "token_type": "bearer"}
    except jwt.ExpiredSignatureError:
        return False, "Token expirado"
    except JWTError:
        return False, "Token no válido"