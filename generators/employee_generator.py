from app.controllers.employee_controller import EmployeeController
from generators.fake_data import FakeData
from shared.validators import validate_length


class EmployeeGenerator:
    FIRST_NAME_LEN = 45
    LAST_NAME_LEN = 45
    PHONE_MAX_LEN = 25
    EMAIL_MAX_LEN = 100

    @staticmethod
    def generate(first_name: str, last_name: str, phone: str, email: str,
                 store_id: int = None, commit: bool = True) -> None:
        validate_length(first_name, EmployeeGenerator.FIRST_NAME_LEN)
        validate_length(last_name, EmployeeGenerator.LAST_NAME_LEN)
        validate_length(phone, EmployeeGenerator.PHONE_MAX_LEN)
        validate_length(email, EmployeeGenerator.EMAIL_MAX_LEN)

        EmployeeController.create(
            first_name=first_name, last_name=last_name, phone=phone,
            email=email, store_id=store_id, commit=commit)


def create_employees():
    EmployeeGenerator.generate(
        first_name="John",
        last_name="Henry",
        phone="+64 072 113 46 92",
        email="john.henry@store.se",
        store_id=1
    )

    # EmployeeGenerator.generate(
    #     first_name="John",
    #     last_name="Henry",
    #     phone="+64 072 113 46 92",
    #     email="john.henry@store.se",
    #     store_id=1
    # )

    # EmployeeGenerator.generate(
    #     first_name="Mary",
    #     last_name="Washington",
    #     phone="+64 070 991 75 42",
    #     email="mary.washington@store.se",
    #     store_id=2
    # )


# TODO: step 1: models
# TODO: step 2: test that it works


def test_store_employee():
    employee = EmployeeController.find_by_id(1)
    print(employee)


def test_employee_customer():
    pass


def main():
    # test_store_employee()
    first_name, last_name = FakeData.generate_full_name().split(" ")
    # EmployeeGenerator.generate(
    #     first_name=first_name,
    #     last_name=last_name,
    #     phone=FakeData.generate_phone_number(),
    #     email=FakeData.generate_email(f"{first_name}.{last_name}")
    # )

    EmployeeGenerator.generate(
        first_name=first_name,
        last_name=last_name,
        phone=FakeData.generate_phone_number(),
        email=FakeData.generate_email(f"{first_name}.{last_name}"),
    )

    # create_employees()
    # EmployeeController.pprint_all()
    # test_store_employee()
    # test_employee_customer()


if __name__ == "__main__":
    main()
