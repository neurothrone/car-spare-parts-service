from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.storage import Storage
else:
    from app.data._mysql.models.storage import Storage
