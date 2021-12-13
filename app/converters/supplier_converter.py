from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.supplier_repository import SupplierRepository as MongoSupplierRepository
from app.data._mysql.repositories.supplier_repository import SupplierRepository as MysqlSupplierRepository
from app.data._mongo.repositories.contact_person_repository import ContactPersonRepository as MongoContactPersonRepository


# class SupplierConverter:
#     @classmethod
def convert_from_mysql_to_mongo():
    for supplier in MysqlSupplierRepository.find_all():
        as_dict = supplier.__dict__
        del as_dict["_sa_instance_state"]
        as_dict = {key: value for key, value in as_dict.items() if value is not None}

        as_dict['contact_person_id'] = \
            MongoContactPersonRepository.find(contact_person_id=supplier.contact_person_id)._id
        print()
        MongoSupplierRepository.create(**as_dict)

def main():
    convert_from_mysql_to_mongo()


if __name__ == "__main__":
    main()
