import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print "Connected with result code "+str(rc)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Topic1")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print "Python program detected a mqtt message!"
    print msg.topic+" "+str(msg.payload)
    # add SQL insert here


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Client connects to host on port, with timeout
client.connect("localhost")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
