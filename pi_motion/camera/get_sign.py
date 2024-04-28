import os
import numpy as np
from PIL import Image as img
from os import listdir
from os.path import isfile, join
mypathLit = "d:/pi/sign/05-20210611175729-00.jpg"
mypathUnlit = "d:/pi/sign/07-20210611182023-00.jpg"

sourceImage = img.open(mypathUnlit)
pixelTreshold = 0

for y in range (0, sourceImage.height):
    for x in range (0, sourceImage.width):
        pixel = sourceImage.getpixel((x,y))
        
        if pixel[0] > 100: pixelTreshold = pixelTreshold + 1
        if pixel[1] > 100: pixelTreshold = pixelTreshold + 1
        if pixel[2] > 100: pixelTreshold = pixelTreshold + 1
print ( f"PixelThreshold = {pixelTreshold}")