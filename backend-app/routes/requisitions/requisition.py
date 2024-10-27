from fastapi import APIRouter, HTTPException
from models.requisitions.requisition import Requisitions
from schema.requisitions.requisition import Requisition,Vacancy,Applicant,cvFile
from pydantic import BaseModel, EmailStr


from fastapi import APIRouter, HTTPException, UploadFile, File, BackgroundTasks,Form
from pydantic import BaseModel
from pathlib import Path
import string
import random
from fastapi.responses import JSONResponse, FileResponse
from PIL import Image, ExifTags

requisition_router = APIRouter()




def generate_random_string(length=8):
    """Genera un string aleatorio para usar como identificador único."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

async def upload_image_utility(file: UploadFile = File(...)):
    upload_dir = Path.cwd() / "files" / "images" / "vacancies"
    upload_dir.mkdir(parents=True, exist_ok=True)

    random_value = generate_random_string()
    file_extension = Path(file.filename).suffix
    original_file_path = upload_dir / (f"vacancy_image_{random_value}{file_extension}")

    with open(original_file_path, "wb") as myfile:
        content = await file.read()
        myfile.write(content)

    # Procesamiento de la imagen: rotar y redimensionar
    process_image(original_file_path)

    return random_value

def process_image(file_path):
    """ Procesa la imagen para rotar y redimensionar según sea necesario """
    with Image.open(file_path) as img:
        img = rotate_image(img)
        img = resize_image(img)
        img.save(file_path)



def rotate_image(image):
    """ Rotar la imagen basado en los metadatos EXIF, si están disponibles """
    try:
        # Buscar el tag de orientación en los tags EXIF disponibles
        orientation_tag = None
        for tag, value in ExifTags.TAGS.items():
            if value == 'Orientation':
                orientation_tag = tag
                break

        # Proceder solo si encontramos el tag de orientación
        if orientation_tag and hasattr(image, '_getexif'):
            exif = image._getexif()  # Obtener los datos EXIF

            if exif is not None and orientation_tag in exif:
                # Verificar la orientación y rotar la imagen si es necesario
                orientation = exif[orientation_tag]
                if orientation == 3:
                    image = image.rotate(180, expand=True)
                elif orientation == 6:
                    image = image.rotate(270, expand=True)
                elif orientation == 8:
                    image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError, TypeError):
        # Manejar los errores comunes cuando no hay datos EXIF o no contienen 'Orientation'
        print("No EXIF orientation data found or error processing EXIF data.")
    
    return image
def resize_image(image, size=(600, 600)):
    """ Redimensiona la imagen a un tamaño especificado """
    image.thumbnail(size)
    return image






class Vacancy(BaseModel):
    requisition_id: int
    created_by: int
    title: str
    description: str
    image_identifier: str  # Este campo se completará con el resultado de la carga de la imagen

@requisition_router.post('/create-vacancy', tags=["vacancy"])
async def create_vacancy(
    requisition_id: int = Form(...),
    created_by: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks()
):
    # Usar la función de utilidad para cargar la imagen y obtener el identificador
    image_identifier = await upload_image_utility(file)

    # Crear la instancia de la vacante con los datos proporcionados, incluido el identificador de la imagen
    vacancy = Vacancy(
        requisition_id=requisition_id,
        created_by=created_by,
        title=title,
        description=description,
        image_identifier=image_identifier
    )

    # Insertar los datos de la vacante en la base de datos
    # Ejemplo: db.create_vacancy(vacancy.dict())
    # Suponiendo que la función de base de datos acepta un diccionario Pydantic

    return {"message": "Vacancy created successfully", "vacancy": vacancy.dict()}




@requisition_router.get('/get-all-requisitions',tags=["requisition"])
def get_all_requisition():
    requisition_instance = Requisitions()
    result = requisition_instance.get_all_requisitions()
    return result


@requisition_router.get('/get-requisition-areas',tags=["requisition"])
def get_all_requisition():
    requisition_instance = Requisitions()
    result = requisition_instance.get_areas()
    return result



class authorize_schema(BaseModel):
    requisition_id:int
    reponsible_id:int
  
  
  
@requisition_router.put('/authorize_requisition')
def authorize_requisition(data:authorize_schema):
    requisition_instance = Requisitions()
    result = requisition_instance.authorize_requisition(data.requisition_id,data.reponsible_id)
    return result
    
    
    
@requisition_router.put('/reject_requisition')
def reject_requisition(data:authorize_schema):
    requisition_instance = Requisitions()
    result = requisition_instance.reject_requisition(data.requisition_id,data.reponsible_id)
    return result


    
@requisition_router.put('/reject_requisition_by_hr')
def reject_requisition(data:authorize_schema):
    requisition_instance = Requisitions()
    result = requisition_instance.reject_requisition_by_hr(data.requisition_id,data.reponsible_id)
    return result
    
@requisition_router.get('/get-all-vacancies',tags=["requisition"])
def get_all_requisition():
    requisition_instance = Requisitions()
    result = requisition_instance.get_all_vacancies()
    return result


@requisition_router.post('/create-requisition',tags=["requisition"])
def get_all_requisition(requisition:Requisition):
    requisition_instance = Requisitions()
    result = requisition_instance.create_requisition(requisition)
    return result




@requisition_router.get("/vacancy-image/{image_identifier}", tags=["requisition"])
def get_vacancy_image(image_identifier: str):
    # Ruta base donde se almacenan las imágenes
    image_dir = Path.cwd() / "files" / "images" / "vacancies"
    
    # Buscar archivos que coincidan con el identificador, independientemente de la extensión
    files = list(image_dir.glob(f"vacancy_image_{image_identifier}.*"))

    # Verificar si se encontraron imágenes
    if not files:
        raise HTTPException(status_code=404, detail="Image not found")
    
    # Devolver la primera imagen que coincida si hay múltiples formatos
    return FileResponse(files[0])


@requisition_router.post("/apply", tags=["requisition"])
async def apply_for_vacancy(
    name: str = Form(...),
    email: EmailStr = Form(...),
    phone: str = Form(...),
    vacancy_id: int = Form(...),
    cv_file: UploadFile = File(...)
):
    # Guardar el archivo CV y obtener el identificador único
    cv_file_id = save_cv_file(cv_file)

    # Crear la instancia de Applicant con el identificador del archivo
    applicant = Applicant(
        name=name,
        email=email,
        phone=phone,
        cv_file_id=0,  # Usar el identificador generado
        vacancy_id=vacancy_id,
        lap_id=1  # Siempre empezamos en el lap_id 1 según tu modelo
    )

    # Insertar los datos del applicant en la base de datos
    requisition_instance = Requisitions()
    result = requisition_instance.create_applicant(data=applicant,cv_file=cvFile(url_file=cv_file_id))

    return result

def save_cv_file(cv_file: UploadFile):
    # Definir el directorio donde se guardarán los archivos CV
    file_dir = Path.cwd() / "files" / "cvs"
    file_dir.mkdir(parents=True, exist_ok=True)

    # Generar un identificador único para el archivo
    file_id = generate_random_string()
    file_name = file_id + Path(cv_file.filename).suffix  # El nombre del archivo incluye el identificador

    # Guardar el archivo en el sistema de archivos
    file_path = file_dir / file_name
    with open(file_path, "wb") as file_out:
        file_out.write(cv_file.file.read())

    return file_id  # Devolver el identificador del archivo, que será almacenado en la DB

@requisition_router.get("/cv/{cv_id}", tags=["requisition"], response_class=FileResponse)
def get_cv(cv_id: str):
    # Directorio donde se guardan los archivos CV
    cvs_dir = Path.cwd() / "files" / "cvs"
    
    # Buscar el archivo en el directorio basado en el identificador único
    file_path = next(cvs_dir.glob(f"{cv_id}.*"), None)

    # Verificar si se encontró el archivo
    if file_path is None:
        raise HTTPException(status_code=404, detail="CV not found")

    # Devolver el archivo como una respuesta de archivo
    return FileResponse(path=file_path, media_type='application/pdf', filename=file_path.name)



