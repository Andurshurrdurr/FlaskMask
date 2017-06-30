import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Reading(Base):
    __tablename__ = 'values'
    id = Column(Integer, primary_key = True)
    dev_id = Column(String(16), ForeignKey('devices.dev_id'))
    value = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)

class Devices(Base):
    __tablename__ = 'devices'
    dev_id = Column(String(16), primary_key = True)
    description = Column(String(20))
    user_id = Column(Integer, ForeignKey('users.id'))

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    email = Column(String(80), nullable = False)
    picture = Column(String(250))

engine = create_engine('mysql+mysqldb://root:example@db:3306/sensario')

Base.metadata.create_all(engine)
