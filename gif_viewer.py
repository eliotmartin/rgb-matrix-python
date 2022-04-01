#!/usr/bin/env python

import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageSequence, GifImagePlugin

# Configuration matrix for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.multiplexing = 0
options.brightness = 100
options.limit_refresh_rate_hz = 100
matrix = RGBMatrix(options=options)

offscreen_canvas = matrix.CreateFrameCanvas()


# Function to load a GIF and loop through it on the Matrix
def gifViewer(imageFile, offscreen_canvas, gifLoops, offsetX, offsetY):
  # Open a gif and get the frames
  image = Image.open(imageFile)
  frames = ImageSequence.Iterator(image)

  # Loop through gif frames and display on matrix.
  for loops in range(gifLoops):
    for frame in range(0, image.n_frames):
        offscreen_canvas.Clear()
        image.seek(frame)
        offscreen_canvas.SetImage(image.convert('RGB'), offsetX, offsetY)
        time.sleep(0.01)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)

  # clear the screen
  offscreen_canvas.Clear()
  offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)




# Main
def main():
  imageFile = "dayz.gif"
  gifLoops = 33000
  offsetX = 0
  offsetY = 0
  gifViewer(imageFile, offscreen_canvas, gifLoops, offsetX, offsetY)

            

if __name__ == "__main__":
    main()