from __future__ import annotations
from app.settings import Settings

if Settings.TESTING:
    from tests._mongo.db import db
else:
    from app.data._mongo.db import db

from app.data._mongo.models import Document


class Store(Document):
    collection = db.stores
