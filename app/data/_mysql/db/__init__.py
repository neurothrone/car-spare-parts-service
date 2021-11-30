from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import Config

engine = create_engine(url=Config.get_base_config())


Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
