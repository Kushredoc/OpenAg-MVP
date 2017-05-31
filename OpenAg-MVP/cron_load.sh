#write out current crontab
crontab -l > mycron
#Add sensor logging, run every 20 minutes
echo "/20 * * * * python /home/pi/python/logSensors.py"
#add temperature checking every minute
echo "/1 * * * * python /home/pi/python/thermostat.py"
#add light checking every five minutes
echo "/5 * * * * python /home/pi/python/ambientLight.py"
#take photo every 4 hours
echo "* /4 * * * /home/pi/Documents/OpenAg-MVP/webcam.sh"