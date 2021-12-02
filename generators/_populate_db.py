from app.controllers.employee_controller import EmployeeController
from generators.customer_generator import CustomerGenerator
from generators.employee_generator import EmployeeGenerator
from generators.product_generator import ProductGenerator
from generators.store_generator import StoreGenerator


def populate_db():
    StoreGenerator.populate_database(amount=100)
    EmployeeGenerator.populate_database(amount=100)
    CustomerGenerator.populate_database(amount=100)
    ProductGenerator.populate_database(amount=100)


def main():
    # populate_db()
    EmployeeController.connect_employees_to_stores(min_=1, max_=3)
    # EmployeeController.reset_all_employees_store()


if __name__ == "__main__":
    main()
