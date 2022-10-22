from sqlalchemy.orm import Session
from platform_api.db.models import User

def test_session(db: Session):
    pass

def test_user(user: User):
    assert user.username == "Nightwish"
    assert user.user_id == 1