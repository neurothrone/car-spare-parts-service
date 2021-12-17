from __future__ import annotations
from datetime import date
from typing import Optional

from app.controllers import BaseController
from app.data.models.order import Order
from app.data.models.product import Product
from app.data.repositories.order_repository import OrderRepository


class OrderController(BaseController):
    repository = OrderRepository
    required_attributes = {"ordered_date", "shipped_date",
                           "delivery_date", "status", "customer_id"}

    @classmethod
    def create(cls, ordered_date: date, shipped_date: date,
               delivery_date: date, status: str, customer_id: Optional[int | str]) -> None:
        cls.repository.create(ordered_date=ordered_date, shipped_date=shipped_date,
                              delivery_date=delivery_date, status=status, customer_id=customer_id)

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[Order]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def find_by_ordered_date(cls, ordered_date: date) -> Optional[Order]:
        return cls.repository.find_by_ordered_date(ordered_date)

    @classmethod
    def find_by_shipped_date(cls, shipped_date: date) -> Optional[Order]:
        return cls.repository.find_by_shipped_date(shipped_date)

    @classmethod
    def find_by_delivery_date(cls, delivery_date: date) -> Optional[Order]:
        return cls.repository.find_by_delivery_date(delivery_date)

    @classmethod
    def find_by_status(cls, status: str) -> Optional[Order]:
        return cls.repository.find_by_status(status)

    @classmethod
    def add_order_to_product(cls, order: Order, product: Product) -> None:
        cls.repository.add_order_to_product(order, product)

    @classmethod
    def remove_order_from_product(cls, order: Order, product: Product) -> None:
        cls.repository.remove_order_from_product(order, product)
