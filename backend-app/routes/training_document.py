from fastapi import APIRouter,Form,File
from models.site_document import SiteDocument  # Asegúrate de que este módulo esté correctamente importado
from schema.site_document import SiteDocumentSchemaPost  


from fastapi import APIRouter, UploadFile, File,Form
from fastapi.responses import FileResponse
from os import getcwd
from os.path import splitext
from pathlib import Path



training_document_router = APIRouter()


@training_document_router.post('/upload-file-training/')
async def upload_user_photo(site_id: str = Form(...), name: str = Form(...), file: UploadFile = File(...)):
    # Obtener la extensión del archivo
    file_extension = splitext(file.filename)[1]

    # Directorio donde se guardarán las imágenes
    upload_dir = Path(getcwd()) / "files" / "documents" / "training" / site_id

    # Crear la carpeta "users" si no existe
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Combinar el nombre del archivo con el directorio
    file_path = upload_dir / (site_id + " " + name + file_extension)

    with open(file_path, "wb") as myflle:
        content = await file.read()
        myflle.write(content)

    return "hecho"


@training_document_router.get("/get-training-document/{site_id}/{name}")
def get_site_document(site_id: str, name: str):
    base_dir = getcwd() + "/files" + "/documents" + "/training" + "/" + site_id 

    # Lista de extensiones de archivo a buscar en orden de preferencia
    file_extensions = ['.pdf', '.jpg', '.jpeg', '.gif', '.bmp']

    for extension in file_extensions:
        file_path = base_dir + "/" + site_id + " " + name + extension
        print (file_path)
        file = Path(file_path)

        if file.exists():


            return FileResponse(file)

    print(base_dir)     
    # Si no se encuentra ninguna de las extensiones, puedes devolver un error o un archivo predeterminado
    return "Archivo no encontrado", 404