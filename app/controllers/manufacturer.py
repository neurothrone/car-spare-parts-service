from app.controllers import BaseController
from app.data.models.manufacturer import Manufacturer
from app.data.repositories.manufacturer import ManufacturerRepository


class ManufacturerController(BaseController):
    model = Manufacturer

    @staticmethod
    def find_by_id(_id: int) -> Manufacturer:
        return ManufacturerRepository.find_by_id(_id)
