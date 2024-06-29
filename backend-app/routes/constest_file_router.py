from fastapi import APIRouter, UploadFile,FastAPI, File,Form,BackgroundTasks
from fastapi.responses import FileResponse
from os import getcwd
from os.path import splitext
from pathlib import Path
# from model.files_connection import siteDocumentConnection
# from schema.site_document_schema import SiteDocumentSchemaPost,SiteDocumentSchema
from PIL import Image , ExifTags
from glob import glob

from os import remove
from fastapi.responses import JSONResponse
# conn = siteDocumentConnection()
from fastapi.middleware.cors import CORSMiddleware
import time
app = FastAPI()

# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas los orígenes, ajusta según tus necesidades
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)
router = APIRouter()

def rotate_image(path):
    try:
        image = Image.open(path)

        # Corregir la orientación si es necesario
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())
        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
        image.save(path)
        image.close()
    except (AttributeError, KeyError, IndexError):
        # Casos donde no se encuentren los metadatos EXIF
        pass


def resize_image(path: str, upload_dir: str, product_id: str, file_extension: str):
    sizes = [
        {"width": 96, "height": 96},
        {"width": 300, "height": 300},
        {"width": 600, "height": 600},
    ]

    for size in sizes:
        size_defined = size["width"], size["height"]
        image = Image.open(path, mode='r')
        image.thumbnail(size_defined)
        resized_file_path = upload_dir / (
            "product image " + product_id + " " + str(size["width"]) + 'x' + str(size["height"]) + file_extension)
        image.save(resized_file_path)


@router.get("/")
def root():
    return "hola"

@router.post('/upload-constest-image/{user_id}/{contest_id}/{evidence_id}')
async def upload_user_photo(evidence_id: str, file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks):
    # Directorio donde se guardarán las imágenes
    upload_dir = Path.cwd() / "files" / "images" / "contest" / evidence_id

    # Eliminar la carpeta y archivos existentes
    if upload_dir.is_dir():
        for existing_file in upload_dir.glob("*"):
            remove(existing_file)

    # Crear la carpeta "products"
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Obtener el nombre del archivo
    file_extension = splitext(file.filename)[1]

    # Combinar el nombre del archivo con el directorio
    file_path = upload_dir / ("product image " + evidence_id + file_extension)

    with open(file_path, "wb") as myflle:
        content = await file.read()
        myflle.write(content)
    
    
    rotate_image(file_path)

    background_tasks.add_task(resize_image, file_path, upload_dir, evidence_id, file_extension)
 
    return JSONResponse(content={"message": "hecho"}, status_code=200)





@router.get('/read-product-image/{height}/{product_id}')
def get_photo_profile(product_id: str, height: str):
    timestamp = int(time.time())  # Obtener el timestamp actual

    base_dir = Path(getcwd()) / "files" / "images" / "products" / product_id
    pattern = f"{base_dir}/product image {product_id} {height}x{height}.*"

    # Buscar archivos que coincidan con el patrón
    files = glob(pattern)

    if files:
        # Si se encuentran archivos, devolver el primero
        return FileResponse(files[0], headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "Version": str(timestamp)
        })

    # Si no se encuentra ningún archivo, devolver un error
    return "Archivo no encontrado", 404














# @router.post('/upload-site-documet/')
# async def upload_user_photo(site_name: str = Form(...), type_document: str = Form(...), file: UploadFile = File(...)):
#     # Obtener la extensión del archivo
#     file_extension = splitext(file.filename)[1]

#     # Directorio donde se guardarán las imágenes
#     upload_dir = Path(getcwd()) / "files" / "documents" / "sites" / site_name

#     # Crear la carpeta "users" si no existe
#     upload_dir.mkdir(parents=True, exist_ok=True)

#     # Combinar el nombre del archivo con el directorio
#     file_path = upload_dir / (site_name + " " + type_document + file_extension)

#     with open(file_path, "wb") as myflle:
#         content = await file.read()
#         myflle.write(content)

#     return "hecho"

# @router.get("/get-site-document/{site_name}/{type_document}")
# def get_site_document(site_name: str, type_document: str):
#     base_dir = getcwd() + "/files" + "/documents" + "/sites" + "/" + site_name + "/"

#     # Lista de extensiones de archivo a buscar en orden de preferencia
#     file_extensions = ['.pdf', '.jpg', '.jpeg', '.gif', '.bmp']

#     for extension in file_extensions:
#         file_path = base_dir + "/" + site_name + " " + type_document + extension
#         print (file_path)
#         file = Path(file_path)

#         if file.exists():


#             return FileResponse(file)
                   
    

#     print(base_dir)
#     # Si no se encuentra ninguna de las extensiones, puedes devolver un error o un archivo predeterminado
#     return "Archivo no encontrado", 404


# @router.get("/get-site-documents-info/{site_id}")
# def get_site_documents_info(site_id: str):
#     data = conn.read_all(site_id)
#     return data
                   

# @router.post("/insert/site-document")
# def insert(site_data:SiteDocumentSchemaPost):
#     data = site_data.dict()
    
#     print(data)
#     return conn.write(data)


# @router.put("/update/site-document/{document_id}")
# def update(site_data:SiteDocumentSchemaPost,document_id:str):
#     data = site_data.dict()
#     data['document_id'] = document_id

#     print(data)
#     return conn.update(data)





# @router.post('/upload-site-cover/')
# async def upload_user_photo(site_name: str = Form(...), file: UploadFile = File(...)):
#     # Obtener la extensión del archivo
#     file_extension = splitext(file.filename)[1]

#     # Directorio donde se guardarán las imágenes
#     upload_dir = Path(getcwd()) / "files" / "images" / "sites" / site_name

#     # Crear la carpeta "users" si no existe
#     upload_dir.mkdir(parents=True, exist_ok=True)

#     # Combinar el nombre del archivo con el directorio
#     file_path = upload_dir / ( "site cover"  + file_extension)

#     with open(file_path, "wb") as myflle:
#         content = await file.read()
#         myflle.write(content)




#     return "hecho"


# @router.get('/read-site-cover/{site_name}')
# def get_photo_profile(site_name: str):
#     base_dir = getcwd() + "/files" + "/images" + "/sites" + "/" + site_name + "/"

#     # Lista de extensiones de archivo a buscar en orden de preferencia
#     file_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']

#     for extension in file_extensions:
#         file_path = base_dir +  "site cover" + extension
#         print (file_path)
#         file = Path(file_path)

#         if file.exists():
#             return FileResponse(file)

#     print(base_dir)
#     # Si no se encuentra ninguna de las extensiones, puedes devolver un error o un archivo predeterminado
#     return "Archivo no encontrado", 404

