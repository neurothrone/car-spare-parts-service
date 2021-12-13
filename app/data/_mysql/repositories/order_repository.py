from typing import Optional

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
    def find_by_customer(cls, customer: str, many: bool = False) -> Optional[Order, list[Order]]:
        if many:
            return session.query(cls.model).filter_by(customer=customer)
        return session.query(cls.model).filter_by(customer=customer).first()

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
