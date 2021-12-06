from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.car_repository import CarRepository

else:
    from app.data._mysql.repositories.car_repository import CarRepository
