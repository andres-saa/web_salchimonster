from fastapi import APIRouter,Depends
from models.employer import Employer
# Importa tu esquema de validación para employer, si existe
from schema.employer import EmployerSchemaPost
# from schema.employer import EmployerSchemaPost
from models.employer import Employer
from schema.employer import EmployerSchemaPost
from auth_utils.Security import Security,authenticate_user,create_access_token

employer_router = APIRouter()
security = Security()



@employer_router.get("/employers")
def get_employers():
    employer_instance = Employer()
    employers = employer_instance.select_all_employers()
    employer_instance.close_connection()
    return employers

@employer_router.get("/employer/dni/{dni}")
def get_employer_by_dni(dni: str):
    employer_instance = Employer()
    employer = employer_instance.select_employer_by_dni(dni)
    employer_instance.close_connection()
    
    if employer:
        return employer
    else:
        raise HTTPException(status_code=404, detail="Employer not found")



@employer_router.get("/employer/{employer_id}")
def get_employer_by_id(employer_id: int):
    employer_instance = Employer()
    employer = employer_instance.select_employer_by_id(employer_id)
    employer_instance.close_connection()
    return employer

@employer_router.post("/employer")
def create_employer(employer: EmployerSchemaPost):  # Asume que tienes un esquema EmployerSchemaPost
    employer_instance = Employer()
    employer_id = employer_instance.insert_employer(employer)
    employer_instance.close_connection()
    return {"employer_id": employer_id}

@employer_router.put("/employer/{employer_id}")
def update_employer(employer_id: int, updated_employer: EmployerSchemaPost):  # Asume que tienes un esquema EmployerSchemaPost
    employer_instance = Employer()
    updated_employer_data = employer_instance.update_employer(employer_id, updated_employer)
    
    if updated_employer_data:
        employer_instance.close_connection()
        return updated_employer_data
    else:
        employer_instance.close_connection()
        return {"message": "Employer not found"}

@employer_router.delete("/employer/{employer_id}")
def delete_employer(employer_id: int):
    employer_instance = Employer()
    result = employer_instance.delete_employer(employer_id)
    employer_instance.close_connection()
    return result  # Puedes personalizar el mensaje de respuesta
