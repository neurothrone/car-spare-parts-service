from app.controllers import BaseController
from app.data.models.employee import Employee
from app.data.repositories.employee_repository import EmployeeRepository


class EmployeeController(BaseController):
    model = Employee

    @classmethod
    def create(cls, first_name: str, last_name: str, phone: str, email: str) -> Employee:
        return EmployeeRepository.create(cls.model,
                                         first_name=first_name,
                                         last_name=last_name,
                                         phone=phone,
                                         email=email)

    @staticmethod
    def find_by_id(_id: int) -> Employee:
        return EmployeeRepository.find_by_id(_id)