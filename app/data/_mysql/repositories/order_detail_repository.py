from typing import Optional, Union

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
    def find_by_quantity_ordered(cls, quantity_ordered: str, many: bool = False) -> Optional[OrderDetail, list[OrderDetail]]:
        if many:
            return session.query(cls.model).filter_by(quantity_ordered=quantity_ordered)
        return session.query(cls.model).filter_by(quantity_ordered=quantity_ordered).first

    @classmethod
    def find_by_price_each(cls, price_each: str, many: bool = False) -> Optional[Union[OrderDetail, list[OrderDetail]]]:
        if many:
            return session.query(cls.model).filter_by(price_each=price_each)
        return session.query(cls.model).filter_by(price_each=price_each).first()

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
