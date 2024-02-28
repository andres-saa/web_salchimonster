from fastapi import APIRouter,Form,File
from models.site_document import SiteDocument  # Asegúrate de que este módulo esté correctamente importado
from schema.site_document import SiteDocumentSchemaPost  
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
    document_instance = SiteDocument()
    message = document_instance.delete_document(document_id)
    document_instance.close_connection()
    return {"message": message}


@site_document_router.post('/upload-file-document/{document_id}')
async def upload_file_document(document_id: int, file: UploadFile = File(...), file_name: str = Form(...)):
    # Extraer la extensión del archivo original
    original_file_extension = splitext(file.filename)[1]

    # Directorio donde se guardarán los archivos
    upload_dir = Path(getcwd()) / "files" / "documents" / str(document_id)

    # Eliminar la carpeta si ya existe, para remover todo su contenido
    if upload_dir.exists():
        shutil.rmtree(upload_dir)
    
    # Crear la carpeta nuevamente después de eliminarla
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Construir el nombre completo del archivo usando el nombre proporcionado y la extensión original
    full_file_name = f"{file_name}{original_file_extension}"
    file_path = upload_dir / full_file_name

    # Guardar el nuevo archivo
    with open(file_path, "wb") as myfile:
        content = await file.read()
        myfile.write(content)

    return {"message": "Archivo subido con éxito", "file_name": file_name, "full_file_name": full_file_name}

from fastapi.responses import FileResponse

from glob import glob

@site_document_router.get("/get-document-file/{document_id}/{file_name}")
def get_document_file(document_id: int, file_name: str):
    base_dir = Path(getcwd()) / "files" / "documents" / str(document_id)
    search_pattern = str(base_dir / f"{file_name}.*")

    matching_files = glob(search_pattern)
    if matching_files:
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
    document_id = document_instance.insert_document(data)
    document_instance.close_connection()
    return {"document_id": document_id}


# @site_document_router.put("/update/site-document/{document_id}")
# def update(site_data: SiteDocumentSchemaPost, document_id: str):
#     document_instance = SiteDocument()
#     data = site_data.dict()
#     data['document_id'] = document_id
#     updated_document = document_instance.update_document(document_id, data)
#     document_instance.close_connection()
#     return updated_document



