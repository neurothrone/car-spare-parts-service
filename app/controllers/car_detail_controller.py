from __future__ import annotations
from typing import Optional

from app.controllers import BaseController
from app.data.models.car_detail import CarDetail
from app.data.repositories.car_detail_repository import CarDetailRepository


class CarDetailController(BaseController):
    repository = CarDetailRepository
    required_attributes = {"brand", "model", "year"}

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[CarDetail]:
        return CarDetailRepository.find_by_id(_id)
