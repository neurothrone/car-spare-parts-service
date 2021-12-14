import unittest

from app.settings import Database, Settings

Settings.DATABASE = Database.MYSQL
Settings.TESTING = True

from app.converters.product_converter import ProductConverter
from app.converters.product_has_supplier_converter import ProductsHasSuppliersConverter
from app.converters.supplier_converter import SupplierConverter
from app.data._mongo.repositories.product_repository import ProductRepository as MongoProductRepository
from app.data._mongo.repositories.supplier_repository import SupplierRepository as MongoSupplierRepository
from app.data._mysql.repositories.product_repository import ProductRepository as MysqlProductRepository
from app.data._mysql.repositories.products_has_suppliers_repository import ProductsHasSuppliersRepository as MysqlProductsHasSupplierRepository
from app.data._mysql.repositories.supplier_repository import SupplierRepository as MysqlSupplierRepository
from generators.product_generator import ProductGenerator
from generators.supplier_generator import SupplierGenerator
from shared.tests.test_printer import TestPrinter


class ProductHasSuppliersConverterTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        MongoProductRepository.delete_all()
        MongoSupplierRepository.delete_all()
        MysqlProductsHasSupplierRepository.remove_all_products_from_all_suppliers()
        MysqlSupplierRepository.delete_all()
        MysqlProductRepository.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        MysqlProductsHasSupplierRepository.remove_all_products_from_all_suppliers()
        MysqlSupplierRepository.delete_all()
        MysqlProductRepository.delete_all()
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    def test_single_product_in_product_has_supplier_conversion(self):
        ProductGenerator.populate_database(amount=5)
        SupplierGenerator.populate_database(amount=5)
        ProductConverter.convert_from_mysql_to_mongo()
        SupplierConverter.convert_from_mysql_to_mongo()

        for product, supplier in zip(MysqlProductRepository.find_all(), MysqlSupplierRepository.find_all()):
            MysqlProductsHasSupplierRepository.add_product_to_supplier(supplier, product)

        ProductsHasSuppliersConverter.convert_from_mysql_to_mongo()

        for mongo_supplier in MongoSupplierRepository.find_all():
            self.assertEqual(len(mongo_supplier.product_has_supplier), 1)

        TestPrinter.add(self.test_single_product_in_product_has_supplier_conversion.__name__)

    def test_multiple_products_in_product_has_supplier_conversion(self):
        ProductGenerator.populate_database(amount=5)
        SupplierGenerator.populate_database(amount=1)
        ProductConverter.convert_from_mysql_to_mongo()
        SupplierConverter.convert_from_mysql_to_mongo()

        mysql_supplier = MysqlSupplierRepository.find_all()[0]

        for product in MysqlProductRepository.find_all():
            MysqlProductsHasSupplierRepository.add_product_to_supplier(mysql_supplier, product)

        ProductsHasSuppliersConverter.convert_from_mysql_to_mongo()
        mongo_supplier = MongoSupplierRepository.find_all()[0]
        self.assertEqual(len(mongo_supplier.product_has_supplier), 5)

        TestPrinter.add(self.test_multiple_products_in_product_has_supplier_conversion.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
