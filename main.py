from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Employee Management API")

# Модель Employee
class Employee(BaseModel):
    id: int
    full_name: str
    email: str

# Пример данных (для простоты - кэш в памяти)
employee_db = [
    Employee(id=1, full_name="John Doe", email="john.doe@example.com"),
    Employee(id=2, full_name="Jane Smith", email="jane.smith@example.com"),
]

# Модель для POST-запросов (без id, так как id генерируется автоматически)
class EmployeeCreate(BaseModel):
    full_name: str
    email: str


@app.get("/api/employees", response_model=List[Employee], tags=["Employees"], summary="Get Employees")
def get_employees():
    """
    Возвращает список всех сотрудников.
    """
    return employee_db


@app.post("/api/employees", response_model=Employee, tags=["Employees"], summary="Create Employee")
def create_employee(employee: EmployeeCreate):
    """
    Создаёт нового сотрудника и возвращает его данные.
    """
    new_id = max([emp.id for emp in employee_db]) + 1 if employee_db else 1
    new_employee = Employee(id=new_id, full_name=employee.full_name, email=employee.email)
    employee_db.append(new_employee)
    return new_employee


@app.get("/api/employees/{employee_id}", response_model=Employee, tags=["Employees"], summary="Get Employee")
def get_employee(employee_id: int):
    """
    Возвращает информацию о сотруднике по его идентификатору.
    """
    for employee in employee_db:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/api/employees/{employee_id}", status_code=204, tags=["Employees"], summary="Delete Employee")
def delete_employee(employee_id: int):
    """
    Удаляет сотрудника по идентификатору.
    """
    global employee_db
    employee_db = [emp for emp in employee_db if emp.id != employee_id]
    return None
