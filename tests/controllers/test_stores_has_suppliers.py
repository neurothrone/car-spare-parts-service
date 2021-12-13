import unittest

from app.settings import Settings

Settings.TESTING = True

from app.controllers.store_controller import StoreController
from app.controllers.supplier_controller import SupplierController
from app.controllers.stores_has_suppliers_controller import StoresHasSuppliersController
from generators.store_generator import StoreGenerator
from generators.supplier_generator import SupplierGenerator
from shared.tests.test_printer import TestPrinter


class StoresHasSuppliersTestCase(unittest.TestCase):
    # region Setup & Cleanup

    def setUp(self) -> None:
        StoreGenerator.populate_database(amount=1, online=False)
        SupplierGenerator.populate_database(amount=1)

    def tearDown(self) -> None:
        StoresHasSuppliersController.remove_all_suppliers_from_all_stores()
        StoreController.delete_all()
        SupplierController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    # endregion Setup & Cleanup

    # region Tests

    def test_add_supplier_to_store(self):
        store = StoreController.find_all()[0]
        supplier = SupplierController.find_all()[0]
        StoresHasSuppliersController.add_supplier_to_store(store, supplier)

        for supplier in store.suppliers:
            self.assertIsNotNone(supplier)

        TestPrinter.add(self.test_add_supplier_to_store.__name__)

    def test_remove_supplier_from_store(self):
        store = StoreController.find_all()[0]
        supplier = SupplierController.find_all()[0]
        StoresHasSuppliersController.add_supplier_to_store(store, supplier)
        StoresHasSuppliersController.remove_supplier_from_store(store, supplier)

        self.assertListEqual(store.suppliers, [])

        TestPrinter.add(self.test_remove_supplier_from_store.__name__)

    # endregion Tests


def main():
    unittest.main()


if __name__ == "__main__":
    main()
