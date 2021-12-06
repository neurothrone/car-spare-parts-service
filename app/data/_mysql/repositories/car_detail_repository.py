from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.car_detail import CarDetail


class CarDetailRepository(BaseRepository):
    model = CarDetail

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[CarDetail]:
        return session.query(cls.model).filter_by(car_detail_id=_id).first()
