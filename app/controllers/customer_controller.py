from app.controllers import BaseController
from app.data.models.customer import Customer
from app.data.repositories.customer_repository import CustomerRepository


class CustomerController(BaseController):
    model = Customer

    @staticmethod
    def find_by_id(_id: int) -> Customer:
        return CustomerRepository.find_by_id(_id)
