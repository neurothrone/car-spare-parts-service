from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.customer import Customer


class CustomerRepository(BaseRepository):
    model = Customer

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Customer]:
        return session.query(cls.model).filter_by(customer_id=_id).first()
