from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.car import Car


class CarRepository(BaseRepository):
    model = Car

    @classmethod
    def find_by_reg_no(cls, reg_no: str) -> Optional[Car]:
        return session.query(cls.model).filter_by(reg_no=reg_no).first()
