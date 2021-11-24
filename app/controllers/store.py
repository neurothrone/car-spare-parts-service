from app.controllers import BaseController
from app.data.models.store import Store
from app.data.repositories.store import StoreRepository


class StoreController(BaseController):
    model = Store

    @staticmethod
    def find_by_id(_id: int) -> Store:
        return StoreRepository.find_by_id(_id)
