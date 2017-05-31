This is a set of code to control the OpenAg MVP (Minimal Viable Product).  It is mostly a collection of python code that runs on the Raspberry Pi.  See the OpenAg forums for discussion and issues:
http://forum.openag.media.mit.edu/


Architecture:
The MVP brain is mostly python scripts involed using cron as the scheduler.  
Python and cron are built into the Raspbian OS, and the Raspberry library to manipulate GPIO pins is already loaded.

The Python is modular so additions and changes can easily be made without affecting the whole system.

Scheduling Control (cron)
    Image capture (webcam.sh)
    Log Sensors (logSensors.py)
    Check Light (ambientLight.py)
    Check Temperature (thermostat.py)

shelf is used for persisting variables (target temperature, prior fan state, prior light state).  It must be initialized before the python code will correctly run.

Data storage is in a csv formatted (without header) flat file (/home/pi/Documents/OpenAg-MVP/data.txt)

For more information on Cron see:
https://docs.oracle.com/cd/E23824_01/html/821-1451/sysrescron-24589.html

Hardware Build:
Fan:
There are two flavors of the fan build, with two options each.  With any of the four options, the software is the same as the GPIO pin will control the transistor or relay with the same logic (assume HIGH is ON).
Option 1) Use a transistor to control the power to the fan (5 volts from the breadboard, or 12 volts from a small transformer)
https://raspberrypi.stackexchange.com/questions/57609/can-i-use-a-transistor-as-a-relay-with-the-pi
Google: "raspberry pi gpio transistor switch" for more examples

Option 2) Use a relay to manage power, either 12 volts from a transformer, or 120 volts with a transformer plugged in.

Light Sensor
Temperature/Humidity Sensor
https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor/overview

Webcam
https://www.raspberrypi.org/documentation/usage/webcams/


Pin Assignment:
https://docs.particle.io/datasheets/raspberrypi-datasheet/#pin-out-diagram
3 - SDA to si7021
5 - SCL to si7021
33 - GPIO13 fan control
37 - GPIO26 photocell input

Build Activities
Assumptions:
1) NOOB install of Raspbian on Raspberry Pi
2) 32G SD card to hold data

Install fswebcam
sudo apt-get install fswebcam

Build directories to hold files

mkdir /home/pi/Documents/OpenAg-MVP
//webcam images go here
mkdir /home/pi/Documents/OpenAg-MVP/webcam
//python code goes here
mkdir /home/pi/python

Download from 

run from Terminal
//initialized shelf with the persistent variables
python /home/pi/python/setup.py
//loads the crontab file with the jobs to run
/home/pi/Documents/OpenAg-MVP/cron_load.sh

Bill of Materials:
1) Raspberry Pi
2) 32G SD card
3) Breadboard
4) Pi breakout board
5) SI7021 temperature/humidity sensor
6) Wire or jumpers
7) Photocell
8) Capacitor 1uF
9) Transistor
10) Resistor

To Do:
1) Add exception handling to the Python code
2) Add a watchdog to the Raspberry
3) Fix the cron email notifications
