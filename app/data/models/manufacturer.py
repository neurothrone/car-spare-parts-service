from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.manufacturer import Manufacturer
else:
    from app.data._mysql.models.manufacturer import Manufacturer
