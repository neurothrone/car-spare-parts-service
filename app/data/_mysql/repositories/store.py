from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.store import Store


class StoreRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Store:
        return session.query(Store).filter_by(store_id=_id).first()
