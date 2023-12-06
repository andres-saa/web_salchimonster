from pydantic import BaseModel
from typing import Optional

# class Product_schema_post(BaseModel):
#     # id:Optional[int]
#     product_name:str
#     product_description:str
#     product_purchase_price:int
#     product_selling_price:int
#     unit_of_measure:str
#     provider_id:int
#     category_id:int

class ProductSchemaPost(BaseModel):
    name: str
    price: int
    description: str
    category_id: Optional[int] = None
    porcion: str
    state: Optional[str] = None


