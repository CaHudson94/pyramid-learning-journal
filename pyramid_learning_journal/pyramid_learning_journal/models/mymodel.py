from sqlalchemy import (
    Column,
    Unicode,
    Integer,
    DateTime,
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(Unicode)
    edit_date = Column(Unicode)
