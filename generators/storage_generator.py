from random import randint, shuffle

from app.settings import Settings

Settings.TESTING = True

from app.controllers.product_controller import ProductController
from app.controllers.store_controller import StoreController
from app.controllers.storage_controller import StorageController


class StorageGenerator:
    # @classmethod
    # def generate(cls,
    #              stock_number: int = 0,
    #              critical_threshold: int = 0,
    #              amount_automatic_order: int = 0) -> None:
    #     pass

    # @classmethod
    # def populate_database(cls, amount: int) -> None:
    #     pass

    @classmethod
    def add_products_to_stores(cls, min_per_store: int, max_per_store: int) -> None:
        stores = StoreController.find_all()
        products = ProductController.find_all()

        if not stores or not products:
            raise ValueError("No stores to add products to or no products to add to stores.")

        products_added = 0

        for store in stores:
            shuffle(products)
            products_to_add = randint(min_per_store, max_per_store)

            for index in range(products_to_add):
                StorageController.add_product_to_store(store, products[index])
                products_added += 1

        print(f"----- {products_added} total products added to all stores -----")

    @classmethod
    def remove_all_products_in_stores(cls) -> None:
        stores = StoreController.find_all()
        products_removed = 0

        for store in stores:
            for storage in store.products:
                StorageController.remove_product_from_store(store, storage.product)
                products_removed += 1

        print(f"----- {products_removed} products removed from all stores -----")

    @classmethod
    def print_products_in_stores(cls) -> None:
        stores = StoreController.find_all()
        total_products = 0

        for store in stores:
            for storage in store.products:
                total_products += 1
                print(type(storage))
                print(f"\tStock number: {storage.stock_number}")
                print(f"\tCritical threshold: {storage.critical_threshold}")
                print(f"\tAutomatic amount: {storage.amount_automatic_order}")
                print(storage.product)
                print(storage.store)

        print(f"----- {total_products} total products in all stores -----")

def main():
    StoreGenerator.populate_database(amount=10)


if __name__ == "__main__":
    main()