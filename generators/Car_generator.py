from __future__ import annotations
from typing import Optional
from app.controllers.car_controller import CarController
from generators.fake_data import FakeData
from shared.validators import validate_length


class CarGenerator:
    COLOR_LEN = 45

    @classmethod
    def generate(cls, color: str, reg_no: Optional[int | str] = None) -> None:
        validate_length(provided=color, limit=CarGenerator.COLOR_LEN)
        CarController.create(color=color, reg_no=reg_no)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        car_plates = FakeData.generate_license_plates(amount)

        for car_plate in car_plates:

            cls.generate(car_plate)

        print(f"----- {amount} Cars generated -----")


def main():
    CarGenerator.populate_database(amount=10)


if __name__ == "__main__":
    main()
