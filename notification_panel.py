#!/usr/bin/env python3

# ------------------------------------------------------------------------
# Notification Panel.
# Control application for MQTT driven RGB LED matrix notification hardare.
# ------------------------------------------------------------------------
# Author: Eliot Martrin
# Version: 0.1.0
# Email: eliot.martin@gmail.com
# ------------------------------------------------------------------------

# Generic/Built-in modules
import random                                                   # Random Number Module                                        
import time                                                     # Time Module

# Other moudles
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics     # Hzeller Rasberrypi RGB LED Matrix module
from PIL import Image                                           # Python Image module
import paho.mqtt.client as mqtt                                 # Eclipse Paho Python MQTT Client module
from itertools import chain                                     # Iteration tools module


messageFlag = "nothing"


# MQTT Callbacks

# Callback for MQTT logging
def on_log(client, userdata, level, buf):
    print("log: "+buf)

# Callback for MQQT Connect
def on_connect(client, userdata, flags, rc):      
    if rc==0:
        print ("Connected to MQTT Broker")
    else:
        print ("Bad connection returned Code=", rc)

# Callback for MQTT Disconnect
def on_disconnect(client, userdata, flags, rc=0):       
    print("Disconnected from MQTT Broker "+str(rc))

# Callback for MQQT Message Recieve
def on_message(client, userdata, msg):                  
    topic=msg.topic
    message_decode=str(msg.payload.decode("utf-8","ignore"))
    if topic == "notification/gmail":
        imageFile = "mail.png"
        imageXPos = 0
        imageYPos = 32
    else:
        print ("Dunno")

    global messageFlag
    messageFlag = "Got it"

# Define MQTT Perameters
broker = '192.168.1.72'                                 # Address of MQTT Broker
port = 1883                                             # Port of MQTT Broker
client = mqtt.Client("python_mqqt_client")              # Create new MQTT Client instance
mqttSubscribeTopic = "notification/#"                   # MQTT Topic
client_id = f'python-mqtt-{random.randint(0, 1000)}'    # MQTT Client ID
username = '#####'                                      # MQTT Broker Username
password = '##############'                             # MQTT Broker Password
# client.on_log = on_log                                # Bind log callback
client.on_connect = on_connect                          # Bind on connect callback
client.on_disconnect = on_disconnect                    # Bind on disconnect callback
client.on_message = on_message                          # Bind on message callback

# Function to connect ot the MQTT Broker
def mqttConnect (client, broker):
    print ("=================================================================")
    print ("Connecting to MQTT Broker ", broker)
    client.connect(broker)
    client.loop_start()

# Function to subscribe to MQTT Topic
def mqttSubscribe (client, mqttSubscribeTopic):
    client.subscribe(mqttSubscribeTopic)


# functiont to publish to MQTT Topic
def mqttPublish (client, mqttPublishTopic, mqttPublishMessage):
    client.publish(mqttPublishTopic, mqttPublishMessage)

# Function to disconnect from the MQTT Broker
def mqttDisconnect(client):
    client.loop_stop()
    client.disconnect ()

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.multiplexing = 0
options.brightness = 100
options.limit_refresh_rate_hz = 100
matrix = RGBMatrix(options=options)

# Define colours list
bb = [0, 0, 0]
rr = [175, 175, 175]
ww = [255, 255, 255]
ss = [196, 196, 196]
ee = [128, 128, 128]

# Define 0-9 large number sprites
largeNumberSprite = [
    [ # 0
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, ww, ww, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, bb, bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, bb, bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb]
    ],
    [ # 1
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww]
    ],
    [ # 2
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww]
    ],
    [ # 3
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb]
    ],
    [ # 4
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, bb, bb, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb]
    ],
    [ # 5
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb]
    ],
    [ # 6
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, bb, bb],
        [bb, bb, ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb]
    ],
    [ # 7
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb, bb, bb]
    ],
    [ # 8
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, bb, bb],
        [ww, ww, ww, ww, ww, ww, bb, bb, bb, bb, ww, ww, bb, bb],
        [ww, ww, ww, ww, ww, ww, bb, bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb],
        [ww, ww, bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, bb, bb, bb, bb, ww, ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb]
    ],
    [ # 9
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [ww, ww, ww, ww, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, bb, bb, bb, bb, bb, bb, ww, ww, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb],
        [bb, bb, ww, ww, ww, ww, ww, ww, ww, ww, bb, bb, bb, bb]
    ],
]

