#!/usr/bin/env python3

# Default Modules
import time
import sys
import random

# Additonal Modules
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from itertools import chain

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
ww = [255, 20, 20]
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

# Main
def main():

    # Flatten the large number sprite multidimensional array
    startList = largeNumberSprite
    flattenedList = spriteListFlatten (startList)
    largeNumberSpriteFlat = flattenedList

    # Flatten the small number sprite multidimensional array
    startList = smallNumberSprite
    flattenedList = spriteListFlatten (startList)
    smallNumberSpriteFlat = flattenedList

    # Define some stuff about the sprite
    spriteSize = "large"    # Size of the sprite

    # Matrix stuff
    offscreen_canvas = matrix.CreateFrameCanvas()

    while True:
        # Get the local time and bring back all the numbers
        hour, minute, second, hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond, second = processLocalTime()

        offscreen_canvas.Clear()

        # Display the first hour number
        displayNumber = hourFirst
        xOrigin = 1         
        yOrigin = 1
        spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

        # Display the second hour number
        displayNumber = hourSecond
        xOrigin = 17        
        yOrigin = 1
        spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

        # Display the first minute number
        displayNumber = minuteFirst
        xOrigin = 1
        yOrigin = 17
        spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

        # Display the second minute number
        displayNumber = minuteSecond
        xOrigin = 17         
        yOrigin = 17
        spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

        # # Display the first second number
        # displayNumber = secondFirst
        # xOrigin = 8       
        # yOrigin = 20
        # spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

        # # Display the second second number
        # displayNumber = secondSecond
        # xOrigin = 17         
        # yOrigin = 20
        # spriteDraw(offscreen_canvas, displayNumber, spriteSize, xOrigin, yOrigin, largeNumberSpriteFlat, smallNumberSpriteFlat)

        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)

if __name__ == "__main__":
    main()