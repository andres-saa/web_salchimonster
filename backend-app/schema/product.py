from pydantic import BaseModel
from typing import Optional




class ProductSchemaPost(BaseModel):
    product_id: int
    name: str
    price:int
    description:str
    category_id:int
    status: bool
    img_identifier:str
    parent_id:int
    


class Product(BaseModel):
    id : Optional[int] = None
    name: str
    description: str
    category_id:  int
  

class Category( BaseModel ):
    id : Optional[ int ] = None
    name : str