from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.car_detail_repository import CarDetailRepository
else:
    from app.data._mysql.repositories.car_detail_repository import CarDetailRepository
