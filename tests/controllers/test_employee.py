import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.controllers.employee_controller import EmployeeController
from app.controllers.store_controller import StoreController
from generators.employee_generator import EmployeeGenerator
from generators.store_generator import StoreGenerator
from shared.tests.test_printer import TestPrinter


class EmployeeControllerTestCase(unittest.TestCase):
    # region Setup & Cleanup

    def setUp(self) -> None:
        EmployeeController.delete_all()

    def tearDown(self) -> None:
        EmployeeController.delete_all()
        StoreController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    # endregion Setup & Cleanup

    # region Utility

    @classmethod
    def setup_employees_and_stores(cls) -> None:
        EmployeeGenerator.populate_database(amount=50)
        StoreGenerator.populate_database(amount=50)
        EmployeeController.connect_employees_to_stores(min_=1, max_=3)

    # endregion Utility

    # region Tests

    def test_find_by_id_found(self):
        EmployeeGenerator.populate_database(amount=1)
        employee = EmployeeController.find_all()[0]
        employee_id = employee._id if Settings.DATABASE == Database.MONGO else employee.employee_id
        employee = EmployeeController.find_by_id(employee_id)
        self.assertIsNotNone(employee)
        TestPrinter.add(self.test_find_by_id_found.__name__)

    def test_find_by_id_not_found(self):
        if Settings.DATABASE == Database.MONGO:
            employee = EmployeeController.find_by_id("61acd805a1dca9c019999999")
        else:
            employee = EmployeeController.find_by_id(9999)
        self.assertIsNone(employee)
        TestPrinter.add(self.test_find_by_id_not_found.__name__)

    def test_find_all_found(self):
        EmployeeGenerator.populate_database(amount=3)
        employees = EmployeeController.find_all()
        self.assertTrue(len(employees) >= 3)
        TestPrinter.add(self.test_find_all_found.__name__)

    def test_find_all_not_found(self):
        EmployeeController.delete_all()
        employees = EmployeeController.find_all()
        self.assertTrue(employees == [])
        TestPrinter.add(self.test_find_all_not_found.__name__)

    def test_delete_all_found(self):
        EmployeeGenerator.populate_database(amount=3)
        count_deleted = EmployeeController.delete_all()
        self.assertTrue(count_deleted >= 3)
        TestPrinter.add(self.test_delete_all_found.__name__)

    def test_delete_all_not_found(self):
        EmployeeController.delete_all()
        count_deleted = EmployeeController.delete_all()
        self.assertFalse(count_deleted > 0)
        TestPrinter.add(self.test_delete_all_not_found.__name__)

    def test_connect_employee_to_store(self):
        EmployeeGenerator.populate_database(amount=1)
        StoreGenerator.populate_database(amount=1, online=False)
        employee = EmployeeController.find_all()[0]
        store = StoreController.find_all()[0]
        EmployeeController.change_store(employee, store)

        if Settings.DATABASE == Database.MONGO:
            self.assertEqual(employee.store_id, store._id)
        else:
            self.assertEqual(employee.store_id, store.store_id)

    def test_connect_employee_to_store_fail(self):
        EmployeeGenerator.populate_database(amount=1)
        StoreGenerator.populate_database(amount=1, online=False)
        employee = EmployeeController.find_all()[0]
        store = StoreController.find_all()[0]

        if Settings.DATABASE == Database.MONGO:
            store._id = None
        else:
            store.store_id = 0

        with self.assertRaises(ValueError):
            EmployeeController.change_store(employee, store)

    def test_connect_employees_to_stores(self):
        self.setup_employees_and_stores()
        employees = EmployeeController.find_all()

        for employee in employees:
            self.assertIsNotNone(employee.store_id)

    def test_reset_all_employees(self):
        self.setup_employees_and_stores()
        EmployeeController.reset_all_employees_store()
        employees = EmployeeController.find_all()

        for employee in employees:
            self.assertIsNone(employee.store_id)

    # endregion Tests


def main():
    unittest.main()


if __name__ == "__main__":
    main()
