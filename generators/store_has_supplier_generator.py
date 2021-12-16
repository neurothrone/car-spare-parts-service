from app.settings import Settings, Database
Settings.TESTING = True

import random
from generators.contact_person_generator import ContactPersonGenerator
from app.controllers.supplier_controller import SupplierController
from generators.store_generator import StoreGenerator
from generators.supplier_generator import SupplierGenerator
from app.controllers.store_controller import StoreController


class StoreHasSupplierGenerator:

    @staticmethod
    def generate(store, supplier) -> None:
        StoreController.add_supplier_to_store(store, supplier)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        ContactPersonGenerator.populate_database(amount)
        SupplierGenerator.populate_database(amount)
        StoreGenerator.populate_database(amount)

        suppliers = SupplierController.find_all()
        stores = StoreController.find_all()

        for i in range(amount):

            if Settings.DATABASE == Database.MONGO:
                pass
            else:
                StoreHasSupplierGenerator.generate(random.choice(stores), random.choice(suppliers))


def main():
    StoreHasSupplierGenerator.populate_database(amount=5)


if __name__ == "__main__":
    main()
