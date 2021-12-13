from typing import Optional, Union

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.order import Order
from app.data._mysql.models.product import Product
from app.data._mysql.repositories.product_repository import ProductRepository


class OrderRepository(BaseRepository):
    model = Order

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Order]:
        return session.query(cls.model).filter_by(order_id=_id).first()

    @classmethod
    def find_by_ordered_date(cls, ordered_date: str,
                             many: bool = False) -> Optional[Order, list[Order]]:
        if many:
            return session.query(cls.model).filter_by(ordered_date=ordered_date)
        return session.query(cls.model).filter_by(ordered_date=ordered_date).first()

    @classmethod
    def find_by_shipped_date(cls, shipped_date: str,
                             many: bool = False) -> Optional[Union[Order, list[Order]]]:
        if many:
            return session.query(cls.model).filter_by(shipped_date=shipped_date)
        return session.query(cls.model).filter_by(shipped_date=shipped_date).first()

    @classmethod
    def find_by_delivery_date(cls, delivery_date: str,
                              many: bool = False) -> Optional[Union[Order, list[Order]]]:
        if many:
            return session.query(cls.model).filter_by(delivery_date=delivery_date)
        return session.query(cls.model).filter_by(delivery_date=delivery_date).first()

    @classmethod
    def find_by_city(cls, status: str, many: bool = False) -> Optional[Union[Order, list[Order]]]:
        if many:
            return session.query(cls.model).filter_by(status=status)
        return session.query(cls.model).filter_by(status=status).first()

    @classmethod
    def add_product(cls, order: Order, product: Product) -> None:
        if cls.has_product(order) or OrderRepository.has_order(product):
            return
        order.product_id = product.product_id
        product.order = Order
        session.commit()

    @classmethod
    def has_product(cls, order: Order) -> bool:
        return order.product_id is not None

    @classmethod
    def has_order(cls, product: Product) -> bool:
        return product.order_details is not None

    @classmethod
    def remove_product(cls, order: Order) -> None:
        if not cls.has_product(order):
            return
        product = ProductRepository.find_by_id(order.product_id)
        product.order = None
        order.product_id = None
        session.commit()
