from fastapi import APIRouter, HTTPException
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
def create_file(file: ArchivedFile):
    files_instance = ArchivedFiles()
    file_id = files_instance.insert_file(file)
    files_instance.close_connection()
    return {**file.dict(), "id_file": file_id}

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



from fastapi import APIRouter
from models.training_file import TrainingFileModel  # Asegúrate de importar tu modelo de archivo de capacitación
from schema.training_file import TrainingFile  # Importa tu esquema Pydantic aquí
from fastapi import FastAPI, UploadFile, File,Form 
from fastapi import APIRouter
from fastapi.responses import FileResponse
from schema.training_file import TrainingFile  # Asegúrate de importar tu esquema Pydantic aquí

from pathlib import Path
from os.path import splitext

archivedFiles_router = APIRouter()



@archivedFiles_router.post("/training-file")
def create_training_file(file: TrainingFile):
    training_file_instance = TrainingFileModel()
    file_id = training_file_instance.insert_file(file)
    training_file_instance.close_connection()
    return {"file_id": file_id}





@archivedFiles_router.post("/upload-training-file/{training_id}")
async def upload_training_file(training_id: str, 
                               file: UploadFile = File(...),
                               custom_filename: str = Form(...)):
    upload_dir = Path.cwd() / "files" / "training" / training_id
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

    file_data = TrainingFile(
        training_id=training_id,
        file_name=final_filename + extension,
        file_url=str(file_path),
        file_type=extension.lstrip('.')
    )

    training_file_instance = TrainingFileModel()
    try:
        file_id = training_file_instance.insert_file(file_data)
    except Exception as e:
        return {"message": "Error al registrar el archivo en la base de datos", "error": str(e)}
    finally:
        training_file_instance.close_connection()

    return {"message": "Archivo subido con éxito", "file_id": file_id, "file_path": str(file_path)}


@archivedFiles_router.delete("/delete-training-file/{file_id}")
def delete_training_file(file_id: int):
    # Obtén la información del archivo de la base de datos
    # Por ejemplo: file_info = get_file_info(file_id)

    file_path = Path(file_info['file_path'])
    if file_path.exists():
        file_path.unlink()  # Elimina el archivo

    # Ahora elimina el registro de la base de datos
    # Por ejemplo: delete_file(file_id)

    return {"message": "Archivo eliminado con éxito"}




@archivedFiles_router.get("/get-training-file/{training_id}/{file_name}")
def get_training_file(training_id: str, file_name: str):
    # Construir la ruta del archivo basada en el training_id y el nombre del archivo
    file_path = Path.cwd() / "files" / "training" / training_id / file_name

    # Verificar si el archivo existe
    if file_path.exists():
        return FileResponse(file_path)
    else:
        return {"message": "Archivo no encontrado"}, 404