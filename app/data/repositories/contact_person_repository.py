from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories.contact_person_repository import ContactPersonRepository
else:
    from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository
