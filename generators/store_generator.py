from app.controllers.product_controller import ProductController
from app.controllers.store_controller import StoreController
from app.controllers.supplier_controller import SupplierController
from app.data.models.store import StoreType
from generators.fake_data import FakeData
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
    def populate_database(cls, amount: int) -> None:
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


def test_store_fail():
    StoreController.create(store_type=StoreType.PHYSICAL,
                           phone="+64 70 722 88 88",
                           email="store@example.se")
    StoreController.create(store_type=StoreType.ONLINE,
                           phone="+64 70 722 88 88",
                           email="store@example.se",
                           address="Tarbergsgatan 25",
                           zip_code="172 41",
                           city="Karlstad")


def test_store_product():
    # TODO: retrieval
    store = StoreController.find_by_id(1)
    print(store)
    product = ProductController.find_by_id(1)

    # TODO: adding (with defaults and with custom)
    # StoreController.add_product_to_store(store, product)
    # StoreController.add_product_to_store(store,
    #                                      product,
    #                                      stock_number=19,
    #                                      critical_threshold=5,
    #                                      amount_automatic_order=15)

    # TODO: removing
    StoreController.remove_product_from_store(store, product)

    for shp in store.products:
        print(type(shp))
        print(f"\tStock number: {shp.stock_number}")
        print(f"\tCritical threshold: {shp.critical_threshold}")
        print(f"\tAutomatic amount: {shp.amount_automatic_order}")
        print(shp.product)
        print(shp.store)


def test_store_supplier():
    store = StoreController.find_by_id(1)

    print(store)
    print(store.suppliers)

    supplier = SupplierController.find_by_id(4)
    print(supplier)

    # StoreController.add_supplier_to_store(store, supplier)
    StoreController.remove_supplier_from_store(store, supplier)

    for supplier in store.suppliers:
        print(supplier)

    print(store)


def main():
    StoreGenerator.populate_database(amount=100)
    StoreGenerator.generate_online_store()

    # create_stores()
    # test_store_fail()
    # test_store_product()
    # test_store_supplier()


if __name__ == "__main__":
    main()
