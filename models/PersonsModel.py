# https://docs.sqlalchemy.org/en/20/core/types.html
# https://docs.sqlalchemy.org/en/20/orm/relationships.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

from config.database import Base

from sqlalchemy import Column, Integer, String, Float,Text,TIMESTAMP,Date,DateTime,Boolean,BLOB,ForeignKey,Table
from sqlalchemy.orm import relationship
from .PersonsPersonsModel import persons_persons
from .PersonsReservationsModel import persons_reservations

class PersonsModel(Base):

    __tablename__ = "persons"

    id = Column(Integer, primary_key = True)

    firstName1 = Column(String(250), nullable=False, unique=False) # type: string
    firstName2 = Column(String(250), nullable=True, unique=False) # type: string
    lastName1 = Column(String(250), nullable=False, unique=False) # type: string
    lastName2 = Column(String(250), nullable=True, unique=False) # type: string
    comment = Column(Text, nullable=True, unique=False) # type: text
    age = Column(Integer) # type: int
    weight = Column(Float(14,2), nullable=True, unique=False) # type: float
    dateBirth = Column(TIMESTAMP, nullable=True, unique=False) # type: timestamp
    dateDeath = Column(Date, nullable=True, unique=False) # type: date
    timeBirth = Column(DateTime, nullable=True, unique=False) # type: time
    isAlive = Column(Boolean) # type: boolean
    email = Column(String, nullable=True, unique=False) # type: mail
    photo = Column(BLOB) # type: photo
    url = Column(String, nullable=True, unique=False) # type: url
    cv = Column(String, nullable=True, unique=False) # type: file
    fingerPrint = Column(BLOB, nullable=True, unique=False) # type: blob
    iris = Column(String, nullable=True, unique=False) # type: string

    # 1.One to One Unidirectional
    # classDiagram
    # Persons "0..1" --> "1..1" Addresses
    
    idAddresses = Column(Integer, ForeignKey('addresses.id'), nullable=True)    
    addresses = relationship('AddressesModel', uselist=False, backref='persons')

    # 2.One to One Bidirectional
    # classDiagram
    # Persons "1..1" --> "1..1" Ids
    
    idIds = Column(Integer, ForeignKey('ids.id'), nullable=False)    
    ids = relationship('IdsModel', back_populates='persons')

    # 7. Many to Many Bidirectional
    # classDiagram
    # Persons "0..*" --> "0..*" Persons
    
    # 7. Many to Many Bidirectional.INVERSE
    # classDiagram
    # Persons "0..*" --> "0..*" Persons
    
    persons = relationship('PersonsModel', secondary=persons_persons, back_populates='persons')

    # 6. Many to Many Unidirectional
    # classDiagram
    # Persons "0..*" --> "0..*" Reservations
    
    reservations = relationship('ReservationsModel', secondary=persons_reservations, back_populates='persons')
