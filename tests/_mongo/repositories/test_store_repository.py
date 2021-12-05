from __future__ import annotations
import unittest

from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.store_repository import StoreRepository
from shared.tests.test_printer import TestPrinter


class StoreRepositoryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.create_single_store()

    def tearDown(self) -> None:
        StoreRepository.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    @classmethod
    def create_single_store(cls) -> None:
        data = {
            "store_type": "p",
            "phone": "071 234 56 78",
            "email": "testcity@store.se",
            "address": "TestStreet 22",
            "zip_code": "123 45",
            "city": "TestCity"
        }
        StoreRepository.create(**data)

    @classmethod
    def create_many_stores(cls) -> None:
        data = [
            {
                "store_type": "p",
                "phone": "076 433 24 53",
                "email": "bjarnby@store.se",
                "address": "Granberg 54",
                "zip_code": "173 42",
                "city": "Bjarnby"
            },
            {
                "store_type": "p",
                "phone": "072 46 22 44",
                "email": "fjorden@store.se",
                "address": "Falkensten 23",
                "zip_code": "342 11",
                "city": "Fjorden"
            },
            {
                "store_type": "o",
                "phone": "076 433 24 53",
                "email": "web@store.se",
                "address": None,
                "zip_code": None,
                "city": None
            }
        ]
        StoreRepository.create_many(data)

    def test_create_one_store(self):
        store = StoreRepository.find_by_city("TestCity")
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_create_one_store.__name__)

    def test_create_many_stores(self):
        self.create_many_stores()
        stores = StoreRepository.find_all()
        self.assertTrue(len(stores) >= 3)
        TestPrinter.add(self.test_create_many_stores.__name__)

    def test_find_by_id_found(self):
        self.create_single_store()
        store_created = StoreRepository.find_by_city("TestCity")
        store = StoreRepository.find_by_id(store_created._id)
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_id_found.__name__)

    def test_find_by_id_not_found(self):
        store = StoreRepository.find_by_id("1")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_id_not_found.__name__)

    def test_find_by_city_found(self):
        self.create_single_store()
        store = StoreRepository.find_by_city("TestCity")
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_city_found.__name__)

    def test_find_by_city_not_found(self):
        store = StoreRepository.find_by_city("Gothenburg")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_city_not_found.__name__)

    def test_find_by_email_found(self):
        self.create_single_store()
        store = StoreRepository.find_by_email("testcity@store.se")
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_email_found.__name__)

    def test_find_by_email_not_found(self):
        store = StoreRepository.find_by_email("no_store@store.se")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_email_not_found.__name__)

    def test_find_by_store_type_found(self):
        self.create_single_store()
        store = StoreRepository.find_by_store_type("p")
        self.assertIsNotNone(store)
        TestPrinter.add(self.test_find_by_store_type_found.__name__)

    def test_find_by_store_type_not_found(self):
        store = StoreRepository.find_by_store_type("o")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_store_type_not_found.__name__)

    def test_find_all_found(self):
        self.create_many_stores()
        stores = StoreRepository.find_all()
        self.assertIsNotNone(stores)
        TestPrinter.add(self.test_find_all_found.__name__)

    def test_find_all_not_found(self):
        StoreRepository.delete_all()
        stores = StoreRepository.find_all()
        self.assertTrue(stores == [])
        TestPrinter.add(self.test_find_all_not_found.__name__)

    def test_delete_one_by_found(self):
        self.create_single_store()
        count_deleted = StoreRepository.delete_by({'store_type': 'p'}, many=False)
        self.assertTrue(count_deleted == 1)
        TestPrinter.add(self.test_delete_one_by_found.__name__)

    def test_delete_one_by_not_found(self):
        StoreRepository.delete_all()
        count_deleted = StoreRepository.delete_by({'store_type': 'p'}, many=False)
        self.assertFalse(count_deleted == 1)
        TestPrinter.add(self.test_delete_one_by_not_found.__name__)

    def test_delete_all_found(self):
        self.create_many_stores()
        count_deleted = StoreRepository.delete_all()
        self.assertTrue(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_found.__name__)

    def test_delete_all_not_found(self):
        StoreRepository.delete_all()
        count_deleted = StoreRepository.delete_all()
        self.assertFalse(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_not_found.__name__)

    def test_find_first_found(self):
        StoreRepository.delete_all()
        self.create_many_stores()
        stores = StoreRepository.find(many=True)
        store = stores.first_or_none()
        self.assertEqual(store.email, "bjarnby@store.se")
        TestPrinter.add(self.test_find_first_found.__name__)

    def test_find_first_not_found(self):
        StoreRepository.delete_all()
        self.create_many_stores()
        stores = StoreRepository.find(many=True)
        store = stores.first_or_none()
        self.assertNotEqual(store.email, "web@store.se")
        TestPrinter.add(self.test_find_first_not_found.__name__)

    def test_find_last_found(self):
        StoreRepository.delete_all()
        self.create_many_stores()
        stores = StoreRepository.find(many=True)
        store = stores.last_or_none()
        self.assertEqual(store.email, "web@store.se")
        TestPrinter.add(self.test_find_last_found.__name__)

    def test_find_last_not_found(self):
        StoreRepository.delete_all()
        self.create_many_stores()
        stores = StoreRepository.find(many=True)
        store = stores.last_or_none()
        self.assertNotEqual(store.email, "bjarnby@store.se")
        TestPrinter.add(self.test_find_last_not_found.__name__)

    def test_find_all_sort_by_sorted(self):
        StoreRepository.delete_all()
        self.create_many_stores()
        stores = StoreRepository.find_all_sort_by("city", True)
        for store, city in zip(stores, [None, "Bjarnby", "Fjorden"]):
            self.assertEqual(store.city, city)
        TestPrinter.add(self.test_find_all_sort_by_sorted.__name__)

    def test_find_all_sort_by_not_sorted(self):
        StoreRepository.delete_all()
        self.create_many_stores()
        stores = StoreRepository.find_all()
        self.assertNotEqual(stores[0].city, None)
        TestPrinter.add(self.test_find_all_sort_by_not_sorted.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
