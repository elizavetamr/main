from fastapi import APIRouter, HTTPException, status
from project.views.employees.crud import EmployeeStorage  # Исправленный импорт
from project.views.employees.schemas import Employee, EmployeeCreate  # Исправленный импорт

# Создаем экземпляр хранилища
storage = EmployeeStorage()

# Создаем роутер с префиксом /employees и тегом Employees
router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.get("/", response_model=list[Employee])
def get_employees():
    """
    Получение списка всех сотрудников.
    """
    return storage.get_all_employees()

@router.get("/{employee_id}", response_model=Employee, responses={
    status.HTTP_404_NOT_FOUND: {
        "description": "Сотрудник не найден",
        "content": {
            "application/json": {
                "example": {"detail": "Employee not found"}
            }
        }
    }
})
def get_employee(employee_id: int):
    """
    Получение информации о сотруднике по ID.
    """
    employee = storage.get_employee(employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return employee

@router.post("/", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee(employee_data: EmployeeCreate):
    """
    Создание нового сотрудника.
    """
    new_employee = storage.create_employee(employee_data)
    return new_employee

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int):
    """
    Удаление сотрудника по ID.
    """
    success = storage.delete_employee(employee_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
