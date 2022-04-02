#!/usr/bin/env python3
# ------------------------------------------------------------------------
# Clock
# Define number sprites and draw a clock on the matrix
# ------------------------------------------------------------------------

# Generic/Built-in modules
import time                                                     # Time Module
import os                                                       # OS Module
import numpy                                                    # Numpy
import random                                                   # Random Numbers

# Other moudles
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics     # Hzeller Rasberrypi RGB LED Matrix module
from itertools import chain                                     # Iteration tools module
from datetime import datetime                                   # more time processing
from PIL import Image, ImageDraw, ImageSequence, GifImagePlugin # Images stuff
import paho.mqtt.client as mqtt                                 # MQTT Cliet





# Configuration for the matrix
options = RGBMatrixOptions()
options.rows, options.cols = 32, 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.multiplexing = 0
options.brightness = 100
options.limit_refresh_rate_hz = 100
matrix = RGBMatrix(options=options)
brightnessValue = 100


# Define colours list
bb = [0, 0, 0]
ww = [255, 20, 20]

# Define 0-9 number sprites
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

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Generic Functions

# Function to clear the terminal
def clearTerminal():
    os.system('cls' if os.name=='nt' else 'clear')

# Function to wait on key press and then exit
def waitOnKey():
    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        clearTerminal()
        quit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Clock functions

# Function to capture local time and extract each digit
def processLocalTime():
    hour, minute, second = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec
    hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond = (int(hour/10)), (int(hour%10)), (int(minute/10)), (int(minute%10)), (int(second/10)), (int(second%10))
    return hour, minute, second, hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond, second

# Function to flatten the multidimensional list
def spriteListFlatten (startList):
    flatListLevel1 = list(chain.from_iterable(startList))           # Flatten the original starting list
    flatListLevel2 = list(chain.from_iterable(flatListLevel1))      # Flatten the next dimension of the list
    flattenedList = list(chain.from_iterable(flatListLevel2))       # Flatten the final dimension of the list
    return flattenedList

# Function to extract the correct RGB data out of the flattened number list
def spriteNumberDraw (offscreen_canvas_clock, displayNumber, xOrigin, yOrigin, smallNumberSpriteFlat):
    xPosition, yPosition = 0, 0
    rComponent, gComponent,bComponent = 0, 0, 0
    listStartingPosition = displayNumber * 147
    listEndingPosition = listStartingPosition + 147
    while yPosition != 7:
        while xPosition != 7:
            rComponent, gComponent, bComponent = smallNumberSpriteFlat[listStartingPosition], smallNumberSpriteFlat[listStartingPosition+1], smallNumberSpriteFlat[listStartingPosition+2]
            offscreen_canvas_clock.SetPixel(xPosition + xOrigin, yPosition + yOrigin, rComponent, gComponent, bComponent)
            listStartingPosition +=3
            xPosition +=1
        yPosition +=1
        xPosition = 0

# Function to draw the hours
def clockDrawHours (offscreen_canvas_clock, hourFirst, hourSecond, smallNumberSpriteFlat, xOrigin, yOrigin, xOriginOffset, yOriginOffset):
    # Display the first hour number
    spriteNumberDraw(offscreen_canvas_clock, hourFirst, xOrigin+xOriginOffset, yOrigin+yOriginOffset, smallNumberSpriteFlat)
    spriteNumberDraw(offscreen_canvas_clock, hourSecond, xOrigin+xOriginOffset+9, yOrigin+yOriginOffset, smallNumberSpriteFlat)

# Function to draw the minutes
def clockDrawMinutes (offscreen_canvas_clock, minuteFirst, minuteSecond, smallNumberSpriteFlat,xOrigin, yOrigin, xOriginOffset, yOriginOffset):
    # Display the first minute number
    spriteNumberDraw(offscreen_canvas_clock, minuteFirst, xOrigin+xOriginOffset, yOrigin+yOriginOffset, smallNumberSpriteFlat)
    spriteNumberDraw(offscreen_canvas_clock, minuteSecond, xOrigin+xOriginOffset+9, yOrigin+yOriginOffset, smallNumberSpriteFlat)

# Function to draw the seconds
def clockDrawSeconds (offscreen_canvas_clock, secondFirst, secondSecond, smallNumberSpriteFlat, xOrigin, yOrigin, xOriginOffset, yOriginOffset):
    # Display the first second number
    spriteNumberDraw(offscreen_canvas_clock, secondFirst, xOrigin+xOriginOffset, yOrigin+yOriginOffset, smallNumberSpriteFlat)
    spriteNumberDraw(offscreen_canvas_clock, secondSecond, xOrigin+xOriginOffset+9, yOrigin+yOriginOffset, smallNumberSpriteFlat)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# GIF Functions

