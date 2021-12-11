from app.data._mongo.db import db
from app.data._mongo.models import BaseDocument


class Supplier(BaseDocument["Supplier"]):
    collection = db.suppliers
