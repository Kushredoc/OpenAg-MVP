#A script to test the functions of the OpenAg-MVP routines
#Run this to validate code and that things are working correctly

from checkLight import *
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
    print ("Check Lights")    
    print (checkLight())
except (RuntimeError):
    print ("Failure in checkLight")

try:
    print ("Get from Bookshelf")    
    print (takeOffShelf("priorLightOn"))
except (RuntimeError):    
    print ("Failure to get value for key")            
    


