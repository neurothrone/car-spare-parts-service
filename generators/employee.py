from app.controllers.employee import EmployeeController
from app.data.models.employee import Employee
from shared.validators import validate_length


class EmployeeGenerator:
    FIRST_NAME_LEN = 45
    LAST_NAME_LEN = 45
    PHONE_MAX_LEN = 25
    EMAIL_MAX_LEN = 100

    @staticmethod
    def generate(first_name: str, last_name: str, phone: str, email: str, store_id: int) -> Employee:
        validate_length(first_name, EmployeeGenerator.FIRST_NAME_LEN)
        validate_length(last_name, EmployeeGenerator.LAST_NAME_LEN)
        validate_length(phone, EmployeeGenerator.PHONE_MAX_LEN)
        validate_length(email, EmployeeGenerator.EMAIL_MAX_LEN)

        return EmployeeController.create(
            first_name=first_name, last_name=last_name, phone=phone,
            email=email, store_id=store_id)


def main():
    # employee = EmployeeGenerator.generate(
    #     first_name="John",
    #     last_name="Henry",
    #     phone="+64 072 113 46 92",
    #     email="john.henry@store.se",
    #     store_id=1
    # )

    employee = EmployeeController.find_by_id(1)
    EmployeeController.pprint(employee)

    # EmployeeController.pprint_all()


if __name__ == "__main__":
    main()
