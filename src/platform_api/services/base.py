from typing import Type, TypeVar, Generic, Optional
from platform_api.db.models import Base
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

ModelType = TypeVar("ModelType", bound=Base)


class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: Session) -> None:
        self.model = model
        self.session = session

    def get(self, id: int) -> Optional[ModelType]:
        db_obj = self.session.query(self.model).get(id)
        if db_obj is None:
            raise HTTPException(status_code=404, detail="Not found")
        return db_obj
