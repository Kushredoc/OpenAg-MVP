# OpenAg-MVP
Code and instructions for building the 'brain' of the controled environment hydroponics unit.
It is mostly a collection of python code that runs on a Raspberry Pi (or similar device).  See the OpenAg [forums](http://forum.openag.media.mit.edu/) for discussion and issues:

The MVP (Minimal Viable Product) is a simplified version of the MIT OpenAg Food Computer.

##Changes

6/21: Added logging of sensor data to CouchDB
7/6/2017 NOTE: webcam.sh is being moved to OpenAg_MVP_UI directory.  This move requires a change to crontab
7/16/2017 Update documentation, minor corrections
7/26/2017 Added validation script for release testing

## Architecture:
The MVP brain is mostly python scripts involed using cron as the scheduler.  
Python and cron are built into the Raspbian OS, and the Raspberry library to manipulate GPIO pins is already loaded.

The Python is modular so additions and changes can easily be made without affecting the whole system.

- Scheduling Control (cron)
    - Image capture (webcam.sh)
    - Log Sensors (logSensors.py)
    - Turn lights On (setLightOn.py)
    _ Tirm lights Off (setLightOff.py)
    - Check Temperature (adjustThermostat.py)

shelf is used for persisting variables (target temperature, prior fan state).  These variables must be initialized before the python code will correctly run, this is done by running the Python file /home/pi/python.setup.py.

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
>
### Software Build Steps

NOTE:
Different builds/downloads of NOOBS seem to have different versions of Python set up as default, though both are likely installed, and the IDE for 2 and 3 are in the programming menu.  This code will work with 2 or 3, but you cannot switch back and forth.  Check which version is the default for your system and stick with it.  To find which version you default to, open a terminal window and type:

```python```

This will display the version number on the first line.  It will also put you into a Python command line - press CTL-D to exit it.

Open this file in your Raspberry Pi so you can cut and paste command line instructions and cron commands.  Highlight the line you want and use Ctl-C to copy it.  On the Terminal window click on "Edit" and select "Paste" (terminal windows don't use the standard Ctl-V to paste). 

- Update the software:

> sudo apt-get update -y

- Upgrade the software, this should default you to running Python 3

> sudo apt-get upgrade -y

- Install fswebcam
> sudo apt-get install fswebcam

- Download the zip file of code from [Github](https://github.com/webbhm/OpenAg-MVP).  Open a file browser and go to Downloads.  You should find the zip file (OpenAg-MVP-master.zip) here. Right click on the zip file to open it, and move the files to the appropriate location.
    - Right click on the file OpenAg-MVP-master.zip and select 'Extract Here', this will create a directory 'OpenAg-MVP-master that contains the files.
    - Click on the new directory (OpenAg-MVP-master) to open it
    - Drag the sub-directory 'OpenAg-MVP to the 'Documents' directory
    - Drag the sub-directory 'python' to the 'pi' directory
    - if it does not already exist, create a sub-directory in OpenAg-MVP called "webcam".  This will hold the camera images.  If it does not exist, the cron job will fail.

- Make webcam.sh executable
    - from the file manager, go to the /home/pi/Documents/OpenAg-MVP directory
    - right click on webcam.sh and select Properties from the menu
    - select the Permissions tab, and on the Execute drop-down select 'Anyone' and hit 'OK'
    
- initialized shelf with the persistent variables.  Double click on the file /home/pi/python/setup.py, and Python will open.  Click on Run menu, then Run Module sub-menu and run the file.

NOTE: There are issues with shelf and version compatability (different storage types in diffrent versions).  If after initializing shelf you find errors regarding "db type", you likely initialized with one version of Python, and are running a different one.  The solution is to note the version your code defaults to running, delete /home/pi/python/bookshelf.db, and re-run the setup.py with the default version.

NOTE: The crontab editor is old and works different from most newer editors (it is command line oriented, and pre-dates graphical interfaces).  To save the file you type Ctl-X, they type 'y' to confirm that you want to save the file.  Read the key commands at the bottom of the editor.

- Open a terminal window and type:
> crontab -e
- Select the second editor option
- Scroll to the bottom of the file and cut & paste the following:

```
*/1 * * * * python /home/pi/python/adjustThermostat.py
0 6 * * * python /home/pi/python/setLightOn.py
30 22 * * * python /home/pi/python/setLightOff.py
*/20 * * * * python /home/pi/python/logSensors.py
1 6-22 * * * /home/pi/Documents/OpenAg-MVP/webcam.sh
```
- adjustThermostat checks the temperature and adjusts the fan every minute
- setLightOn turns lights on at 6AM (change for your needs)
- setLightOff turns lights off at 10:30PM (change for your needs)
- logSensors writes out the temperature and humidity every 20 minutes
- webcam.sh takes an image every hour between 6am and 10pm; avoiding pictures when the lights are out.

## CouchDB Install

- build couchdb

> sudo apt-get install couchdb -y

The -y will accept all the questions with yes

Modify the default.ini initialization file to allow outside access

> sudo leafpad /etc/couchdb/default.ini

  - Click the "Search" then "Find" menu and type HTTPD, and click the "Find" button.
  - Under the HTTPD line,change binding address to: bind_address = 0.0.0.0
  - Click "File" and "Save", then exit the editor.
  - Reboot so this takes effect (From the Main menu, click "Shutdown" and on the sub-menu click "Reboot"

Add a database to hold the sensor output

> curl -X PUT http://localhost:5984/mvp_sensor_data

## Test The New System

NOTE: The validation script assumes you have installed the [UI](ttps://github.com/webbhm/OpenAg_MVP_UI).  You will see errors if the UI in not installed.

  - See the [wiki](https://wiki.openag.media.mit.edu/mvp_debugging) for more details.
  - There is a validation script that goes through almost all of the systems, starting low level with the sensors and working up through the actuators and finally the UI (it is assumed the UI has also been installed.  The script stops part way through (after logging data) so you can look at the output for logging data errors.  After scrolling through the output, press "ENTER" to continue the script.  You will be back at a command prompt when it finishes.
  - To run the script, from a terminal window type:

> bash /home/pi/Documents/OpenAg-MVP/setup/Validate.sh

NOTE"The Validation script (and all *.sh shell scripts) neet to have their permissions set so they are executable.  From the file browser, go to MVP/setup and right mouse click on validate.sh, from the drop down menu select "Properties".  In the "File Properties" window select the "Permissions" tab.  Select "Anyone" for the "Execute" property.  If you are working from the command line, and not from a GUI, then use the following:

> sudo chmod 755 home/pi/MVP/setup/Validate.sh

- This file should run with NO ERRORS.  If any errors are found (indicated by the RED font), then start with the first one,  fix it, and re-run the validation script.  Repeat this process until there are no errors.
  - This script will generate data to the database and take a picture, so the UI charts should have at least one data point when you look at them.  From a browser on the Raspberry Pi, enter:
  
> http://localhost:8000

  - If you are seeing data in the charts, and a picture, then you have successfully built and installed the MVP, and are up and running!!
  
## Final Step ##
  - Now that you have it running, make a backup SD card.  Install a blank SD card (or one that you don't mind being erased) into a USB card reader, and put it into one of the Raspberry Pi's USB ports.  From the main Raspberry menu select "Accessories", then "SD Card Copier". Under "Copy To Device" select the card (usually the second one) and click "Start".  It will take a couple of minutes, but you now have another good copy of the software.

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
4. Automate the build process
    - file movement (clone process?)
    - crontab loading

## Future Development (in no priority):
- GUI interface for setting persistent variables (could be local)
- Web interface for charting of data
- Possible move of data to database
- Add a paristolic pump for when have to be away for a while and need to refill the reservoir (Could be a separate board using Particle).
- Light control for controlable LEDs
