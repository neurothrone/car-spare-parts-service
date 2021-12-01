from app.controllers.manufacturer_controller import ManufacturerController
from app.data.models.manufacturer import Manufacturer
from shared.validators import validate_length


class ManufacturerGenerator:
    COMPANY_NAME_MAX_LEN = 45
    HEAD_OFFICE_PHONE_LEN = 25
    HEAD_OFFICE_ADDRESS_LEN = 100

    @staticmethod
    def generate(company_name: str, head_office_phone: str, head_office_address: str) -> Manufacturer:
        validate_length(provided=company_name, limit=ManufacturerGenerator.COMPANY_NAME_MAX_LEN)
        validate_length(provided=head_office_phone, limit=ManufacturerGenerator.HEAD_OFFICE_PHONE_LEN)
        validate_length(provided=head_office_address, limit=ManufacturerGenerator.HEAD_OFFICE_ADDRESS_LEN)

        return ManufacturerController.create(
            company_name=company_name, head_office_phone=head_office_phone,
            head_office_address=head_office_address)


def main():
    manufacturer = ManufacturerGenerator.generate(
        company_name="Supply Parts AB",
        head_office_phone="+64 73 944 71 23",
        head_office_address="Karbegsgatan 23, 173 43 Nattberg"
    )

    ManufacturerController.pprint(manufacturer)
    ManufacturerController.pprint_all()


if __name__ == "__main__":
    main()
