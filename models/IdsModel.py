# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class IdsModel(Base):

    __tablename__ = "ids"

    id = Column(Integer, primary_key = True)

    number = Column(Integer) # type: int
    img = Column(String, nullable=True, unique=False) # type: img

    # 2.One to One Bidirectional.INVERSE
    # classDiagram
    # Persons "1..1" --> "1..1" Ids
    
    idPersons = Column(Integer, ForeignKey('persons.id'), nullable=False)    
    persons = relationship('PersonsModel', back_populates='ids')
