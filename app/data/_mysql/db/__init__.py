from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, DeclarativeMeta, sessionmaker, Session

from app.config import MysqlConfig

engine = create_engine(url=MysqlConfig.base_config())

Base: DeclarativeMeta = declarative_base()
session_maker: sessionmaker = sessionmaker()
session_maker.configure(bind=engine)
session: Session = session_maker()
