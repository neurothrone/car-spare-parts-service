from sqlalchemy import Column, ForeignKey, Integer, Table

from app.data._mysql.db import Base

stores_has_suppliers = Table("stores_has_suppliers",
                             Base.metadata,
                             Column("store_id", Integer, ForeignKey("stores.store_id")),
                             Column("supplier_id", Integer, ForeignKey("suppliers.supplier_id")))
