from app.controllers.product import ProductController
from app.data.models.product import Product


class ProductGenerator:
    NAME_MAX_LEN = 45
    DESCRIPTION_MAX_LEN = 255

    @staticmethod
    def generate(name: str, description: str, cost: float, price: float) -> Product:
        if len(name) > ProductGenerator.NAME_MAX_LEN:
            raise ValueError(f"Max length of name is {ProductGenerator.NAME_MAX_LEN}.")

        if len(description) > ProductGenerator.DESCRIPTION_MAX_LEN:
            raise ValueError(f"Max length of name is {ProductGenerator.DESCRIPTION_MAX_LEN}.")

        if cost > price:
            raise ValueError(f"Cost is greater than price.")

        return ProductController.create(
            name=name, description=description, cost=cost, price=price)


def main():
    product = ProductGenerator.generate(
        name="Part D",
        description="Description about product",
        cost=25,
        price=30
    )

    product = ProductController.find_by_id(2)
    print(product)


if __name__ == "__main__":
    main()
