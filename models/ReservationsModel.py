# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class ReservationsModel(Base):

    __tablename__ = "reservations"

    id = Column(Integer, primary_key = True)

    number = Column(Integer) # type: int

    # 3.Many to One Unidirectional
    # classDiagram
    # Reservations "0..*" --> "0..1" Tables
    
    tables = relationship('TablesModel', backref='reservations')
