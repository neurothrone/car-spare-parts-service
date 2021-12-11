from __future__ import annotations
from typing import Optional

from app.controllers import BaseController
from app.data.models.order_detail import OrderDetail
from app.data.repositories.order_detail_repository import OrderDetailRepository


class OrderDetailController(BaseController):
    repository = OrderDetailRepository
    required_attributes = {"order_id", "product_id",
                           "quantity_ordered", "price_each"}

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[OrderDetail]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def create(cls, quantity_ordered: str, price_each: str,
               order_id: Optional[int] = None, product_id: Optional[int] = None,) -> None:
        OrderDetailRepository.create(quantity_ordered=quantity_ordered,
                                     price_each=price_each,
                                     order_id=order_id, product_id=product_id)
