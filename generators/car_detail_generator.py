from __future__ import annotations

from app.settings import Settings

Settings.TESTING = True

from app.controllers.car_detail_controller import CarDetailController
from generators.fake_data import FakeData
from shared.validators import validate_length


class CarDetailGenerator:
    BRAND_LEN = 45
    MODEL_LEN = 45
    YEAR_LEN = int

    @classmethod
    def generate(cls, brand: str, model: str, year: int) -> None:
        validate_length(provided=brand, limit=CarDetailGenerator.BRAND_LEN)
        validate_length(provided=model, limit=CarDetailGenerator.MODEL_LEN)

        CarDetailController.create(brand=brand, model=model, year=year)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        cars = FakeData.generate_cars(amount)

        for car in cars:
            cls.generate(brand=car.brand, model=car.model, year=car.year)

        print(f"----- {amount} Car models generated -----")


def main():
    CarDetailGenerator.populate_database(10)


if __name__ == "__main__":
    main()
