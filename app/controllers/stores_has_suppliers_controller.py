from app.controllers import BaseController
from app.data.models.store import Store
from app.data.models.supplier import Supplier
from app.data.repositories.stores_has_suppliers_repository import StoresHasSuppliersRepository


class StoresHasSuppliersController(BaseController):
    repository = StoresHasSuppliersRepository

    @classmethod
    def add_supplier_to_store(cls, store: Store, supplier: Supplier) -> None:
        cls.repository.add_supplier_to_store(store, supplier)

    @classmethod
    def remove_supplier_from_store(cls, store: Store, supplier: Supplier) -> None:
        cls.repository.remove_supplier_from_store(store, supplier)

    @classmethod
    def remove_all_suppliers_from_all_stores(cls) -> None:
        cls.repository.remove_all_suppliers_from_all_stores()
