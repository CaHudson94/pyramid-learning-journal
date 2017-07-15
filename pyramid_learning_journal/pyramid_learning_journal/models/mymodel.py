from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    creation_date = Column(String)
    edit_date = Column(String)
