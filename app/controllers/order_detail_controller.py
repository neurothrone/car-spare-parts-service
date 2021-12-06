from typing import Optional

from app.controllers import BaseController
from app.data.models.order_detail import OrderDetail
from app.data.repositories.order_detail_repository import OrderDetailRepository


class OrderDetailController(BaseController):
    repository = OrderDetailRepository
    required_attributes = {"order_id", "product_id",
                           "quantity_ordered", "price_each"}

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[OrderDetail]:
        return cls.repository.find_by_id(_id)
