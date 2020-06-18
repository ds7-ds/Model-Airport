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
isReady = input()

if(isReady != "Y"):
    # Turn off all devices and shut down model airport
    gpio.setDeviceState("Pavement-Lighting", False)
    gpio.setDeviceState("Backstage-Entrance", False)
    gpio.setDeviceState("Runway-Threshold", False)
    print('[QuickConnect] Exiting...')
    sys.exit(0)

# Run model airport until end time has been reached
# Get input from caller and verify
# If command is legit, run the associated operation

while currentTime < shutOffTime:
    # Initiate airport operation by printing request message to user
    print("ATC Requesting Departure;Type \"SA202 Runway 09 Line Up And Wait\"")
    # Activate the runway and allow robot to move when user enters the right input
    getCommand = input()
    while(getCommand != "SA202 Runway 09 Line Up And Wait"):
        getCommand = input()
    gpio.setDeviceState("Backstage-Entrance", False)
    gpio.setDeviceState("Runway-Threshold", True)
    sleep(3)
    
    # Activate the backstage and allow robot to move
    print("ATC Runway 09 Line Up And Wait;Type \"SA202 Cleared For Takeoff\"")
    getCommand = input()
    while(getCommand != "SA202 Cleared For Takeoff"):
        getCommand = input()
    print("ATC Cleared For Takeoff;Please Wait...")
    gpio.setDeviceState("Runway-Threshold", False)
    gpio.setDeviceState("Backstage-Entrance", True)
    sleep(3)
    # Update time so loop exits correctly
    currentTime = datetime.now()

# Turn off all devices and shut down model airport
print('[QuickConnect] Exiting...')
gpio.setDeviceState("Pavement-Lighting", False)
gpio.setDeviceState("Backstage-Entrance", False)
gpio.setDeviceState("Runway-Threshold", False)
