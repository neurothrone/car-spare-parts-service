from app.controllers import BaseController
from app.data.models.order import Order
from app.data.repositories.order_repository import OrderRepository


class OrderController(BaseController):
    model = Order

    @staticmethod
    def find_by_id(_id: int) -> Order:
        return OrderRepository.find_by_id(_id)
