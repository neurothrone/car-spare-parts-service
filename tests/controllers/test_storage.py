import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.controllers.product_controller import ProductController
from app.controllers.storage_controller import StorageController
from app.controllers.store_controller import StoreController
from generators.product_generator import ProductGenerator
from generators.store_generator import StoreGenerator
from shared.tests.test_printer import TestPrinter


class StorageTestCase(unittest.TestCase):
    # region Setup & Cleanup

    def setUp(self) -> None:
        StoreGenerator.populate_database(amount=1, online=False)
        ProductGenerator.populate_database(amount=1)

    def tearDown(self) -> None:
        StorageController.remove_all_products_from_all_stores()
        StoreController.delete_all()
        ProductController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    # endregion Setup & Cleanup

    # region Tests

    def test_add_product_to_store(self):
        store = StoreController.find_all()[0]
        product = ProductController.find_all()[0]
        StorageController.add_product_to_store(store, product)
        for storage in store.products:
            self.assertIsNotNone(storage)
        TestPrinter.add(self.test_add_product_to_store.__name__)

    def test_add_product_to_store_default_values(self):
        store = StoreController.find_all()[0]
        product = ProductController.find_all()[0]
        StorageController.add_product_to_store(store, product)
        for storage in store.products:
            self.assertEqual(storage.stock_number, 0)
            self.assertEqual(storage.critical_threshold, 0)
            self.assertEqual(storage.amount_automatic_order, 0)
        TestPrinter.add(self.test_add_product_to_store_default_values.__name__)

    def test_add_product_to_store_custom_values(self):
        store = StoreController.find_all()[0]
        product = ProductController.find_all()[0]
        StorageController.add_product_to_store(store,
                                               product,
                                               stock_number=19,
                                               critical_threshold=5,
                                               amount_automatic_order=15)
        for storage in store.products:
            self.assertEqual(storage.stock_number, 19)
            self.assertEqual(storage.critical_threshold, 5)
            self.assertEqual(storage.amount_automatic_order, 15)
        TestPrinter.add(self.test_add_product_to_store_custom_values.__name__)

    def test_remove_product_from_store(self):
        store = StoreController.find_all()[0]
        product = ProductController.find_all()[0]
        StorageController.add_product_to_store(store, product)
        StorageController.remove_product_from_store(store, product)
        for storage in store.products:
            self.assertIsNone(storage)
        TestPrinter.add(self.test_remove_product_from_store.__name__)

    # endregion Tests


def main():
    unittest.main()


if __name__ == "__main__":
    main()
