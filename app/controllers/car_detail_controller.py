from typing import Optional

from app.controllers import BaseController
from app.data.models.car_detail import CarDetail
from app.data.repositories.car_detail_repository import CarDetailRepository


class CarDetailController(BaseController):
    repository = CarDetailRepository
    required_attributes = {"brand", "model", "year"}

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[CarDetail]:
        return CarDetailRepository.find_by_id(_id)

    @classmethod
    def create(cls, brand: str, model: str, year: str) -> None:
        CarDetailRepository.create(brand=brand, model=model, year=year)
