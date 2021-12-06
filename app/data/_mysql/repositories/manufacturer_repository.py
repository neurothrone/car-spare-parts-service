from typing import Optional
from app.data._mysql.db import session
from app.data._mysql.models.manufacturer import Manufacturer
from app.data._mysql.models.product import Product
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository


class ManufacturerRepository(BaseRepository):
    model = Manufacturer

    @staticmethod
    def find_by_id(cls, _id: int) -> Optional[Manufacturer]:
        return session.query(cls.model).filter_by(manufacturer_id=_id).first()

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

    @staticmethod
    def has_product(manufacturer: Manufacturer, product: Product) -> bool:
        for mhp in manufacturer.products:
            if mhp.product.product_id == product.product_id:
                return True
        return False
