from app.controllers.contact_person_controller import ContactPersonController
from app.controllers.supplier_controller import SupplierController
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


def test_supplier_contact_person():
    contact_person = ContactPersonController.find_by_id(2)
    supplier = SupplierController.find_by_id(3)

    print(contact_person)
    print(supplier)

    print()
    print(contact_person.supplier)
    print(f"Supplier, contact_person_id: {supplier.contact_person_id}")

    SupplierController.add_contact_person(supplier, contact_person)
    # SupplierController.remove_contact_person(supplier)

    print()
    print(contact_person.supplier)
    print(f"Supplier, contact_person_id: {supplier.contact_person_id}")


def main():
    # cp = ContactPersonGenerator.generate(
    #     first_name="Mary",
    #     last_name="Pattersson",
    #     phone="+64 70 772 23 23",
    #     email="contact_person@supply_parts.se"
    # )

    test_supplier_contact_person()


if __name__ == "__main__":
    main()
