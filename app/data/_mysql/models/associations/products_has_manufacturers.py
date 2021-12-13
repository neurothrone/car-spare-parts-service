from sqlalchemy import Column, ForeignKey, Integer, Table

from app.data._mysql.db import Base

products_has_manufacturers = Table("products_has_manufacturers",
                                   Base.metadata,
                                   Column("product_id", Integer, ForeignKey("products.product_id"), primary_key=True),
                                   Column("manufacturer_id", Integer, ForeignKey("manufacturers.manufacturer_id"),
                                          primary_key=True))