# Define 0-9 small number sprites
smallNumberSprite = [
    [ # 0
        [bb, bb, ww, ww, ww, bb, bb],
        [bb, ww, bb, bb, ww, ww, bb],
        [ww, ww, bb, bb, bb, ww, ww],
        [ww, ww, bb, bb, bb, ww, ww],
        [ww, ww, ww, bb, bb, ww, ww],
        [bb, ww, ww, bb, bb, ww, bb],
        [bb, bb, ww, ww, ww, bb, bb]
    ],
    [ # 1
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, bb, bb],
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, ww, ww, ww, ww, ww, ww]
    ],
    [ # 2
        [bb, ww, ww, ww, ww, ww, bb],
        [ww, ww, bb, bb, bb, ww, ww],
        [bb, bb, bb, bb, bb, ww, ww],
        [bb, bb, ww, ww, ww, ww, bb],
        [bb, ww, ww, ww, bb, bb, bb],
        [ww, ww, ww, bb, bb, bb, bb],
        [ww, ww, ww, ww, ww, ww, ww]
    ],
    [ # 3
        [bb, ww, ww, ww, ww, ww, ww],
        [bb, bb, bb, bb, ww, ww, bb],
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, ww, ww, ww, ww, bb],
        [bb, bb, bb, bb, bb, ww, ww],
        [ww, ww, bb, bb, bb, ww, ww],
        [bb, ww, ww, ww, ww, ww, bb]
    ],
    [ # 4
        [bb, bb, bb, ww, ww, ww, bb],
        [bb, bb, ww, ww, ww, ww, bb],
        [bb, ww, ww, bb, ww, ww, bb],
        [ww, ww, bb, bb, ww, ww, bb],
        [ww, ww, ww, ww, ww, ww, ww],
        [bb, bb, bb, bb, ww, ww, bb],
        [bb, bb, bb, bb, ww, ww, bb]
    ],
    [ # 5
        [ww, ww, ww, ww, ww, ww, ww],
        [ww, ww, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, ww, ww, bb],
        [bb, bb, bb, bb, bb, ww, ww],
        [bb, bb, bb, bb, bb, ww, ww],
        [ww, ww, bb, bb, bb, ww, ww],
        [bb, ww, ww, ww, ww, ww, bb]
    ],
    [ # 6
        [bb, bb, ww, ww, ww, ww, bb],
        [bb, ww, ww, bb, bb, bb, bb],
        [ww, ww, bb, bb, bb, bb, bb],
        [ww, ww, ww, ww, ww, ww, bb],
        [ww, ww, bb, bb, bb, ww, ww],
        [ww, ww, bb, bb, bb, ww, ww],
        [bb, ww, ww, ww, ww, ww, bb]
    ],
    [ # 7
        [ww, ww, ww, ww, ww, ww, ww],
        [ww, bb, bb, bb, bb, ww, ww],
        [bb, bb, bb, bb, ww, ww, bb],
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, bb, ww, ww, bb, bb],
        [bb, bb, bb, ww, ww, bb, bb]
    ],
    [ # 8
        [bb, ww, ww, ww, ww, ww, bb],
        [ww, ww, bb, bb, bb, ww, bb],
        [ww, ww, ww, bb, bb, ww, bb],
        [bb, ww, ww, ww, ww, bb, bb],
        [ww, bb, bb, ww, ww, ww, ww],
        [ww, bb, bb, bb, bb, ww, ww],
        [bb, ww, ww, ww, ww, ww, bb]
    ],
    [ # 9
        [bb, ww, ww, ww, ww, ww, bb],
        [ww, ww, bb, bb, bb, ww, ww],
        [ww, ww, bb, bb, bb, ww, ww],
        [bb, ww, ww, ww, ww, ww, ww],
        [bb, bb, bb, bb, bb, ww, ww],
        [bb, bb, bb, bb, ww, ww, bb],
        [bb, ww, ww, ww, ww, bb, bb]
    ],    
]

# Function to capture local time and extract each digit
def processLocalTime():
    # Capture local time
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec

    # Seperate HH MM SS
    hourFirst = (int(hour/10))
    hourSecond = (int(hour%10))
    minuteFirst = (int(minute/10))
    minuteSecond = (int(minute%10))
    secondFirst = (int(second/10))
    secondSecond = (int(second%10))
    
    return hour, minute, second, hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond, second

# Function to wait on key press and then exit
def waitOnKey():
    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)

# Function to flatten the multidimensional list
def spriteListFlatten (startList):
    flatListLevel1 = list(chain.from_iterable(startList))           # Flatten the original starting list
    flatListLevel2 = list(chain.from_iterable(flatListLevel1))      # Flatten the next dimension of the list
    flattenedList = list(chain.from_iterable(flatListLevel2))       # Flatten the final dimension of the list
    return flattenedList


