from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.car_detail import CarDetail


class CarDetailRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> CarDetail:
        return session.query(CarDetail).filter_by(car_detail_id=_id).first()
