from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.order_detail import OrderDetail


class OrderDetailRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> OrderDetail:
        return session.query(OrderDetail).filter_by(order_detail_id=_id).first()
