import unittest

from app.controllers.store_controller import StoreController
from app.settings import Database, Settings
from shared.models.types import StoreType
from shared.tests.test_printer import TestPrinter
from tests.data import store_data, stores_data


class StoreControllerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        StoreController.delete_all()

    def tearDown(self) -> None:
        StoreController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    @classmethod
    def create_single_store(cls) -> None:
        StoreController.create(**store_data)

    @classmethod
    def create_many_stores(cls) -> None:
        StoreController.create_many(stores_data)

    def test_find_by_id_found(self):
        self.create_single_store()
        store_created = StoreController.find_by_city("TestCity")

        if Settings.DATABASE == Database.MONGO:
            store = StoreController.find_by_id(store_created._id)
        else:
            store = StoreController.find_by_id(store_created.store_id)

        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_id_found.__name__)

    def test_find_by_id_not_found(self):
        if Settings.DATABASE == Database.MONGO:
            store = StoreController.find_by_id("61acd805a1dca9c019999999")
        else:
            store = StoreController.find_by_id(9999)
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_id_not_found.__name__)

    def test_create_one_store(self):
        self.create_single_store()
        store = StoreController.find_by_city("TestCity")
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_create_one_store.__name__)

    def test_create_many_stores(self):
        self.create_many_stores()
        stores = StoreController.find_all()
        self.assertTrue(len(stores) >= 3)
        TestPrinter.add(self.test_create_many_stores.__name__)

    def test_find_by_city_found(self):
        self.create_single_store()
        store = StoreController.find_by_city("TestCity")
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_city_found.__name__)

    def test_find_by_city_not_found(self):
        store = StoreController.find_by_city("Gothenburg")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_city_not_found.__name__)

    def test_find_by_email_found(self):
        self.create_single_store()
        store = StoreController.find_by_email("testcity@store.se")
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_email_found.__name__)

    def test_find_by_email_not_found(self):
        store = StoreController.find_by_email("no_store@store.se")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_email_not_found.__name__)

    def test_find_by_store_type_found(self):
        self.create_single_store()
        store = StoreController.find_by_store_type(StoreType.PHYSICAL)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_store_type_found.__name__)

    def test_find_by_store_type_not_found(self):
        store = StoreController.find_by_store_type(StoreType.ONLINE)
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_store_type_not_found.__name__)

    def test_find_all_found(self):
        self.create_many_stores()
        stores = StoreController.find_all()
        self.assertIsNotNone(stores)
        TestPrinter.add(self.test_find_all_found.__name__)

    def test_find_all_not_found(self):
        StoreController.delete_all()
        stores = StoreController.find_all()
        self.assertTrue(stores == [])
        TestPrinter.add(self.test_find_all_not_found.__name__)

    def test_delete_all_found(self):
        self.create_many_stores()
        count_deleted = StoreController.delete_all()
        self.assertTrue(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_found.__name__)

    def test_delete_all_not_found(self):
        StoreController.delete_all()
        count_deleted = StoreController.delete_all()
        self.assertFalse(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_not_found.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
