import datetime
from random import randint, uniform

from faker import Faker
from faker_vehicle import VehicleProvider
from faker.providers import DynamicProvider

product_provider = DynamicProvider(
    provider_name="product",
    elements=["battery", "steering-wheel", "tail-light", "head-light"]
)

product_description_list = [
    "test1", "test2", "test3", "test4"
]


class CarData:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self) -> str:
        return f"CarData(make={self.make}, model={self.model}, year={self.year}"

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"


class Location:
    def __init__(self, address: str, street_no: int, zip_code: int, city: str) -> None:
        self.address = address
        self.street_no = street_no
        self.zip_code = zip_code
        self.city = city

    def __repr__(self) -> str:
        return f"Location(address={self.address}, street_no={self.street_no}," \
               f" zip_code={self.zip_code}, city={self.city})"

    def __str__(self) -> str:
        return f"{self.address} {self.street_no}, {self.zip_code} {self.city}"


class ProductData:
    def __init__(self, name: str, description: str, cost: float, price: float) -> None:
        self.name = name
        self.description = description
        self.cost = cost
        self.price = price

    def __repr__(self) -> str:
        return f"ProductData(name={self.name}, description={self.description}," \
               f"cost={self.cost}, price={self.price})"

    def __str__(self) -> str:
        return f"{self.name}: {self.description}\ncost: {self.cost}, price: {self.price}"


class FakeData:
    _faker: Faker = Faker("sv_SE")
    _faker.add_provider(VehicleProvider)
    _faker.add_provider(product_provider)

    MIN_AGE = 18
    MAX_AGE = 72

    @classmethod
    def configure_locale(cls, locale: str) -> None:
        cls._faker = Faker(locale=locale)

    @staticmethod
    def generate_random_int(min_: int, max_: int) -> int:
        return randint(min_, max_)

    @staticmethod
    def generate_random_float(min_: float, max_: float,
                              scale: int = 2) -> float:
        return round(uniform(min_, max_), scale)

    @classmethod
    def generate_full_name(cls) -> str:
        return cls._faker.name()

    @classmethod
    def generate_full_names(cls, amount: int, unique: bool = True) -> list[str]:
        if unique:
            full_names_set = set()
            while len(full_names_set) < amount:
                full_names_set.add(cls._faker.name())
            return list(full_names_set)

        return [cls._faker.name() for _ in range(amount)]

    @classmethod
    def generate_phone_number(cls) -> str:
        return cls._faker.phone_number()

    @staticmethod
    def generate_phone_numbers(amount: int) -> list[str]:
        phones = set()
        while len(phones) < amount:
            phones.add(FakeData.generate_phone_number())
        return list(phones)

    @staticmethod
    def generate_email(username: str, domain_name: str = "example", domain: str = "se") -> str:
        return f"{username}@{domain_name}.{domain}"

    @classmethod
    def generate_emails(cls, full_names: list[str], amount: int,
                        domain_name: str = "example", domain: str = "se") -> list[str]:
        emails = list()
        if amount > len(full_names):
            raise ValueError("Amount needs to be equal to or less than the length of full_names.")
        for i in range(amount):
            first_name, last_name = full_names[i].split(" ")
            email = cls.generate_email(
                username=f"{first_name.lower()}.{last_name.lower()}",
                domain_name=domain_name,
                domain=domain
            )
            emails.append(email)
        return emails

    @classmethod
    def generate_location(cls) -> Location:
        lines = cls._faker.address().split("\n")
        address, street_no = lines[0].split(" ")
        zip_code, city = lines[1].split(" ")
        return Location(address=address, street_no=int(street_no), zip_code=int(zip_code), city=city)

    @classmethod
    def generate_locations(cls, amount: int) -> list[Location]:
        return [cls.generate_location() for _ in range(amount)]

    @classmethod
    def generate_license_plate(cls) -> str:
        return cls._faker.license_plate()

    @classmethod
    def generate_license_plates(cls, amount: int) -> list[str]:
        license_plates = set()
        while len(license_plates) < amount:
            license_plates.add(FakeData.generate_license_plate())
        return list(license_plates)

    @classmethod
    def generate_color_name(cls) -> str:
        return cls._faker.safe_color_name()

    @classmethod
    def generate_15_color_names(cls) -> list[str]:
        max_colors = 15
        colors = set()
        while len(colors) < max_colors:
            colors.add(FakeData.generate_color_name())
        return list(colors)

    @classmethod
    def generate_date(cls) -> datetime.date:
        return cls._faker.date_of_birth(minimum_age=FakeData.MIN_AGE, maximum_age=FakeData.MAX_AGE)

    @classmethod
    def generates_dates(cls, amount: int) -> list[datetime.date]:
        return [cls.generate_date() for _ in range(amount)]

    @classmethod
    def generate_car(cls) -> CarData:
        # .vehicle_object() generates a dict with capitalized keys
        # convert keys to lowercase before using them
        data = {key.lower(): value for (key, value) in cls._faker.vehicle_object().items() if key != "Category"}
        return CarData(**data)

    @classmethod
    def generate_cars(cls, amount: int) -> list[CarData]:
        return [cls.generate_car() for _ in range(amount)]

    @classmethod
    def generate_company(cls) -> str:
        return cls._faker.company()

    @classmethod
    def generate_companies(cls, amount: int) -> list[str]:
        companies = set()
        while len(companies) < amount:
            companies.add(FakeData.generate_company())
        return list(companies)

    @classmethod
    def generate_product_name(cls) -> str:
        return cls._faker.product().capitalize()

    @classmethod
    def generate_product_description(cls) -> str:
        return cls._faker.sentence(ext_word_list=product_description_list).capitalize()

    @classmethod
    def generate_product(cls, cost_scale: int = 1) -> ProductData:
        cost = FakeData.generate_random_float(10, 100, scale=cost_scale)
        price = round(cost * 1.25, cost_scale)
        return ProductData(
            name=FakeData.generate_product_name(),
            description=FakeData.generate_product_description(),
            cost=cost,
            price=price)


