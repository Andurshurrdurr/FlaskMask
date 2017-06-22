"""Seeds the database with restaurants and menuitems"""

from model.model import Base, Readings, Devices
from app.model.makesession import makesession

session = makesession(Base)

print "Attempting to seed database with dummy device:"

# Create dummy user
Device1 = Devices(
                id="12345",
                sensor_type="testingsensor"
)
session.add(User1)
session.commit()

print "added dummy device"
