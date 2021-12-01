from app.data._mysql.db import session
from app.data._mysql.models import ContactPerson
from app.data._mysql.models.manufacturer import Manufacturer
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository


class ManufacturerRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Manufacturer:
        return session.query(Manufacturer).filter_by(manufacturer_id=_id).first()

    @staticmethod
    def add_contact_person(manufacturer: Manufacturer, contact_person: ContactPerson) -> None:
        if ManufacturerRepository.has_contact_person(manufacturer) or ManufacturerRepository.has_supplier(contact_person):
            return

        manufacturer.contact_person_id = contact_person.contact_person_id
        contact_person.manufacturer = manufacturer
        session.commit()

    @staticmethod
    def remove_contact_person(manufacturer: Manufacturer) -> None:
        if not ManufacturerRepository.has_contact_person(manufacturer):
            return

        contact_person = ContactPersonRepository.find_by_id(manufacturer.contact_person_id)
        contact_person.manufacturer = None
        manufacturer.contact_person_id = None
        session.commit()

    @staticmethod
    def has_contact_person(manufacturer: Manufacturer) -> bool:
        return manufacturer.contact_person_id is not None

    @staticmethod
    def has_supplier(contact_person: ContactPerson) -> bool:
        return contact_person.manufacturer is not None
