from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.products_has_suppliers_repository import ProductsHasSuppliersRepository
else:
    from app.data._mysql.repositories.products_has_suppliers_repository import ProductsHasSuppliersRepository
