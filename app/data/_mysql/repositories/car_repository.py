from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.car import Car


class CarRepository(BaseRepository):
    @staticmethod
    def find_by_reg_no(reg_no: str) -> Car:
        return session.query(Car).filter_by(reg_no=reg_no).first()
