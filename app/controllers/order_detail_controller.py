from app.controllers import BaseController
from app.data.models.order_detail import OrderDetail
from app.data.repositories.order_detail_repository import OrderDetailRepository


class OrderDetailController(BaseController):
    model = OrderDetail

    @staticmethod
    def find_by_id(_id: int) -> OrderDetail:
        return OrderDetailRepository.find_by_id(_id)
