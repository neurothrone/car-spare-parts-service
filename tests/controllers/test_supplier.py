import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.controllers.supplier_controller import SupplierController
from generators.contact_person_generator import ContactPersonGenerator
from generators.supplier_generator import SupplierGenerator
from shared.tests.test_printer import TestPrinter


class SupplierTestCase(unittest.TestCase):

    def setUp(self) -> None:
        SupplierController.delete_all()

    def tearDown(self) -> None:
        SupplierController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        ContactPersonGenerator.populate_database(amount=100)
        SupplierGenerator.populate_database(amount=1)
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    def test_find_by_id_found(self):
        SupplierGenerator.populate_database(amount=5)
        supplier_created = SupplierController.find_all()[0]

        if Settings.DATABASE == Database.MONGO:
            supplier = SupplierController.find_by_id(supplier_created._id)
        else:
            supplier = SupplierController.find_by_id(supplier_created.supplier_id)

        self.assertIsNotNone(supplier)
        TestPrinter.add(self.test_find_by_id_found.__name__)

    def test_find_by_id_not_found(self):
        if Settings.DATABASE == Database.MONGO:
            supplier = SupplierController.find_by_id("61acd805a1dca9c019999999")
        else:
            supplier = SupplierController.find_by_id(9999)

        self.assertIsNone(supplier)
        TestPrinter.add(self.test_find_by_id_not_found.__name__)

    def test_find_by_company_name(self):
        SupplierGenerator.populate_database(amount=1)
        supplier_created = SupplierController.find_all()[0]
        supplier = SupplierController.find_by_company_name(supplier_created.company_name)
        self.assertIsNotNone(supplier)
        TestPrinter.add(self.test_find_by_company_name.__name__)

    def test_find_by_company_name_not_found(self):
        supplier = SupplierController.find_by_company_name("DO THIS SHIT")

        self.assertIsNone(supplier)
        TestPrinter.add(self.test_find_by_company_name_not_found.__name__)

    def test_find_by_head_office_phone(self):
        SupplierGenerator.populate_database(amount=1)
        supplier_created = SupplierController.find_all()[0]
        supplier = SupplierController.find_by_head_office_phone(supplier_created.head_office_phone)

        self.assertIsNotNone(supplier)
        TestPrinter.add(self.test_find_by_head_office_phone.__name__)

    def test_find_by_head_office_phone_not_found(self):
        supplier = SupplierController.find_by_head_office_phone('070 00 93 71 35 25')

        self.assertIsNone(supplier)
        TestPrinter.add(self.test_find_by_head_office_phone_not_found.__name__)

    def test_find_by_head_office_address(self):
        SupplierGenerator.populate_database(amount=1)
        supplier_created = SupplierController.find_all()[0]
        supplier = SupplierController.find_by_head_office_address(supplier_created.head_office_address)

        self.assertIsNotNone(supplier)
        TestPrinter.add(self.test_find_by_head_office_address.__name__)

    def test_find_by_head_office_address_not_found(self):
        supplier = SupplierController.find_by_head_office_address('ALEBACKENVÄGENGATAN 7')

        self.assertIsNone(supplier)
        TestPrinter.add(self.test_find_by_head_office_address_not_found.__name__)

    def test_find_all_found(self):
        SupplierGenerator.populate_database(amount=3)
        suppliers = SupplierController.find_all()
        self.assertIsNotNone(suppliers)
        TestPrinter.add(self.test_find_all_found.__name__)

    def test_find_all_not_found(self):
        suppliers = SupplierController.find_all()
        self.assertTrue(len(suppliers) == 0)
        TestPrinter.add(self.test_find_all_not_found.__name__)

    def test_delete_all_found(self):
        SupplierGenerator.populate_database(amount=3)
        count_deleted = SupplierController.delete_all()
        self.assertTrue(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_found.__name__)

    def test_delete_all_not_found(self):
        count_deleted = SupplierController.delete_all()
        self.assertFalse(count_deleted > 0)
        TestPrinter.add(self.test_delete_all_not_found.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
