from app.controllers import BaseController
from app.data.models.supplier import Supplier
from app.data.repositories.supplier import SupplierRepository


class SupplierController(BaseController):
    model = Supplier

    @staticmethod
    def find_by_id(_id: int) -> Supplier:
        return SupplierRepository.find_by_id(_id)
