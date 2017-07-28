#!/bin/bash
# Validation of the MVP 3.0 directory structure and code

RED='\033[0;31m'
NC='\033[0m'

printf "MVP 1.0 Validation script\n"
printf "If any ${RED}RED${NC}, stop and fix it, then re-run this script\n"
printf "\n---Check for directories---\n"

main_dir=/home/pi/Documents/OpenAg-MVP
ui_dir=/home/pi/MVP_UI
python_dir=/home/pi/python

dir=$main_dir
cd  $dir &> /dev/null
if [ $? = 0 ]
then
    printf "$dir OK\n"
else
    printf "${RED}$dir not found, extract from Github${NC}\n"
fi

dir=$main_dir/setup
cd  $dir &> /dev/null
if [ $? = 0 ]
then
    printf "$dir OK\n"
else
    printf "${RED}$dir not found, extract from Github${NC}\n"
fi

dir=$ui_dir
cd  $dir &> /dev/null
if [ $? = 0 ]
then
    printf "$dir OK\n"
else
    printf "${RED}$dir not found, extract from Github${NC}\n"
fi

printf "\n---Check CouchDB ---\n"
curl http://localhost:5984/ &> /dev/null
if [ $? = 0 ]
then
    printf "CouchDB OK \n"
else
    printf "${RED}CouchDB not installed or running${NC}\n"
fi

curl http://localhost:5984/mvp_sensor_data &> /dev/null
if [ $? = 0 ]
then
    printf "Sensor database OK\n"
else
    printf "${RED}Sensor database not created${NC}\n"
fi

curl http://localhost:5984/mvp_sensor_data/_design/doc &> /dev/null
if [ $? = 0 ]
then
    printf "Design Doc installed OK\n"
else
    printf "${RED}Design doc not installed${NC}\n"
fi

printf "\n---Test Variable Persistence---\n"

cmd=$python_dir/testShelf.py
python $cmd &> /dev/null
if [ $? = 0 ]
then
    printf "Variable Persistence OK\n"
else
    printf "${RED}$cmd not working or not installed${NC}\n"
fi

printf "\n---Test Sensors---\n"

cmd=$python_dir/testSI7021.py
python $cmd &> /dev/null
if [ $? = 0 ]
then
    printf "SI7021 OK\n"
else
    printf "${RED}$cmd not working or not installed${NC}\n"
fi

printf "\n---Test Data Logger---\n"

cmd=$python_dir/logSensors.py
python $cmd &> /dev/null
if [ $? = 0 ]
then
    printf "Sensor Logging OK\n"
else
    printf "${RED}$cmd not working or not installed${NC}\n"
fi

python $cmd

printf "\n---Check Output for good data, no Failures or missing values---\n"
read -p "Press Enter to continue"

printf "\n---Test Actuators---\n"

cmd=$python_dir/testThermostat.py
python $cmd &> /dev/null
if [ $? = 0 ]
then
    printf "Thermostat OK\n"
else
    printf "${RED}$cmd not working or not installed${NC}\n"
fi

cmd=$python_dir/setLightOff.py
python $cmd &> /dev/null
if [ $? = 0 ]
then
    printf "Set Lights Off OK\n"
else
    printf "${RED}$cmd not working or not installed${NC}\n"
fi

cmd=$python_dir/setLightOn.py
python $cmd &> /dev/null
if [ $? = 0 ]
then
    printf "Set Lights On OK\n"
else
    printf "${RED}$cmd not working or not installed${NC}\n"
fi

cmd=$main_dir/webcam.sh
bash $cmd &> /dev/null
if [ $? = 0 ]
then
    printf "Webcam OK\n"
else
    printf "${RED}$cmd not working or not installed${NC}\n"
fi

printf "\n---Building website, if you got this far, there is some data---\n"

cmd=$ui_dir/scripts/render.sh
bash $cmd &> /dev/null
if [ $? = 0 ]
then
    printf "Website render OK\n"
else
    printf "${RED}$cmd not working or not installed${NC}\n"
fi

printf "\n---Done---\n"

