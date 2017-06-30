"""Contains functions for doing stuff with device readings"""
from model import Base, Reading  # , Devices
from makesession import makesession
session = makesession(Base)


def create_reading(dev_id, value):
    """Gets parameters for a new restaurants and adds it into the db"""
    raw_data = Reading(dev_id=dev_id, value=value)
    session.add(raw_data)
    session.commit()
    print "Inserted new sensorvalue to database!"
    return True
