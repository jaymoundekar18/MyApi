from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
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




# -------------------------------------------------
# Bank schemas for request and response models
# -------------------------------------------------

class TransactionBase(BaseModel):
    transaction_id: str
    from_user_id: str
    to_user_id: str
    amount: float
    transaction_type: str   # send / receive
    status: str # success / failed / pending
    created_at: datetime


class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    pass


class BankCustomerBase(BaseModel):
    user_id: str
    name: str
    phone_number: str
    email: EmailStr
    account_number: str
    upi_id: str
    account_balance: float

class BankCustomerCreate(BankCustomerBase):
    password: str
    transactions: list[TransactionCreate]  = Field(default_factory=list)

class BankCustomerResponse(BankCustomerBase):
    id: str
    transactions: list[TransactionResponse]

class BankCustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    account_number: Optional[str] = None
    upi_id: Optional[str] = None
    account_balance: Optional[float] = None
    password: Optional[str] = None
    transactions: Optional[list[TransactionCreate]] = None