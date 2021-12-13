from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.order_detail import OrderDetail
from app.data._mysql.models import Product


class OrderDetailRepository(BaseRepository):
    model = OrderDetail

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[OrderDetail]:
        return session.query(cls.model).filter_by(order_detail_id=_id).first()

    @classmethod
    def find_by_order(cls, order: str, many: bool = False) -> Optional[OrderDetail, list[OrderDetail]]:
        if many:
            return session.query(cls.model).filter_by(order=order)
        return session.query(cls.model).filter_by(order=order).first

    @classmethod
    def add_product_to_order_detail(cls, order_detail: OrderDetail, product: Product) -> None:
        if cls.has_product(order_detail) or OrderDetailRepository.has_order(product):
            return

        order_detail.product_id = product.product_id
        product.order_detail = OrderDetail
        session.commit()

    @classmethod
    def has_product(cls, order_detail: OrderDetail) -> bool:
        return order_detail.product_id is not None

    @classmethod
    def has_order(cls, product: Product) -> bool:
        return product.order_detail is not None
