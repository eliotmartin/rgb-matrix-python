#!/usr/bin/env python3
#create and display numbers 0-9

import time
import sys
import json

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image

# Configuration for the matrix
# options = RGBMatrixOptions()
# options.rows = 32
# options.cols = 32
# options.chain_length = 1
# options.parallel = 1
# options.hardware_mapping = 'adafruit-hat'
# options.row_address_type = 0
# options.scan_mode = 0
# options.multiplexing = 0
# options.gpio_slowdown = 4
# options.brightness = 100
# options.show_refresh_rate = 0
# options.drop_privileges = False
# matrix = RGBMatrix(options=options)

# Function to wait on key press and then exit
def waitOnKey():
    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)


# Function to draw progress bar box
def drawProgressBarBox(offscreen_canvas,progressBarXOrigin,progressBarYOrigin,progressBarLength,progressBarHeight):
    white = graphics.Color(255, 255, 255)
    graphics.DrawLine(offscreen_canvas, progressBarXOrigin, progressBarYOrigin, progressBarXOrigin + progressBarLength, progressBarYOrigin, white)
    graphics.DrawLine(offscreen_canvas, progressBarXOrigin + progressBarLength, progressBarYOrigin, progressBarXOrigin + progressBarLength, progressBarYOrigin + progressBarHeight, white)
    graphics.DrawLine(offscreen_canvas, progressBarXOrigin, progressBarYOrigin + progressBarHeight, progressBarXOrigin + progressBarLength, progressBarYOrigin + progressBarHeight, white)
    graphics.DrawLine(offscreen_canvas, progressBarXOrigin, progressBarYOrigin, progressBarXOrigin, progressBarYOrigin + progressBarHeight, white)


# Function to work out the current progress
def computeProgress(progressTarget, progressCurrent, progressBarLength):
    progressBarComputed = progressCurrent / progressTarget * (progressBarLength - 1)
    return progressBarComputed

# Function to fill the progress bar with the computed progress
def drawProgressBar(offscreen_canvas,progressBarComputed, progressBarXOrigin, progressBarYOrigin, progressBarHeight):
    x = 0
    xmax = int(progressBarComputed)+1
    green = graphics.Color(0, 128, 0)
    while x != xmax:
        graphics.DrawLine(offscreen_canvas, progressBarXOrigin + x + 1, progressBarYOrigin + 1, progressBarXOrigin + x + 1, progressBarYOrigin + progressBarHeight - 1, green)
        x += 1


# Main
def main():

    if __name__ == "__main__":
        main()