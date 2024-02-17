from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse


import os
from fastapi import UploadFile, File,Form
from pathlib import Path

from os.path import splitext
from typing import List
from models.archived_file import ArchivedFiles,Areas,DocumentTypes  # Asume que has movido la clase a models/archived_files.py
from schema.archived_file import ArchivedFile,Area,DocumentType  # Asume que este es tu esquema Pydantic

archivedFiles_router = APIRouter()

@archivedFiles_router.get("/archived-files")
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
async def create_file(file: UploadFile = File(...), file_data: ArchivedFile = dict):
    files_instance = ArchivedFiles()
    file_id = files_instance.insert_file(file, file_data)
    files_instance.close_connection()

    # Crear la carpeta 'files' si no existe
    files_folder = Path("files")
    files_folder.mkdir(parents=True, exist_ok=True)

    # Guardar el archivo en la carpeta 'files'
    file_path = files_folder / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {"filename": file.filename, "file_data": file_data, "id_file": file_id}




@archivedFiles_router.post("/upload-archived-file/{training_id}")
async def upload_training_file(training_id: str, 
                               file: UploadFile = File(...),
                               custom_filename: str = Form(...)):
    upload_dir = Path.cwd() / "files" / "archived_files" / training_id
    upload_dir.mkdir(parents=True, exist_ok=True)

    _, extension = splitext(file.filename)
    final_filename = custom_filename
    file_path = upload_dir / f"{final_filename}{extension}"

    # Verificar si el archivo ya existe y modificar el nombre si es necesario
    counter = 1
    while file_path.exists():
        final_filename = f"{custom_filename}_{counter}"
        file_path = upload_dir / f"{final_filename}{extension}"
        counter += 1

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)


@archivedFiles_router.get("/get-archived-file/{training_id}/{filename}")
async def get_archived_file(training_id: str, filename: str):
    file_path = Path.cwd() / "files" / "archived_files" / training_id / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(str(file_path))
    


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
    result = files_instance.delete_file(file_id)
    files_instance.close_connection()
    if result is None:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted successfully"}


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
