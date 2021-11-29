from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.product import Product


class ProductRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Product:
        return session.query(Product).filter_by(product_id=_id).first()