def print_sequence(sequence: list) -> None:
    for item in sequence:
        print(item)


def test_name_generation():
    full_names = FakeData.generate_full_names(500)
    print_sequence(full_names)


def test_email_generation():
    full_names = FakeData.generate_full_names(500)
    emails = FakeData.generate_emails(full_names, 500)
    print_sequence(emails)


def test_phone_generation():
    phone_numbers = FakeData.generate_phone_numbers(500)
    print_sequence(phone_numbers)


def test_address_generation():
    locations = FakeData.generate_locations(500)
    print_sequence(locations)


def test_reg_no_generation():
    # print(FakeData.generate_license_plate())
    license_plates = FakeData.generate_license_plates(500)
    print_sequence(license_plates)


def test_color_generation():
    # print(FakeData.generate_color_name())
    print_sequence(FakeData.generate_15_color_names())


def test_date_generation():
    # print(FakeData.generate_date())
    print_sequence(FakeData.generates_dates(500))


def test_car_generation():
    # print(FakeData.generate_car())
    print_sequence(FakeData.generate_cars(500))


def test_company_generation():
    # print(FakeData.generate_company())
    print_sequence(FakeData.generate_companies(500))


def test_product_name_generation():
    print(FakeData.generate_product_name())


def test_product_description_generation():
    print(FakeData.generate_product_description())


def test_product_generation():
    for _ in range(10):
        print(FakeData.generate_product())


def main():
    # test_name_generation()
    # test_email_generation()
    # test_phone_generation()
    # test_address_generation()
    # test_reg_no_generation()
    # test_color_generation()
    # test_date_generation()
    # test_car_generation()
    # test_company_generation()
    # test_product_name_generation()
    # test_product_description_generation()
    test_product_generation()


if __name__ == "__main__":
    main()
