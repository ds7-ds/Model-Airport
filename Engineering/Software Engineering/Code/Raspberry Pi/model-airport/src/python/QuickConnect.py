# Import libraries
import sys
from time import sleep
from ModelAirportGPIO import ModelAirportGPIO
from datetime import datetime, timedelta

# Setup GPIO
gpio = ModelAirportGPIO()

# Turn lights on
gpio.setDeviceState("Pavement-Lighting", True)

# Align robot at the backstage
gpio.setDeviceState("Backstage-Entrance", True)
sleep(1)

# Determine end time for program
currentTime = datetime.now()
shutOffTime = currentTime + timedelta(seconds = 30)

# Determine if caller is ready to run the airport
print("[QuickConnect][Input] Ready?")
#isReady = stdin.readline()
isReady = input()

if(isReady != "Y"):
    # Turn off all devices and shut down model airport
    gpio.setDeviceState("Pavement-Lighting", False)
    gpio.setDeviceState("Backstage-Entrance", False)
    gpio.setDeviceState("Runway-Threshold", False)
    print('[QuickConnect] Exiting...')
    sys.exit(0)

# Run model airport until end time has been reached
while currentTime < shutOffTime:
    # Activate the runway and allow robot to move
    gpio.setDeviceState("Backstage-Entrance", False)
    gpio.setDeviceState("Runway-Threshold", True)
    sleep(20)
    # Activate the backstage and allow robot to move
    gpio.setDeviceState("Runway-Threshold", False)
    gpio.setDeviceState("Backstage-Entrance", True)
    sleep(20)
    # Update time so loop exits correctly
    currentTime = datetime.now()

# Turn off all devices and shut down model airport
print('[QuickConnect] Exiting...')
gpio.setDeviceState("Pavement-Lighting", False)
gpio.setDeviceState("Backstage-Entrance", False)
gpio.setDeviceState("Runway-Threshold", False)
