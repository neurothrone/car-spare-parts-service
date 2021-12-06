from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories import BaseRepository
else:
    from app.data._mysql.repositories import BaseRepository
