#!/usr/bin/env python3

# Clock for 32 x 32 RGB LED Matrix

import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
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
options.show_refresh_rate = 0

matrix = RGBMatrix(options=options)


# Lists for colours
B = [0, 0, 0]           # Black
W = [255, 255, 255]     # White
R = [255, 0, 0]         # Red

# List for number sprites
numberSprite =[
    [# ZERO
        [W, W, W],
        [W, B, W],
        [W, B, W],
        [W, B, W],
        [W, W, W]
    ],
    [# ONE               
        [B, W, B],
        [W, W, B],
        [B, W, B],
        [B, W, B],
        [B, W, B]
    ],
    [# TWO               
        [W, W, W],
        [B, B, W],
        [W, W, W],
        [W, B, B],
        [W, W, W]
    ],
    [# THREE               
        [W, W, W],
        [B, B, W],
        [W, W, W],
        [B, B, W],
        [W, W, W]
    ],
        [# FOUR               
        [W, B, W],
        [W, B, W],
        [W, W, W],
        [B, B, W],
        [B, B, W]
    ],
        [# FIVE               
        [W, W, W],
        [W, B, B],
        [W, W, W],
        [B, B, W],
        [W, W, W]
    ],
        [# SIX               
        [W, W, W],
        [W, B, B],
        [W, W, W],
        [W, B, W],
        [W, W, W]
    ],
        [# SEVEN               
        [W, W, W],
        [B, B, W],
        [B, B, W],
        [B, B, W],
        [B, B, W]
    ],
        [# EIGHT               
        [W, W, W],
        [W, B, W],
        [W, W, W],
        [W, B, W],
        [W, W, W]
    ],
        [# NINE               
        [W, W, W],
        [W, B, W],
        [W, W, W],
        [B, B, W],
        [B, B, W]
    ],
]

seperatorSprite =[
    [# :
        [B, R, B],
        [B, R, B],
        [B, B, B],
        [B, R, B],
        [B, R, B]
    ],
]





def draw_seperator(displayDigit, xOffset, yOffset): # Function to draw time seperator
    xOriginDigit = 0                               # Where the first number x
    yOriginDigit = 0                               # Where the first number y
    rgbComponent = 0                               # rgb component value (0=R, 1=G, 2=B)
    spriteRow = 0                                  # row of colours across a sprite
    spriteColumn = 0                               # column of colours down a sprite
    r = 0                                          # Red value
    g = 0                                          # Green value
    b = 0                                          # Blue


    while spriteRow <5:
        while spriteColumn <3:
            while rgbComponent <3:
              
                if rgbComponent == 0:
                    r =(seperatorSprite[displayDigit][spriteRow][spriteColumn][rgbComponent]) # Set BLUE component value
            
                elif rgbComponent == 1:
                    g = (seperatorSprite[displayDigit][spriteRow][spriteColumn][rgbComponent]) # Set GREEN component value
            
                else:
                    b = (seperatorSprite[displayDigit][spriteRow][spriteColumn][rgbComponent]) # Set BLUE component value
 
                matrix.SetPixel(xOriginDigit+spriteColumn+xOffset, yOriginDigit+spriteRow+yOffset, r, g, b)

                rgbComponent += 1
            rgbComponent = 0
            spriteColumn += 1
        spriteColumn = 0
        spriteRow += 1








def draw_digit(displayDigit, xOffset, yOffset):    # Function to draw time number
    xOriginDigit = 0                               # Where the first number x
    yOriginDigit = 0                               # Where the first number y
    rgbComponent = 0                               # rgb component value (0=R, 1=G, 2=B)
    spriteRow = 0                                  # row of colours across a sprite
    spriteColumn = 0                               # column of colours down a sprite
    r = 0                                          # Red value
    g = 0                                          # Green value
    b = 0                                          # Blue


    while spriteRow <5:
        while spriteColumn <3:
            while rgbComponent <3:
              
                if rgbComponent == 0:
                    r =(numberSprite[displayDigit][spriteRow][spriteColumn][rgbComponent]) # Set BLUE component value
            
                elif rgbComponent == 1:
                    g = (numberSprite[displayDigit][spriteRow][spriteColumn][rgbComponent]) # Set GREEN component value
            
                else:
                    b = (numberSprite[displayDigit][spriteRow][spriteColumn][rgbComponent]) # Set BLUE component value
 
                matrix.SetPixel(xOriginDigit+spriteColumn+xOffset, yOriginDigit+spriteRow+yOffset, r, g, b)

                rgbComponent += 1
            rgbComponent = 0
            spriteColumn += 1
        spriteColumn = 0
        spriteRow += 1









while True:
    # Capture the time
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec

    # Parse out the digits
    hourFirst = (int(hour/10))
    hourSecond = (int(hour%10))
    minuteFirst = (int(minute/10))
    minuteSecond = (int(minute%10))
    secondFirst = (int(second/10))
    secondSecond = (int(second%10))




    clockStartX = 2
    clockStartY = 10

    # Draw the first hour digit
    displayDigit = hourFirst
    xOffset = 0 + clockStartX
    yOffset = 0 + clockStartY
    draw_digit(displayDigit,xOffset,yOffset)

    # Draw the second hour digit
    displayDigit = hourSecond
    xOffset = 4 + clockStartX
    yOffset = 0 + clockStartY
    draw_digit(displayDigit,xOffset,yOffset)


    # Draw the seperator
    displayDigit = 0
    xOffset = 7 + clockStartX
    yOffset = 0 + clockStartY
    draw_seperator(displayDigit,xOffset,yOffset)


    # Draw the first minute digit
    displayDigit = minuteFirst
    xOffset = 10 + clockStartX
    yOffset = 0 + clockStartY
    draw_digit(displayDigit,xOffset,yOffset)

    # Draw the second minute digit
    displayDigit = minuteSecond
    xOffset = 14 + clockStartX
    yOffset = 0 + clockStartY
    draw_digit(displayDigit,xOffset,yOffset)


    # Draw the seperator
    displayDigit = 0
    xOffset = 17 + clockStartX
    yOffset = 0 + clockStartY
    draw_seperator(displayDigit,xOffset,yOffset)


    # Draw the first second digit
    displayDigit = secondFirst
    xOffset = 20 + clockStartX
    yOffset = 0 + clockStartY
    draw_digit(displayDigit,xOffset,yOffset)

    # Draw the second second digit
    displayDigit = secondSecond
    xOffset = 24 + clockStartX
    yOffset = 0 + clockStartY
    draw_digit(displayDigit,xOffset,yOffset)

    time.sleep(1)

# Wait for CTRL-C
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)