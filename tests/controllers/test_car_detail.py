import unittest

from app.settings import Database, Settings

Settings.TESTING = True

from app.controllers.car_detail_controller import CarDetailController
from generators.car_detail_generator import CarDetailGenerator
from shared.tests.test_printer import TestPrinter


class CarDetailControllerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        CarDetailController.delete_all()

    def tearDown(self) -> None:
        CarDetailController.delete_all()

    @classmethod
    def setUpClass(cls) -> None:
        TestPrinter.reset()

    @classmethod
    def tearDownClass(cls) -> None:
        TestPrinter.print_passed_tests()

    def test_find_by_id_found(self):
        CarDetailGenerator.populate_database(amount=1)
        car_detail_created = CarDetailController.find_all()[0]

        if Settings.DATABASE == Database.MONGO:
            car_detail = CarDetailController.find_by_id(car_detail_created._id)
        else:
            car_detail = CarDetailController.find_by_id(car_detail_created.car_detail_id)

        self.assertIsNotNone(car_detail)
        TestPrinter.add(self.test_find_by_id_found.__name__)

    def test_find_by_id_not_found(self):
        if Settings.DATABASE == Database.MONGO:
            car_detail = CarDetailController.find_by_id("61acd805a1dca9c019999999")
        else:
            car_detail = CarDetailController.find_by_id(0)

        self.assertIsNone(car_detail)
        TestPrinter.add(self.test_find_by_id_not_found.__name__)

    def test_find_by_brand_found(self):
        CarDetailGenerator.populate_database(amount=1)
        car_detail_created = CarDetailController.find_all()[0]
        car_detail = CarDetailController.find_by_brand(car_detail_created.brand)

        self.assertIsNotNone(car_detail)
        TestPrinter.add(self.test_find_by_brand_found.__name__)

    def test_find_by_brand_not_found(self):
        car_detail = CarDetailController.find_by_brand("The Laser gun")
        self.assertIsNone(car_detail)
        TestPrinter.add(self.test_find_by_brand_not_found.__name__)

    def test_find_by_model_found(self):
        CarDetailGenerator.populate_database(amount=1)
        car_detail_created = CarDetailController.find_all()[0]
        car_detail = CarDetailController.find_by_model(car_detail_created.model)
        self.assertIsNotNone(car_detail)
        TestPrinter.add(self.test_find_by_brand_found.__name__)

    def test_find_by_model_not_found(self):
        car_detail = CarDetailController.find_by_model("Extra bacon")
        self.assertIsNone(car_detail)
        TestPrinter.add(self.test_find_by_model_not_found.__name__)

    def test_find_by_year_found(self):
        CarDetailGenerator.populate_database(amount=1)
        car_detail_created = CarDetailController.find_all()[0]
        car_detail = CarDetailController.find_by_year(car_detail_created.year)
        self.assertIsNotNone(car_detail)
        TestPrinter.add(self.test_find_by_brand_found.__name__)

    def test_find_by_year_not_found(self):
        car_detail = CarDetailController.find_by_year("Around 9000")
        self.assertIsNone(car_detail)
        TestPrinter.add(self.test_find_by_year_not_found.__name__)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
