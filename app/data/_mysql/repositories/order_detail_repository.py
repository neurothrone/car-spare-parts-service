from __future__ import annotations

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
    def find_by_quantity_ordered(cls, quantity_ordered: int,
                                 many: bool = False) -> Optional[OrderDetail | list[OrderDetail]]:
        if many:
            return session.query(cls.model).filter_by(quantity_ordered=quantity_ordered)
        return session.query(cls.model).filter_by(quantity_ordered=quantity_ordered).first()

    @classmethod
    def find_by_price_each(cls, price_each: float, many: bool = False) -> Optional[OrderDetail | list[OrderDetail]]:
        if many:
            return session.query(cls.model).filter_by(price_each=price_each)
        return session.query(cls.model).filter_by(price_each=price_each).first()

    @classmethod
    def add_product_to_order_detail(cls, order_detail: OrderDetail, product: Product) -> None:
        if cls.has_product(order_detail, product):
            return

        order_detail.product.append(order_detail)
        session.commit()

    @classmethod
    def remove_product_from_order_detail(cls, order_detail: OrderDetail, product: Product) -> None:
        if not cls.has_product(order_detail, product):
            return

        order_detail.product.remove(product)
        session.commit()

    @classmethod
    def has_product(cls, product: Product, order_detail: OrderDetail) -> bool:
        if not order_detail.product:
            return False

        for product_order_details in order_detail.product:
            if product_order_details.order_id == product.order_id:
                return True
        return False
