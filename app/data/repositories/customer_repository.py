from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.customer_repository import CustomerRepository
else:
    from app.data._mysql.repositories.customer_repository import CustomerRepository
