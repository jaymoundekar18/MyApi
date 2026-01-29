from pydantic import BaseModel, EmailStr
from typing import Optional

class EmployeeBase(BaseModel):
    firstname: str
    lastname: str
    gender: str
    email: EmailStr
    address: str
    phone: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: str
