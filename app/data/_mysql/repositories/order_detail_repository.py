from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.order_detail import OrderDetail


class OrderDetailRepository(BaseRepository):
    model = OrderDetail

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[OrderDetail]:
        return session.query(cls.model).filter_by(order_detail_id=_id).first()
