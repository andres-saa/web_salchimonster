from fastapi import APIRouter, HTTPException
from models.neighborhood import Neighborhood  # Asegúrate de que el módulo y la clase sean accesibles
from schema.neighborhood import NeighborhoodSchema  # Asegúrate de que el esquema Pydantic sea accesible

neighborhood_router = APIRouter()

@neighborhood_router.get("/neighborhoods")
def get_neighborhoods():
    neighborhood_instance = Neighborhood()
    neighborhoods = neighborhood_instance.select_all_neighborhoods()
    neighborhood_instance.close_connection()
    return neighborhoods

@neighborhood_router.get("/neighborhood/{neighborhood_id}")
def get_neighborhood_by_id(neighborhood_id: int):
    neighborhood_instance = Neighborhood()
    neighborhood = neighborhood_instance.select_neighborhood_by_id(neighborhood_id)
    neighborhood_instance.close_connection()
    if neighborhood is None:
        raise HTTPException(status_code=404, detail="Neighborhood not found")
    return neighborhood

@neighborhood_router.post("/neighborhood", response_model=NeighborhoodSchema)
def create_neighborhood(neighborhood: NeighborhoodSchema):
    neighborhood_instance = Neighborhood()
    neighborhood_id = neighborhood_instance.insert_neighborhood(neighborhood)
    neighborhood_instance.close_connection()
    return {**neighborhood.dict(), "neighborhood_id": neighborhood_id}

@neighborhood_router.delete("/neighborhood/{neighborhood_id}")
def delete_neighborhood(neighborhood_id: int):
    neighborhood_instance = Neighborhood()
    message = neighborhood_instance.delete_neighborhood(neighborhood_id)
    neighborhood_instance.close_connection()
    return {"message": message}

@neighborhood_router.put("/neighborhood/{neighborhood_id}", response_model=NeighborhoodSchema)
def update_neighborhood(neighborhood_id: int, updated_neighborhood: NeighborhoodSchema):
    neighborhood_instance = Neighborhood()
    updated_neighborhood_data = neighborhood_instance.update_neighborhood(neighborhood_id, updated_neighborhood)
    neighborhood_instance.close_connection()
    if updated_neighborhood_data is None:
        raise HTTPException(status_code=404, detail="Neighborhood not found")
    return updated_neighborhood_data

@neighborhood_router.get("/neighborhoods/by-city/{city_id}")
def get_neighborhoods_by_city_id(city_id: int):
    neighborhood_instance = Neighborhood()
    neighborhoods = neighborhood_instance.select_neighborhoods_by_city_id(city_id)
    neighborhood_instance.close_connection()

    if not neighborhoods:
        raise HTTPException(status_code=404, detail="No neighborhoods found for the given city_id")
    return neighborhoods


@neighborhood_router.get("/neighborhoods/by-site/{site_id}")
def get_neighborhoods_by_site_id(site_id: int):
    neighborhood_instance = Neighborhood()
    neighborhoods = neighborhood_instance.select_neighborhoods_by_site_id(site_id)
    neighborhood_instance.close_connection()

    if not neighborhoods:
        raise HTTPException(status_code=404, detail="No neighborhoods found for the given site_id")
    return neighborhoods
