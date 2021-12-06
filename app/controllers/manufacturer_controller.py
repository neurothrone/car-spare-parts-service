from typing import Optional

from app.controllers import BaseController
from app.data.models.manufacturer import Manufacturer
from app.data.repositories.manufacturer_repository import ManufacturerRepository


class ManufacturerController(BaseController):
    repository = ManufacturerRepository
    required_attributes = {"company_name", "head_office_phone",
                           "head_office_address", "contact_person_id"}

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Manufacturer]:
        return cls.repository.find_by_id(_id)
