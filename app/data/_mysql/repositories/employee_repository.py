from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.employee import Employee


class EmployeeRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Employee:
        return session.query(Employee).filter_by(employee_id=_id).first()

    @classmethod
    def change_store(cls, employee: Employee, store_id: int) -> None:
        employee.store_id = store_id
        cls.save_to_db(employee)
