import unittest

from app.settings import Database, Settings

Settings.DATABASE = Database.MYSQL
Settings.TESTING = True

from app.converters.product_converter import ProductConverter
from app.converters.storage_converter import StorageConverter
from app.converters.store_converter import StoreConverter
from app.data._mongo.repositories.product_repository import ProductRepository as MongoProductRepository
from app.data._mongo.repositories.store_repository import StoreRepository as MongoStoreRepository
from app.data._mysql.repositories.product_repository import ProductRepository as MysqlProductRepository
from app.data._mysql.repositories.storage_repository import StorageRepository as MysqlStorageRepository
from app.data._mysql.repositories.store_repository import StoreRepository as MysqlStoreRepository
from generators.product_generator import ProductGenerator
from generators.store_generator import StoreGenerator
from shared.tests.test_printer import TestPrinter


class StorageConverterTestCase(unittest.TestCase):
    # region Setup & Cleanup

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        MongoProductRepository.delete_all()
        MongoStoreRepository.delete_all()
        MysqlStorageRepository.remove_all_products_from_all_stores()
        MysqlStoreRepository.delete_all()
        MysqlProductRepository.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        MysqlStorageRepository.remove_all_products_from_all_stores()
        MysqlStoreRepository.delete_all()
        MysqlProductRepository.delete_all()
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    # endregion Setup & Cleanup

    # region Tests

    def test_single_product_in_storage_conversion(self):
        ProductGenerator.populate_database(amount=5)
        StoreGenerator.populate_database(amount=5, online=False)
        ProductConverter.convert_from_mysql_to_mongo()
        StoreConverter.convert_from_mysql_to_mongo()

        for product, store in zip(MysqlProductRepository.find_all(), MysqlStoreRepository.find_all()):
            MysqlStorageRepository.add_product_to_store(store, product)

        StorageConverter.convert_from_mysql_to_mongo()

        for mongo_store in MongoStoreRepository.find_all():
            self.assertEqual(len(mongo_store.storage), 1)

        TestPrinter.add(self.test_single_product_in_storage_conversion.__name__)

    def test_multiple_products_in_storage_conversion(self):
        ProductGenerator.populate_database(amount=5)
        StoreGenerator.populate_database(amount=1, online=False)
        ProductConverter.convert_from_mysql_to_mongo()
        StoreConverter.convert_from_mysql_to_mongo()

        mysql_store = MysqlStoreRepository.find_all()[0]

        for product in MysqlProductRepository.find_all():
            MysqlStorageRepository.add_product_to_store(mysql_store, product)

        StorageConverter.convert_from_mysql_to_mongo()
        mongo_store = MongoStoreRepository.find_all()[0]
        self.assertEqual(len(mongo_store.storage), 5)

        TestPrinter.add(self.test_multiple_products_in_storage_conversion.__name__)

    # endregion Tests


def main():
    unittest.main()


if __name__ == "__main__":
    main()
