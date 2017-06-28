"""Seeds the database with restaurants and menuitems"""
print "doing imports for seed"
from model.model import Base, Reading, Devices, Users
from model.makesession import makesession

session = makesession(Base)

# Then we seed the db
print "Attempting to seed database with dummy device:"

# # Create dummy user
# User1 = Users(
#                 id=1,
#                 name="testuser",
#                 email="example@example.com"
#                 )
# session.add(User1)
# session.commit()

# Create dummy device
# Device1 = Devices(
#                 dev_id="temp",
#                 description="temperature sensor",
#                 user_id=3
# )
# session.add(Device1)
# session.commit()

Device2 = Devices(
                dev_id="pressure",
                description="Pressure sensor",
                user_id=3
)
session.add(Device2)


Device3 = Devices(
                dev_id="humidity",
                description="humidity sensor",
                user_id=3
)
session.add(Device3)


Device4 = Devices(
                dev_id="co2",
                description="co2 sensor",
                user_id=3
)
session.add(Device4)
session.commit()

print "added dummy devices"
