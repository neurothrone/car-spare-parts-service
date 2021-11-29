from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.manufacturer import Manufacturer


class ManufacturerRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Manufacturer:
        return session.query(Manufacturer).filter_by(manufacturer_id=_id).first()
