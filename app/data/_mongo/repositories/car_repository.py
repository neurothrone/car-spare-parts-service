from __future__ import annotations
from app.data._mongo.models.car import Car
from app.data._mongo.repositories import BaseRepository


class CarRepository(BaseRepository):
    model = Car
