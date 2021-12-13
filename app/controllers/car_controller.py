from typing import Optional
from app.data.models.car_detail import CarDetail
from app.controllers import BaseController
from app.data.models.car import Car
from app.data.repositories.car_repository import CarRepository
from app.data.models.customer import Customer


class CarController(BaseController):
    repository = CarRepository
    required_attributes = {"reg_no", "color", "car_detail_id", "customer_id"}

    @classmethod
    def create_car(cls, reg_no: str, color: str,
                   car_detail_id: Optional[int] = None, customer_id: Optional[int] = None) -> None:
        CarRepository.create(reg_no=reg_no,
                             color=color,
                             car_detail_id=car_detail_id,
                             customer_id=customer_id)

    @classmethod
    def find_by_reg_no(cls, reg_no: str) -> Optional[Car]:
        return cls.repository.find_by_reg_no(reg_no)

    @classmethod
    def find_by_color(cls, color: str) -> Optional[Car]:
        return cls.repository.find_by_color(color)

    @classmethod
    def add_car_detail_to_car(cls, car: Car, car_detail: CarDetail) -> None:
        cls.repository.add_car_detail_to_car(car, car_detail)

    @classmethod
    def remove_car_detail_from_car(cls, car: Car, car_detail: CarDetail) -> None:
        cls.repository.remove_car_detail_from_car(car, car_detail)

    @classmethod
    def add_customer_to_car(cls, car: Car, customer: Customer) -> None:
        cls.repository.add_car_detail_to_car(car, customer)

    @classmethod
    def remove_customer_from_car(cls, car: Car, customer: Customer) -> None:
        cls.repository.remove_car_detail_from_car(car, customer)
