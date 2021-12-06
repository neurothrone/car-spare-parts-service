from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.supplier_repository import SupplierRepository
else:
    from app.data._mysql.repositories.supplier_repository import SupplierRepository
