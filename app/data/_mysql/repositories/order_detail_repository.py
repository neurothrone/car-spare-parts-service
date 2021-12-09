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
    def add_product_to_order_detail(cls, orderdetail: OrderDetail, product: Product) -> None:
        if cls.has_product(orderdetail) or OrderDetailRepository.has_order(product):
            return

        orderdetail.product_id = product.product_id
        product.orderdetail = OrderDetail
        session.commit()

    @classmethod
    def has_product(cls, orderdetail: OrderDetail) -> bool:
        return orderdetail.product_id is not None

    @classmethod
    def has_order(cls, product: Product) -> bool:
        return product.order_details is not None
