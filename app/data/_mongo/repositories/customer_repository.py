from app.data._mongo.models.customer import Customer
from app.data._mongo.repositories import BaseRepository


class CustomerRepository(BaseRepository):
    model = Customer
