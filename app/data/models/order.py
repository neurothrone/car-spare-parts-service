from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.order import Order
else:
    from app.data._mysql.models.order import Order
