import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.data._mongo.repositories.store_repository import StoreRepository
from generators.store_generator import StoreGenerator
from shared.models.types import StoreType
from shared.tests.test_printer import TestPrinter


class StoreRepositoryTestCase(unittest.TestCase):
    # region Setup & Cleanup

    def setUp(self) -> None:
        StoreRepository.delete_all()

    def tearDown(self) -> None:
        StoreRepository.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    # endregion Setup & Cleanup

    # region Tests

    def test_create_one_store(self):
        StoreGenerator.populate_database(amount=1)
        store_created = StoreRepository.find_all()[0]
        store = StoreRepository.find_by_city(store_created.city)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_create_one_store.__name__)

    def test_create_many_stores(self):
        StoreGenerator.populate_database(amount=3)
        stores = StoreRepository.find_all()
        self.assertTrue(len(stores) >= 3)
        TestPrinter.add(self.test_create_many_stores.__name__)

    def test_find_by_id_found(self):
        StoreGenerator.populate_database(amount=1)
        store_created = StoreRepository.find_all()[0]
        store = StoreRepository.find_by_id(store_created._id)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_id_found.__name__)

    def test_find_by_id_not_found(self):
        store = StoreRepository.find_by_id("61acd805a1dca9c019999999")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_id_not_found.__name__)

    def test_find_by_city_found(self):
        StoreGenerator.populate_database(amount=1)
        store_created = StoreRepository.find_all()[0]
        store = StoreRepository.find_by_city(store_created.city)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_city_found.__name__)

    def test_find_by_city_not_found(self):
        store = StoreRepository.find_by_city("The Outer Belt")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_city_not_found.__name__)

    def test_find_by_email_found(self):
        StoreGenerator.populate_database(amount=1)
        store_created = StoreRepository.find_all()[0]
        store = StoreRepository.find_by_email(store_created.email)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_email_found.__name__)

    def test_find_by_email_not_found(self):
        store = StoreRepository.find_by_email("no_store@store.se")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_email_not_found.__name__)

    def test_find_by_store_type_found(self):
        StoreGenerator.populate_database(amount=1, online=False)
        store = StoreRepository.find_by_store_type(StoreType.PHYSICAL)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_store_type_found.__name__)

    def test_find_by_store_type_not_found(self):
        StoreGenerator.populate_database(amount=1, online=False)
        store = StoreRepository.find_by_store_type(StoreType.ONLINE)
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_store_type_not_found.__name__)

    def test_find_all_found(self):
        StoreGenerator.populate_database(amount=3)
        stores = StoreRepository.find_all()
        self.assertIsNotNone(stores)
        TestPrinter.add(self.test_find_all_found.__name__)

    def test_find_all_not_found(self):
        StoreRepository.delete_all()
        stores = StoreRepository.find_all()
        self.assertTrue(stores == [])
        TestPrinter.add(self.test_find_all_not_found.__name__)

    def test_delete_one_by_found(self):
        StoreGenerator.populate_database(amount=1, online=False)
        count_deleted = StoreRepository.delete_by(
            {'store_type': StoreType.PHYSICAL}, many=False)
        self.assertTrue(count_deleted == 1)
        TestPrinter.add(self.test_delete_one_by_found.__name__)

    def test_delete_one_by_not_found(self):
        StoreRepository.delete_all()
        count_deleted = StoreRepository.delete_by(
            {'store_type': StoreType.PHYSICAL}, many=False)
        self.assertFalse(count_deleted > 0)
        TestPrinter.add(self.test_delete_one_by_not_found.__name__)

    def test_delete_all_found(self):
        StoreGenerator.populate_database(amount=3)
        count_deleted = StoreRepository.delete_all()
        self.assertTrue(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_found.__name__)

    def test_delete_all_not_found(self):
        StoreRepository.delete_all()
        count_deleted = StoreRepository.delete_all()
        self.assertFalse(count_deleted > 0)
        TestPrinter.add(self.test_delete_all_not_found.__name__)

    def test_find_first_found(self):
        StoreRepository.delete_all()
        StoreGenerator.populate_database(amount=3)
        first_store = StoreRepository.find_all()[0]
        stores = StoreRepository.find(many=True)
        store = stores.first_or_none()
        self.assertEqual(store.email, first_store.email)
        TestPrinter.add(self.test_find_first_found.__name__)

    def test_find_first_not_found(self):
        StoreRepository.delete_all()
        StoreGenerator.populate_database(amount=3)
        last_store = StoreRepository.find_all()[-1]
        stores = StoreRepository.find(many=True)
        store = stores.first_or_none()
        self.assertNotEqual(store.email, last_store.email)
        TestPrinter.add(self.test_find_first_not_found.__name__)

    def test_find_last_found(self):
        StoreRepository.delete_all()
        StoreGenerator.populate_database(amount=3)
        last_store = StoreRepository.find_all()[-1]
        stores = StoreRepository.find(many=True)
        store = stores.last_or_none()
        self.assertEqual(store.email, last_store.email)
        TestPrinter.add(self.test_find_last_found.__name__)

    def test_find_last_not_found(self):
        StoreRepository.delete_all()
        StoreGenerator.populate_database(amount=3)
        first_store = StoreRepository.find_all()[0]
        stores = StoreRepository.find(many=True)
        store = stores.last_or_none()
        self.assertNotEqual(store.email, first_store.email)
        TestPrinter.add(self.test_find_last_not_found.__name__)

    # endregion Tests


def main():
    if not Settings.DATABASE == Database.MONGO:
        raise ValueError("Settings not set to Mongo database.")

    unittest.main()


if __name__ == "__main__":
    main()
