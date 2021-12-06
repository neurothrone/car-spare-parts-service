from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.store_repository import StoreRepository
else:
    from app.data._mysql.repositories.store_repository import StoreRepository
