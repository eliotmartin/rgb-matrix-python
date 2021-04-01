#!/usr/bin/env python3

import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions

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
options.gpio_slowdown = 2
options.panel_type = "FM6126A"

matrix = RGBMatrix(options=options)

# Try to set a pixel
x = 0
y = 0
r = 255
g = 0
b = 0

while y < 32:
    while x < 32:
        matrix.SetPixel(x, y, r, g, b)
        x += 1
        print (x, " - ", y)
        time.sleep(.05)
    x = 0
    y += 1

# Wait for CTRL-C
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
