from app.data._mongo.db import db
from app.data._mongo.models import BaseDocument


class Manufacturer(BaseDocument['Manufacturer']):
    collection = db.manufacturers
