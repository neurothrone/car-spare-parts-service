from app.settings import Settings
Settings.TESTING = True

from app.controllers.product_controller import ProductController
from generators.fake_data import FakeData


class ProductGenerator:
    NAME_MAX_LEN = 45
    DESCRIPTION_MAX_LEN = 255

    @classmethod
    def generate(cls, name: str, description: str, cost: float, price: float) -> None:
        if len(name) > ProductGenerator.NAME_MAX_LEN:
            raise ValueError(f"Max length of name is {cls.NAME_MAX_LEN}.")

        if len(description) > ProductGenerator.DESCRIPTION_MAX_LEN:
            raise ValueError(f"Max length of name is {cls.DESCRIPTION_MAX_LEN}.")

        if cost > price:
            raise ValueError(f"Cost is greater than price.")

        ProductController.create(
            name=name, description=description, cost=cost, price=price)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        for _ in range(amount):
            product = FakeData.generate_product(cost_scale=1)

            cls.generate(
                name=product.name,
                description=product.description,
                cost=product.cost,
                price=product.price)

        print(f"----- {amount} Products generated -----")


def main():
    ProductGenerator.populate_database(amount=500)


if __name__ == "__main__":
    main()
