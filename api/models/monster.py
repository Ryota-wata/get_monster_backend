from sqlalchemy import Column, Integer, String
from api.db import Base


class Monster(Base):
    __tablename__ = "monsters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(15))