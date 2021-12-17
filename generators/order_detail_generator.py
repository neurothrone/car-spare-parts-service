from __future__ import annotations
from random import randint

from app.settings import Settings

Settings.TESTING = True

from app.controllers.order_controller import OrderController
from app.controllers.order_detail_controller import OrderDetailController
from app.controllers.product_controller import ProductController
from generators.order_generator import OrderGenerator
from generators.product_generator import ProductGenerator


class OrderDetailGenerator:
    @classmethod
    def generate(cls, order_id: int, product_id: int,
                 quantity_ordered: int, price_each: float) -> None:
        OrderDetailController.create(quantity_ordered=quantity_ordered, price_each=price_each,
                                     order_id=order_id, product_id=product_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        order_details = OrderDetailController.find_all()
        products = ProductController.find_all()

        if not order_details:
            OrderGenerator.populate_database(amount)
            order_details = OrderController.find_all()

        if not products:
            ProductGenerator.populate_database(amount)
            products = ProductController.find_all()

        for order_detail, product in zip(order_details, products):
            cls.generate(order_id=order_detail.order_id,
                         product_id=product.product_id,
                         quantity_ordered=randint(1, 9),
                         price_each=randint(1, 100))

        print(f"----- {amount} Order Details generated -----")


def main():
    OrderDetailGenerator.populate_database(amount=10)


if __name__ == "__main__":
    main()
