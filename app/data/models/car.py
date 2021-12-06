from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.car import Car
else:
    from app.data._mysql.models.car import Car
