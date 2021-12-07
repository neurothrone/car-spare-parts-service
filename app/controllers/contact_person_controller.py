from app.controllers import BaseController
from app.data.models.contact_person import ContactPerson
from app.data.repositories.contact_person_repository import ContactPersonRepository
from typing import Optional


class ContactPersonController(BaseController):
    model = ContactPerson

    @staticmethod
    def find_by_id(_id: int) -> Optional[ContactPerson]:
        return ContactPersonRepository.find_by_id(_id)

    @classmethod
    def create(cls, first_name: str, last_name: str, phone: str, email: str = None) -> None:
        ContactPersonRepository.create(first_name=first_name,
                                       last_name=last_name,
                                       phone=phone,
                                       email=email)
