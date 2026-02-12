from bson import ObjectId
from app.database import employee_collection
from app.database import users_collection, products_collection, orders_collection
from app.models import employee_helper, user_helper, product_helper, order_helper

# ---------------------------
# Employee CURD operations
# ---------------------------

# CREATE
def add_employee(employee: dict):
    result = employee_collection.insert_one(employee)
    new_employee = employee_collection.find_one(
        {"_id": result.inserted_id}
    )
    return employee_helper(new_employee)

# READ ALL
def get_all_employees():
    return [
        employee_helper(emp)
        for emp in employee_collection.find()
    ]

# READ ONE
def get_employee(id: str):
    employee = employee_collection.find_one({"_id": ObjectId(id)})
    if employee:
        return employee_helper(employee)
    return None

# UPDATE
def update_employee(id: str, data: dict):
    employee_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    employee = employee_collection.find_one({"_id": ObjectId(id)})
    return employee_helper(employee)

# DELETE
def delete_employee(id: str):
    employee_collection.delete_one({"_id": ObjectId(id)})
    return True


# ---------------------------
# E-commerce operations
# ---------------------------

# Get all users
def get_all_users():
    return [user_helper(user) for user in users_collection.find()]

# Get all products
def get_all_products():
    return [product_helper(product) for product in products_collection.find()]

# Get all orders
def get_all_orders():
    return [order_helper(order) for order in orders_collection.find()]
