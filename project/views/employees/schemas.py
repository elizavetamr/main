from pydantic import BaseModel, EmailStr, ConfigDict

# Базовая схема
class EmployeeBase(BaseModel):
    full_name: str
    email: EmailStr

# Схема для создания объекта
class EmployeeCreate(EmployeeBase):
    pass

# Схема для чтения/отображения объекта
class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True  # Для совместимости с объектами ORM (если в будущем понадобится база данных)


class MySchema(BaseModel):
    # Ваши поля схемы
    model_config = ConfigDict(from_attributes=True)
