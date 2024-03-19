from fastapi import APIRouter,Form,File,HTTPException
from models.site_document import SiteDocument  # Asegúrate de que este módulo esté correctamente importado
from schema.site_document import SiteDocumentSchemaPost,SiteFileType  
from datetime import datetime
import uuid

from fastapi import APIRouter, UploadFile, File,Form
from fastapi.responses import FileResponse
from os import getcwd
from os.path import splitext
from pathlib import Path

from fastapi import APIRouter, File, Form, UploadFile
from pathlib import Path
from os import getcwd
from os.path import splitext
import shutil

# Asegúrate de que este esquema esté correctamente definido
site_document_router = APIRouter()

@site_document_router.get("/site_documents")
def get_site_documents():
    document_instance = SiteDocument()
    documents = document_instance.select_all_documents()
    document_instance.close_connection()
    return documents

@site_document_router.get("/site_document/{document_id}")
def get_site_document_by_id(document_id: int):
    document_instance = SiteDocument()
    document = document_instance.select_document_by_id(document_id)
    document_instance.close_connection()
    return document

@site_document_router.post("/site-document")
def create_site_document(document: SiteDocumentSchemaPost):
    document_instance = SiteDocument()
    document_id = document_instance.insert_document(document)
    created_document = document_instance.select_document_by_id(document_id)
    document_instance.close_connection()
    # Aquí puedes agregar lógica adicional si necesitas guardar un archivo usando el document_id como nombre
    return {"document_id": created_document['document_id']}


@site_document_router.put("/site-document/{document_id}")
def update_site_document(document_id: int, updated_document: SiteDocumentSchemaPost):
    document_instance = SiteDocument()
    updated_document_data = document_instance.update_document(document_id, updated_document)
    
    if updated_document_data:
        document_instance.close_connection()
        return updated_document_data
    else:
        document_instance.close_connection()
        return {"message": "Document not found"}




@site_document_router.delete("/site_document/{document_id}")
def delete_site_document(document_id: int):
    # Localiza el directorio donde se almacenan los archivos del documento
    document_dir = Path(getcwd()) / "files" / "documents" / str(document_id)

    # Elimina el directorio y todos los archivos dentro de él si existe
    if document_dir.exists():
        shutil.rmtree(document_dir)

    # Elimina el registro de la base de datos
    document_instance = SiteDocument()
    message = document_instance.delete_document(document_id)
    document_instance.close_connection()
    
    # Retorna el mensaje de confirmación
    return {"message": message}


@site_document_router.post('/upload-file-document/{document_id}')
async def upload_file_document(document_id: int, file: UploadFile = File(...), file_name: str = Form(...)):
    original_file_extension = splitext(file.filename)[1]
    upload_dir = Path(getcwd()) / "files" / "documents" / str(document_id)

    if upload_dir.exists():
        shutil.rmtree(upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Iniciar el sufijo de duplicado y el nombre completo del archivo
    duplicate_suffix = 1
    full_file_name = f"{file_name}{original_file_extension}"
    file_path = upload_dir / full_file_name

    # Verificar si el archivo ya existe y actualizar el nombre en consecuencia
    while file_path.exists():
        full_file_name = f"{file_name}-{duplicate_suffix}{original_file_extension}"
        file_path = upload_dir / full_file_name
        duplicate_suffix += 1

    # Guardar el archivo
    with open(file_path, "wb") as myfile:
        content = await file.read()
        myfile.write(content)

    return {"message": "Archivo subido con éxito", "file_name": file_name, "full_file_name": full_file_name}



from fastapi.responses import FileResponse

from glob import glob

@site_document_router.get("/get-document-file/{document_id}/{file_name}")
def get_document_file(document_id: int, file_name: str):
    base_dir = Path(getcwd()) / "files" / "documents" / str(document_id)
    # Buscar archivos que coincidan con el nombre proporcionado y cualquier sufijo numérico
    search_pattern = str(base_dir / f"{file_name}*.*")

    matching_files = glob(search_pattern)
    if matching_files:
        # Si hay múltiples coincidencias, esto podría ajustarse para seleccionar el archivo deseado
        return FileResponse(matching_files[0])
    else:
        return {"message": "Archivo no encontrado"}, 404
     
     
@site_document_router.get("/get-site-documents-info/{site_id}")
def get_site_documents_info(site_id: str):
    document_instance = SiteDocument()
    # Asumiendo que se debe implementar un nuevo método o ajustar uno existente
    data = document_instance.select_documents_by_site_id(site_id)  # Este es un método hipotético
    document_instance.close_connection()
    return data
                   

@site_document_router.post("/site-document")
def insert(site_data: SiteDocumentSchemaPost):
    document_instance = SiteDocument()
    data = site_data

    # Comprobar si el documento ya existe y ajustar el nombre de ser necesario
    base_name = data.name
    if document_instance.document_exists(base_name):
        max_suffix = document_instance.get_max_suffix(base_name)
        new_suffix = max_suffix + 1
        new_name = f"{base_name}-{new_suffix}"
        data.document_name = new_name  # Asumiendo que 'name' es un atributo de 'SiteDocumentSchemaPost'

    document_id = document_instance.insert_document(data)
    document_instance.close_connection()
    return {"document_id": document_id}



@site_document_router.get("/site-file-types")
def get_all_site_file_types():
    document_instance = SiteDocument()
    types = document_instance.get_all_site_file_types()
    document_instance.close_connection()
    return types

@site_document_router.get("/site-file-type/{type_id}")
def get_site_file_type(type_id: int):
    document_instance = SiteDocument()
    file_type = document_instance.get_site_file_type(type_id)
    document_instance.close_connection()
    if not file_type:
        raise HTTPException(status_code=404, detail="Site file type not found")
    return file_type

@site_document_router.post("/site-file-type")
def create_site_file_type(file_type: SiteFileType):
    document_instance = SiteDocument()
    type_id = document_instance.create_site_file_type(file_type)
    new_file_type = document_instance.get_site_file_type(type_id)
    document_instance.close_connection()
    return new_file_type


@site_document_router.put("/site-file-type/{type_id}")
def update_site_file_type(type_id: int, file_type: SiteFileType):
    document_instance = SiteDocument()

    document_instance.update_site_file_type(type_id, file_type)
    
    # updated_file_type = document_instance.get_site_file_type(updated_type_id)
    document_instance.close_connection()
    # return updated_file_type

@site_document_router.delete("/site-file-type/{type_id}")
def delete_site_file_type(type_id: int):
    document_instance = SiteDocument()
    document_instance.delete_site_file_type(type_id)
    document_instance.close_connection()
    return {"message": "Site file type deleted successfully"}

# @site_document_router.put("/update/site-document/{document_id}")
# def update(site_data: SiteDocumentSchemaPost, document_id: str):
#     document_instance = SiteDocument()
#     data = site_data.dict()
#     data['document_id'] = document_id
#     updated_document = document_instance.update_document(document_id, data)
#     document_instance.close_connection()
#     return updated_document




