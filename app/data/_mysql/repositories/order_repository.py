from __future__ import annotations
from datetime import datetime
from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.models.order import Order
from app.data._mysql.models.product import Product
from app.data._mysql.repositories import BaseRepository


class OrderRepository(BaseRepository):
    model = Order

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Order]:
        return session.query(cls.model).filter_by(order_id=_id).first()

    @classmethod
    def find_by_ordered_date(cls, ordered_date: datetime,
                             many: bool = False) -> Optional[Order | list[Order]]:
        if many:
            return session.query(cls.model).filter_by(ordered_date=ordered_date)
        return session.query(cls.model).filter_by(ordered_date=ordered_date).first()

    @classmethod
    def find_by_shipped_date(cls, shipped_date: datetime,
                             many: bool = False) -> Optional[Order | list[Order]]:
        if many:
            return session.query(cls.model).filter_by(shipped_date=shipped_date)
        return session.query(cls.model).filter_by(shipped_date=shipped_date).first()

    @classmethod
    def find_by_delivery_date(cls, delivery_date: datetime.date,
                              many: bool = False) -> Optional[Order | list[Order]]:
        if many:
            return session.query(cls.model).filter_by(delivery_date=delivery_date)
        return session.query(cls.model).filter_by(delivery_date=delivery_date).first()

    @classmethod
    def find_by_status(cls, status: str, many: bool = False) -> Optional[Order | list[Order]]:
        if many:
            return session.query(cls.model).filter_by(status=status)
        return session.query(cls.model).filter_by(status=status).first()

    @classmethod
    def add_order_to_product(cls, order: Order, product: Product) -> None:
        if cls.has_product(order, product):
            return

        order.products.append(product)
        session.commit()

    @classmethod
    def remove_order_from_product(cls, order: Order, product: Product) -> None:
        if not cls.has_product(order, product):
            return

        order.products.remove(product)
        session.commit()

    @classmethod
    def has_product(cls, order: Order, product: Product) -> bool:
        if not order.products:
            return False

        for order_products in order.products:
            if order_products.product_id == product.product_id:
                return True
        return False
