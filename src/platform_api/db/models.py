from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = sa.Column(sa.Integer, autoincrement=True, nullable=False, primary_key=True)
    username = sa.Column(sa.String, nullable=False, unique=True)