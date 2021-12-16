from __future__ import annotations
from typing import Optional

from app.data._mongo.models.order_detail import OrderDetail
from app.data._mongo.models.product import Product
from app.data._mongo.repositories import BaseRepository


class OrderDetailRepository(BaseRepository):
    model = OrderDetail

    @classmethod
    def find_by_quantity_ordered(cls, quantity_ordered: int, many: bool = False) -> Optional[OrderDetail]:
        return cls.find(many=many, quantity_ordered=quantity_ordered)

    @classmethod
    def find_by_price_each(cls, price_each: float, many: bool = False) -> Optional[OrderDetail]:
        return cls.find(many=many, price_each=price_each)

    @classmethod
    def add_product_to_order_detail(cls, order_detail: OrderDetail, product: Product) -> None:
        pass

    @classmethod
    def remove_product_from_order_detail(cls, order_detail: OrderDetail, product: Product) -> None:
        pass
