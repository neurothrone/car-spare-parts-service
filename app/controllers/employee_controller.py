from random import randint
from typing import Optional

from app.controllers import BaseController
from app.controllers.store_controller import StoreController
from app.data.models.store import Store, StoreType
from app.data.models.employee import Employee
from app.data.repositories.employee_repository import EmployeeRepository


class EmployeeController(BaseController):
    model = Employee

    @classmethod
    def create(cls, first_name: str, last_name: str, phone: str, email: str,
               store_id: Optional[int] = None) -> None:
        EmployeeRepository.create(cls.model,
                                  first_name=first_name,
                                  last_name=last_name,
                                  phone=phone,
                                  email=email,
                                  store_id=store_id)

    @staticmethod
    def find_by_id(_id: int) -> Employee:
        return EmployeeRepository.find_by_id(_id)

    @staticmethod
    def change_store(employee: Employee, store_id: Optional[int]) -> None:
        if store_id is not None:
            if store_id < 1:
                raise ValueError("Invalid value for store_id. Can not be zero or negative.")

            store = StoreController.find_by_id(store_id)

            if store.store_type == StoreType.ONLINE:
                raise ValueError("Employee can't work at online store.")

            if employee.store_id == store_id:
                raise ValueError("Employee is already working there.")

        EmployeeRepository.change_store(employee, store_id)

    @classmethod
    def connect_employees_to_stores(cls, min_: int, max_: int) -> None:
        employees: list[Employee] = cls.find_all()
        stores: list[Store] = StoreController.find_all()
        total_employees = len(employees)
        total_stores = len(stores)

        employee_index = 0
        store_index = 0

        while employee_index < total_employees and store_index < total_stores:
            employees_in_store = randint(min_, max_)

            try:
                for _ in range(employees_in_store):
                    if stores[store_index].store_type == StoreType.ONLINE:
                        continue

                    cls.change_store(
                        employee=employees[employee_index],
                        store_id=stores[store_index].store_id)
                    employee_index += 1
            except IndexError:
                break

            store_index += 1

    @classmethod
    def reset_all_employees_store(cls):
        employees: list[Employee] = cls.find_all()

        for employee in employees:
            cls.change_store(employee, None)
