from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.data._mysql.models import Base


class ProductHasSupplier(Base):
    __tablename__ = "products_has_suppliers"

    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"), primary_key=True)

    supplier = relationship("Supplier", back_populates="products")
    product = relationship("Product", back_populates="suppliers")
