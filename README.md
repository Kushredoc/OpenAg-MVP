# OpenAg-MVP
Code and instructions for building the 'brain' of the controled environment hydroponics unit.
It is mostly a collection of python code that runs on a Raspberry Pi (or similar device).  See the OpenAg [forums](http://forum.openag.media.mit.edu/) for discussion and issues:


The MVP (Minimal Viable Product) is a simplified version of the MIT OpenAg Food Computer.


## Architecture:
The MVP brain is mostly python scripts involed using cron as the scheduler.  
Python and cron are built into the Raspbian OS, and the Raspberry library to manipulate GPIO pins is already loaded.

The Python is modular so additions and changes can easily be made without affecting the whole system.

- Scheduling Control (cron)
    - Image capture (webcam.sh)
    - Log Sensors (logSensors.py)
    - Check Light (ambientLight.py)
    - Check Temperature (thermostat.py)

shelf is used for persisting variables (target temperature, prior fan state, prior light state).  These variables must be initialized before the python code will correctly run, this is done by running the Python file /home/pi/python.setup.py.
**NOTE** In my setup, the python icon runs version 3, while clicking a file runs 2.7.9; due to significant differences between versions you have to have consistency with what is run.

Data storage is in a csv formatted (without header) flat file (/home/pi/Documents/OpenAg-MVP/data.txt)

For more information on Cron [see:](https://docs.oracle.com/cd/E23824_01/html/821-1451/sysrescron-24589.html)

## Hardware Build:

**Fan:**
There are two fans, one for circulation and one for exhausting excess heat  These can run off the Raspberry's 5V or from a external 12V transformer

**Temperature/Humidity Sensor**
A si7021 sensor on an I2C bus is used for temperature and humidity.  See the following for (instructions)[https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor/overview] on use and wiring.

**Webcam**
A standard USB camera is used for imaging (though the Raspberry Pi camera is an option).  See [here](https://www.raspberrypi.org/documentation/usage/webcams/) for instructions

**Relay**
A set of relays controled by GPIO pins is used to turn lights on and off (120V), and the exhaust fan (12V)

# Pin Assignment:
Refer to the following [diagram](https://docs.particle.io/datasheets/raspberrypi-datasheet/#pin-out-diagram) for the Raspberry's pin names:

Code follows the board number convention.

- '3 - SDA to si7021'
- '5 - SCL to si7021'
- '29 - light relay (relay #4)'
- '31 - (reserved for relay #3)'
- '33 - (reserved for relay #2)'
- '35 - GPIO13 fan control (relay #1)'


## Build Activities
### Assumptions:
1. NOOB install of Raspbian on Raspberry Pi
2. The Raspbian system has been configured 
    - for localization (time, timezone)
    - wifi is established and connected
    - I2C has been enabled
2. 32G SD card to hold data
3. Sensors and relay are wired to the Pi.  If you try to run the code without sensors, some of it will error out (I/O Error, I noticed in the getTempC() function).  This will ripple up to error out the cron job for logSensorData.py.

### Software Build Steps

 - Install fswebcam
> sudo apt-get install fswebcam

- Download code from [Github](https://github.com/webbhm/OpenAg-MVP).  Click on the zip file to open it, and move the files to the appropriate location.
    - Right click on the file OpenAg-MVP-master.zip and select 'Extract Here', this will create a directory 'OpenAg-MVP-master that contains the files.
    - Drag the sub-directory 'OpenAg-MVP to the 'Documents' directory
    - Drag the sub-directory 'python' to the 'pi' directory

- initialized shelf with the persistent variables.  Double click on the file /home/pi/pythin/setup.py, and Python will open.  Click on Run menu, then Run Module sub-menu and run the file.

- From a terminal, type:

> crontab -e

- Select the second editor option
- Scroll to the bottom of the file and type the following

> */1 * * * * python /home/pi/python/thermostat.py

> */5 * * * * python /home/pi/python/ambientLight.py

> */20 * * * * python /home/pi/python/logSensors.py

> 1 6-22 * * * /home/pi/Documents/OpenAg-MVP/webcam.sh

## Bill of Materials:
- Raspberry Pi
- 32G SD card
- SI7021 temperature/humidity sensor
- Wire or jumpers
- Relay

## To Do:
1. Add exception handling to the Python code
2. Add a watchdog to the Raspberry
3. Fix the cron email notifications

## Future Development (in no priority):
- GUI interface for setting persistent variables (could be local)
- Web interface for charting of data
- Possible move of data to database
- Add a paristolic pump for when have to be away for a while and need to refill the reservoir (Could be a separate board using Particle).
- Light control for controlable LEDs
