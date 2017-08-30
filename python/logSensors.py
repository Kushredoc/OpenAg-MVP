#!/usr/bin/python

#Check sensors and log to file
from si7021 import getTempC, getHumidity
from logData import logData

try:
    temp = getTempC()
    logData("si7921_top", "Success", "temperature", "{:10.1f}".format(temp), '')
except (IOError):    
        logData("si7921_top", "Failure", "temperature", '', '')

try:
    humid = getHumidity()
    logData("si7021_top", "Success", "humidity", "{:10.1f}".format(humid), '')
except (IOError):    
        logData("si7921_top", "Failure", "humidity", '', '')

