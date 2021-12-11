from app.data._mongo.models.manufacturer import Manufacturer
from app.data._mongo.repositories import BaseRepository


class ManufacturerRepository(BaseRepository):
    model = Manufacturer
