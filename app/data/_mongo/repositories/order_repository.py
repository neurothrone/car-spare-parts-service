from __future__ import annotations
from datetime import datetime
from typing import Optional

from app.data._mongo.models.order import Order
from app.data._mongo.models.product import Product
from app.data._mongo.repositories import BaseRepository


class OrderRepository(BaseRepository):
    model = Order

    @classmethod
    def find_by_ordered_date(cls, ordered_date: datetime,
                             many: bool = False) -> Optional[Order | list[Order]]:
        return cls.find(many=many, ordered_date=ordered_date)

    @classmethod
    def find_by_shipped_date(cls, shipped_date: datetime,
                             many: bool = False) -> Optional[Order | list[Order]]:
        return cls.find(many=many, shipped_date=shipped_date)

    @classmethod
    def find_by_delivery_date(cls, delivery_date: datetime.date,
                              many: bool = False) -> Optional[Order | list[Order]]:
        return cls.find(many=many, delivery_date=delivery_date)

    @classmethod
    def find_by_status(cls, status: str, many: bool = False) -> Optional[Order | list[Order]]:
        return cls.find(many=many, status=status)

    @classmethod
    def add_order_to_product(cls, order: Order, product: Product) -> None:
        pass

    @classmethod
    def remove_order_from_product(cls, order: Order, product: Product) -> None:
        pass

    @classmethod
    def has_product(cls, order: Order, product: Product) -> bool:
        pass

