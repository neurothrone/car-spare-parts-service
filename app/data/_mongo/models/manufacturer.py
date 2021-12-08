from __future__ import annotations
from app.data._mongo.models import BaseDocument
from app.settings import Settings
if Settings.TESTING:
    from tests.mongo.db import db
else:
    from app.data._mongo.db import db


class Manufacturer(BaseDocument['Manufacturer']):
    collection = db.manufacturers
