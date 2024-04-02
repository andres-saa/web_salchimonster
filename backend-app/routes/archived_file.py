from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Depends
from fastapi.responses import FileResponse
from datetime import datetime

# from pathlib import Path
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from pathlib import Path
import shutil

import os
from fastapi import UploadFile, File,Form
from pathlib import Path

from os.path import splitext
from typing import List
from models.archived_file import ArchivedFiles,Areas,DocumentTypes  # Asume que has movido la clase a models/archived_files.py
from schema.archived_file import ArchivedFile,Area,DocumentType  # Asume que este es tu esquema Pydantic

archivedFiles_router = APIRouter()

@archivedFiles_router.get("/archived-files" )
def get_files():
    files_instance = ArchivedFiles()
    files = files_instance.select_all_files()
    files_instance.close_connection()
    return files


@archivedFiles_router.get("/archived-file/{file_id}")
def get_file_by_id(file_id: int):
    files_instance = ArchivedFiles()
    file = files_instance.select_file_by_id(file_id)
    files_instance.close_connection()
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file



@archivedFiles_router.post("/archived-file")
async def create_file(file_data: ArchivedFile):
    files_instance = ArchivedFiles()
    file_id = files_instance.insert_file(file_data)
    files_instance.close_connection()

    return {"file_id": file_id}




# @archivedFiles_router.post("/upload-archived-file/{training_id}")
# async def upload_training_file(training_id: str, 
#                                file: UploadFile = File(...),
#                                custom_filename: str = Form(...)):
#     upload_dir = Path.cwd() / "files" / "archived_files" / training_id
#     upload_dir.mkdir(parents=True, exist_ok=True)

#     _, extension = splitext(file.filename)
#     final_filename = custom_filename
#     file_path = upload_dir / f"{final_filename}{extension}"

#     # Verificar si el archivo ya existe y modificar el nombre si es necesario
#     counter = 1
#     while file_path.exists():
#         final_filename = f"{custom_filename}_{counter}"
#         file_path = upload_dir / f"{final_filename}{extension}"
#         counter += 1

#     with open(file_path, "wb") as buffer:
#         content = await file.read()
#         buffer.write(content)


# @archivedFiles_router.get("/get-archived-file/{training_id}/{filename}")
# async def get_archived_file(training_id: str, filename: str):
#     file_path = Path.cwd() / "files" / "archived_files" / training_id / filename
    
#     if not file_path.exists():
#         raise HTTPException(status_code=404, detail="File not found")
    
#     return FileResponse(str(file_path))
    
# @archivedFiles_router.post("/upload-archived-file/{archived_id}")

# async def upload_training_file(file: UploadFile, archived_id:int, filedata:ArchivedFile ):
#     archived_instance = ArchivedFiles()
#     file_db = archived_instance.select_file_by_id(archived_id)
#     # return file

#     if (file_db):
#         upload_dir = Path.cwd() / "files" / "archived_files" / str(file_db['area_name'])  / str(file_db['type_name']) 
#         upload_dir.mkdir(parents=True, exist_ok=True)
#     else:
#         return 'paila'
#     _, extension = splitext(file.filename)
#     # return file
#     final_filename = str(file_db['file_name'])
#     file_path = upload_dir / f"{final_filename}{extension}"
    
#     with open(file_path, "wb") as buffer:
#         content = await file.read()
#         buffer.write(content)

#     return "hecho"


@archivedFiles_router.get("/archived-files/area/{area_id}")
def get_files_by_area(area_id: int):
    files_instance = ArchivedFiles()
    files = files_instance.select_files_by_area(area_id)
    files_instance.close_connection()
    return files

@archivedFiles_router.get("/archived-files/type/{type_id}")
def get_files_by_type(type_id: int):
    files_instance = ArchivedFiles()
    files = files_instance.select_files_by_type(type_id)
    files_instance.close_connection()
    return files

@archivedFiles_router.get("/archived-files/{area_id}/{type_id}")
def get_files_by_area_and_type(area_id: int, type_id: int):
    files_instance = ArchivedFiles()
    files = files_instance.select_files_by_area_and_type(area_id, type_id)
    files_instance.close_connection()
    if not files:
        raise HTTPException(status_code=404, detail="Files not found")
    return files


@archivedFiles_router.post("/upload-archived-file/")
async def upload_archived_file(
    file: UploadFile = File(...),
    id_area: int = Form(...),
    id_type: int = Form(...),
    file_name: str = Form(...),  # El nombre deseado sin extensión
):
    # Instancia de la clase para manejar archivos archivados
    files_instance = ArchivedFiles()
    
    # Determinar la extensión del archivo y el nombre final
    _, extension = splitext(file.filename)
    final_filename = f"{file_name}{extension}"

    # Construir la ruta de destino relativa y absoluta
    relative_path = Path("files") / "archived_files" / f"area_{id_area}" / f"tipo_{id_type}"
    upload_dir = Path.cwd() / relative_path
    upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = upload_dir / final_filename

    # Asegurar nombre único
    counter = 1
    while file_path.exists():
        final_filename = f"{file_name}_{counter}{extension}"
        file_path = upload_dir / final_filename
        counter += 1

    # Guardar el archivo
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Construir la URL del archivo relativa para la base de datos, asegurándose de no incluir doble slash
    file_url = str(relative_path / final_filename).replace("\\", "/")

    # Crear registro en la base de datos con el nombre final del archivo y la URL relativa
    file_data = ArchivedFile(
        file_name=final_filename,
        file_url=file_url,  # Usando la ruta relativa desde "files"
        upload_date=datetime.now(),
        id_area=id_area,
        id_type=id_type,
        file_extension=extension.lstrip('.')  # Eliminar el punto inicial de la extensión si existe
    )
    file_id = files_instance.insert_file(file_data)

    return {"file_id": file_id, "file_name": final_filename, "file_path": file_url}

