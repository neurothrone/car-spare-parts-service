from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.supplier_repository import SupplierRepository as MongoSupplierRepository
from app.data._mysql.repositories.supplier_repository import SupplierRepository as MysqlSupplierRepository
from app.data._mongo.repositories.contact_person_repository import ContactPersonRepository as MongoContactPersonRepository


class SupplierConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for supplier in MysqlSupplierRepository.find_all():
            as_dict = supplier.__dict__
            as_dict = {key: value for key, value in as_dict.items() if value is not None}

            as_dict['contact_person_id'] = MongoContactPersonRepository.find(contact_person_id=supplier.contact_person_id)._id

            del as_dict["_sa_instance_state"]

            products = []
            for product in supplier.products:
                products.append({
                    "cost": float(product.cost),
                    "price": float(product.price),
                    "name": product.name,
                    "product_id": product.product_id
                })

            stores = []
            for store in supplier.stores:
                stores.append({
                    "store_id": store.store_id,
                    "phone": store.phone,
                    "address": store.address,
                    "store_type": store.store_type
                })

            as_dict['stores'] = stores

            MongoSupplierRepository.create(**as_dict)

        print('Supplier is Converted')


def main():
    SupplierConverter.convert_from_mysql_to_mongo()


if __name__ == '__main__':
    main()
