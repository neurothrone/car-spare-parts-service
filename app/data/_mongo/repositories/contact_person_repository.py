from __future__ import annotations
from typing import Optional

from app.data._mongo.repositories import BaseRepository
from app.data._mongo.models.contact_person import ContactPerson


class ContactPersonRepository(BaseRepository):
    model = ContactPerson

    @classmethod
    def find_by_first_name(cls, first_name: str, many: bool = False) -> Optional[ContactPerson | list[ContactPerson]]:
        return cls.find(many=many, first_name=first_name)

    @classmethod
    def find_by_last_name(cls, last_name: str, many: bool = False) -> Optional[ContactPerson | list[ContactPerson]]:
        return cls.find(many=many, last_name=last_name)

    @classmethod
    def find_by_phone(cls, phone: str, many: bool = False) -> Optional[ContactPerson | list[ContactPerson]]:
        return cls.find(many=many, phone=phone)

    @classmethod
    def find_by_email(cls, email: str, many: bool = False) -> Optional[ContactPerson | list[ContactPerson]]:
        return cls.find(many=many, email=email)
