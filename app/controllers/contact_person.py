from app.controllers import BaseController
from app.data.models.contact_person import ContactPerson
from app.data.repositories.contact_person import ContactPersonRepository


class ContactPersonController(BaseController):
    model = ContactPerson

    @staticmethod
    def find_by_id(_id: int) -> ContactPerson:
        return ContactPersonRepository.find_by_id(_id)
