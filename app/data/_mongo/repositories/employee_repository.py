from typing import Optional

from app.data._mongo.models.employee import Employee
from app.data._mongo.models.store import Store
from app.data._mongo.repositories import BaseRepository


class EmployeeRepository(BaseRepository):
    model = Employee

    @classmethod
    def change_store(cls, employee: Employee, store: Optional[Store]) -> None:
        if not store:
            employee.store_id = None
        else:
            if not store._id:
                raise ValueError("Store ID can not be None.")

            if employee.store_id == store._id:
                raise ValueError("Employee is already working there.")

            employee.store_id = store._id

        employee.save()