@archivedFiles_router.get("/get-archived-file/{area_id}/{file_type_id}/{file_name}")
def get_training_file(area_id: str, file_type_id: str, file_name: str):
    # Construir la ruta del directorio basada en el área y el tipo de archivo
    directory_path = Path.cwd() / "files" / "archived_files" / f"area_{area_id}"  / f"tipo_{file_type_id}" 

    # Construir el patrón de búsqueda para el archivo, sin incluir la extensión
    file_pattern = file_name + ".*"

    # Buscar todos los archivos que coincidan con el patrón en el directorio especificado
    matching_files = list(directory_path.glob(file_pattern))

    # Verificar si se encontró al menos un archivo
    if matching_files:
        # Devolver el primer archivo encontrado
        return FileResponse(str(matching_files[0]))
    else:
        # Si no se encuentra ningún archivo, devolver un mensaje de error
        raise HTTPException(status_code=404, detail="Archivo no encontrado")


@archivedFiles_router.put("/archived-file/{file_id}")
def update_file(file_id: int, file: ArchivedFile):
    files_instance = ArchivedFiles()
    updated_file = files_instance.update_file(file_id, file)
    files_instance.close_connection()
    if updated_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return updated_file


@archivedFiles_router.delete("/archived-file/{file_id}")
def delete_file(file_id: int):
    files_instance = ArchivedFiles()
    file = files_instance.select_file_by_id(file_id)  # Step 1: Get file details
    
    if file is None:
        files_instance.close_connection()
        raise HTTPException(status_code=404, detail="File not found")

    # Construct the full path to the file. Adjust the path construction based on your actual file storage structure.
    file_path = Path.cwd() / file['file_url']  # Adjust the path according to your structure

    # Step 2: Delete the file from the filesystem if it exists
    if file_path.exists():
        file_path.unlink()
        
        
    # Step 3: Delete the file record from the database
    result = files_instance.delete_file(file_id)
    files_instance.close_connection()

    if result is None:
        raise HTTPException(status_code=500, detail="Error deleting file record from the database")

    return {"message": "File deleted successfully from both database and storage", "noe":file_path}



areas_router = APIRouter()

@areas_router.get("/areas")
def get_areas():
    areas_instance = Areas()
    areas = areas_instance.select_all_areas()
    areas_instance.close_connection()
    return areas

@areas_router.get("/area/{area_id}")
def get_area_by_id(area_id: int):
    areas_instance = Areas()
    area = areas_instance.select_area_by_id(area_id)
    areas_instance.close_connection()
    if area is None:
        raise HTTPException(status_code=404, detail="Area not found")
    return area

@areas_router.post("/area")
def create_area(area: Area):
    areas_instance = Areas()
    area_id = areas_instance.insert_area(area.area_name)  # Ajusta según tu esquema
    areas_instance.close_connection()
    return {**area.dict(), "id_area": area_id}

@areas_router.put("/area/{area_id}")
def update_area(area_id: int, area: Area):
    areas_instance = Areas()
    updated_area = areas_instance.update_area(area_id, area.area_name)  # Ajusta según tu esquema
    areas_instance.close_connection()
    if updated_area is None:
        raise HTTPException(status_code=404, detail="Area not found")
    return updated_area

@areas_router.delete("/area/{area_id}")
def delete_area(area_id: int):
    areas_instance = Areas()
    result = areas_instance.delete_area(area_id)
    areas_instance.close_connection()
    return {"message": result}


types_router = APIRouter()

@types_router.get("/archived-file-types")
def get_types():
    types_instance = DocumentTypes()
    types = types_instance.select_all_types()
    types_instance.close_connection()
    return types

@types_router.get("/archived-file-type/{type_id}")
def get_type_by_id(type_id: int):
    types_instance = DocumentTypes()
    type = types_instance.select_type_by_id(type_id)
    types_instance.close_connection()
    if type is None:
        raise HTTPException(status_code=404, detail="Document type not found")
    return type

@types_router.post("/archived-file-type")
def create_type(type: DocumentType):
    types_instance = DocumentTypes()
    type_id = types_instance.insert_type(type.type_name)  # Ajusta según tu esquema
    types_instance.close_connection()
    return {**type.dict(), "id_type": type_id}

@types_router.put("/archived-file-type/{type_id}")
def update_type(type_id: int, type: DocumentType):
    types_instance = DocumentTypes()
    updated_type = types_instance.update_type(type_id, type.type_name)  # Ajusta según tu esquema
    types_instance.close_connection()
    if updated_type is None:
        raise HTTPException(status_code=404, detail="Document type not found")
    return updated_type

@types_router.delete("/archived-file-type/{type_id}")
def delete_type(type_id: int):
    types_instance = DocumentTypes()
    result = types_instance.delete_type(type_id)
    types_instance.close_connection()
    return {"message": result}
