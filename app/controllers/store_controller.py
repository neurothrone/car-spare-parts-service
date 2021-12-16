from __future__ import annotations
from typing import Optional

from app.controllers import BaseController
from app.data.models.store import Store
from app.data.models.supplier import Supplier
from app.data.repositories.store_repository import StoreRepository
from shared.exc.store import (InvalidStoreTypeError, InvalidRequiredArgsError, OnlineStoreExistsError,
                              OnlineStoreInvalidArgsError, PhysicalStoreInvalidArgsError)
from shared.models.types import StoreType


class StoreController(BaseController):
    repository = StoreRepository
    required_attributes = {"store_type", "phone", "email", "address", "zip_code", "city"}

    # region Store

    @classmethod
    def create(cls, store_type: str, phone: str, email: str,
               address: str = None, zip_code: str = None, city: str = None) -> None:
        if store_type not in [StoreType.PHYSICAL, StoreType.ONLINE]:
            raise InvalidStoreTypeError("Store type can only be 'p' or 'o'.")

        for value in [store_type, phone, email]:
            if not value:
                raise InvalidRequiredArgsError("Store type, phone and email can not be None")

        if store_type == StoreType.ONLINE:
            for value in [address, zip_code, city]:
                if value:
                    raise OnlineStoreInvalidArgsError("An online store must not have an address, zip code or city")

            if cls.repository.find_by_store_type(store_type=StoreType.ONLINE):
                raise OnlineStoreExistsError("An online store exists already")

        if store_type == StoreType.PHYSICAL:
            for value in [address, zip_code, city]:
                if not value:
                    raise PhysicalStoreInvalidArgsError("A physical store must have an address, zip code or city")

        cls.repository.create(store_type=store_type, phone=phone,
                              email=email, address=address,
                              zip_code=zip_code, city=city)

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[Store]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def find_by_city(cls, city: str) -> Optional[Store]:
        return cls.repository.find_by_city(city)

    @classmethod
    def find_by_email(cls, email: str) -> Optional[Store]:
        return cls.repository.find_by_email(email)

    @classmethod
    def find_by_store_type(cls, store_type: str) -> Store:
        return cls.repository.find_by_store_type(store_type)

    @classmethod
    def find_all_by_store_type(cls, store_type: str) -> list[Store]:
        return cls.repository.find_by_store_type(store_type, many=True)

    # endregion Store

    # region Store-Supplier

    @classmethod
    def add_supplier_to_store(cls, store: Store, supplier: Supplier) -> None:
        cls.repository.add_supplier_to_store(store, supplier)

    @classmethod
    def remove_supplier_from_store(cls, store: Store, supplier: Supplier) -> None:
        cls.repository.remove_supplier_from_store(store, supplier)

    @classmethod
    def remove_all_suppliers_from_all_stores(cls) -> None:
        cls.repository.remove_all_suppliers_from_all_stores()

    # endregion Store-Supplier
