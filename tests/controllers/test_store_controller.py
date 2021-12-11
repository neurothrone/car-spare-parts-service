import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.controllers.store_controller import StoreController
from generators.store_generator import StoreGenerator
from shared.models.types import StoreType
from shared.tests.test_printer import TestPrinter


class StoreControllerTestCase(unittest.TestCase):
    # region Setup & Cleanup

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

    # endregion Setup & Cleanup

    # region Tests

    def test_find_by_id_found(self):
        StoreGenerator.populate_database(amount=1)
        store_created = StoreController.find_all()[0]

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

    def test_create_physical_store_fail(self):
        with self.assertRaises(ValueError):
            StoreController.create(store_type=StoreType.PHYSICAL,
                                   phone="+64 70 722 88 88",
                                   email="store@example.se")
        TestPrinter.add(self.test_create_physical_store_fail.__name__)

    def test_create_online_store_fail(self):
        with self.assertRaises(ValueError):
            StoreController.create(store_type=StoreType.ONLINE,
                                   phone="+64 70 722 88 88",
                                   email="store@example.se",
                                   address="Tarbergsgatan 25",
                                   zip_code="172 41",
                                   city="Karlstad")
        TestPrinter.add(self.test_create_online_store_fail.__name__)

    def test_create_many_stores(self):
        StoreGenerator.populate_database(amount=3)
        stores = StoreController.find_all()
        self.assertTrue(len(stores) >= 3)
        TestPrinter.add(self.test_create_many_stores.__name__)

    def test_find_by_city_found(self):
        StoreGenerator.populate_database(amount=1)
        store_created = StoreController.find_all()[0]
        store = StoreController.find_by_city(store_created.city)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_city_found.__name__)

    def test_find_by_city_not_found(self):
        store = StoreController.find_by_city("The Moon")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_city_not_found.__name__)

    def test_find_by_email_found(self):
        StoreGenerator.populate_database(amount=1)
        store_created = StoreController.find_all()[0]
        store = StoreController.find_by_email(store_created.email)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_email_found.__name__)

    def test_find_by_email_not_found(self):
        store = StoreController.find_by_email("no_store@store.se")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_email_not_found.__name__)

    def test_find_by_store_type_found(self):
        StoreGenerator.populate_database(amount=1, online=False)
        store = StoreController.find_by_store_type(StoreType.PHYSICAL)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_store_type_found.__name__)

    def test_find_by_store_type_not_found(self):
        store = StoreController.find_by_store_type(StoreType.ONLINE)
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_store_type_not_found.__name__)

    def test_find_all_found(self):
        StoreGenerator.populate_database(amount=3)
        stores = StoreController.find_all()
        self.assertIsNotNone(stores)
        TestPrinter.add(self.test_find_all_found.__name__)

    def test_find_all_not_found(self):
        StoreController.delete_all()
        stores = StoreController.find_all()
        self.assertTrue(stores == [])
        TestPrinter.add(self.test_find_all_not_found.__name__)

    def test_delete_all_found(self):
        StoreGenerator.populate_database(amount=3)
        count_deleted = StoreController.delete_all()
        self.assertTrue(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_found.__name__)

    def test_delete_all_not_found(self):
        StoreController.delete_all()
        count_deleted = StoreController.delete_all()
        self.assertFalse(count_deleted > 0)
        TestPrinter.add(self.test_delete_all_not_found.__name__)

    # endregion Tests


def main():
    unittest.main()


if __name__ == "__main__":
    main()
