"""Seeds the database with restaurants and menuitems"""
print "doing imports for seed"
from model.model import Base, Reading, Devices, Users
from model.makesession import makesession

session = makesession(Base)
# First we clear the db
try:
    r = session.query(Reading).delete()

    session.commit()
    print "cleared all sensorreadings"


    d = session.query(Devices).delete()

    session.commit()
    print "cleared all devices"
    
    u = session.query(Users).delete()

    session.commit()
    print "cleared all users"

    print "Successfully cleared database!"
except Exception as e:
    session.rollback()
    print "an error occured: "
    print e
