"""This script gets udp packets, strips the data and inserts it into the raw
values database"""

from socket import *
import json
from model.model_devices import create_reading

#validaddress = "87.137.72.165"
validaddress = "62.225.39.28"

def parsedata(data):
    """This funcion parses the data for inserting to the database"""
    try:
        # First we get device id
        j = json.loads(data)
        for v in j:
            print v
        # Next we get the values
        dev_id = j["id"]
        val = j["v"]
        # And we parse the data into a dictionary
        datadict = {"dev_id": dev_id, "value": val}
        # We return a dictionary of the data
        return datadict
    except Exception as e:
        print e
        return False

def validatedevice(address):
    """Checks to see if the ip address is from the device"""
    if validaddress in address:
        return True
    else:
        print "Invalid device address!"
        return False

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('0.0.0.0', 16666))

print "Serving udp on 0.0.0.0, port 16666"
print "Going to loop.."

while True:
        # Gets UDP data
        message, address = serverSocket.recvfrom(1024)

        print "Got message!"
        print message
        print "From: "
        print address
        try:
            if validatedevice(address):
                data = parsedata(message)
                create_reading(data["dev_id"], data["value"])
        except Exception as e:
