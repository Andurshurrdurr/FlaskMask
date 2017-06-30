"""Contains functions for doing CRUD on the Readings table"""

from model import Base, Reading, Devices
from makesession import makesession

session = makesession(Base)

def read_readings(device_id):
    """
    list out 10 recent readings for a specific device
    """
    print "reading db for: " + device_id
    readings = session.query(Reading).filter_by(dev_id=device_id).order_by(Reading.id.desc()).all()
    strlist = []
    count = 0
    for i in readings:
        count += 1
        v = int(i.value)
        strlist.append(v)
        if count > 10:
            print strlist
            print "returning list of values"
            return str(strlist)

# Creating readings is left up to the udp server

def delete_readings(device_id):
    """deletes all readings for a device"""
    # First we query the db
    readings = session.query(Reading).filter_by(dev_id=device_id).all()
    # Then we delete the item from db through the session
    session.delete(readings)
    session.commit()
    # Finally we return the restaurant id
    return True
