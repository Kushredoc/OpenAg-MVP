# Test of the thermostat
# Low value should turn off
# High value should turn on

from adjustThermostat import *

print ("Check Thermostat Low")
print (adjustThermostat(15))
print ("Check Thermostat High")
print (adjustThermostat(75))
