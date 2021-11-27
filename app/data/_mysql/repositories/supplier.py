from app.data._mysql.db import session
from app.data._mysql.models import ContactPerson
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.contact_person import ContactPersonRepository


class SupplierRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Supplier:
        return session.query(Supplier).filter_by(supplier_id=_id).first()

    @staticmethod
    def add_contact_person(supplier: Supplier, contact_person: ContactPerson,
                           remove_existing: bool = False) -> None:
        if remove_existing:
            SupplierRepository.remove_contact_person(supplier)

        supplier.contact_person_id = contact_person.contact_person_id
        contact_person.supplier = supplier
        session.commit()

    @staticmethod
    def remove_contact_person(supplier: Supplier) -> None:
        if not supplier.contact_person_id:
            raise ValueError("Supplier has no contact person.")

        contact_person = ContactPersonRepository.find_by_id(supplier.contact_person_id)
        contact_person.supplier = None
        supplier.contact_person_id = None
        session.commit()
