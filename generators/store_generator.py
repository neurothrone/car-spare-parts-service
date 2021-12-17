from app.settings import Settings
Settings.TESTING = True

from app.controllers.store_controller import StoreController
from generators.fake_data import FakeData
from shared.models.types import StoreType
from shared.validators import validate_length


class StoreGenerator:
    STORE_TYPE_MAX_LEN = 1
    PHONE_MAX_LEN = 25
    EMAIL_MAX_LEN = 100

    @classmethod
    def generate(cls, store_type: str, phone: str, email: str,
                 address: str = None, zip_code: str = None, city: str = None) -> None:
        validate_length(store_type, cls.STORE_TYPE_MAX_LEN)
        validate_length(phone, cls.PHONE_MAX_LEN)
        validate_length(email, cls.EMAIL_MAX_LEN)

        StoreController.create(
            store_type=store_type, phone=phone, email=email,
            address=address, zip_code=zip_code, city=city)

    @classmethod
    def generate_online_store(cls) -> None:
        cls.generate(store_type=StoreType.ONLINE,
                     phone=FakeData.generate_phone_number(),
                     email=FakeData.generate_email(username="web", domain_name="store"))

    @classmethod
    def populate_database(cls, amount: int, online: bool = True) -> None:
        stores_generated = amount

        if not StoreController.find_by_store_type(StoreType.ONLINE) and online:
            cls.generate_online_store()
            stores_generated += 1

        phone_numbers = FakeData.generate_phone_numbers(amount)
        locations = FakeData.generate_locations(amount)

        for i in range(amount):
            email = FakeData.generate_email(username=locations[i].address,
                                            domain_name="store",
                                            domain="se")
            cls.generate(store_type=StoreType.PHYSICAL,
                         phone=phone_numbers[i],
                         email=email.lower(),
                         address=f"{locations[i].address} {locations[i].street_no}",
                         zip_code=str(locations[i].zip_code),
                         city=locations[i].city)

        print(f"----- {stores_generated} Stores generated -----")


def main():
    StoreGenerator.populate_database(amount=20)


if __name__ == "__main__":
    main()
