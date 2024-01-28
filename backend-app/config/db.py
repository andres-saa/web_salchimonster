# config/db.py

from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtén las credenciales de la base de datos desde las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Construye la URL de la base de datos
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Crea el engine de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

meta = MetaData()

# Asociar el engine con la MetaData al llamar create_all
meta.create_all(bind=engine)

conn = engine.connect()
