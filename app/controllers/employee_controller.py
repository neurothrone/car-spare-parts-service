from __future__ import annotations
from random import randint
from typing import Optional

from app.controllers import BaseController
from app.controllers.store_controller import StoreController
from app.data.models.store import Store
from app.data.models.employee import Employee
from app.data.repositories.employee_repository import EmployeeRepository
from shared.models.types import StoreType


class EmployeeController(BaseController):
    repository = EmployeeRepository
    required_attributes = {"first_name", "last_name", "phone", "email", "store_id"}

    @staticmethod
    def find_by_id(_id: int | str) -> Optional[Employee]:
        return EmployeeRepository.find_by_id(_id)

    @classmethod
    def create(cls, first_name: str, last_name: str, phone: str, email: str,
               store_id: Optional[int] = None) -> None:
        EmployeeRepository.create(first_name=first_name,
                                  last_name=last_name,
                                  phone=phone,
                                  email=email,
                                  store_id=store_id)

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

        if not employees or not stores:
            raise ValueError("There are either no employees or no stores to connect.")

        total_employees = len(employees)
        total_stores = len(stores)

        employees_connected = 0
        stores_with_employees = 0

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
                    employees_connected += 1
                    employee_index += 1
            except IndexError:
                break

            store_index += 1
            stores_with_employees += 1

        print(f"----- {employees_connected} Employees connected to {stores_with_employees} Stores -----")

    @classmethod
    def reset_all_employees_store(cls) -> None:
        employees: list[Employee] = cls.find_all()
        employees_count = 0

        for employee in employees:
            if employee.store_id:
                cls.change_store(employee, None)
                employees_count += 1

        print(f"----- {employees_count} Employees store has been reset -----")
