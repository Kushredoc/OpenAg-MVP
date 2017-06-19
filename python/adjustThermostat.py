from thermostat import adjustThermostat
from si7021 import getTempC
from logData import logData

try:
    temp = getTempC()
    adjustThermostat(temp)  
except (IOError):
    print("Failure to get temperature, no sensor found; check pins and sensor")
    logData("Temp", "Failure", "Sensor not found")

  
    
