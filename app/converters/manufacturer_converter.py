from app.settings import Settings
from data._mongo.repositories.store_repository import StoreRepository

Settings.TESTING = True

from app.data._mongo.repositories.manufacturer_repository import ManufacturerRepository as MongoManufacturerRepository
from app.data._mysql.repositories.manufacturer_repository import ManufacturerRepository as MysqlManufacturerRepository
from app.data._mongo.repositories.contact_person_repository import ContactPersonRepository as MongoContactPersonRepository


class ManufacturerConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for manufacturer in MysqlManufacturerRepository.find_all():
            as_dict = manufacturer.__dict__
            as_dict = {key: value for key, value in as_dict.items() if value is not None}
            as_dict['contact_person_id'] = MongoContactPersonRepository.find(contact_person_id=manufacturer.contact_person_id)._id

            del as_dict["_sa_instance_state"]

            products = []
            for product in manufacturer.products:
                products.append({
                    "cost": float(product.cost),
                    "price": float(product.price),
                    "name": product.name,
                    "product_id": product.product_id
                })

            as_dict['products'] = products

            MongoManufacturerRepository.create(**as_dict)

        print('Manufacturer is Converted')


def main():
    ManufacturerConverter.convert_from_mysql_to_mongo()


if __name__ == '__main__':
    main()
