from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.data._mysql.models import Base


class ProductHasManufacturer(Base):
    __tablename__ = "products_has_manufacturers"

    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.manufacturer_id"), primary_key=True)

    manufacturer = relationship("ManuFacturer", back_populates="manufacturers")
    product = relationship("Product", back_populates="suppliers")
