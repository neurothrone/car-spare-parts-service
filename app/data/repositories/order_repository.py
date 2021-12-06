from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.order_repository import OrderRepository
else:
    from app.data._mysql.repositories.order_repository import OrderRepository
