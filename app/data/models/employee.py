from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.employee import Employee
else:
    from app.data._mysql.models.employee import Employee
