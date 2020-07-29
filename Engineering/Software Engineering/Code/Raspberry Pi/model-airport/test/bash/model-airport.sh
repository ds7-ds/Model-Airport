#!/bin/bash


read -t 2 -p "Waiting for desktop to load..."
echo ""


echo "Logging bash output to file..."
flashDriveID=E89D-1133
logFilePath=/media/pi/$flashDriveID/model-airport/logs
echo $(date) >> log.txt
cp log.txt $logFilePath

echo "Checking messaging proxy server status..."
if wget -q --spider https://model-airport.herokuapp.com
then
	echo ONLINE
else
	echo OFFLINE
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now	
fi


echo "Checking webcam proxy server status..."
if wget -q --spider https://whispering-sea-51322.herokuapp.com
then
	echo ONLINE
else
	echo OFFLINE
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now
fi


echo "Finding model airport control and webcam software..."
: '
If flash drive changes, fix the ID by looking it up on CMD using this path ../../media/pi/FLASH-DRIVE-ID
'
controlSoftwareFilePath=/media/pi/$flashDriveID/model-airport/src/node/model-airport-core
webcamSoftwareFilePath=/media/pi/$flashDriveID/model-airport/src/node/model-airport-webcam-proxy-local/bin
if [ -d $controlSoftwareFilePath ]
then
	echo "Directory found..."
	cd $controlSoftwareFilePath
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
endTime=$(date --date='35 minutes')
endTimeInt=$(date --date='35 minutes' +%s)
echo $startTime
echo $endTime


echo "Running software until shut-down time..."
runTimeInt=$(date +%s)
while [ $runTimeInt -le $endTimeInt ]
do
	if ! pgrep node
	then
		echo "Restarting..."
		cd $controlSoftwareFilePath
		lxterminal -e 'bash -c "node model-airport.js; exit"'
		cd $webcamSoftwareFilePath
		lxterminal -e 'bash -c "node www; exit"'
	fi
	read -t 10 -p "Checking in 10 seconds..."
	echo 
	runTimeInt=$(date +%s)
done


read -t 10 -p "Shutting down software and RPi..."
: '
	stackoverflow.com/questions/21470362/find-the-pids-of-running-processes-and-store-as-an-array
'
for pid in `ps -ef | pgrep node`; do kill $pid; done
sudo shutdown -h now
