# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer,ForeignKey,Table

#Intermediate table
persons_reservations = Table(
    'persons_reservations',
    Base.metadata,
    Column('idPersons', Integer, ForeignKey('persons.id'), primary_key=True),
    Column('idReservations', Integer, ForeignKey('reservations.id'), primary_key=True),
)
