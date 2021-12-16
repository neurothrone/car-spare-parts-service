import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.controllers.car_controller import CarController
from generators.car_generator import CarGenerator
from shared.tests.test_printer import TestPrinter


class CarDetailControllerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        CarController.delete_all()

    def tearDown(self) -> None:
        CarController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    def test_find_by_reg_no_not_found(self):
        if Settings.DATABASE == Database.MONGO:
            car = CarController.find_by_reg_no("61acd805a1dca9c019999999")
        else:
            car = CarController.find_by_reg_no("reg_no")
        self.assertIsNone(car)
        TestPrinter.add(self.test_find_by_reg_no_not_found.__name__)

    def test_find_by_color_not_found(self):
        car = CarController.find_by_color("One Color to Rule them all")
        self.assertIsNone(car)
        TestPrinter.add(self.test_find_by_color_not_found.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
