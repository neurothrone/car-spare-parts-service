from generators.customer_generator import CustomerGenerator
from generators.employee_generator import EmployeeGenerator
from generators.product_generator import ProductGenerator
from generators.store_generator import StoreGenerator


def populate_db():
    StoreGenerator.populate_database(amount=100)
    EmployeeGenerator.populate_database(amount=100)
    CustomerGenerator.populate_database(amount=100)
    ProductGenerator.populate_database(amount=100)
    StoreGenerator.add_products_to_stores(min_per_store=1, max_per_store=5)


def main():
    # populate_db()
    # EmployeeController.connect_employees_to_stores(min_=1, max_=3)
    # EmployeeController.reset_all_employees_store()

    # StoreGenerator.populate_database(amount=100)
    # StoreGenerator.add_products_to_stores(min_per_store=1, max_per_store=5)
    StoreGenerator.print_products_in_stores()
    # StoreGenerator.remove_all_products_in_stores()


if __name__ == "__main__":
    main()
