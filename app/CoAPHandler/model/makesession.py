"""Initiates a database session"""
from sqlalchemy import create_engine #, *func* to aggregate
from sqlalchemy.orm import sessionmaker

def makesession(Base):
    #Initiate the engine obj mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
    engine = create_engine('mysql+mysqldb://root:example@db:3306/sensario')
    # Bind engine and the base obj
    Base.metadata.bind = engine
    # Init the session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    #return session obj
    return session
