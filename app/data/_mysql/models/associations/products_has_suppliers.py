from sqlalchemy import Column, ForeignKey, Integer, Table

from app.data._mysql.db import Base

products_has_suppliers = Table("products_has_suppliers",
                               Base.metadata,
                               Column("product_id", Integer, ForeignKey("products.product_id"), primary_key=True),
                               Column("supplier_id", Integer, ForeignKey("suppliers.supplier_id"), primary_key=True))
