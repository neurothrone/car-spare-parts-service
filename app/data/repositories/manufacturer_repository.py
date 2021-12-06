from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.manufacturer_repository import ManufacturerRepository
else:
    from app.data._mysql.repositories.manufacturer_repository import ManufacturerRepository
