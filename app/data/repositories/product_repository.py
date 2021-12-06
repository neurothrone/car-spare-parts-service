from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.product_repository import ProductRepository
else:
    from app.data._mysql.repositories.product_repository import ProductRepository

