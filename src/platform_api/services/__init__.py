from .user import UserService
from fastapi import Depends
from platform_api.db.session import get_session


def get_user_service(session=Depends(get_session)) -> UserService:
    return UserService(session)
