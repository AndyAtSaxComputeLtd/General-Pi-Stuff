#!/usr/bin/env python3
import json
import sys
import subprocess 
import json

imageFile = 'sample.jpg'
carCheckFile = 'vehicle_check.json'
carReg = 'car_reg.json'
year = ''
colour = ''
make = ''
model = ''
validMot = ''
motDate = ''

# No Parameters, Mock everything
if len(sys.argv) == 1:
    # Mock Car Reg Read
    carReg = 'C:/Users/deepc/Documents/Source/pi_motion/camera/' + carReg
    with open(carReg, 'r') as myfile:
        data=myfile.read()
    carReg = json.loads(data)

    # Mock Car Check
    carCheckFile = 'C:/Users/deepc/Documents/Source/pi_motion/camera/' + carCheckFile
    with open(carCheckFile, 'r') as myfile:
        data=myfile.read()
    carCheck = json.loads(data)

    plate = 'ay20yru'
    confidence = '100'


# 1 Parameter, Image Name so ALPR it to get number plate
elif len(sys.argv) == 2:
    imageFile = sys.argv[1]
    # call alpr
    process = subprocess.Popen(["alpr", "-c", "gb", "-n", "1", str(imageFile), "-j" ],
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)

    # Get the Car Reg Details
    jsonS,_  = process.communicate()
    carReg = json.loads(jsonS)

    plate = str(carReg['results'][0]['candidates'][0]['plate'])
    confidence = str(carReg['results'][0]['candidates'][0]['confidence'])

    # Call Vehicle Check
    # Mock Car Check
    with open(carCheckFile, 'r') as myfile:
        data=myfile.read()
    carCheck = json.loads(data)

    exit 

elif len(sys.argv) > 2 and len(sys.argv) < 4:
    imageFile= sys.argv[1]
    plate = sys.argv[2]

elif len(sys.argv) == 4:
    imageFile = sys.argv[1]
    plate = sys.argv[2]
    carCheckFile = sys.argv[3]
else:
    raise Exception('Arguuments', 'Unknown Error')

if carCheck is not None:
    year = str(carCheck['VehicleDetails']['Year'])
    colour = str(carCheck['VehicleDetails']['Colour'])
    make = str(carCheck['VehicleDetails']['MakeDvsa'])
    model = str(carCheck['VehicleDetails']['ModelDvsa'])
    validMot = str(carCheck['CalculatedMot']['ValidMot'])
    motDate = str(carCheck['CalculatedMot']['MotDate'])
    SUCCESS = str(carCheck['Success'])

details = str( imageFile + ' ' + make+ ' ' + model+ ' ' + year+ ' ' + colour+ ' ' + validMot+ ' ' + motDate+ ' ' + plate+ ' ' + confidence)
print(details)