# Function to load a GIF and loop through it on the Matrix
def gifViewer(imageFile, offscreen_canvas_clock, gifLoops, offsetX, offsetY):
  # Open a gif and get the frames
  image = Image.open(imageFile)
  frames = ImageSequence.Iterator(image)

  # Loop through gif frames and display on matrix.
  for loops in range(gifLoops):
    for frame in range(0, image.n_frames):
        offscreen_canvas_clock.Clear()
        image.seek(frame)
        offscreen_canvas_clock.SetImage(image.convert('RGB'), offsetX, offsetY)
        time.sleep(0.05)
        offscreen_canvas_clock = matrix.SwapOnVSync(offscreen_canvas_clock)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MQTT Functions

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



class callbackMessage:
    displayMode = "clock"

    def on_message(self, client, userdata, msg):            # Callback for message
        topic=msg.topic
        message_decode=str(msg.payload.decode("utf-8","ignore"))
        print ("Message recieved")
        print ("Topic: ", topic)
        print ("Message: ", message_decode)
     
        if topic == "matrix/power":
            print ("==================================================================")
            print ("Clock power was toggled to", message_decode)
            print ("==================================================================")
            if message_decode == "off":
                brightnessValue = 0
                matrix.brightness = brightnessValue
            else:
                brightnessValue = 100
                matrix.brightness = brightnessValue

        elif topic == "matrix/notify":
            print ("=================================================================")
            print (topic, "has been triggered")
            print ("=================================================================")

            
        else:
            print ("=================================================================")
            print (topic, "can't be handled")
            print ("=================================================================")
            displayMode = "clock"

          
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main
def main():

    # Configuration for MQTT
    broker = 'localhost'                                    # Address of MQTT Broker
    port = 1883                                             # Port of MQTT Broker
    client = mqtt.Client("python_mqqt_client")              # Create new MQTT Client instance
    topic = "/matrix/notification"                          # MQTT Topic
    client_id = f'python-mqtt-{random.randint(0, 1000)}'    # MQTT Client ID
    username = 'eliot'                                      # MQTT Broker Username
    password = 'Exploding2142!'                             # MQTT Broker Password
    #client.on_log = on_log                                 # Bind log callback
    client.on_connect = on_connect                          # Bind on connect callback
    client.on_disconnect = on_disconnect                    # Bind on disconnect callback
    client.on_message = callbackMessage().on_message        # Bind on message callback
    clearTerminal()

    # Connect to MQTT Broker
    print ("Connecting to MQTT Broker", broker)
    client.connect(broker)
    client.loop_start()

    # Subscribe to MQTT Topic
    client.subscribe("matrix/#")
   

    # Run the clock
    print ("The clock is running")
    print ("=================================================================")

    # Do the intial time capture
    hour, minute, second, hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond, second = processLocalTime()
    currentMinute = minute

    # Flatten the small number sprite multidimensional array
    startList = smallNumberSprite
    smallNumberSpriteFlat  = spriteListFlatten (startList)

    # Set up the matrix canvas
    offscreen_canvas_clock = matrix.CreateFrameCanvas()
    xOrigin, yOrigin = 8, 4

    # Main loop
    while 1:

        # Process local time
        hour, minute, second, hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond, second = processLocalTime()

        # Draw small digital clock
        if callbackMessage().displayMode == "clock":
            clockDrawHours (offscreen_canvas_clock, hourFirst, hourSecond, smallNumberSpriteFlat, xOrigin, yOrigin, 0, 0)
            clockDrawMinutes (offscreen_canvas_clock, minuteFirst, minuteSecond, smallNumberSpriteFlat, xOrigin, yOrigin, 0, 8)
            clockDrawSeconds (offscreen_canvas_clock, secondFirst, secondSecond, smallNumberSpriteFlat, xOrigin, yOrigin, 0, 16)
            offscreen_canvas_clock = matrix.SwapOnVSync(offscreen_canvas_clock)
        else:
            imageFile = "ben.gif"
            gifLoops = 10
            offsetX = 0
            offsetY = 0
            gifViewer(imageFile, offscreen_canvas_clock, gifLoops, offsetX, offsetY)

     
if __name__ == "__main__":
    main()