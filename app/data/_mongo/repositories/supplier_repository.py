from app.data._mongo.models.supplier import Supplier
from app.data._mongo.repositories import BaseRepository


class SupplierRepository(BaseRepository):
    model = Supplier
