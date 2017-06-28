from socket import *
import json

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
message = json.dumps({"id":"temperature", "v":25})
remote = "172.104.135.67"
dev = "10.100.0.79"
addr = (remote, 16666)

print "sending udp req"

clientSocket.sendto(message, addr)
