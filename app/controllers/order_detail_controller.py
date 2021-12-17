from __future__ import annotations
from typing import Optional

from app.controllers import BaseController
from app.data.models.order_detail import OrderDetail
from app.data.models.product import Product
from app.data.repositories.order_detail_repository import OrderDetailRepository


class OrderDetailController(BaseController):
    repository = OrderDetailRepository
    required_attributes = {"order_id", "product_id",
                           "quantity_ordered", "price_each"}

    @classmethod
    def create(cls, order_id: int, product_id: int,
               quantity_ordered: str, price_each: str) -> None:
        OrderDetailRepository.create(order_id=order_id, product_id=product_id,
                                     quantity_ordered=quantity_ordered, price_each=price_each)

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[OrderDetail]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def find_by_quantity_ordered(cls, quantity_ordered: int) -> Optional[OrderDetail]:
        return cls.repository.find_by_quantity_ordered(quantity_ordered)

    @classmethod
    def find_by_price_each(cls, price_each: float) -> Optional[OrderDetail]:
        return cls.repository.find_by_price_each(price_each)

    @classmethod
    def add_product_to_order_detail(cls, order_detail: OrderDetail, product: Product) -> None:
        cls.repository.add_product_to_order_detail(order_detail, product)

    @classmethod
    def remove_product_from_order_detail(cls, order_detail: OrderDetail, product: Product) -> None:
        cls.repository.remove_product_from_order_detail(order_detail, product)
