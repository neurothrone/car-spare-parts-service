from app.controllers.contact_person import ContactPersonController
from app.controllers.supplier import SupplierController
from app.data.models.contact_person import ContactPerson
from shared.validators import validate_length


class ContactPersonGenerator:
    COMPANY_NAME_MAX_LEN = 45
    FIRST_NAME_MAX_LEN = 45
    LAST_NAME_MAX_LEN = 45
    PHONE_MAX_LEN = 25
    EMAIL_MAX_LEN = 100

    @staticmethod
    def generate(first_name: str, last_name: str, phone: str, email: str) -> ContactPerson:
        validate_length(provided=first_name, limit=ContactPersonGenerator.FIRST_NAME_MAX_LEN)
        validate_length(provided=last_name, limit=ContactPersonGenerator.LAST_NAME_MAX_LEN)
        validate_length(provided=phone, limit=ContactPersonGenerator.PHONE_MAX_LEN)
        validate_length(provided=email, limit=ContactPersonGenerator.EMAIL_MAX_LEN)

        return ContactPersonController.create(
            first_name=first_name, last_name=last_name,
            phone=phone, email=email)


def main():
    # cp = ContactPersonGenerator.generate(
    #     first_name="Mary",
    #     last_name="Pattersson",
    #     phone="+64 70 772 23 23",
    #     email="contact_person@supply_parts.se"
    # )

    cp = ContactPersonController.find_by_id(2)
    supplier = SupplierController.find_by_id(3)
    # print(supplier)

    print(cp.supplier)
    print(f"Supplier, cp id: {supplier.contact_person_id}")

    # setup contact person and supplier
    # cp.supplier = supplier
    # supplier.contact_person_id = cp.contact_person_id
    # session.commit()

    # print(cp.supplier is not None)
    # print(supplier.contact_person_id is not None)

    # ContactPersonController.pprint_all()


if __name__ == "__main__":
    main()
