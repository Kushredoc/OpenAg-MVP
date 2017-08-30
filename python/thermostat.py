#!/usr/bin/python

#thermostat.py
#controlls the exhaust fan, turns it on when temperature is over the target temperature
#Fan is assumed to be wired to Pin 33 (GPIO 13)
#Pin 30 may control a relay or be a transistor switch, assumes HIGH means ON

import RPi.GPIO as GPIO
from logData import logData
from bookshelf import takeOffShelf, putOnShelf
from si7021 import getTempC

def adjustThermostat(temp):
    "Turn the fan on or off in relationship to target temperature"
    print ("Adjust Thermostat %s" %str(temp))

    fanPin = 35
    currentFanOn = True
    priorFanOnKey = "priorFanOn"
    targetTempKey = "targetTemp"
    priorFanOn = takeOffShelf(priorFanOnKey)
    targetTemp = takeOffShelf(targetTempKey)
    print("Target Temp %s" %targetTemp)
    print("Current Temp: %s" %temp)
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
#avoid switching pin state and messing up condition    
#    GPIO.setup(fanPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#    fanOn = GPIO.input(fanPin)
    
    if temp > targetTemp:
        GPIO.setup(fanPin, GPIO.OUT)
        GPIO.output(fanPin, GPIO.HIGH)
        print("Fan On")
    else:
        GPIO.setup(fanPin, GPIO.OUT)
        GPIO.output(fanPin, GPIO.LOW)    
        currentFanOn = False
        print("Fan Off")

#separate reporting logic for issues during restart where flag not match reality
    print ("CurrentFanOn: " + str(currentFanOn))
    print ("PriorFanOn: " + str(priorFanOn))
    if currentFanOn != priorFanOn:
        print ("Fans not equal")
        if currentFanOn:
            logData("Exhaust Fan", "Success", "switch", "ON", "Current Temp: " + str(temp))
            print("Fan change - fan ON")
        else:
            logData("Exhaust Fan", "Success", "switch", "OFF", "Current Temp: " + str(temp))
            print ("Fan change - fan OFF")
            
    putOnShelf(priorFanOnKey, currentFanOn)

