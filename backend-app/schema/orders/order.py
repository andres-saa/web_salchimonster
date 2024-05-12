from pydantic import BaseModel, constr, conint, condecimal
from typing import Optional
from datetime import date


class Orders(BaseModel):
    id: Optional[str] = None  # assuming varchar is of max_length 255
    user_id: int
    site_id: int
    delivery_person_id: int

class DeliveryPersons(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    name: str
    phone_number: str

class OrderNotes(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    order_id: str
    notes: str

class OrderStatus(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    status: str
    order_id: str
    timestamp: date

class OrderStatusHistory(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    status: str
    order_id: str
    timestamp: date

class PaymentMethodOptions(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    name: str

class OrderDetails(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    order_id: str
    payment_method_option_id: int
    delivery_price: int

class OrderItems(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    order_id: str
    product_id: int
    quantity: int
    price: int


class AdditionalOrderTypes(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    name: str


class AdditionalItems(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    name: str
    type_id: int
    price: int


class OrderAdditionalItems(BaseModel):
    id: Optional[int] = None  # assuming varchar is of max_length 255
    name: str
    price: int
    additional_item_id: int
    order_item_id: int


class Cancellation_request (BaseModel):
    id: Optional[int] = None
    order_id:str
    responsible:str
    reason:str



