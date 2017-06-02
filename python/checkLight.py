#Light Control
#Controls the turning on and turning off of lights
#Lights are wired into Relay #4 (Pin 29)

import RPi.GPIO as GPIO
from time import strftime, localtime
from bookshelf import takeOffShelf, putOnShelf
from logData import logData


def checkLight():
    "Check the time and determine if the lights need to be changed"
    lightPin = 29
    currentLightOn = True
    lightOnKey = "lightOn"
    lightOffKey = "lightOff"
    priorLightOnKey = "priorLightOn"
    lightsOn = takeOffShelf(lightOnKey)
    lightsOff = takeOffShelf(lightOffKey)
    priorLightOn = takeOffShelf(priorLightOnKey)

    currentTime = strftime("%H%M", localtime())
    print("Current time: " + currentTime)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
#    GPIO.setup(lightPin, GPIO.IN)
   
#flip the switch no matter what
    if currentTime >= lightsOff:
        print ("Turn lights off")
        GPIO.setup(lightPin, GPIO.OUT)
        GPIO.output(lightPin, GPIO.LOW)
        currentLightOn = False

    if currentTime >= lightsOn:
        print ("Turn lights on")
        GPIO.setup(lightPin, GPIO.OUT)
        GPIO.output(lightPin, GPIO.HIGH)


    if currentLightOn != priorLightOn:
        if currentLightOn:
            logData("LightChange", "On", '')
            print("Light change - ON")
        else:
            logData("LightChange", "Off", '')
            print("Light change - OFF")
        putOnShelf(priorLightOnKey, currentLightOn)
    
            
    

