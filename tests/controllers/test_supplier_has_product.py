import unittest
from tests.helpers.dbutil import *
from app.controllers.product_controller import ProductController
from generators.product_generator import ProductGenerator
from generators.contact_person_generator import ContactPersonGenerator
from app.controllers.supplier_controller import SupplierController
from generators.supplier_generator import SupplierGenerator
from shared.tests.test_printer import TestPrinter
from app.settings import Settings
Settings.TESTING = True


class ManufacturerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        create_db()
        ContactPersonGenerator.populate_database(amount=100)
        SupplierGenerator.populate_database(amount=1)
        ProductGenerator.populate_database(amount=2)
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        delete_db()
        TestPrinter.print_passed_tests()

    def test_add_product_to_supplier(self):
        product = ProductController.find_all()[0]
        product_two = ProductController.find_all()[1]
        supplier = SupplierController.find_all()[0]
        SupplierController.add_product_to_supplier(supplier, product)
        SupplierController.add_product_to_supplier(supplier, product_two)
        print('----- The two products are: -----')
        for suppliers_product in supplier.products:
            print(suppliers_product.product.name)
            self.assertIsNotNone(suppliers_product)
        TestPrinter.add(self.test_add_product_to_supplier.__name__)

    def test_remove_product_from_supplier(self):
        product = ProductController.find_all()[0]
        product_two = ProductController.find_all()[1]
        supplier = SupplierController.find_all()[0]
        SupplierController.add_product_to_supplier(supplier, product)
        SupplierController.add_product_to_supplier(supplier, product_two)
        SupplierController.remove_product_from_supplier(supplier, product)
        SupplierController.remove_product_from_supplier(supplier, product_two)
        for suppliers_product in supplier.products:
            self.assertIsNone(suppliers_product)
        TestPrinter.add(self.test_remove_product_from_supplier.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
