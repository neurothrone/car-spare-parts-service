from typing import Optional

from app.controllers import BaseController
from app.data.models.order import Order
from app.data.repositories.order_repository import OrderRepository


class OrderController(BaseController):
    repository = OrderRepository
    required_attributes = {"ordered_date", "shipped_date",
                           "delivery_date", "status", "customer_id"}

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Order]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def create(cls, ordered_date: str, shipped_date: str, delivery_date: str,
               status: str, customer_id: Optional[int] = None) -> None:
        OrderRepository.create(ordered_date=ordered_date, shipped_date=shipped_date,
                               delivery_date=delivery_date, status=status, customer_id=customer_id)
