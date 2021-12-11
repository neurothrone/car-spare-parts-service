from __future__ import annotations
from app.controllers import BaseController
from app.data.models.contact_person import ContactPerson
from app.data.repositories.contact_person_repository import ContactPersonRepository
from typing import Optional


class ContactPersonController(BaseController):
    repository = ContactPersonRepository
    required_attributes = {"first_name", "last_name", "phone", "email"}

    @classmethod
    def create(cls, first_name: str, last_name: str, phone: str, email: str) -> None:
        cls.repository.create(first_name=first_name,
                              last_name=last_name,
                              phone=phone,
                              email=email)

    @classmethod
    def find_by_id(cls, _id: Optional[int | str]) -> Optional[ContactPerson]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def find_by_first_name(cls, first_name: str) -> Optional[ContactPerson]:
        return cls.repository.find_by_first_name(first_name)

    @classmethod
    def find_by_last_name(cls, last_name: str) -> Optional[ContactPerson]:
        return cls.repository.find_by_last_name(last_name)

    @classmethod
    def find_by_phone(cls, phone: str) -> Optional[ContactPerson]:
        return cls.repository.find_by_phone(phone)

    @classmethod
    def find_by_email(cls, email: str) -> Optional[ContactPerson]:
        return cls.repository.find_by_email(email)
