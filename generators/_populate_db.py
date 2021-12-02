from app.controllers.employee_controller import EmployeeController
from generators.employee_generator import EmployeeGenerator
from generators.store_generator import StoreGenerator


def populate_db():
    StoreGenerator.populate_database(amount=100)
    StoreGenerator.generate_online_store()
    EmployeeGenerator.populate_database(amount=100)


def main():
    # EmployeeController.connect_employees_to_stores(min_=1, max_=3)
    EmployeeController.reset_all_employees_store()


if __name__ == "__main__":
    main()
