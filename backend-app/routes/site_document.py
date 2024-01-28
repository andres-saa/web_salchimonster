from fastapi import APIRouter,Form,File
from models.site_document import SiteDocument  # Asegúrate de que este módulo esté correctamente importado
from schema.site_document import SiteDocumentSchemaPost  


from fastapi import APIRouter, UploadFile, File,Form
from fastapi.responses import FileResponse
from os import getcwd
from os.path import splitext
from pathlib import Path


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


@site_document_router.post('/upload-file-document/')
async def upload_user_photo(site_id: str = Form(...), type_document: str = Form(...), file: UploadFile = File(...)):
    # Obtener la extensión del archivo
    file_extension = splitext(file.filename)[1]

    # Directorio donde se guardarán las imágenes
    upload_dir = Path(getcwd()) / "files" / "documents" / "sites" / site_id

    # Crear la carpeta "users" si no existe
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Combinar el nombre del archivo con el directorio
    file_path = upload_dir / (site_id + " " + type_document + file_extension)

    with open(file_path, "wb") as myflle:
        content = await file.read()
        myflle.write(content)

    return "hecho"


@site_document_router.post('/upload-file-document/')
async def upload_user_photo(site_id: str = Form(...), type_document: str = Form(...), file: UploadFile = File(...)):
    # Obtener la extensión del archivo
    file_extension = splitext(file.filename)[1]

    # Directorio donde se guardarán las imágenes
    upload_dir = Path(getcwd()) / "files" / "documents" / "sites" / site_id

    # Crear la carpeta "users" si no existe
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Combinar el nombre del archivo con el directorio
    file_path = upload_dir / (site_id + " " + type_document + file_extension)

    with open(file_path, "wb") as myflle:
        content = await file.read()
        myflle.write(content)

    return "hecho"

@site_document_router.get("/get-site-document/{site_id}/{type_document}")
def get_site_document(site_id: str, type_document: str):
    base_dir = getcwd() + "/files" + "/documents" + "/sites" + "/" + site_id 

    # Lista de extensiones de archivo a buscar en orden de preferencia
    file_extensions = ['.pdf', '.jpg', '.jpeg', '.gif', '.bmp']

    for extension in file_extensions:
        file_path = base_dir + "/" + site_id + " " + type_document + extension
        print (file_path)
        file = Path(file_path)

        if file.exists():


            return FileResponse(file)
                   
    

    print(base_dir)     
    # Si no se encuentra ninguna de las extensiones, puedes devolver un error o un archivo predeterminado
    return "Archivo no encontrado", 404


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



