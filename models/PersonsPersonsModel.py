# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer,ForeignKey,Table

#Intermediate table
persons_persons = Table(
    'persons_persons',
    Base.metadata,
    Column('id1Persons', Integer, ForeignKey('persons.id'), primary_key=True),
    Column('id2Persons', Integer, ForeignKey('persons.id'), primary_key=True),
)
