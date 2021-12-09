from __future__ import annotations
from typing import Optional

from app.controllers import BaseController
from app.data.models.order import Order
from app.data.repositories.order_repository import OrderRepository


class OrderController(BaseController):
    repository = OrderRepository
    required_attributes = {"ordered_date", "shipped_date",
                           "delivery_date", "status", "customer_id"}

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[Order]:
        return cls.repository.find_by_id(_id)
