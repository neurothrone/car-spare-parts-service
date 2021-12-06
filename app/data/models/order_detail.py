from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.order_detail import OrderDetail
else:
    from app.data._mysql.models.order_detail import OrderDetail
