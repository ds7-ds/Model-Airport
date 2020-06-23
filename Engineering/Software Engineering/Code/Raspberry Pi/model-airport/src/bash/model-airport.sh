#!/bin/bash


echo "Finding model airport software..."
if [ -d ../../../../media/pi/9484-DE4D/model-airport/src/node ]
then
	echo "Directory found..."
	cd ../../../../media/pi/9484-DE4D/model-airport/src/node
	if [ -f model-airport.js ]
	then
		echo "File found..."
	else
		echo "File not found..."
		read -t 30 -p "Closing in 30 seconds..."
		exit
	fi
else
	echo "Directory not found..."
	read -t 30 -p "Closing in 30 seconds..."
	exit
fi


echo "Determining start-up and shut-down times..."
startTime=$(date)
startTimeInt=$(date +%s)
endTime=$(date --date='30 minutes')
endTimeInt=$(date --date='30 minutes' +%s)
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


echo "Shutting down software and RPi..."
if pgrep node
then
	softwarePID=$(pgrep node)
	kill $softwarePID
fi


