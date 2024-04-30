# # authentication.py

# from jose import jwt
# from datetime import datetime, timedelta
# from passlib.context import CryptContext
# from fastapi import HTTPException, Depends
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from typing import Optional
# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from pydantic import BaseModel
# from datetime import datetime, timedelta
# from typing import Optional

# # Importa tu modelo Employer y esquema de validación EmployerSchemaPost
# from models.employer import Employer
# from schema.employer import EmployerSchemaPost


# # Configuración de seguridad
# class Security:
#     def __init__(self):
#         self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token-employer")
#         self.secret_key = "your_secret_key"  # Cambia esto a una clave secreta segura
#         self.token_expiration = timedelta(hours=1)

# security = Security()

# # Modelo Pydantic para el inicio de sesión
# class LoginSchema(BaseModel):
#     dni: str
#     password: str

# # Función para autenticar al usuario sin encriptación de contraseña
# def authenticate_user(dni: str, password: str):
#     print('hola')
#     employer_instance = Employer()
#     user = employer_instance.select_employer_by_dni(dni)
#     employer_instance.close_connection()

#     if user and user.get("password") == password:
#         return user

# # Función para crear un token JWT
# def create_access_token(data: dict, expires_delta: timedelta = 10):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + security.token_expiration
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, security.secret_key, algorithm="HS256")
#     return encoded_jwt

# # Función para obtener el usuario actual a partir del token
# def get_current_user(token: str = Depends(security.oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, security.secret_key, algorithms=["HS256"])
#         return payload
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token expirado")
#     except jwt.JWTError:
#         raise HTTPException(status_code=401, detail="Token no válido")

# # Función para verificar si un usuario tiene un rol específico
# def is_user_authorized(roles: list):
#     def check_authorization(current_user: dict = Depends(get_current_user)):
#         user_roles = current_user.get("rol", [])
#         for role in roles:
#             if role in user_roles:
#                 return True
#         raise HTTPException(status_code=403, detail="No autorizado")
#     return check_authorization
    