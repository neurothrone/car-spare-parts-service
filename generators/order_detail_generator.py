import random
from app.settings import Settings, Database
from data._mysql.models import OrderDetail

Settings.TESTING = True

from generators.customer_generator import CustomerGenerator
from app.controllers.order_detail_controller import OrderDetailController
from generators.product_generator import ProductGenerator
from app.controllers.product_controller import ProductController
from app.controllers.order_controller import OrderController
from generators.order_generator import OrderGenerator


class OrderDetailGenerator:

    @staticmethod
    def generate(product, order_detail) -> None:
        OrderDetailController.add_product_to_order_detail(product, order_detail)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        CustomerGenerator.populate_database(amount)
        OrderGenerator.populate_database(amount)
        ProductGenerator.populate_database(amount)

        quantity_ordered = random.randint(1, 10)
        each_price = random.randint(5000, 80000)

        products = ProductController.find_all()
        orders = OrderController.find_all()

        for i in range(amount):

            if Settings.DATABASE == Database.MONGO:
                pass
            else:
                order_detail = OrderDetail()
                order_detail.order_id = random.choice(orders).order_id
                product = random.choice(products)
                order_detail.product_id = product.product_id
                order_detail.quantity_ordered = quantity_ordered
                order_detail.price_each = each_price

                OrderDetailGenerator.generate(order_detail=order_detail, product=product)


def main():
    OrderDetailGenerator.populate_database(amount=2)


if __name__ == "__main__":
    main()
