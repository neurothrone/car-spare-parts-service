from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.product import Product


class ProductRepository(BaseRepository):
    model = Product

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Product]:
        return session.query(cls.model).filter_by(product_id=_id).first()
