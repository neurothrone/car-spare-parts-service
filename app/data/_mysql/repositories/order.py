from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.order import Order


class OrderRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Order:
        return session.query(Order).filter_by(order_id=_id).first()
