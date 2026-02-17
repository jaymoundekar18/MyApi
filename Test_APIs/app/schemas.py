from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

# -------------------------------------------------
# Employee schemas for request and response models
# -------------------------------------------------

class EmployeeBase(BaseModel):
    firstname: str
    lastname: str
    gender: str
    email: EmailStr
    address: str
    phone: str
    empid: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: str


# -------------------------------------------------
# E-commerce schemas for request and response models
# -------------------------------------------------

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    country: str
    age: int
    signup_date: datetime

class ProductResponse(BaseModel):
    id: str
    name: str
    price: float
    category: str
    in_stock: int

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderResponse(BaseModel):
    id: str
    user_id: str
    items: list[OrderItem]
    total_amount: float
    order_date: datetime
    status: str
