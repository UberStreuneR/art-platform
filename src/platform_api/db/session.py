from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from platform_api.config import get_settings

engine = create_engine(get_settings().database_url, pool_pre_ping=True)

def create_session():
    Session = sessionmaker(bind=engine)
    return Session()