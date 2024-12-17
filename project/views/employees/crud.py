from dataclasses import dataclass, field
from typing import Dict, List, Optional
from project.views.employees.schemas import Employee, EmployeeCreate  # Исправленный импорт

@dataclass
class EmployeeStorage:
    # Поле для хранения последнего выданного идентификатора
    last_id: int = 0

    # Словарь для хранения сотрудников: {id: Employee}
    employees: Dict[int, Employee] = field(default_factory=dict)

    @property
    def next_id(self) -> int:
        """Генерирует новый уникальный идентификатор для сотрудника."""
        self.last_id += 1
        return self.last_id

    def create_employee(self, employee_data: EmployeeCreate) -> Employee:
        """
        Создает нового сотрудника, присваивает ему уникальный ID
        и сохраняет в словаре.
        """
        new_id = self.next_id
        new_employee = Employee(id=new_id, **employee_data.dict())
        self.employees[new_id] = new_employee
        return new_employee

    def get_all_employees(self) -> List[Employee]:
        """
        Возвращает список всех сотрудников.
        """
        return list(self.employees.values())

    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """
        Возвращает сотрудника по ID или None, если сотрудник не найден.
        """
        return self.employees.get(employee_id)

    def delete_employee(self, employee_id: int) -> bool:
        """
        Удаляет сотрудника по ID. Возвращает True, если сотрудник удален,
        или False, если сотрудник с таким ID не найден.
        """
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False

