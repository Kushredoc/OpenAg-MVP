#!/usr/bin/python

from thermostat import adjustThermostat
from si7021 import getTempC
from logData import logData

try:
    temp = getTempC()
    adjustThermostat(temp)  
except (IOError):
    print("Failure to get temperature, no sensor found; check pins and sensor")
    logData("si7921-top", "Failure", "temperature", "", "Sensor not found")

  
    
