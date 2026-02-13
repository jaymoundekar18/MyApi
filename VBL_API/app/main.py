from fastapi import FastAPI, HTTPException
from app.schemas import VblUserCreate, VblUserResponse, VblUserUpdate
from app import operations
from app.schemas import LoginRequest, LoginResponse
from app.schemas import VblBookBase

app = FastAPI(title="VBL API")

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the VBL API!",
            "guide": "You can create, read, update, and delete users records using the endpoints provided."}

# Authenticate User Credentials
@app.post("/login", response_model=LoginResponse)
def login_user(credentials: LoginRequest):
    user = operations.authenticate_user(
        credentials.username,
        credentials.password
    )
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    return user

# ------- User Endpoints -------
@app.post("/users", response_model=VblUserResponse)
def create_user(user: VblUserCreate):
    return operations.add_user(user.dict())

@app.get("/users", response_model=list[VblUserResponse])
def list_users():
    return operations.get_all_users()

@app.get("/users/id{id}", response_model=VblUserResponse)
def get_user(id: str):
    user = operations.get_user_byID(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/username{username}", response_model=VblUserResponse)
def get_user(username: str):
    user = operations.get_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# @app.put("/users/{id}", response_model=VblUserResponse)
# def update_user(id: str, user: VblUserCreate):
#     updated_user = operations.update_user(id, user.dict())
#     if not updated_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return updated_user

@app.patch("/users/{id}", response_model=VblUserResponse)
def update_user(id: str, user: VblUserUpdate):
    updated_user = operations.update_user(
        id,
        user.dict(exclude_unset=True)
    )
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{id}")
def remove_user(id: str):
    operations.delete_user(id)
    return {"message": "User deleted successfully"}

# ------- End of User Endpoints -------


# ------- Book Endpoints -------

@app.post("/users/{user_id}/books", response_model=VblUserResponse)
def add_book(user_id: str, book: VblBookBase):
    return operations.add_book_to_user(user_id, book.dict())

@app.get("/users/{user_id}/books", response_model=list[VblBookBase])
def list_user_books(user_id: str):
    return operations.get_user_books(user_id)

@app.get("/users/{user_id}/booknames", response_model=list[str])
def list_user_booknames(user_id: str):
    return operations.get_user_booknames(user_id)

@app.get("/users/{user_id}/books/{book_index}", response_model=VblBookBase)
def get_book(user_id: str, book_index: int):
    book = operations.get_user_book(user_id, book_index)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/users/{user_id}/books/{book_index}", response_model=VblUserResponse)
def update_book(user_id: str, book_index: int, book: VblBookBase):
    updated_user = operations.update_user_book(user_id, book_index, book.dict())
    if not updated_user:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_user

@app.delete("/users/{user_id}/books/{book_index}", response_model=VblUserResponse)
def delete_book(user_id: str, book_index: int):
    updated_user = operations.delete_user_book(user_id, book_index)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_user
