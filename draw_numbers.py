#!/usr/bin/env python3
#create and display numbers 0-9

import time
import sys
import json

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from progress_bar import drawProgressBarBox, computeProgress, drawProgressBar
from PIL import Image

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.row_address_type = 0
options.scan_mode = 0
options.multiplexing = 0
options.gpio_slowdown = 4
options.brightness = 100
options.drop_privileges = False
matrix = RGBMatrix(options=options)


# Define colours
bb = [0, 0, 0]
rr = [255, 0, 0]
ww = [255, 255, 255]

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

# Function to wait on key press and then exit
def waitOnKey():
    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)

# Function to draw number sprite
def draw_NumberSprite(offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin):

    rgbComponent = 0                               # Red, Green, or Blue component (0=R, 1=G, 2=B)
    spriteRow = 0                                  # Counter for the rows of pixels being drawm
    spriteColumn = 0                               # Counter for the column of pixels being drawn
    redComponent = 0                               # Red value
    greenComponent = 0                             # Green value
    blueComponent = 0                              # Blue
    

   
    # Setup rows and columns depending on the size of sprite required
    if spriteSize == "large":
        maxSpriteRows = 14
        maxSpriteColumns = 14
        spriteList = largeNumberSprite
    elif spriteSize == "small":
        maxSpriteRows = 7
        maxSpriteColumns = 7
        spriteList = smallNumberSprite
    else:
        print ("spriteSize not recogonised (expecting 'large' or 'small)")
        sys.exit(0)

    # Move throught the columns and rows of the specified sprite and extract the RGB value for each pixel
    while spriteRow <maxSpriteRows:
        while spriteColumn <maxSpriteColumns:
            while rgbComponent <3:
                
                # Set the Red component
                if rgbComponent == 0: 
                    if inverseFlag == True: 
                        redComponent = 255 - (spriteList[displayNumber][spriteRow][spriteColumn][rgbComponent]) # Set Inverse of RED component value
                    else:
                        redComponent = (spriteList[displayNumber][spriteRow][spriteColumn][rgbComponent]) # Set RED component value

                # Set the Green component
                elif rgbComponent == 1:
                    if inverseFlag == True:
                        greenComponent = 255 - (spriteList[displayNumber][spriteRow][spriteColumn][rgbComponent]) # Set inverse of GREEN component value
                    else:
                        greenComponent = (spriteList[displayNumber][spriteRow][spriteColumn][rgbComponent]) # Set GREEN component value
                    
                # Set the Blue component
                else:
                    if inverseFlag == True:
                        blueComponent = 255 - (spriteList[displayNumber][spriteRow][spriteColumn][rgbComponent]) # Set inverse of BLUE component value
                    else:
                        blueComponent = (spriteList[displayNumber][spriteRow][spriteColumn][rgbComponent]) # Set BLUE component value

                # Now we have that value, draw it on the matrix display
                
                offscreen_canvas.SetPixel(spriteXOrigin+spriteColumn+spriteXOffset, spriteYOrigin+spriteRow+spriteYOffset, redComponent, greenComponent, blueComponent)
                

                rgbComponent += 1
            rgbComponent = 0
            spriteColumn += 1
        spriteColumn = 0
        spriteRow += 1
    

# Function to captrure local time and extract each digit
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
    
    return hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond, second

# process to display the clock on the matrix
def displayClock(offscreen_canvas, hourFirst, hourSecond, minuteFirst, minuteSecond, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin):
    if spriteSize == "large":
        #draw the large version
        # Draw first hour digit
        displayNumber = hourFirst
        spriteXOffset = 1
        spriteYOffset = 1
        draw_NumberSprite (offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)

        # Draw second hour digit
        displayNumber = hourSecond
        spriteXOffset = 17
        spriteYOffset = 1
        draw_NumberSprite (offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)

        # Draw first minute digit
        displayNumber = minuteFirst
        spriteXOffset = 1
        spriteYOffset = 17
        draw_NumberSprite (offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)

        # Draw second minute digit
        displayNumber = minuteSecond
        spriteXOffset = 17
        spriteYOffset = 17
        draw_NumberSprite (offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)
    else:
        # Draw the small version
        # Draw first hour digit
        displayNumber = hourFirst
        spriteXOffset = 1
        spriteYOffset = 1
        draw_NumberSprite (offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)

        # Draw second hour digit
        displayNumber = hourSecond
        spriteXOffset = 10
        spriteYOffset = 1
        draw_NumberSprite (offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)

        # Draw first minute digit
        displayNumber = minuteFirst
        spriteXOffset = 1
        spriteYOffset = 10
        draw_NumberSprite (offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)

        # Draw second minute digit
        displayNumber = minuteSecond
        spriteXOffset = 10
        spriteYOffset = 10
        draw_NumberSprite (offscreen_canvas, displayNumber, spriteXOffset, spriteYOffset, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)



# Main
def main():

    offscreen_canvas = matrix.CreateFrameCanvas()

    # Draw progress bar box
    progressBarLength = 15
    progressBarHeight = 3
    progressBarXOrigin = 8
    progressBarYOrigin = 22
    progressCurrent = 0
    progressTarget = 60
    inverseFlag = False
    spriteSize = "small"
    spriteXOrigin = 7                            
    spriteYOrigin = 3
    

    # display a small version of the clock            
    while True:

        #Clear the offscreen canvas
        offscreen_canvas.Clear()

        # Get the local tim and brig the numbers back
        hourFirst, hourSecond, minuteFirst, minuteSecond, secondFirst, secondSecond, second = processLocalTime()
        
        # compute the progress and display the progress bar
        progressCurrent = second
        drawProgressBarBox(offscreen_canvas,progressBarXOrigin,progressBarYOrigin,progressBarLength,progressBarHeight)
        progressBarComputed = computeProgress(progressTarget, progressCurrent, progressBarLength)
        drawProgressBar (offscreen_canvas, progressBarComputed, progressBarXOrigin, progressBarYOrigin, progressBarHeight)
        
        # Display the clock
        displayClock(offscreen_canvas, hourFirst, hourSecond, minuteFirst, minuteSecond, inverseFlag, spriteSize, spriteXOrigin, spriteYOrigin)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)  

        # Wait for a second
        time.sleep(1)

    # hang on for a key press
    waitOnKey()

if __name__ == "__main__":
    main()