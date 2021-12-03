from typing import Generic, TypeVar

from app.data._mysql.db import Base, Config

T = TypeVar("T", bound="BaseModel")


class BaseModel(Base, Generic[T]):
    __abstract__ = True

    # __table_args__ = {"schema": Config.DB_NAME}

    def __repr__(self) -> str:
        attributes = ", ".join(f"{k}={v}" for k, v in self.to_dict().items())
        return f"{self.__class__.__name__}({attributes})"

    def __str__(self) -> str:
        attributes = "\n".join(f"\t{k}: {v}" for k, v in self.to_dict().items())
        return f"{self.__class__.__name__}:\n{attributes}"

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if k != "_sa_instance_state"}


from app.data._mysql.models.store import Store
from app.data._mysql.models.customer import Customer
from app.data._mysql.models.employee import Employee
from app.data._mysql.models.product import Product
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.models.contact_person import ContactPerson
from app.data._mysql.models.manufacturer import Manufacturer
from app.data._mysql.models.associations.store_has_product import StoreHasProduct
from app.data._mysql.models.associations.store_has_supplier import StoreHasSupplier
from app.data._mysql.models.associations.product_has_manufacturer import ProductHasManufacturer
from app.data._mysql.models.associations.product_has_supplier import ProductHasSupplier
