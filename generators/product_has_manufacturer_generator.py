import random

from app.settings import Settings, Database
Settings.TESTING = True

from generators.contact_person_generator import ContactPersonGenerator
from app.controllers.manufacturer_controller import ManufacturerController
from generators.product_generator import ProductGenerator
from generators.manufacturer_generator import ManufacturerGenerator
from app.controllers.product_controller import ProductController


class ManufacturerHasProductGenerator:

    @staticmethod
    def generate(product, manufacturer) -> None:
        ManufacturerController.add_product_to_manufacturer(manufacturer, product)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        ContactPersonGenerator.populate_database(amount)
        ManufacturerGenerator.populate_database(amount)
        ProductGenerator.populate_database(amount)

        products = ProductController.find_all()
        manufacturers = ManufacturerController.find_all()

        for i in range(amount):

            if Settings.DATABASE == Database.MONGO:
                pass
            else:
                ManufacturerHasProductGenerator.generate(random.choice(products), random.choice(manufacturers))

        print(f"----- {amount} Manufacturers and products generated -----")


def main():
    ManufacturerHasProductGenerator.populate_database(amount=5)


if __name__ == "__main__":
    main()