# Function to extract the correct RGB data out of the flattened list
def spriteDraw (offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat):
    # Define some variables that the function needs to pull sprite info out of the flattened list
    xPosition = 0
    yPosition = 0
    rComponent = 0
    gComponent = 0
    bComponent = 0

    # Configure the extraction algorthim based on the required sprite size
    if spriteSize == "large":
        listStartingPosition = displayNumber * 588
        xPositionMax = 14
        yPositionMax = 14
        listEndingPosition = listStartingPosition + 588
        spriteList = largeNumberSpriteFlat

    elif spriteSize == "small":
        listStartingPosition = displayNumber * 147
        xPositionMax = 7
        yPositionMax = 7
        listEndingPosition = listStartingPosition + 147
        spriteList = smallNumberSpriteFlat

    else:
        print ("Error: spriteSize not recogonised - expecting 'large' or 'small")
        sys.exit(0)
    
    # Extraction algorthim
    while yPosition != yPositionMax:
        while xPosition != xPositionMax:

            # Get the RGB value
            rComponent = spriteList[listStartingPosition]
            gComponent = spriteList[listStartingPosition+1]
            bComponent = spriteList[listStartingPosition+2]

            # Set the pixel with the RGB value
            offscreen_canvas.SetPixel(xPosition + xOrigin, yPosition + yOrigin, rComponent, gComponent, bComponent)

            # Move along the list
            listStartingPosition +=3
            xPosition +=1
        yPosition +=1
        xPosition = 0

# Function to clear the clock and toast an image
def imagePopup(imageFile, offscreen_canvas_1, imageXPos, imageYPos):
    image = Image.open(imageFile)

    offscreen_canvas_1.SetImage(image.convert('RGB'), imageXPos, imageYPos)
 
    # Up
    while imageYPos > 4:
        offscreen_canvas_1.Clear()
        offscreen_canvas_1.SetImage(image.convert('RGB'), imageXPos, imageYPos)
        offscreen_canvas_1 = matrix.SwapOnVSync(offscreen_canvas_1)
        imageYPos -= 1
        time.sleep (0.005)

    time.sleep(3)

    # Down
    while imageYPos < 50:
        offscreen_canvas_1.Clear()
        offscreen_canvas_1.SetImage(image.convert('RGB'), imageXPos, imageYPos)
        offscreen_canvas_1 = matrix.SwapOnVSync(offscreen_canvas_1)
        imageYPos += 1
        time.sleep (0.005)

# Function to draw a small Clock with seconds
def clockSmallSeconds(offscreen_canvas, spriteSize, largeNumberSpriteFlat, smallNumberSpriteFlat):
    hour, minute, second, hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond, second = processLocalTime()

    offscreen_canvas.Clear()

    # Display the first hour number
    displayNumber = hourFirst
    xOrigin = 8         
    yOrigin = 4
    spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

    # Display the second hour number
    displayNumber = hourSecond
    xOrigin = 17        
    yOrigin = 4
    spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

    # Display the first minute number
    displayNumber = minuteFirst
    xOrigin = 8       
    yOrigin = 12
    spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

    # Display the second minute number
    displayNumber = minuteSecond
    xOrigin = 17         
    yOrigin = 12
    spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

    # Display the first second number
    displayNumber = secondFirst
    xOrigin = 8       
    yOrigin = 20
    spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

    # Display the second second number
    displayNumber = secondSecond
    xOrigin = 17         
    yOrigin = 20
    spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)




# Main
def main():

    # Connect to MQTT Broker and subscribe to topic
    mqttConnect(client, broker)
    mqttSubscribe (client, mqttSubscribeTopic)

    # Flatten the large number sprite multidimensional array
    startList = largeNumberSprite
    flattenedList = spriteListFlatten (startList)
    largeNumberSpriteFlat = flattenedList

    # Flatten the small number sprite multidimensional array
    startList = smallNumberSprite
    flattenedList = spriteListFlatten (startList)
    smallNumberSpriteFlat = flattenedList

    # Define some stuff about the sprite
    spriteSize = "small"    # Size of the sprite

    # Matrix stuff
    offscreen_canvas = matrix.CreateFrameCanvas()
    
    global messageFlag


    while 1:
        clockSmallSeconds (offscreen_canvas, spriteSize, largeNumberSpriteFlat, smallNumberSpriteFlat)
        time.sleep(1)
        if messageFlag == "Got it":
            imageFile = "mail.png"
            imageXPos = 4
            imageYPos = 32
            offscreen_canvas_1 = matrix.CreateFrameCanvas()
            imagePopup(imageFile, offscreen_canvas_1, imageXPos, imageYPos)
            messageFlag = "nothing"
            

if __name__ == "__main__":
    main()







