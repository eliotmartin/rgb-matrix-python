#!/usr/bin/env python3
#create and display numbers 0-9

import time
import sys
import json

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image

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



def imagePopup(imageFile, offscreen_canvas, imageXPos, imageYPos):
    image = Image.open(imageFile)
    offscreen_canvas.SetImage(image.convert('RGB'), imageXPos, imageYPos)
 
    # Up
    while imageYPos > -1:
        offscreen_canvas.Clear()
        offscreen_canvas.SetImage(image.convert('RGB'), imageXPos, imageYPos)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        imageYPos -= 1
        time.sleep (0.005)

    time.sleep (3)

    # Down
    while imageYPos < 32:
        offscreen_canvas.Clear()
        offscreen_canvas.SetImage(image.convert('RGB'), imageXPos, imageYPos)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        imageYPos += 1
        time.sleep (0.005)



def main():

    # Matrix stuff
    offscreen_canvas = matrix.CreateFrameCanvas()

    # Image stuff
    imageFile = "mail.png"
    imageXPos = 0
    imageYPos = 32
    imagePopup(imageFile,offscreen_canvas, imageXPos, imageYPos)


if __name__ == "__main__":
    main() 