from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.product_repository import ProductRepository as MongoProductRepository
from app.data._mongo.repositories.store_repository import StoreRepository as MongoStoreRepository
from app.data._mysql.repositories.storage_repository import StorageRepository as MysqlStorageRepository


class StorageConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for storage in MysqlStorageRepository.find_all():
            store = MongoStoreRepository.find(store_id=storage.store_id)
            product = MongoProductRepository.find(product_id=storage.product_id)

            store_as_dict = store.__dict__

            if not store_as_dict.get("storage", None):
                store_as_dict["storage"] = []

            # if product already exists in storage, skip this iteration
            has_product = False
            for storage_product in store_as_dict["storage"]:
                if storage_product["product_id"] == product._id:
                    has_product = True
                    break

            if has_product:
                continue

            store_as_dict["storage"].append({
                "product_id": product._id,
                "amount_automatic_order": storage.amount_automatic_order,
                "critical_threshold": storage.critical_threshold,
                "stock_number": storage.stock_number
            })

            store.replace_one({"_id": store._id}, store.__dict__)

        # delete product_id mysql remnant
        for product in MongoProductRepository.find_all():
            if hasattr(product, "product_id"):
                product.delete_field("product_id")

        # delete store_id mysql remnant
        for store in MongoStoreRepository.find_all():
            store_as_dict = store.__dict__

            if store_as_dict.get("store_id", None):
                del store_as_dict["store_id"]
                store.replace_one({"_id": store._id}, store.__dict__)
