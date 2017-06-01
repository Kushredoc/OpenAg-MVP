#A script to test the functions of the OpenAg-MVP routines
#Run this to validate code and that things are working correctly

from photoCell import *
from si7021 import *
from bookshelf import *

try:
    print ("Execute getTempC")
    print (getTempC())
except (RuntimeError):
    print ("Failure to get Temperature")

try:
    print ("Execute getHumidity")    
    print (getHumidity())
except (RuntimeError):
    print ("Failure to get Humidity")

try:
    print ("Execute getCellTime of photocell")    
    print (getCellTime())
except (RuntimeError):
    print ("Failure to get cell time")

try:
    print ("Get from Bookshelf")    
    print (takeOffShelf("priorLightOn"))
except (RuntimeError):    
    print ("Failure to get value for key")            
    
try:
    print ("Execute checkLightState - determine if lights on or off")    
    print (checkLightState())
except (RuntimeError):
    print ("Failure to check lights")



