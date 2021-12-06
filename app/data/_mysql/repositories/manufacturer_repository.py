from app.data._mysql.db import session
from app.data._mysql.models import ContactPerson
from app.data._mysql.models.manufacturer import Manufacturer
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository
from app.data._mysql.models.product import Product


class ManufacturerRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Manufacturer:
        return session.query(Manufacturer).filter_by(manufacturer_id=_id).first()

    @staticmethod
    def add_contact_person(manufacturer: Manufacturer, contact_person: ContactPerson) -> None:
        if ManufacturerRepository.has_contact_person(manufacturer):
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
    def add_product_to_supplier(manufacturer: Manufacturer,
                                product: Product) -> None:
        if ManufacturerRepository.has_product(manufacturer, product):
            return

        manufacturer.products.append(product)
        session.commit()

    @staticmethod
    def remove_product_from_supplier(supplier: Manufacturer,
                                     product: Product) -> None:
        if ManufacturerRepository.has_product(supplier, product):
            return

        supplier.products.remove(product)
        session.commit()

    @staticmethod
    def has_contact_person(manufacturer: Manufacturer) -> bool:
        return manufacturer.contact_person_id is not None

    @staticmethod
    def has_product(manufacturer: Manufacturer, product: Product) -> bool:
        for mhp in manufacturer.products:
            if mhp.product.product_id == product.product_id:
                return True
        return False
