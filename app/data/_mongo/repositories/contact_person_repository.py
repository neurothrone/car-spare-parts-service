from __future__ import annotations
from typing import Optional


from app.data._mongo.models.product import Product

from app.data._mongo.models.contact_person import ContactPerson
from app.data._mongo.repositories import BaseRepository


class ContactPersonRepository(BaseRepository):
    model = ContactPerson




