import unittest
from tests.helpers.dbutil import *
from app.controllers.product_controller import ProductController
from generators.product_generator import ProductGenerator
from generators.contact_person_generator import ContactPersonGenerator
from app.controllers.manufacturer_controller import ManufacturerController
from generators.manufacturer_generator import ManufacturerGenerator
from shared.tests.test_printer import TestPrinter
from app.settings import Settings
Settings.TESTING = True


class ManufacturerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        create_db()
        ContactPersonGenerator.populate_database(amount=100)
        ManufacturerGenerator.populate_database(amount=1)
        ProductGenerator.populate_database(amount=1)
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        delete_db()
        TestPrinter.print_passed_tests()

    def test_add_product_to_manufacturer(self):
        product = ProductController.find_all()[0]
        manufacturer = ManufacturerController.find_all()[0]
        ManufacturerController.add_product_to_manufacturer(manufacturer, product)
        for manufacturers_product in manufacturer.products:
            self.assertIsNotNone(manufacturers_product)
        TestPrinter.add(self.test_add_product_to_manufacturer.__name__)

    def test_remove_product_from_manufacturer(self):
        product = ProductController.find_all()[0]
        manufacturer = ManufacturerController.find_all()[0]
        ManufacturerController.add_product_to_manufacturer(manufacturer, product)
        ManufacturerController.remove_product_from_manufacturer(manufacturer, product)
        for manufacturers_product in manufacturer.products:
            self.assertIsNone(manufacturers_product)
        TestPrinter.add(self.test_remove_product_from_manufacturer.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
