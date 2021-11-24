from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.customer import Customer


class CustomerRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Customer:
        return session.query(Customer).filter_by(customer_id=_id).first()
