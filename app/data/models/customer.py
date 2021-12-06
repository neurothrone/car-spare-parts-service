from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.customer import Customer
else:
    from app.data._mysql.models.customer import Customer
