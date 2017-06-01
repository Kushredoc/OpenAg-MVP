#Light Control
#Controls the turning on and turning off of lights
#Lights are wired into Relay #4 (Pin 29)

import RPi.GPIO as GPIO
from time import strftime, localtime
from bookshelf import takeOffShelf, putOnShelf
from logData import logData


def checkLight():
    "Check the time and determine if the lights need to be changed"
    lightOnKey = "lightOn"
    lightOffKey = "lightOff"
    lightPin = 29
    lightsOn = takeOffShelf(lightOnKey)
    lightsOff = takeOffShelf(lightOffKey)

    currentTime = strftime("%H%M", localtime())
    print("Current time: " + currentTime)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(lightPin, GPIO.IN)
    
    if GPIO.input(lightPin):
        print("Lights are ON")
        if currentTime >= lightsOff:
            print ("Turn lights off")
            GPIO.setup(lightPin, GPIO.OUT)
            GPIO.output(lightPin, GPIO.LOW)
            logData("LightChange", "Off", '')
        else:
            #reset to prior state
            GPIO.setup(lightPin, GPIO.OUT)
            GPIO.output(lightPin, GPIO.HIGH)

    else:
        print("Lights are OFF")
        if currentTime >= lightsOn:
            print ("Turn lights on")
            GPIO.setup(lightPin, GPIO.OUT)
            GPIO.output(lightPin, GPIO.LOW)
            logData("LightChange", "On", '')
        else:
            #reset to prior state
            GPIO.setup(lightPin, GPIO.OUT)
            GPIO.output(lightPin, GPIO.LOW)

    

