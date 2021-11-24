from app.controllers import BaseController
from app.data.models.employee import Employee
from app.data.repositories.employee import EmployeeRepository


class EmployeeController(BaseController):
    model = Employee

    @staticmethod
    def find_by_id(_id: int) -> Employee:
        return EmployeeRepository.find_by_id(_id)
