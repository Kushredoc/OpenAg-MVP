#External module imports
import RPi.GPIO as GPIO
import time

def getCellTime():
    "Get the time it takes to charge a capacitor with the photocell, this is a rough measurement of light"
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    photoCellPin = 37
    reading = 0
    GPIO.setup(photoCellPin, GPIO.OUT)
    GPIO.output(photoCellPin, GPIO.LOW)
    time.sleep(1)
    GPIO.setup(photoCellPin, GPIO.IN)
    while not GPIO.input(photoCellPin):
        reading += 1
    print ("Light is: %s" %reading)
    return reading
    

