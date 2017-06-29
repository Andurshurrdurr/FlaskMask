"""Initiates a database session"""
from sqlalchemy import create_engine #, *func* to aggregate
from sqlalchemy.orm import sessionmaker

def makesession(Base):
    # SQLite: sqlite:///dbname.db
    # mysqlconnector: mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
    # Current mysql+mysqldb://root:example@db:3306/sensario
    engine = create_engine('sqlite:///mqtt_test.db')
    # Bind engine and the base obj
    Base.metadata.bind = engine
    # Init the session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    #return session obj
    return session
