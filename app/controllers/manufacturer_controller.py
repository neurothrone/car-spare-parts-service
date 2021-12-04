from app.controllers import BaseController
from app.data.models.manufacturer import Manufacturer
from app.data.repositories.manufacturer_repository import ManufacturerRepository
from app.data.models.contact_person import ContactPerson


class ManufacturerController(BaseController):
    model = Manufacturer

    @staticmethod
    def find_by_id(_id: int) -> Manufacturer:
        return ManufacturerRepository.find_by_id(_id)

    @staticmethod
    def add_contact_person(manufacturer: Manufacturer, contact_person: ContactPerson) -> None:
        ManufacturerRepository.add_contact_person(manufacturer, contact_person)

    @staticmethod
    def remove_contact_person(manufacturer: Manufacturer) -> None:
        ManufacturerRepository.remove_contact_person(manufacturer)
