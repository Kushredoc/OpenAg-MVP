#Check sensors and log to file
from si7021 import getTempC, getHumidity
from logData import logData

logData("Temperature", "{:10.1f}".format(getTempC()), '')
logData("Humidity", "{:10.1f}".format(getHumidity()), '')

