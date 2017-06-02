#write out current crontab
crontab -l > mycron
#Add sensor logging, run every 20 minutes
echo "/20 * * * * python /home/pi/python/logSensors.py"
#add temperature checking every minute
echo "/1 * * * * python /home/pi/python/thermostat.py"
#take photo every 4 hours when lights are on
echo "6,12,4,8 * * * /home/pi/Documents/OpenAg-MVP/webcam.sh"
