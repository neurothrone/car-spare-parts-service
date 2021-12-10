from typing import Optional

from app.controllers import BaseController
from app.data.models.car import Car
from app.data.repositories.car_repository import CarRepository


class CarController(BaseController):
    repository = CarRepository
    required_attributes = {"reg_no", "color", "car_detail_id", "customer_id"}

    @classmethod
    def find_by_reg_no(cls, reg_no: str) -> Optional[Car]:
        return cls.repository.find_by_reg_no(reg_no)

    @classmethod
    def create_car(cls, reg_no: str, color: str,
                   car_detail_id: Optional[int] = None, customer_id: Optional[int] = None) -> None:
        CarRepository.create(reg_no=reg_no,
                             color=color,
                             car_detail_id=car_detail_id,
                             customer_id=customer_id)
