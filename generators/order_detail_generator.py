import random
from app.settings import Settings, Database

Settings.TESTING = True

from generators.customer_generator import CustomerGenerator
from app.controllers.order_detail_controller import OrderDetailController
from generators.product_generator import ProductGenerator
from app.controllers.product_controller import ProductController
from app.controllers.order_controller import OrderController
from generators.order_generator import OrderGenerator
from generators.fake_data import FakeData


class OrderDetailGenerator:

    @staticmethod
    def generate(product, order, quantity_ordered: int, price_each: float) -> None:
        OrderController.add_order_to_product(order, product)
        # OrderController.create(quantity_ordered=quantity_ordered,
        #                              price_each=price_each)

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
                OrderDetailGenerator.generate(product=random.choice(products),
                                              order=random.choice(orders),
                                              quantity_ordered=quantity_ordered,
                                              price_each=each_price)

                # cls.generate(quantity_ordered=quantity_ordered,
                #              price_each=each_price)

        print(f"----- {amount} Manufacturers and products generated -----")


def main():
    OrderDetailGenerator.populate_database(amount=5)


if __name__ == "__main__":
    main()
