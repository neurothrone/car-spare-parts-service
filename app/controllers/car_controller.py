from app.controllers import BaseController
from app.data.models.car import Car
from app.data.repositories.car_repository import CarRepository


class CarController(BaseController):
    model = Car

    @staticmethod
    def find_by_reg_no(reg_no: str) -> Car:
        return CarRepository.find_by_reg_no(reg_no)
