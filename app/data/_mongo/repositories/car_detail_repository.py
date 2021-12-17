from __future__ import annotations
from app.data._mongo.models.car_detail import CarDetail
from app.data._mongo.repositories import BaseRepository


class CarDetailRepository(BaseRepository):
    model = CarDetail
