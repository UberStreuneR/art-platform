from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from platform_api.config import get_settings
from typing import Generator

engine = create_engine(get_settings().database_url, pool_pre_ping=True)


def create_session():
    Session = sessionmaker(bind=engine)
    return Session()


# dependency
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
