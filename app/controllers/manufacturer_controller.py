from __future__ import annotations
from typing import Optional

from app.controllers import BaseController
from app.data.models.manufacturer import Manufacturer
from app.data.models.product import Product
from app.data.models.contact_person import ContactPerson
from app.data.repositories.manufacturer_repository import ManufacturerRepository


class ManufacturerController(BaseController):
    repository = ManufacturerRepository
    required_attributes = {"company_name", "head_office_phone",
                           "head_office_address", "contact_person_id"}

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[Manufacturer]:
        return cls.repository.find_by_id(_id)

    # region Manufacturer-ContactPerson

    @classmethod
    def add_contact_person(cls, manufacturer: Manufacturer,
                           contact_person: ContactPerson) -> None:
        cls.repository.add_contact_person(manufacturer, contact_person)

    @classmethod
    def remove_contact_person(cls, manufacturer: Manufacturer) -> None:
        cls.repository.remove_contact_person(manufacturer)

    @classmethod
    def has_contact_person(cls, manufacturer: Manufacturer) -> bool:
        return manufacturer.contact_person_id is not None

    # endregion Manufacturer-ContactPerson

    # region Manufacturer-Product

    @classmethod
    def add_product_to_manufacturer(cls, manufacturer: Manufacturer,
                                    product: Product) -> None:
        cls.repository.add_product_to_manufacturer(manufacturer, product)

    @classmethod
    def remove_product_from_manufacturer(cls, manufacturer: Manufacturer,
                                         product: Product) -> None:
        cls.repository.remove_product_from_manufacturer(manufacturer, product)

    @classmethod
    def has_manufacturer(cls, contact_person: ContactPerson) -> bool:
        return contact_person.manufacturer is not None

    # endregion Manufacturer-Product
