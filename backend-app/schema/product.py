from pydantic import BaseModel
from typing import Optional




class ProductSchemaPost(BaseModel):
    product_id: Optional[int] = None
    name: str
    price:int
    last_price:Optional[int] = None
    description:str
    category_id:int
    status: bool
    img_identifier:str
    parent_id: Optional[int] = None
    restaurant_id: Optional[int] = None
    has_recipe: Optional[bool] = False
    gramos: Optional[int] = None
    


class Product(BaseModel):
    id : Optional[int] = None
    name: str
    description: str
    category_id:  int
  

class Category( BaseModel ):
    id : Optional[ int ] = None
    name : str