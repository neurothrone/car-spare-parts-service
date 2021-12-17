from app.data._mongo.models.product import Product
from app.data._mongo.models.products_has_suppliers import ProductsHasSuppliers
from app.data._mongo.models.supplier import Supplier
from app.data._mongo.repositories import BaseRepository
from app.data._mongo.repositories.supplier_repository import SupplierRepository


class ProductsHasSuppliersRepository(BaseRepository):
    model = ProductsHasSuppliers

    @classmethod
    def has_product(cls, supplier: Supplier, product: Product) -> bool:
        for supplier_product in supplier.products:
            if supplier_product.product_id == product._id:
                return True
        return False

    @classmethod
    def add_product_to_supplier(cls, product: Product,
                                supplier: Supplier) -> None:
        if cls.has_product(product, supplier):
            return

        pass

    @classmethod
    def remove_product_from_supplier(cls, product: Product,
                                     supplier: Supplier) -> None:
        if cls.has_product(product, supplier):
            return

        if not supplier.products:
            return

        pass

    @classmethod
    def remove_all_products_from_all_suppliers(cls) -> None:
        suppliers = SupplierRepository.find_all()

        for supplier in suppliers:
            for products_has_suppliers in supplier.products:
                cls.remove_product_from_supplier(supplier, products_has_suppliers.product)
