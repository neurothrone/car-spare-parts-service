from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.models.contact_person import ContactPerson
else:
    from app.data._mysql.models.contact_person import ContactPerson
