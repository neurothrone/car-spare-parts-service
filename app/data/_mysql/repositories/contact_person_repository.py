from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.contact_person import ContactPerson


class ContactPersonRepository(BaseRepository):
    model = ContactPerson

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[ContactPerson]:
        return session.query(cls.model).filter_by(contact_person_id=_id).first()
