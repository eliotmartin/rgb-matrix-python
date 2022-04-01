#!/usr/bin/env python3

import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from matrix_clock import display_big_clock
from PIL import Image

image_file = "test_image.png"
image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat' 

matrix = RGBMatrix(options=options)

# Create a thumbnail that first our screen
# image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)



clockStartX = 2
clockStartY = 1
seperatorDisplay = True

# white = graphics.Color(255, 255, 255)
# graphics.DrawLine(matrix, 1, 7, 30, 7, white)


x =4
y =32
while y > 15:
    matrix.SetImage(image.convert('RGB'),x,y)
    display_big_clock(clockStartX,clockStartY)
    matrix.SetImage(image.convert('RGB'),x,y)
    seperatorDisplay = not seperatorDisplay
    time.sleep(0.1)
    y -= 1

time.sleep(2)

while y < 32:
    matrix.SetImage(image.convert('RGB'),x,y)
    display_big_clock(clockStartX,clockStartY)
    seperatorDisplay = not seperatorDisplay
    time.sleep(0.005)
    time.sleep(0.005)
    y += 1

# try:
#     print("Press CTRL-C to stop.")
#     while True:
#         time.sleep(100)
# except KeyboardInterrupt:
#     sys.exit(0)