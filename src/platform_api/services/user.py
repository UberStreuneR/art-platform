from typing import Optional
from platform_api.services.base import BaseService
from platform_api.db.models import User
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException


class UserService(BaseService[User]):
    def __init__(self, session: Session) -> None:
        super().__init__(User, session)

    def get_by_username(self, username: str) -> Optional[User]:
        db_obj = self.session.query(self.model).where(
            User.username == username).first()
        if db_obj is None:
            raise HTTPException(
                status_code=404, detail="User with such username was not found")
        return db_obj
