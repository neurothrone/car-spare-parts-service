from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.contact_person import ContactPerson


class ContactPersonRepository(BaseRepository):
    model = ContactPerson

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[ContactPerson]:
        return session.query(cls.model).filter_by(contact_person_id=_id).first()

    @classmethod
    def find_by_first_name(cls, first_name: str) -> ContactPerson:
        return session.query(cls.model).filter_by(first_name=first_name).first()

    @classmethod
    def find_by_last_name(cls, last_name: str) -> ContactPerson:
        return session.query(cls.model).filter_by(last_name=last_name).first()
