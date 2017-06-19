#A script to test the functions of the OpenAg-MVP routines
#Run this to validate code and that things are working correctly

from si7021 import *
from bookshelf import *
from adjustThermostat import *
from setLightOn import *
from setLightOff import *

try:
    print ("Execute getTempC")
    print (getTempC())
except (IOError):
    print ("Failure to get Temperature")

try:
    print ("Execute getHumidity")    
    print (getHumidity())
except (IOError):
    print ("Failure to get Humidity")

try:
    print ("Get from Bookshelf")    
    print (takeOffShelf("targetTemp"))
except (RuntimeError):    
    print ("Failure to get value for key")

try:
    print ("Check Thermostat High")
    print (adjustThermostat(75))
except (RuntimeError):
    print ("Failure adjusting thermostat: High")

try:
    print ("Check Thermostat Low")
    print (adjustThermostat(15))
except (RuntimeError):
    print ("Failure adjusting thermostat: Low")

try:
    print ("Turn Light On")
    print (setLightOn())
except (RuntimeError):
    print ("Failure to turn light ON")    
   
try:
    print ("Turn Light OFF")
    print (setLightOff())
except (RuntimeError):
    print ("Failure to turn light OFF")    


