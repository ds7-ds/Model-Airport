#!/bin/bash


echo "Logging bash output to file..."
flashDriveID=E89D-1133
logFilePath=/media/pi/$flashDriveID/model-airport/logs
echo $(date) >> log.txt


read -t 2 -p "Waiting for desktop to load..."
echo ""
echo "Waiting for desktop to load..." >> log.txt


echo "Checking messaging proxy server status..."
echo "Checking messaging proxy server status..." >> log.txt
if wget -q --spider https://model-airport.herokuapp.com
then
	echo ONLINE
	echo ONLINE >> log.txt
else
	echo OFFLINE
	echo OFFLINE >> log.txt
	echo "Shutting down in 30 seconds..." >> log.txt
	cp log.txt $logFilePath
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now	
fi


echo "Checking webcam proxy server status..."
if wget -q --spider https://whispering-sea-51322.herokuapp.com
then
	echo ONLINE
	echo ONLINE >> log.txt
else
	echo OFFLINE
	echo OFFLINE >> log.txt
	echo "Shutting down in 30 seconds..." >> log.txt
	cp log.txt $logFilePath
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now
fi


echo "Finding model airport control and webcam software..."
echo "Finding model airport control and webcam software..." >> log.txt
: '
If flash drive changes, fix the ID by looking it up on CMD using this path ../../media/pi/FLASH-DRIVE-ID
'
controlSoftwareFilePath=/media/pi/$flashDriveID/model-airport/src/node/model-airport-core
webcamSoftwareFilePath=/media/pi/$flashDriveID/model-airport/src/node/model-airport-webcam-proxy-local/bin
if [ -d $controlSoftwareFilePath ]
then
	echo "Directory found..."
	echo "Directory found..." >> log.txt
	cd $controlSoftwareFilePath
	if [ -f model-airport.js ]
	then
		echo "File found..."
		echo "File found..." >> log.txt
	else
		echo "File not found..."
		echo "File not found..." >> log.txt
		echo "Shutting down in 30 seconds..." >> log.txt
	  cp log.txt $logFilePath
		read -t 30 -p "Shutting down in 30 seconds..."
		sudo shutdown -h now
	fi
else
	echo "Directory not found..."
	echo "Directory not found..." >> log.txt
	echo "Shutting down in 30 seconds..." >> log.txt
  cp log.txt $logFilePath
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now
fi


echo "Determining start-up and shut-down times..."
echo "Determining start-up and shut-down times..." >> log.txt
startTime=$(date)
startTimeInt=$(date +%s)
endTime=$(date --date='35 minutes')
endTimeInt=$(date --date='35 minutes' +%s)
echo $startTime
echo $startTime >> log.txt
echo $endTime
echo $endTime >> log.txt


echo "Running software until shut-down time..."
echo "Running software until shut-down time..." >> log.txt
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


echo "Shutting down software and RPi..." >> log.txt
cp log.txt $logFilePath
read -t 10 -p "Shutting down software and RPi..."
: '
	stackoverflow.com/questions/21470362/find-the-pids-of-running-processes-and-store-as-an-array
'
for pid in `ps -ef | pgrep node`; do kill $pid; done
sudo shutdown -h now
