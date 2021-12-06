from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.data._mysql.models import BaseModel


class ProductHasManufacturer(BaseModel):
    __tablename__ = "products_has_manufacturers"

    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.manufacturer_id"), primary_key=True)

    manufacturer = relationship("Manufacturer", back_populates="products")
    product = relationship("Product", back_populates="manufacturers")
