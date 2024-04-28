import os
from PIL import Image as img
from os import listdir
from os.path import isfile, join
mypath = "d:/pi"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    # print(f"{mypath}/{file}")
    sourceImage = img.open(f"{mypath}/{file}")

    #lx,ly rx, ry; origin is top left and 0,0
    croppedImage = sourceImage.crop((1300, 500, 1950, 1000))
    # full_path = os.path.join(mypath, file)
    croppedImage.save(f"{mypath}/edited/{file}")

    os.rename(f"{mypath}/{file}", f"{mypath}/done/{file}")

print('Done')