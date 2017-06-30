from sqlalchemy import (
    Column,
    String,
    Integer,
)

from .meta import Base


class Entry(Base):
    """."""

    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    title = Column(String(convert_unicode=True))
    body = Column(String(convert_unicode=True))
    creation_date = Column(String(convert_unicode=True))
    edit_date = Column(String(convert_unicode=True))

#  https://stackoverflow.com/questions/5735242/proper-way-to-insert-strings-to-a-sqlalchemy-unicode-column
#  for  2/3 model creation compatibilty without warnings
