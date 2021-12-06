from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.supplier import Supplier
else:
    from app.data._mysql.models.supplier import Supplier
