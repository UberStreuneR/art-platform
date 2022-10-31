from sqlalchemy.orm import Session
from platform_api.db.models import User
from platform_api.services.user import UserService


def test_get_user(user: User, user_service: UserService):
    db_user = user_service.get(user.user_id)
    assert db_user.username == user.username
    assert db_user.user_id == user.user_id
    assert db_user.hashed_password == user.hashed_password
    

def test_get_user_by_usename(user: User, user_service: UserService):
    db_user = user_service.get_by_username(user.username)
    assert db_user.username == user.username
    assert db_user.user_id == user.user_id
    assert db_user.hashed_password == user.hashed_password