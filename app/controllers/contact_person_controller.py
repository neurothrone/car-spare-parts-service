from typing import Optional

from app.controllers import BaseController
from app.data.models.contact_person import ContactPerson
from app.data.repositories.contact_person_repository import ContactPersonRepository


class ContactPersonController(BaseController):
    repository = ContactPersonRepository
    required_attributes = {"first_name", "last_name", "phone", "email"}

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[ContactPerson]:
        return cls.repository.find_by_id(_id)
