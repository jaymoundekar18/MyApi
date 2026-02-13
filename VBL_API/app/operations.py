from bson import ObjectId
from app.database import vbl_collection
from app.models import vbluser_helper
from app.security import hash_password, verify_password

# Autenticate User Credentials
def authenticate_user(username: str, password: str):
    user = vbl_collection.find_one({"username": username})
    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    return vbluser_helper(user)

# ------- User Operations -------

# Create New User
def add_user(user: dict):
    user["password"] = hash_password(user["password"])
    result = vbl_collection.insert_one(user)
    new_user = vbl_collection.find_one(
        {"_id": result.inserted_id}
    )
    return vbluser_helper(new_user)

# Get all Users
def get_all_users():
    return [
        vbluser_helper(usr)
        for usr in vbl_collection.find()
    ]

# Get User by ID
def get_user_byID(id: str):
    user = vbl_collection.find_one({"_id": ObjectId(id)})
    if user:
        return vbluser_helper(user)
    return None

# Get User by Username
def get_by_username(uname: str):
    user = vbl_collection.find_one({"username": uname})
    if user:
        return vbluser_helper(user)
    return None
    
# Update User by ID
def update_user(id: str, data: dict):
    if "password" in data:
        data["password"] = hash_password(data["password"])
    vbl_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    user = vbl_collection.find_one({"_id": ObjectId(id)})
    return vbluser_helper(user)


# Delete User by ID
def delete_user(id: str):
    vbl_collection.delete_one({"_id": ObjectId(id)})
    return True

# ------- End of User Operations -------


# ------- Book Operations -------

# Add Book to User's Collection
def add_book_to_user(user_id: str, book: dict):
    vbl_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$push": {"books": book}}
    )
    user = vbl_collection.find_one({"_id": ObjectId(user_id)})
    return vbluser_helper(user)

# Get User's Book Collection
def get_user_books(user_id: str):
    user = vbl_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user.get("books", [])
    return []

# Get User's Book Names
def get_user_booknames(user_id: str):
    user = vbl_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return [book["book_name"] for book in user.get("books", [])]
    return []

# Get Specific Book from User's Collection
def get_user_book(user_id: str, book_index: int):
    user = vbl_collection.find_one({"_id": ObjectId(user_id)})
    if user and 0 <= book_index < len(user.get("books", [])):
        return user["books"][book_index]
    return None

# Update Specific Book in User's Collection
def update_user_book(user_id: str, book_index: int, data: dict):
    user = vbl_collection.find_one({"_id": ObjectId(user_id)})
    if not user or book_index >= len(user.get("books", [])):
        return None

    # Update the book
    user["books"][book_index].update(data)
    vbl_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"books": user["books"]}}
    )
    user = vbl_collection.find_one({"_id": ObjectId(user_id)})
    return vbluser_helper(user)

# Delete Specific Book from User's Collection
def delete_user_book(user_id: str, book_index: int):
    user = vbl_collection.find_one({"_id": ObjectId(user_id)})
    if not user or book_index >= len(user.get("books", [])):
        return None

    user["books"].pop(book_index)
    vbl_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"books": user["books"]}}
    )
    return vbluser_helper(user)
