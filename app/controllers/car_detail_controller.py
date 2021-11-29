from app.controllers import BaseController
from app.data.models.car_detail import CarDetail
from app.data.repositories.car_detail_repository import CarDetailRepository


class CarDetailController(BaseController):
    model = CarDetail

    @staticmethod
    def find_by_id(_id: int) -> CarDetail:
        return CarDetailRepository.find_by_id(_id)
