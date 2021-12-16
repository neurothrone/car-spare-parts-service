from app.controllers.car_controller import CarController
from generators.car_generator import CarGenerator
from shared.tests.test_printer import TestPrinter
import unittest
from app.settings import Database, Settings
Settings.TESTING = True


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
            store = CarController.find_by_reg_no("61acd805a1dca9c019999999")
        else:
            store = CarController.find_by_reg_no("regno")
        self.assertIsNone(store)
        TestPrinter.add(self.test_find_by_reg_no_not_found.__name__)

    def test_find_by_color_not_found(self):
        brand = CarController.find_by_color("The gun")
        self.assertIsNone(brand)
        TestPrinter.add(self.test_find_by_color_not_found.__name__)


def main():

    if __name__ == '__main__':
        main()
