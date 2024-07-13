# Usa la imagen base de Python 3.9 con Alpine
FROM python:3.9-alpine

# Copia el contenido actual del directorio en el directorio /mi_app en el contenedor
COPY . /mi_app

# Establece /mi_app como el directorio de trabajo
WORKDIR /mi_app

RUN pip install --upgrade pip
# Instala las dependencias de Python usando pip
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto donde Uvicorn estará disponible
EXPOSE 8000

# Comando predeterminado para ejecutar al iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
