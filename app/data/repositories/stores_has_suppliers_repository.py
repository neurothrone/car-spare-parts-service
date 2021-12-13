from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.stores_has_suppliers_repository import StoresHasSuppliersRepository
else:
    from app.data._mysql.repositories.stores_has_suppliers_repository import StoresHasSuppliersRepository
