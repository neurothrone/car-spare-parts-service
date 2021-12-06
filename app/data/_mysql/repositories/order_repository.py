from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.order import Order


class OrderRepository(BaseRepository):
    model = Order

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Order]:
        return session.query(cls.model).filter_by(order_id=_id).first()
