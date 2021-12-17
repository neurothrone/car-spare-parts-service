from app.data._mysql.models.product import Product
from app.data._mysql.models.associations.products_has_suppliers import products_has_suppliers
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.supplier_repository import SupplierRepository


class ProductsHasSuppliersRepository(BaseRepository):
    model = products_has_suppliers

    @classmethod
    def add_product_to_supplier(cls, supplier: Supplier, product: Product) -> None:
        if cls.has_product(product, supplier):
            return

        supplier_product = products_has_suppliers
        supplier_product.product = product

        supplier.products.append(supplier_product)
        cls.save_many_to_db([product, supplier])

    @classmethod
    def remove_product_from_supplier(cls, supplier: Supplier, product: Product) -> None:
        if not cls.has_product(product, supplier):
            return
        if not supplier.products:
            return

        for supplier_product in supplier.products:
            if supplier_product.product.product_id == product.product_id:
                cls.delete_from_db(supplier_product)
                return

    @classmethod
    def has_product(cls, supplier: Supplier, product: Product) -> bool:
        for supplier_product in supplier.products:
            if supplier_product.product_id == product.product_id:
                return True
        return False

    @classmethod
    def remove_all_products_from_all_suppliers(cls) -> None:
        suppliers = SupplierRepository.find_all()

        for supplier in suppliers:
            for supplier_product in supplier.products:
                cls.remove_product_from_supplier(supplier, supplier_product.product)
