from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.employee import Employee
from app.data._mysql.models.store import Store


class EmployeeRepository(BaseRepository):
    model = Employee

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Employee]:
        return session.query(cls.model).filter_by(employee_id=_id).first()

    @classmethod
    def change_store(cls, employee: Employee, store: Optional[Store]) -> None:
        if store is not None:
            if store.store_id < 1:
                raise ValueError("Invalid value for store_id. Can not be zero or negative.")

            if employee.store_id == store.store_id:
                raise ValueError("Employee is already working there.")

            employee.store_id = store.store_id
        else:
            employee.store_id = None
        cls.save_to_db(employee)
