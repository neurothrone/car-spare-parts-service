from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.order_detail_repository import OrderDetailRepository

else:
    from app.data._mysql.repositories.order_detail_repository import OrderDetailRepository
