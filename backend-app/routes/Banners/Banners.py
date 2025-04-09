from fastapi import FastAPI, HTTPException, Depends ,APIRouter
from models.Banners.Banners import Banners 
from pydantic import BaseModel
from typing import List,Optional

banner_router = APIRouter()


class BannerAppSchema(BaseModel):
    index: int
    img_identifier: str

class BannerAppSchema2(BaseModel):
    id:int
    index: int
    img_identifier: str

class BannerReorderSchema(BaseModel):
    banners: List[BannerAppSchema]


class aditional_type_schema(BaseModel):
    name:str
    max_selected:int
    
class aditional_schema(BaseModel):
    name:str
    type_id:int
    price:int
    
class aditional_schema_edit(BaseModel):
    name:str
    price:int

class FlavorAssociationSchema(BaseModel):
    product_id: int 
    flavor_ids: List[int] 
    
class FlavorEditSchema(BaseModel):
    name: str

class FlavorDeleteSchema(BaseModel):
    soft_delete: bool
additions = Banners()




@banner_router.post("/banners/reorder")
def reorder_banners(banners: List[BannerAppSchema2]):
    if not banners:
        raise HTTPException(status_code=400, detail="No banners provided for reordering.")
    
    result = additions.reorder_banners(banners)
    
    if result.get("status") == "success":
        return result
    else:
        raise HTTPException(status_code=500, detail=result.get("message"))
    


@banner_router.post("/banners/")
def create_banner(banner: BannerAppSchema):
    result = additions.create_banner(banner)
    return result

@banner_router.get("/banners/")
def read_banners():
    banners = additions.get_banners()
    return banners

@banner_router.get("/banners/{banner_id}", response_model=BannerAppSchema)
def read_banner(banner_id: int):
    banner = additions.get_banner_by_id(banner_id)
    if banner:
        return BannerAppSchema(**banner)
    else:
        raise HTTPException(status_code=404, detail="Banner not found")

@banner_router.put("/banners/{banner_id}", response_model=BannerAppSchema)
def update_banner(banner_id: int, banner: BannerAppSchema):
    result = additions.update_banner(banner_id, banner)
    if result:
        return BannerAppSchema(id=result[0]['id'], **banner.dict())
    else:
        raise HTTPException(status_code=404, detail="Banner not found")

@banner_router.delete("/banners/{banner_id}", response_model=dict)
def delete_banner(banner_id: int):
    result = additions.delete_banner(banner_id)
    if result:
        return {"status": "success", "message": "Banner deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Banner not found")
