from typing import Optional, Union

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.car_detail import CarDetail


class CarDetailRepository(BaseRepository):
    model = CarDetail

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[CarDetail]:
        return session.query(cls.model).filter_by(car_detail_id=_id).first()

    @classmethod
    def find_by_brand(cls, brand: str, many: bool = False) -> Optional[Union[CarDetail, list[CarDetail]]]:
        if many:
            return session.query(cls.model).filter_by(brand=brand)
        return session.query(cls.model).filter_by(brand=brand).first()

    @classmethod
    def find_by_model(cls, model: str, many: bool = False) -> Optional[Union[CarDetail, list[CarDetail]]]:
        if many:
            return session.query(cls.model).filter_by(model=model)
        return session.query(cls.model).filter_by(model=model).first()

    @classmethod
    def find_by_year(cls, year: str, many: bool = False) -> Optional[Union[CarDetail, list[CarDetail]]]:
        if many:
            return session.query(cls.model).filter_by(year=year)
        return session.query(cls.model).filter_by(year=year).first()
