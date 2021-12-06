from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.store import Store
else:
    from app.data._mysql.models.store import Store
