from datetime import datetime, timedelta
from jose import jwt
from models.employer import Employer
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional

class Security:
    def __init__(self):
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token-employer")
        self.secret_key = "your_secret_key"  # Cambia esto a una clave secreta segura
        self.token_expiration = timedelta(hours=1)

security = Security()

# Modelo Pydantic para el inicio de sesión
class LoginSchema(BaseModel):
    dni: str
    password: str

# Función para autenticar al usuario sin encriptación de contraseña
def authenticate_user(dni: str, password: str):
    employer_instance = Employer()
    user = employer_instance.select_employer_by_dni(dni)
    # print(user)
    employer_instance.close_connection()

    print(user)
    if user and user.get("password") == password:  # Access the 'password' key in the dictionary
        return user

# Función para crear un token JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + security.token_expiration
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, security.secret_key, algorithm="HS256")
    return encoded_jwt
