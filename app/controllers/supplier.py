from app.controllers import BaseController
from app.data.models.contact_person import ContactPerson
from app.data.models.supplier import Supplier
from app.data.repositories.supplier import SupplierRepository


class SupplierController(BaseController):
    model = Supplier

    @staticmethod
    def find_by_id(_id: int) -> Supplier:
        return SupplierRepository.find_by_id(_id)

    @staticmethod
    def add_contact_person(supplier: Supplier, contact_person: ContactPerson) -> None:
        SupplierRepository.add_contact_person(supplier, contact_person)

    @staticmethod
    def remove_contact_person(supplier: Supplier) -> None:
        SupplierRepository.remove_contact_person(supplier)
