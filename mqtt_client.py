#!/usr/bin/env python3
# Python MQTT

import random                                        
import time  
import paho.mqtt.client as mqtt         

# Callback functions
def on_log(client, userdata, level, buf):               # Callback for logging
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):            # Callback for connection
    if rc==0:
        print ("Connected to MQTT Broker")
    else:
        print ("Bad connection returned Code=", rc)

def on_disconnect(client, userdata, flags, rc=0):       # Callback for disconnect
    print("Disconnected from MQTT Broker "+str(rc))

def on_message(client, userdata, msg):                  # Callback for message
    topic=msg.topic
    message_decode=str(msg.payload.decode("utf-8","ignore"))
    print ("Message recieved")
    print ("Topic: ", topic)
    print ("Message: ", message_decode)
    # Call some other functions depending on what the message was
    if topic == "notification/jira":
        notification_toast_jira()
    elif topic == "notification/gmail":
        notification_toast_gmail()
    else:
        print ("=================================================================")
        print ("Pretend that", topic, "can't be handled")
        print ("=================================================================")   

def notification_toast_gmail():                          # Function for displaying gmail notification
    print ("==================================================================")
    print ("Pretend that a notification for GMAIL was displayed on the Matrix!")
    print ("==================================================================")

def notification_toast_jira():                          # Function for displaying Jira notification
    print ("=================================================================")
    print ("Pretend that a notification for JIRA was displayed on the Matrix!")
    print ("=================================================================")

# Define MQTT
broker = '192.168.1.72'                                 # Address of MQTT Broker
port = 1883                                             # Port of MQTT Broker
client = mqtt.Client("python_mqqt_client")              # Create new MQTT Client instance
topic = "/matrix/notification"                          # MQTT Topic
client_id = f'python-mqtt-{random.randint(0, 1000)}'    # MQTT Client ID
username = 'eliot'                                      # MQTT Broker Username
password = 'Exploding2142!'                             # MQTT Broker Password
# client.on_log = on_log                                  # Bind log callback
client.on_connect = on_connect                          # Bind on connect callback
client.on_disconnect = on_disconnect                    # Bind on disconnect callback
client.on_message = on_message                          # Bind on message callback

# Connect ot the MQTT Broker
print ("=================================================================")
print ("Connecting to MQTT Broker ", broker)
client.connect(broker)
client.loop_start()

# Subscribe to MQTT Topic
client.subscribe("notification/#")
# client.subscribe("notification/jira")

# Publish to MQTT Topic
# client.publish("notification/gmail","Test message from python MQTT client")

# Wait for a bit (this is where I can do other stuff)
time.sleep (60)

# Disconnect from the MQTT Broker
client.loop_stop()
client.disconnect ()
print ("=================================================================")





