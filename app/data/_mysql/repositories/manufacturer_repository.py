from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.manufacturer import Manufacturer


class ManufacturerRepository(BaseRepository):
    model = Manufacturer

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Manufacturer]:
        return session.query(cls.model).filter_by(manufacturer_id=_id).first()
