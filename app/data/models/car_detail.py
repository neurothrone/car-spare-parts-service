from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.car_detail import CarDetail
else:
    from app.data._mysql.models.car_detail import CarDetail

