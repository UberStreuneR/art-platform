from platform_api.db.models import User
from platform_api.db.session import create_session
from platform_api.routers.auth import pwd_context
users = [
    {
        "username": "Nightwish",
        "password": "topsecret"
    }
]


def hashed_user(user):
    user.update({"hashed_password": pwd_context.hash(user['password'])})
    del user['password']
    return user


def insert_mock_data(session):
    user_rows = [User(**hashed_user(user)) for user in users]
    session.add_all(user_rows)
    session.commit()


if __name__ == '__main__':
    session = create_session()
    insert_mock_data(session)
