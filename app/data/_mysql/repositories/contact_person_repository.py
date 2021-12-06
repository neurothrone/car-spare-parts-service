from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.contact_person import ContactPerson


class ContactPersonRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> ContactPerson:
        return session.query(ContactPerson).filter_by(contact_person_id=_id).first()

    @staticmethod
    def find_by_first_name(first_name: str) -> ContactPerson:
        return session.query(ContactPerson).filter_by(first_name=first_name).first()

    @staticmethod
    def find_by_last_name(last_name: str) -> ContactPerson:
        return session.query(ContactPerson).filter_by(last_name=last_name).first()
