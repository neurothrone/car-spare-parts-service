from app.controllers import BaseController
from app.data.models.store import Store
from app.data.models.supplier import Supplier
from app.data.repositories.store import StoreRepository


class StoreController(BaseController):
    model = Store

    @staticmethod
    def find_by_id(_id: int) -> Store:
        return StoreRepository.find_by_id(_id)

    @staticmethod
    def add_supplier_to_store(store: Store, supplier: Supplier) -> None:
        StoreRepository.add_supplier_to_store(store, supplier)

    @staticmethod
    def remove_supplier_from_store(store: Store, supplier: Supplier) -> None:
        StoreRepository.remove_supplier_from_store(store, supplier)
