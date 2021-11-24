from app.controllers import BaseController
from app.data.models.car import Car, CarDetail
from app.data.repositories.car import CarRepository, CarDetailRepository


class CarController(BaseController):
    model = Car

    @staticmethod
    def find_by_reg_no(reg_no: str) -> Car:
        return CarRepository.find_by_reg_no(reg_no)


class CarDetailController(BaseController):
    model = CarDetail

    @staticmethod
    def find_by_id(_id: int) -> CarDetail:
        return CarDetailRepository.find_by_id(_id)
