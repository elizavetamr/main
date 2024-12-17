from fastapi import APIRouter
from project.views.employees.api import router as employees_router  # Импортируем employees_router

# Создаем основной роутер
router = APIRouter()

# Подключаем employees_router
router.include_router(employees_router, prefix="/employees")


