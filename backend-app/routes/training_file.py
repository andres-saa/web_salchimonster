from fastapi import APIRouter
from models.training_file import TrainingFileModel  # Asegúrate de importar tu modelo de archivo de capacitación
from schema.training_file import TrainingFile  # Importa tu esquema Pydantic aquí
from fastapi import FastAPI, UploadFile, File,Form 
from fastapi import APIRouter
from fastapi.responses import FileResponse
from schema.training_file import TrainingFile  # Asegúrate de importar tu esquema Pydantic aquí

from pathlib import Path
from os.path import splitext

training_file_router = APIRouter()

@training_file_router.get("/training-files")
def get_training_files():
    training_file_instance = TrainingFileModel()
    files = training_file_instance.select_all_files()
    training_file_instance.close_connection()
    return files



@training_file_router.get("/training-files/{training_id}")
def get_files_by_training_id(training_id: int):
    training_file_instance = TrainingFileModel()
    files = training_file_instance.select_files_by_training_id(training_id)
    training_file_instance.close_connection()
    return files

@training_file_router.get("/training-file/{file_id}")
def get_training_file_by_id(file_id: int):
    training_file_instance = TrainingFileModel()
    file = training_file_instance.select_file_by_id(file_id)
    training_file_instance.close_connection()
    return file

@training_file_router.delete("/training-file/{file_id}")
def delete_training_file(file_id: int):
    training_file_instance = TrainingFileModel()
    result = training_file_instance.delete_file(file_id)
    training_file_instance.close_connection()
    return {"message": result}

@training_file_router.post("/training-file")
def create_training_file(file: TrainingFile):
    training_file_instance = TrainingFileModel()
    file_id = training_file_instance.insert_file(file)
    training_file_instance.close_connection()
    return {"file_id": file_id}





@training_file_router.post("/upload-training-file/{training_id}")
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


@training_file_router.delete("/delete-training-file/{file_id}")
def delete_training_file(file_id: int):
    # Obtén la información del archivo de la base de datos
    # Por ejemplo: file_info = get_file_info(file_id)

    file_path = Path(file_info['file_path'])
    if file_path.exists():
        file_path.unlink()  # Elimina el archivo

    # Ahora elimina el registro de la base de datos
    # Por ejemplo: delete_file(file_id)

    return {"message": "Archivo eliminado con éxito"}




@training_file_router.get("/get-training-file/{training_id}/{file_name}")
def get_training_file(training_id: str, file_name: str):
    # Construir la ruta del archivo basada en el training_id y el nombre del archivo
    file_path = Path.cwd() / "files" / "training" / training_id / file_name

    # Verificar si el archivo existe
    if file_path.exists():
        return FileResponse(file_path)
    else:
        return {"message": "Archivo no encontrado"}, 404