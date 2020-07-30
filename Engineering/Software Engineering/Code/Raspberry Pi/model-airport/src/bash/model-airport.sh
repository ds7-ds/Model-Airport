#!/bin/bash


echo "Logging bash output to file..."
: '
If flash drive changes, fix the ID by looking it up on CMD using this path ../../media/pi/FLASH-DRIVE-ID
'
flashDriveID=E89D-1133
logFilePath=/media/pi/$flashDriveID/model-airport/logs
cd ~
echo "------------------------------------------------------------" >> log.txt


echo "Waiting for desktop to load..." >> log.txt
read -t 15 -p "Waiting for desktop to load..."
echo


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
	echo "------------------------------------------------------------" >> log.txt
	cp log.txt $logFilePath
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now	
fi


echo "Checking webcam proxy server status..."
echo "Checking webcam proxy server status..." >> log.txt
if wget -q --spider https://whispering-sea-51322.herokuapp.com
then
	echo ONLINE
	echo ONLINE >> log.txt
else
	echo OFFLINE
	echo OFFLINE >> log.txt
	echo "Shutting down in 30 seconds..." >> log.txt
	echo "------------------------------------------------------------" >> log.txt
	cp log.txt $logFilePath
	read -t 30 -p "Shutting down in 30 seconds..."
	sudo shutdown -h now
fi


echo "Finding model airport control and webcam software..."
echo "Finding model airport control and webcam software..." >> log.txt
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
		cd ~
		echo "File found..." >> log.txt
	else
		echo "File not found..."
		cd ~
		echo "File not found..." >> log.txt
		echo "Shutting down in 30 seconds..." >> log.txt
		echo "------------------------------------------------------------" >> log.txt
		cp log.txt $logFilePath
		read -t 30 -p "Shutting down in 30 seconds..."
		sudo shutdown -h now
	fi
else
	echo "Directory not found..."
	cd ~
	echo "Directory not found..." >> log.txt
	echo "Shutting down in 30 seconds..." >> log.txt
	echo "------------------------------------------------------------" >> log.txt
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
		read -t 1
		cd ~
		echo $(date) >> log.txt
		ps -eaf | grep node | grep -v -e bash -e grep | awk '/model-airport.js/ {print $2 " " $9}' >> log.txt
		ps -eaf | grep node | grep -v -e bash -e grep | awk '/www/ {print $2 " " $9}' >> log.txt
	fi
	read -t 10 -p "Checking in 10 seconds..."
	echo 
	runTimeInt=$(date +%s)
done


cd ~
echo "Shutting down software and RPi..." >> log.txt
echo "------------------------------------------------------------" >> log.txt
cp log.txt $logFilePath
read -t 10 -p "Shutting down software and RPi..."
: '
	stackoverflow.com/questions/21470362/find-the-pids-of-running-processes-and-store-as-an-array
'
for pid in `ps -ef | pgrep node`; do kill $pid; done
sudo shutdown -h now
