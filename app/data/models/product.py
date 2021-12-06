from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.product import Product
else:
    from app.data._mysql.models.product import Product
