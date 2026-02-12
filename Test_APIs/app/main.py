from fastapi import FastAPI, HTTPException
from app.schemas import EmployeeCreate, EmployeeResponse
from app.schemas import UserResponse, ProductResponse, OrderResponse 
from app import curd

app = FastAPI(title="Employees API")

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the my API!",
            "guide": "You can get E-commerce data using endpoints /users, /products, and /orders. Or can perform CRUD operations on employee records using /employee endpoint."}

# -----------------------
# Employee CRUD endpoints 
# -----------------------

@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate):
    return curd.add_employee(employee.dict())

@app.get("/employees", response_model=list[EmployeeResponse])
def list_employees():
    return curd.get_all_employees()

@app.get("/employees/{id}", response_model=EmployeeResponse)
def get_employee(id: str):
    employee = curd.get_employee(id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{id}", response_model=EmployeeResponse)
def update_employee(id: str, employee: EmployeeCreate):
    return curd.update_employee(id, employee.dict())

@app.delete("/employees/{id}")
def remove_employee(id: str):
    curd.delete_employee(id)
    return {"message": "Employee deleted successfully"}


# ----------------------------------------------------
# E-commerce endpoints for users, products, and orders
# ----------------------------------------------------

@app.get("/users", response_model=list[UserResponse])
def list_users():
    return curd.get_all_users()

@app.get("/products", response_model=list[ProductResponse])
def list_products():
    return curd.get_all_products()

@app.get("/orders", response_model=list[OrderResponse])
def list_orders():
    return curd.get_all_orders()
