from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.models import ContactPerson
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository


class SupplierRepository(BaseRepository):
    model = Supplier

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Supplier]:
        return session.query(cls.model).filter_by(supplier_id=_id).first()

    @classmethod
    def add_contact_person(cls, supplier: Supplier, contact_person: ContactPerson) -> None:
        if cls.has_contact_person(supplier) or SupplierRepository.has_supplier(contact_person):
            return

        supplier.contact_person_id = contact_person.contact_person_id
        contact_person.supplier = supplier
        session.commit()

    @classmethod
    def remove_contact_person(cls, supplier: Supplier) -> None:
        if not cls.has_contact_person(supplier):
            return

        contact_person = ContactPersonRepository.find_by_id(supplier.contact_person_id)
        contact_person.supplier = None
        supplier.contact_person_id = None
        session.commit()

    @classmethod
    def has_contact_person(cls, supplier: Supplier) -> bool:
        return supplier.contact_person_id is not None

    @classmethod
    def has_supplier(cls, contact_person: ContactPerson) -> bool:
        return contact_person.supplier is not None
