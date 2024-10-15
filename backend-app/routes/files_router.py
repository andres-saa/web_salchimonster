from fastapi import APIRouter, UploadFile,FastAPI, File,Form,BackgroundTasks,HTTPException
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
from models.contest.contest import Contest
# conn = siteDocumentConnection()
from fastapi.middleware.cors import CORSMiddleware
import time
from PIL import Image
from io import BytesIO
from datetime import datetime,timedelta
import pytz
import random
import string



def get_image_creation_date(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                date_taken_tag = 36867  # Tag EXIF para la fecha y hora original
                if date_taken_tag in exif_data:
                    date_taken = exif_data[date_taken_tag]
                    datetime_taken = datetime.strptime(date_taken, '%Y:%m:%d %H:%M:%S')
                    bogota_timezone = pytz.timezone('America/Bogota')
                    localized_datetime = bogota_timezone.localize(datetime_taken)
                    return localized_datetime
            return None
    except Exception as e:
        print(f"Error al leer los metadatos EXIF: {e}")
        return None
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




# resize_image, file_path, upload_dir, evidence_id,contest_id,user_id, file_extension

def resize_contest_image(path: str, upload_dir: str, evidence_id: str,contest_id:str,user_id:str, file_extension: str):
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
            "contest_"+contest_id+"_user_"+user_id+"_evidence_"+evidence_id+"_"+ str(size["width"]) + 'x' + str(size["height"]) + file_extension)
        image.save(resized_file_path)

@router.get("/")
def root():
    return "hola"


@router.post('/upload-product-image/{product_id}')
async def upload_user_photo(product_id: str, file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks):
    # Directorio donde se guardarán las imágenes
    upload_dir = Path.cwd() / "files" / "images" / "products" / product_id

    
    

    # Eliminar la carpeta y archivos existentes
    if upload_dir.is_dir():
        for existing_file in upload_dir.glob("*"):
            remove(existing_file)

    # Crear la carpeta "products"
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Obtener el nombre del archivo
    file_extension = splitext(file.filename)[1]

    # Combinar el nombre del archivo con el directorio
    file_path = upload_dir / ("product image " + product_id + file_extension)

    with open(file_path, "wb") as myflle:
        content = await file.read()
        myflle.write(content)
    
    
    rotate_image(file_path)

    background_tasks.add_task(resize_image, file_path, upload_dir, product_id, file_extension)
 
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
        return FileResponse(files[0])
        

    # Si no se encuentra ningún archivo, devolver un error
    return "Archivo no encontrado", 404


@router.get('/read-contest-image/{height}/{user_id}/{contest_id}/{evidence_id}')
def get_photo_profile( height: str,user_id:str, evidence_id: str,contest_id:str,):
    timestamp = int(time.time())  # Obtener el timestamp actual

    base_dir = Path(getcwd()) / "files" / "images" /"contests"/ f"contest_{contest_id}" / f"user_{user_id}"
    pattern = f"{base_dir}/contest_{contest_id}_" + f"user_{user_id}_" + f"evidence_{evidence_id}_{height}x{height}.*"
    # pattern = f"contest_{contest_id}_" + f"user_{user_id}_" + f"evidence_{evidence_id}" + file_extension

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




@router.post('/upload-constest-image/{user_id}/{contest_id}/{evidence_id}')
async def upload_user_photo(user_id: str, evidence_id: str, contest_id: str, file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    # Directorio donde se guardarán las imágenes
    upload_dir = Path.cwd() / "files" / "images" / "contests" / f"contest_{contest_id}" / f"user_{user_id}"
    contest_instance = Contest()
    # Crear la carpeta si no existe
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Obtener la extensión del archivo
    file_extension = splitext(file.filename)[1]

    # Combinar el nombre del archivo con el directorio
    file_path = upload_dir / (f"contest_{contest_id}_" + f"user_{user_id}_" + f"evidence_{evidence_id}" + file_extension)

    with open(file_path, "wb") as myfile:
        content = await file.read()
        myfile.write(content)

    # Obtener y mostrar la fecha de creación de la imagen
    image_creation_date = get_image_creation_date(file_path)
    bogota_now = datetime.now(pytz.timezone('America/Bogota'))

    if image_creation_date is None or bogota_now - image_creation_date > timedelta(minutes=5):
        contest_instance.deleteEvidenceByImageError(evidence_id)
        raise HTTPException(status_code=400, detail="La foto fue tomada hace más de 5 minutos.")


    rotate_image(file_path)

    background_tasks.add_task(resize_contest_image, file_path, upload_dir, evidence_id, contest_id, user_id, file_extension)

  
    contest_instance.updateEntryImageUrl(evidence_id, f"/read-contest-image/300/{user_id}/{contest_id}/{evidence_id}")
    contest_instance.close_connection()

    return JSONResponse(content={"message": "hecho"}, status_code=200)


def generate_random_string(length=8):
    """Genera un string aleatorio para usar como identificador único."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))




@router.get('/read-photo-product/{image_identifier}')
def get_photo_product(image_identifier: str):
    base_dir = Path(getcwd()) / "files" / "images" / "products"
    pattern = f"{base_dir}/product_image_{image_identifier}.*"

    # Buscar archivos que coincidan con el patrón
    files = glob(pattern)

    if files:
        # Si se encuentran archivos, devolver el primero
        return FileResponse(files[0])

    return "Archivo no encontrado", 404


def resize_image_for_all_resolutions(path: str, upload_dir: Path, random_value: str, file_extension: str):
    sizes = [96, 300, 600]  # Resoluciones de ejemplo
    for size in sizes:
        image = Image.open(path, mode='r')
        image.thumbnail((size, size))
        size_dir = upload_dir / str(size)  # Carpeta para cada resolución
        size_dir.mkdir(parents=True, exist_ok=True)
        resized_file_path = size_dir / (f"product_image_{random_value}_{size}{file_extension}")
        image.save(resized_file_path)

@router.post('/upload-photo-product')
async def upload_photo_product(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    # Directorio base donde se guardarán las imágenes
    upload_dir = Path.cwd() / "files" / "images" / "products"
    
    # Crear la carpeta base si no existe
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Generar un valor aleatorio para la imagen
    random_value = generate_random_string()

    # Obtener la extensión del archivo
    file_extension = splitext(file.filename)[1]

    # Combinar el nombre del archivo con el valor aleatorio
    original_file_path = upload_dir / (f"product_image_{random_value}{file_extension}")

    # Guardar el archivo original
    with open(original_file_path, "wb") as myfile:
        content = await file.read()
        myfile.write(content)

    # Rotar la imagen si es necesario
    rotate_image(original_file_path)

    # Redimensionar la imagen en segundo plano (para diferentes resoluciones)
    background_tasks.add_task(resize_image_for_all_resolutions, original_file_path, upload_dir, random_value, file_extension)

    # Guardar el identificador de la imagen en la base de datos si es necesario
    # Ejemplo: db.save_image_url(random_value)

    return JSONResponse(content={"message": "hecho", "image_identifier": random_value}, status_code=200)


@router.get('/read-photo-product/{image_identifier}/{width}')
def get_photo_product(image_identifier: str, width: int):
    # Directorio base de las imágenes
    base_dir = Path(getcwd()) / "files" / "images" / "products" / str(width)
    
    # Patrón para encontrar la imagen con el identificador y el ancho solicitado
    pattern = f"{base_dir}/product_image_{image_identifier}_{width}.*"

    # Buscar archivos que coincidan con el patrón
    files = glob(pattern)

    if files:
        # Si se encuentran archivos, devolver el primero
        return FileResponse(files[0])

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

