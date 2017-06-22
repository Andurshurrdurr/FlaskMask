"""Contains models for doing CRUD for restaurants"""

from model import Base, Devices

from makesession import makesession

session = makesession(Base)

def read_devices(device_id=None, user_id=None):
    """
    Queries the database for devices. Takes device_id and userid args,
    and returns:
    1. If restaurantid = None & user_id != None -> Returns all devices for user
    2. if device_id != None -> Returns info on device
    """
    if restaurantid == None:
        if user_id == None:
            # Getting all devices in db
            return (session.query(Devices).all())
        else:
            # Getting all devices belonging to user
            return (session.query(Devices).filter_by(user.id=user_id).all(), None)
    else:
        device = session.query(Devices).filter_by(id=device_id).one()
        if restaurant.user_id == user_id:
            # We return tuple[1] True to indicate that user owns device
            return ([restaurant], True)
        else:
            # Return false to indicate user is not owner
            return ([restaurant], False)

def create_device(device_id, description):
    """Gets parameters for a new restaurants and adds it into the db"""
    device = Devices(
                        id=device_id,
                        description=description
                      )
    session.add(device)
    session.commit()
    return True

def update_device(device_id, description):
    """Updates a restaurant in the db, returns a string if successful"""
    device = session.query(Devices).filter_by(id=device_id).one()
    device.name = name
    device.description = description
    session.add(device)
    session.commit()
    return True

def delete_restaurant(device_id):
    """Deletes restaurant with passed id"""
    device = session.query(Devices).filter_by(id=device_id).one()
    session.delete(device)
    session.commit()
    return True
