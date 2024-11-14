# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship

class RestaurantsModel(Base):

    __tablename__ = "restaurants"

    id = Column(Integer, primary_key = True)

    name = Column(String(250), nullable=False, unique=True) # type: string

    # 4. One to Many Unidirectional
    # classDiagram
    # Restaurants "0..1" --> "0..*" Menus
    
    menus = relationship('MenusModel', backref='restaurants')

    # 5. One to Many Bidirectional
    # classDiagram
    # Restaurants "0..1" --> "0..*" Tables
    
    tables = relationship('TablesModel', back_populates='restaurants')
