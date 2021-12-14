from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.product_repository import ProductRepository as MongoProductRepository
from app.data._mongo.repositories.supplier_repository import SupplierRepository as MongoSupplierRepository
from app.data._mysql.repositories.products_has_suppliers_repository import ProductsHasSuppliersRepository as MysqlProductsHasSuppliersRepository


class ProductsHasSuppliersConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for supplier_product in MysqlProductsHasSuppliersRepository.find_all():
            supplier = MongoSupplierRepository.find(supplier_id=supplier_product.store_id)
            product = MongoProductRepository.find(product_id=supplier_product.product_id)

            supplier_as_dict = supplier.__dict__

            if not supplier_as_dict.get("products_has_supplier", None):
                supplier_as_dict["products_has_supplier"] = []

            has_product = False
            for supplier_product in supplier_as_dict["products_has_supplier"]:
                if supplier_product["product_id"] == product._id:
                    has_product = True
                    break

            if has_product:
                continue

            supplier_as_dict["products_has_supplier"].append({
                "product_id": product._id
            })

            supplier.replace_one({"_id": supplier._id}, supplier.__dict__)

        for product in MongoProductRepository.find_all():
            if hasattr(product, "product_id"):
                product.delete_field("product_id")

        for supplier in MongoSupplierRepository.find_all():
            supplier_as_dict = supplier.__dict__

            if supplier_as_dict.get("supplier_id", None):
                del supplier_as_dict["supplier_id"]
                supplier.replace_one({"_id": supplier._id}, supplier.__dict__)
