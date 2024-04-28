#!/usr/bin/env python3
import os
from PIL import Image as img
from os import listdir, remove
from os.path import isfile, join

debug = True
mypath = "d:/pi"
# mypath = "/var/lib/motion"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    sourceImage = img.open(f"{mypath}/{file}")
    signImage = sourceImage.crop((1823, 654, 1833, 672))
    # count pixels > 100 colour
    pixelTreshold = 0
    for y in range (0, signImage.height):
        for x in range (0, signImage.width):
            pixel = signImage.getpixel((x,y))

            if pixel[0] > 100:
                if pixel[1] > 100:
                    pixelTreshold = pixelTreshold + 1

    # process the images
    croppedImage = sourceImage.crop((1300, 500, 1950, 1000))

    if pixelTreshold >16:
        croppedImage.save(f"{mypath}/lit/{file}")
        print(f"checking file {file} - Lit Speed Cam    - {pixelTreshold}")
    else:
        croppedImage.save(f"{mypath}/unlit/{file}")
        print(f"checking file {file} - Un-Lit Speed Cam - {pixelTreshold}")
    if debug is False:
        os.remove(f"{mypath}/{file}")
print("Done !")    