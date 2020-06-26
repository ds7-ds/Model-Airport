#!/bin/bash

read -t 15 -p "Waiting for desktop to load..."
echo

echo "Checking proxy server status..."
if wget -q --spider https://model-airport.herokuapp.com
then
	echo ONLINE
else
	echo OFFLINE
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now	
fi

echo "Finding model airport software..."
: '
If flash drive changes, fix the ID by looking it up on CMD using this path ../../media/pi/FLASH-DRIVE-ID
'
flashDriveID=E89D-1133
filePath=../../../../media/pi/$flashDriveID/model-airport/src/node
if [ -d $filePath ]
then
	echo "Directory found..."
	cd $filePath
	if [ -f model-airport.js ]
	then
		echo "File found..."
	else
		echo "File not found..."
		read -t 30 -p "Shutting down in 30 seconds..."
		sudo shutdown -h now
	fi
else
	echo "Directory not found..."
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now
fi


echo "Determining start-up and shut-down times..."
startTime=$(date)
startTimeInt=$(date +%s)
endTime=$(date --date='40 minutes')
endTimeInt=$(date --date='40 minutes' +%s)
echo $startTime
echo $endTime



echo "Running software until shut-down time..."
runTimeInt=$(date +%s)
while [ $runTimeInt -le $endTimeInt ]
do
	if ! pgrep node
	then
		echo "Restarting..."
		lxterminal -e 'bash -c "node model-airport.js; exit"'
	fi
	read -t 10 -p "Checking in 10 seconds..."
	echo 
	runTimeInt=$(date +%s)
done


read -t 10 -p "Shutting down software and RPi..."
if pgrep node
then
	softwarePID=$(pgrep node)
	kill $softwarePID
fi
sudo shutdown -h now