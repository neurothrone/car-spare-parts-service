from __future__ import annotations
from typing import Optional

from app.controllers.product_controller import ProductController
from app.settings import Settings
from generators.order_generator import OrderGenerator
from generators.product_generator import ProductGenerator

Settings.TESTING = True

from app.controllers.order_detail_controller import OrderDetailController
from generators.fake_data import FakeData


class OrderDetailGenerator:

    @classmethod
    def generate_order_details(cls, quantity_ordered: int, price_each: float,
                               order_id: Optional[int | str], product_id: Optional[int | str]) -> None:
        OrderDetailController.create(quantity_ordered=quantity_ordered, price_each=price_each,
                                     order_id=order_id, product_id=product_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        quantity_orders = FakeData.generate_random_int(1, 9)
        price_per_each = FakeData.generate_random_float(1, 100)
        order_details = OrderDetailController.find_all()
        products = ProductController.find_all()
        for quantity_order, price_each, \
            order_detail, product in zip(order_details, products, quantity_orders, price_per_each):
            cls.generate_order_details(quantity_order, price_each, product.product_id)

        print(f"----- {amount} Products generated -----")


def main():
    if __name__ == '__main__':
        main()
