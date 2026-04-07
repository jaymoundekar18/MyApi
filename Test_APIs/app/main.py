from fastapi import FastAPI, HTTPException
from app.schemas import EmployeeCreate, EmployeeResponse, BankCustomerCreate, BankCustomerResponse
from app.schemas import UserResponse, ProductResponse, OrderResponse 
from app import curd

app = FastAPI(title="Multi API")

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the my API!",
            "guide": "You can get E-commerce data using endpoints /users , /products , and /orders . Or can perform CRUD operations on employee records using /employees endpoint."}

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


# -------------------------------------------------
# Customer CRUD Endpoints
# -------------------------------------------------

@app.post("/customers", response_model=BankCustomerResponse)
def create_customer(customer: BankCustomerCreate):
    return curd.add_customer(customer.dict())


@app.get("/customers", response_model=list[BankCustomerResponse])
def list_customers():
    return curd.get_all_customers()


@app.get("/customers/{id}", response_model=BankCustomerResponse)
def get_customer(id: str):
    customer = curd.get_customer_by_id(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@app.put("/customers/{id}", response_model=BankCustomerResponse)
def update_customer(id: str, customer: BankCustomerCreate):
    return curd.update_customer(id, customer.dict())


@app.delete("/customers/{id}")
def delete_customer(id: str):
    curd.delete_customer(id)
    return {"message": "Customer deleted successfully"}


@app.post("/login")
def login(user_id: str, password: str):
    customer = curd.authenticate_customer(user_id, password)
    if not customer:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return customer


@app.get("/transactions/{user_id}")
def get_transactions(user_id: str):
    return curd.get_transactions(user_id)


@app.post("/transactions/{user_id}")
def add_transaction(user_id: str, transaction: dict):
    return curd.add_transaction(user_id, transaction)


@app.post("/transfer")
def transfer(from_user_id: str, to_user_id: str, amount: float):
    result = curd.transfer_money(from_user_id, to_user_id, amount)
    if not result:
        raise HTTPException(status_code=400, detail="Transfer failed")
    return {"message": "Transfer successful"}