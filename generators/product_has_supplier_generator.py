import random
from app.settings import Settings, Database
Settings.TESTING = True

from generators.contact_person_generator import ContactPersonGenerator
from app.controllers.supplier_controller import SupplierController
from generators.product_generator import ProductGenerator
from generators.supplier_generator import SupplierGenerator
from app.controllers.product_controller import ProductController


class SupplierHasProductGenerator:

    @staticmethod
    def generate(product, supplier) -> None:
        SupplierController.add_product_to_supplier(supplier, product)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        ContactPersonGenerator.populate_database(amount)
        SupplierGenerator.populate_database(amount)
        ProductGenerator.populate_database(amount)

        products = ProductController.find_all()
        suppliers = SupplierController.find_all()

        for i in range(amount):

            if Settings.DATABASE == Database.MONGO:
                pass
            else:
                SupplierHasProductGenerator.generate(random.choice(products), random.choice(suppliers))

        print(f"----- {amount} Suppliers and products generated -----")


def main():
    SupplierHasProductGenerator.populate_database(amount=5)


if __name__ == "__main__":
    main()
