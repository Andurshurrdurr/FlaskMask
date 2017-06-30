"""Seeds the database with restaurants and menuitems"""

from model.model import Base, Devices
from model.makesession import makesession

session = makesession(Base)

print "Attempting to seed database with dummy device:"

Device2 = Devices(
                dev_id="1",
                description="Distance sensor"
)

session.add(Device2)
session.commit()

print "added dummy device"
