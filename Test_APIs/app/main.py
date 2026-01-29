from fastapi import FastAPI, HTTPException
from app.schemas import EmployeeCreate, EmployeeResponse
from app import curd

app = FastAPI(title="Employees API")

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Employees API!",
            "guide": "You can create, read, update, and delete employee records using the endpoints provided."}

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
