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
    title = Column(String(convert_unicode=True))
    body = Column(String(convert_unicode=True))
    creation_date = Column(String(convert_unicode=True))
    edit_date = Column(String(convert_unicode=True))
