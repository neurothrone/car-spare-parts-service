from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.supplier import Supplier


class SupplierRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Supplier:
        return session.query(Supplier).filter_by(supplier_id=_id).first()
