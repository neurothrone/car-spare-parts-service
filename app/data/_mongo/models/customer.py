from app.data._mongo.db import db
from app.data._mongo.models import BaseDocument


class Customer(BaseDocument["Customer"]):
    collection = db.customers
