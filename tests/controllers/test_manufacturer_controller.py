import unittest
from tests.helpers.dbutil import *

from app.controllers.contact_person_controller import ContactPersonController
from app.settings import Database, Settings
from generators.contact_person_generator import ContactPersonGenerator

Settings.TESTING = True

# from tests.data import store_data, stores_data
from app.controllers.manufacturer_controller import ManufacturerController
from generators.manufacturer_generator import ManufacturerGenerator
from shared.tests.test_printer import TestPrinter


class ManufacturerControllerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass
        #ManufacturerController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        create_db()
        ContactPersonGenerator.populate_database(amount=100)
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        delete_db()
        TestPrinter.print_passed_tests()

    def test_find_by_id_found(self):
        ManufacturerGenerator.populate_database(amount=1)
        manufacturer_created = ManufacturerController.find_all()[0]

        if Settings.DATABASE == Database.MONGO:
            manufacturer = ManufacturerController.find_by_id(manufacturer_created._id)
        else:
            manufacturer = ManufacturerController.find_by_id(manufacturer_created.manufacturer_id)

        self.assertIsNotNone(manufacturer)
        TestPrinter.add(self.test_find_by_id_found.__name__)

    def test_find_by_id_not_found(self):
        if Settings.DATABASE == Database.MONGO:
            manufacturer = ManufacturerController.find_by_id("61acd805a1dca9c019999999")
        else:
            manufacturer = ManufacturerController.find_by_id(9999)

        self.assertIsNone(manufacturer)
        TestPrinter.add(self.test_find_by_id_not_found.__name__)

    def test_find_by_company_name(self):
        ManufacturerGenerator.populate_database(amount=1)
        manufacturer_created = ManufacturerController.find_by_company_name("AB Anderson")[0]
        manufacturer = ManufacturerController.find_by_company_name(manufacturer_created.company_name)
        self.assertIsNotNone(manufacturer)
        TestPrinter.add(self.test_find_by_company_name.__name__)

    def test_find_by_company_name_not_found(self):
        store = ManufacturerController.find_by_company_name("AB Anderson")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_company_name_not_found.__name__)

    def test_find_by_head_office_phone(self):
        ManufacturerGenerator.populate_database(amount=1)
        manufacturer_created = ManufacturerController.find_by_head_office_phone("076 234 56 78")[0]
        manufacturer = ManufacturerController.find_by_head_office_phone(manufacturer_created.head_office_phone)
        self.assertIsNotNone(manufacturer)
        TestPrinter.add(self.test_find_by_head_office_phone.__name__)

    def test_find_by_head_office_phone_not_found(self):
        store = ManufacturerController.find_by_head_office_phone("076 234 56 78")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_head_office_phone_not_found.__name__)

    def test_find_by_head_office_address(self):
        ManufacturerGenerator.populate_database(amount=1)
        manufacturer_created = ManufacturerController.find_by_head_office_address("Testtest 7")[0]
        manufacturer = ManufacturerController.find_by_head_office_address(manufacturer_created.head_office_address)
        self.assertIsNotNone(manufacturer)
        TestPrinter.add(self.test_find_by_head_office_address.__name__)

    def test_find_by_head_office_address_not_found(self):
        store = ManufacturerController.find_by_head_office_address("Testtest 7")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_head_office_address_not_found.__name__)

    def test_add_product_to_manufacturer(self):
        pass
        # ManufacturerController.add_product_to_manufacturer()
        # product = ManufacturerController.find_by_id()

    def test_remove_product_from_manufacturer(self):
        pass

    def test_find_all_found(self):
        ManufacturerGenerator.populate_database(amount=3)
        stores = ManufacturerController.find_all()
        self.assertIsNotNone(stores)
        TestPrinter.add(self.test_find_all_found.__name__)

    def test_find_all_not_found(self):
        ManufacturerController.delete_all()
        stores = ManufacturerController.find_all()
        self.assertTrue(stores == [])
        TestPrinter.add(self.test_find_all_not_found.__name__)

    def test_delete_all_found(self):
        ManufacturerGenerator.populate_database(amount=3)
        count_deleted = ManufacturerController.delete_all()
        self.assertTrue(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_found.__name__)

    def test_delete_all_not_found(self):
        ManufacturerController.delete_all()
        count_deleted = ManufacturerController.delete_all()
        self.assertFalse(count_deleted > 0)
        TestPrinter.add(self.test_delete_all_not_found.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
