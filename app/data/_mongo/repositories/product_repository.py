from app.data._mongo.models.product import Product
from app.data._mongo.repositories import BaseRepository


class ProductRepository(BaseRepository):
    model = Product
