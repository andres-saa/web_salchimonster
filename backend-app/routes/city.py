from fastapi import APIRouter
from models.city import City  # Asegúrate de que el módulo y la clase sean accesibles
from schema.city import citySchema  # Asegúrate de que el esquema Pydantic sea accesible

city_router = APIRouter()

@city_router.get("/cities")
def get_cities():
    city_instance = City()
    cities = city_instance.select_all_cities()
    city_instance.close_connection()
    return cities

@city_router.get("/city/{city_id}")
def get_city_by_id(city_id: int):
    city_instance = City()
    city = city_instance.select_city_by_id(city_id)
    city_instance.close_connection()
    return city

@city_router.post("/city")
def create_city(city: citySchema):
    city_instance = City()
    city_id = city_instance.insert_city(city)
    city_instance.close_connection()
    return {"city_id": city_id}

@city_router.delete("/city/{city_id}")
def delete_city(city_id: int):
    city_instance = City()
    result = city_instance.delete_city(city_id)
    city_instance.close_connection()
    return {"message": result}

@city_router.put("/city/{city_id}", response_model=citySchema)
def update_city(city_id: int, updated_city: citySchema):
    city_instance = City()
    updated_city_data = city_instance.update_city(city_id, updated_city)
    city_instance.close_connection()
    
    if updated_city_data:
        return updated_city_data
    else:
        return {"message": "City not found"}
