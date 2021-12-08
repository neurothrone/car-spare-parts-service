from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.contact_person import ContactPerson
from app.data._mysql.models.manufacturer import Manufacturer
from app.data._mysql.models.product import Product
from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository


class ManufacturerRepository(BaseRepository):
    model = Manufacturer

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Manufacturer]:
        return session.query(cls.model).filter_by(manufacturer_id=_id).first()

    # region Manufacturer-ContactPerson

    @classmethod
    def add_contact_person(cls, manufacturer: Manufacturer, contact_person: ContactPerson) -> None:
        if cls.has_contact_person(manufacturer) or ManufacturerRepository.has_manufacturer(contact_person):
            return

        manufacturer.contact_person_id = contact_person.contact_person_id
        contact_person.manufacturer = manufacturer
        session.commit()

    @classmethod
    def remove_contact_person(cls, manufacturer: Manufacturer) -> None:
        if not cls.has_contact_person(manufacturer):
            return

        contact_person = ContactPersonRepository.find_by_id(manufacturer.contact_person_id)
        contact_person.manufacturer = None
        manufacturer.contact_person_id = None
        session.commit()

    @classmethod
    def has_contact_person(cls, manufacturer: Manufacturer) -> bool:
        return manufacturer.contact_person_id is not None

    @classmethod
    def has_manufacturer(cls, contact_person: ContactPerson) -> bool:
        return contact_person.manufacturer is not None

    # endregion Manufacturer-ContactPerson

    # region Manufacturer-Product

    @staticmethod
    def add_product_to_manufacturer(manufacturer: Manufacturer,
                                    product: Product) -> None:
        if ManufacturerRepository.has_product(manufacturer, product):
            return

        manufacturer.products.append(product)
        session.commit()

    @staticmethod
    def remove_product_from_manufacturer(manufacturer: Manufacturer,
                                         product: Product) -> None:
        if ManufacturerRepository.has_product(manufacturer, product):
            return

        manufacturer.products.remove(product)
        session.commit()

    @classmethod
    def has_product(cls, manufacturer: Manufacturer, product: Product) -> bool:
        for mhp in manufacturer.products:
            if mhp.product.product_id == product.product_id:
                return True
        return False

    # endregion Manufacturer-Product
