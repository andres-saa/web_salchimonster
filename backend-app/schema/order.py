from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal
from datetime import date
from schema.user import user_schema_post

class order_schema_post(BaseModel):
    order_products: List[dict]
    user_id: int
    site_id: int
    order_status: dict
    payment_method: str
    delivery_person_id: int
    status_history: List[dict]
    delivery_price: Decimal
    order_notes:str
    user_data: dict

class AdditionalItem(BaseModel):
    id: int
    name: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint
    type_id: int  # Assuming this should not be null
    price: Optional[Decimal] = None 
    

class AdditionalOrderType(BaseModel):
    id: int  # Not nullable as it's a primary key
    name: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint
    
    
class DeliveryPerson(BaseModel):
    id: int  # Not nullable as it's a primary key
    name: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint
    phone_number: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint

    
class OrderDetail(BaseModel):
    id: int  # Not nullable as it's a primary key
    order_id: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint
    payment_method_option_id: Optional[int] = None  # Assuming NULL is allowed
    delivery_price: Optional[Decimal] = None  # Using Decimal for numeric precision, assuming NULL is allowed




class OrderNote(BaseModel):
    id: int  # Not nullable as it's a primary key
    order_id: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint
    notes: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint





class OrderStatusHistory(BaseModel):
    id: int  # Not nullable as it's a primary key
    status: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint
    order_id: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint
    timestamp: Optional[date] = None  # Assuming NULL is allowed and using date type for the timestamp


class Order(BaseModel):
    id: str  # Not nullable as it's a primary key and a string type
    user_id: Optional[int] = None  # Assuming NULL is allowed as there's no NOT NULL constraint
    site_id: Optional[int] = None  # Assuming NULL is allowed
    delivery_person_id: Optional[int] = None  # Assuming NULL is allowed
    
    
class PaymentMethodOption(BaseModel):
    id: int  # Not nullable as it's a primary key
    name: Optional[str] = None  # Assuming NULL is allowed as there's no NOT NULL constraint




class AdditionalItem(BaseModel):
    id: int
    name: Optional[str] = None
    type_id: int
    price: Optional[Decimal] = None
    
    
class AdditionalItemMin(BaseModel):
    aditional_item_instance_id: int
    quantity:int

class minOrderItem(BaseModel):
    product_instance_id: int
    quantity: int

class OrderItem(minOrderItem):
    price: Decimal
    additional_items: Optional[List[AdditionalItem]] = None

class OrderStatus(BaseModel):
    status: str
    timestamp: date

class OrderSchemaPost(BaseModel):
    order_products: List[minOrderItem]
    order_aditionals:list[AdditionalItemMin]
    user_id: Optional[int] = None
    site_id: int
    pe_site_id:int
    order_status:Optional[OrderStatus] = None
    status_history: Optional[List[OrderStatus]] = None
    payment_method_id: int
    delivery_price: int
    order_notes: str
    user_data: user_schema_post
    inserted_by:Optional[int] = None
    pe_json:Optional[object] = {}
    total:int