# Test retreival of variables

from persistVariable import *

print("***Test variable storage***")
print("Target Temp: %s" %str(getVariable('targetTemp')))
print("Prior Fan On: %s" %str(getVariable('priorFanOn')))
