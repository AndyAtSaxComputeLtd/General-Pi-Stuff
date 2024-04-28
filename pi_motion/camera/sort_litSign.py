import os
from PIL import Image as img
from os import listdir, remove
from os.path import isfile, join

debug = True

mypath = "d:/pi"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    # print(f"{mypath}/{file}")
    sourceImage = img.open(f"{mypath}/{file}")
    signImage = sourceImage.crop((1823, 654, 1833, 672))
    # count pixels > 100 colour
    pixelTreshold = 0
    for y in range (0, signImage.height):
        for x in range (0, signImage.width):
            pixel = signImage.getpixel((x,y))
            
            if pixel[0] > 100: pixelTreshold = pixelTreshold + 1
            if pixel[1] > 100: pixelTreshold = pixelTreshold + 1
            if pixel[2] > 100: pixelTreshold = pixelTreshold + 1
    print ( f"PixelThreshold = {pixelTreshold}")

    croppedImage = sourceImage.crop((1300, 500, 1950, 1000))
    if pixelTreshold > 100:
        croppedImage.save(f"{mypath}/lit/{file}")    
        if debug is True: 
            print (f"LIT = {mypath}/lit/{file}")
    else:
        if debug is True:
            croppedImage.save(f"{mypath}/unlit/{file}")
            print (f"UNLIT = {mypath}/lit/{file}")
    if debug is False:
        os.remove(f"{mypath}/{file}")
    # else:
        # os.rename(f"{mypath}/{file}", f"{mypath}/done/{file}")
print('Done')