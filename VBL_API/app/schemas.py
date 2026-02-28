from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class VblBookBase(BaseModel):
    book_name: str
    book_author: str
    genre: str
    reading_time: str
    book_pages: int
    book_review: Optional[str] = ""
    rating: float
    book_status: Optional[str] = ""
    start_date: Optional[str] = ""
    end_date: Optional[str] = ""

class YearGoal(BaseModel):
    year: str
    goal: int
    completed: int

class Streak(BaseModel):
    current_streak: int = 0
    longest_streak: int = 0
    last_read_date: Optional[str] = None  

class VblUserBase(BaseModel):
    fullname: str
    email: EmailStr
    username: str
    books: list[VblBookBase] = Field(default_factory=list)
    yearly_goal: list[YearGoal] = Field(default_factory=list)
    streak: Optional[Streak] = None

class VblUserCreate(VblUserBase):
    password: str

class VblUserResponse(VblUserBase):
    id: str

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    id: str
    fullname: str
    email: EmailStr
    username: str

class VblUserUpdate(BaseModel):
    fullname: Optional[str] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    books: Optional[list[VblBookBase]] = None
    yearly_goal: Optional[list[YearGoal]] = None
    streak: Optional[Streak] = None

