from si7021 import getTempC, getHumidity

print("***Test SI7021 Sensor***")
print ("Temperature in Celsius is : %.2f C" %getTempC())
print ("Relative Humidity is : %.2f %%" %getHumidity())
