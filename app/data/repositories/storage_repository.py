from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.storage_repository import StorageRepository
else:
    from app.data._mysql.repositories.storage_repository import StorageRepository
