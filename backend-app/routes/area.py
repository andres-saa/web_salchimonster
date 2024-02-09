# from fastapi import APIRouter
# from models.area import Area
# from schema.area import AreaSchemaPost, AreaSchemaGet

# area_router = APIRouter()

# @area_router.get("/areas")
# def get_areas():
#     area_instance = Area()
#     areas = area_instance.select_all_areas()
#     area_instance.close_connection()
#     return areas

# @area_router.get("/area/{area_id}")
# def get_area_by_id(area_id: int):
#     area_instance = Area()
#     area = area_instance.select_area_by_id(area_id)
#     area_instance.close_connection()
#     return area

# @area_router.delete("/area/{area_id}")
# def delete_area(area_id: int):
#     area_instance = Area()
#     result = area_instance.delete_area(area_id)
#     area_instance.close_connection()
#     return {"message": result}

# @area_router.post("/area")
# def create_area(area: AreaSchemaPost):
#     area_instance = Area()
#     area_id = area_instance.insert_area(area)
#     area_instance.close_connection()
#     return {"area_id": area_id}

# @area_router.put("/area/{area_id}")
# def update_area(area_id: int, updated_area: AreaSchemaPost):
#     area_instance = Area()
#     updated_area_data = area_instance.update_area(area_id, updated_area)
#     area_instance.close_connection()
#     return updated_area_data if updated_area_data else {"message": "Area not found"}

# @area_router.get("/areas/site/{site_id}")
# def get_areas_by_site_id(site_id: int):
#     area_instance = Area()
#     areas = area_instance.select_areas_by_site_id(site_id)
#     area_instance.close_connection()
#     return areas

# @area_router.get("/areas/city/{city_id}")
# def get_areas_by_city(city_id: int):
#     area_instance = Area()
#     areas = area_instance.select_areas_by_city_id(city_id)
#     area_instance.close_connection()
#     return areas