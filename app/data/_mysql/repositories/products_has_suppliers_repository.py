from app.data._mysql.models.product import Product
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.supplier_repository import SupplierRepository


class ProductsHasSuppliersRepository(BaseRepository):
    model = NotImplemented

    @classmethod
    def add_product_to_supplier(cls, supplier: Supplier, product: Product) -> None:
        if cls.has_product(product, supplier):
            return

        supplier.product.append(supplier)
        cls.save_many_to_db([product, supplier])

    @classmethod
    def remove_product_from_supplier(cls, supplier: Supplier, product: Product) -> None:
        if not cls.has_product(product, supplier):
            return

        supplier.product.remove(supplier)
        cls.save_many_to_db([product, supplier])

    @classmethod
    def has_product(cls, supplier: Supplier, product: Product) -> bool:
        if not supplier.products:
            return False

        for supplier_product in supplier.products:
            if supplier_product.product_id == product.product_id:
                return True
        return False
