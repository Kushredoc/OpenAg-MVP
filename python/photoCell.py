#ambientLight.py
#Checks the light via a photo cell and determines of the lights are on or off
#If the is a change, log the chanage
#External module imports
import RPi.GPIO as GPIO
import time

from logData import logData

from bookshelf import takeOffShelf, putOnShelf

def getCellTime():
    "Get the time it takes to charge a capacitor with the photocell, this is a rough measurement of light"
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    photoCellPin = 37
    reading = 0
    GPIO.setup(photoCellPin, GPIO.OUT)
    GPIO.output(photoCellPin, GPIO.LOW)
    time.sleep(1)
    GPIO.setup(photoCellPin, GPIO.IN)
    while not GPIO.input(photoCellPin):
        reading += 1
    print ("Light is: %s" %reading)
    return reading
    

def checkLightState():
    priorLightOnKey = "priorLightOn"
    priorLightOn = takeOffShelf(priorLightOnKey)
    lightOn = True
#Turn time value to boolean
    currentLight = getCellTime()
    if currentLight > 1000:
        lightOn = False
        print ("Light is Off")
    else:
        print ("Light is On")
#Turn boolean to string
    priorLightOn = takeOffShelf(priorLightOnKey)
    lightState = "ON"
    if lightOn != priorLightOn:
        if not lightOn:
            lightState = "OFF"
            
        logData("LightChange", lightState, '')
        priorLightState = lightState
        putOnShelf(priorLightOnKey, priorLightOn)
