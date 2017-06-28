"""Seeds the database with restaurants and menuitems"""
print "doing imports for seed"
from model.model import Base, Reading, Devices, Users
from model.makesession import makesession

session = makesession(Base)
# First we clear the db
try:
    print "quering db for users..."
    r = session.query(Users).all()
    print r
    for u in r:
        print "found user with id: "
        print u.id

    print "quering db for devices:"
    d = session.query(Devices).all()
    print d
    for i in d:
        print "found device with dev_id: "
        print i.dev_id
        
except Exception as e:
    session.rollback()
    print "An error occured: "
    print e
