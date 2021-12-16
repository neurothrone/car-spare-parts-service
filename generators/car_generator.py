from __future__ import annotations

from app.settings import Settings

Settings.TESTING = True

from app.controllers.car_controller import CarController
from app.controllers.car_detail_controller import CarDetailController
from generators.car_detail_generator import CarDetailGenerator
from generators.fake_data import FakeData
from shared.validators import validate_length


class CarGenerator:
    COLOR_LEN = 45

    @classmethod
    def generate(cls, reg_no: int | str, color: str, car_detail_id: int | str) -> None:
        validate_length(provided=color, limit=CarGenerator.COLOR_LEN)

        CarController.create(reg_no=reg_no, color=color, car_detail_id=car_detail_id)

    @classmethod
    def generate_cars(cls, amount: int) -> None:
        car_colors = FakeData.generate_15_color_names()
        reg_numbers = FakeData.generate_license_plates(amount)
        CarDetailGenerator.populate_database(amount)
        car_details = CarDetailController.find_all()[:amount]

        for reg_number, car_color, car_detail in zip(reg_numbers, car_colors, car_details):
            cls.generate(reg_number, car_color, car_detail.car_detail_id)

        print(f"----- {amount} Cars generated -----")

    @classmethod
    def all_cars_to_dict(cls) -> list[dict]:
        cars = []
        mysql_cars = CarController.find_all()
        for car in mysql_cars:
            car_detail = CarDetailController.find_by_id(car.car_detail_id)
            data = car.__dict__ | car_detail.__dict__
            del data["_sa_instance_state"]
            cars.append(data)
        return cars


def main():
    CarGenerator.generate_cars(amount=10)


if __name__ == "__main__":
    main()
