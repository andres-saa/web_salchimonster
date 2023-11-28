from fastapi import APIRouter
from models.site import Site
from schema.site import site_schema_post

site_router = APIRouter()

@site_router.get("/sites")
def get_sites():
    site_instance = Site()
    sites = site_instance.select_all_sites()
    site_instance.close_connection()
    return sites

@site_router.get("/site/{site_id}")
def get_site_by_id(site_id: int):
    site_instance = Site()
    site = site_instance.select_site_by_id(site_id)
    site_instance.close_connection()
    return site

@site_router.delete("/site/{site_id}")
def delete_site(site_id: int):
    site_instance = Site()
    result = site_instance.delete_site(site_id)
    site_instance.close_connection()
    return {"message": result}

@site_router.post("/site")
def create_site(site: site_schema_post):
    site_instance = Site()
    site_id = site_instance.insert_site(site)
    site_instance.close_connection()
    return {"site_id": site_id}

@site_router.put("/site/{site_id}")
def update_site(site_id: int, updated_site: site_schema_post):
    site_instance = Site()
    updated_site_data = site_instance.update_site(site_id, updated_site)

    if updated_site_data:
        site_instance.close_connection()
        return updated_site_data
    else:
        site_instance.close_connection()
        return {"message": "Site not found"}