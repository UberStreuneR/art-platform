import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

from platform_api.app import create_app
from platform_api.db.session import create_session
from platform_api.db.models import User, Base
from platform_api.services.user import UserService


@pytest.fixture()
def app_client() -> TestClient:
    app = create_app()
    return TestClient(app)


@pytest.fixture(scope="session")
def db() -> Session:
    session = create_session()
    engine = session.bind
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.bind = engine
    Base.metadata.drop_all()
    Base.metadata.create_all()
    return session


@pytest.fixture(scope="session")
def user(db: Session) -> User:
    new_user = User(
        username="Nightwish",
        hashed_password="fakepassword"
    )
    db.add(new_user)
    db.commit()
    return new_user


@pytest.fixture()
def user_service(db: Session) -> UserService:
    return UserService(db)
