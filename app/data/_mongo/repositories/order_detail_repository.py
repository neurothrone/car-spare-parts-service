from __future__ import annotations
from app.data._mongo.repositories import BaseRepository
from app.data._mongo.models.order_detail import OrderDetail


class OrderDetailRepository(BaseRepository):
    model = OrderDetail
