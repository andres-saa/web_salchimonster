from fastapi import APIRouter,Depends
from models.employer import Employer
# Importa tu esquema de validación para employer, si existe
from schema.employer.employer import EmployerSchemaPost
# from schema.employer import EmployerSchemaPost
from models.employer import Employer
from schema.employer.employer import EmployerSchemaPost
from auth_utils.Security import Security,authenticate_user,create_access_token
from fastapi import HTTPException

employer_router = APIRouter()
security = Security()



@employer_router.get("/employers")
def get_employers():
    employer_instance = Employer()
    employers = employer_instance.select_all_employers()
    return employers

@employer_router.get("/employers-basic")
def get_employers():
    employer_instance = Employer()
    employers = employer_instance.select_employers_basic()
    employer_instance.close_connection()
    return employers

@employer_router.get("/employer-basic/{employer_id}")
def get_employer_basic_by_id(employer_id: int):
    employer_instance = Employer()
    employer = employer_instance.select_employer_basic_by_id(employer_id)
    employer_instance.close_connection()
    if employer:
        return employer
    else:
        raise HTTPException(status_code=404, detail="Employer not found")


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

@employer_router.get("/employer/position/{position}")
def get_employer_by_position(position: str):
    employer_instance = Employer()
    employers = employer_instance.select_employer_by_position(position)
    employer_instance.close_connection()
    if employers:
        return employers
    else:
        raise HTTPException(status_code=404, detail="No employers found for this position")
        
@employer_router.get("/employer/site/{site_id}")
def get_employers_by_site_id(site_id: int):
    employer_instance = Employer()
    employers = employer_instance.select_employers_by_site_id(site_id)
    employer_instance.close_connection()

    if employers:
        return employers
    else:
        raise HTTPException(status_code=404, detail="No employers found for this site ID")


@employer_router.get("/employers/grouped-by-position")
def get_employers_grouped_by_position():
    employer_instance = Employer()
    try:
        grouped_employers = employer_instance.select_employers_grouped_by_position()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        employer_instance.close_connection()

    if grouped_employers:
        return grouped_employers
    else:
        raise HTTPException(status_code=404, detail="No employers found grouped by position")



@employer_router.get("/employers/grouped-by-site")
def get_employers_grouped_by_site():
    employer_instance = Employer()
    try:
        grouped_employers = employer_instance.select_employers_grouped_by_site()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        employer_instance.close_connection()

    if grouped_employers:
        return grouped_employers
    else:
        raise HTTPException(status_code=404, detail="No employers found grouped by site")

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
