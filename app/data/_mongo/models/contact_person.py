from app.data._mongo.db import db
from app.data._mongo.models import BaseDocument


class ContactPerson(BaseDocument['ContactPerson']):
    collection = db.contact_persons
