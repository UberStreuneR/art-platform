from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = sa.Column(sa.Integer, autoincrement=True,
                        nullable=False, primary_key=True)
    username = sa.Column(sa.String, nullable=False, unique=True)
    hashed_password = sa.Column(sa.String, nullable=False)
    picture_path = sa.Column(sa.String(20), unique=True, default="image.png")
