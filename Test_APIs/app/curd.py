from bson import ObjectId
from app.database import employee_collection
from app.models import employee_helper

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
