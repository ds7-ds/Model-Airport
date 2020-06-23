# Import libraries
import sys
from time import sleep
from ModelAirportGPIO import ModelAirportGPIO
from datetime import datetime, timedelta

# Setup GPIO
print("[QuickConnect] Setting up GPIO...")
gpio = ModelAirportGPIO()

# Turn lights on
gpio.setDeviceState("Pavement-Lighting", True)

# Align robot at the backstage
print("[QuickConnect] Waiting for robot to align...")
gpio.setDeviceState("Backstage-Entrance", True)
sleep(25)

# Determine end time for program
currentTime = datetime.now()
shutOffTime = currentTime + timedelta(minutes = 75)

# Determine if caller is ready to run the airport
print("[QuickConnect] Ready?")
isReady = input()
while isReady != "Yes":
    # Wait for 10 seconds and then ask again
    sleep(10)
    currentTime = datetime.now()
    # If still no response and past closing time, shut down model airport
    if currentTime > shutOffTime:
        print('[QuickConnect] Exiting...')
        gpio.setDeviceState("Pavement-Lighting", False)
        gpio.setDeviceState("Backstage-Entrance", False)
        gpio.setDeviceState("Runway-Threshold", False)
        sys.exit(0)
    print("[QuickConnect] Ready?")
    isReady = input()

# Run model airport until end time has been reached
# Get input from caller and verify
# If command is legit, run the associated operation

while currentTime < shutOffTime:
    # Initiate airport operation by printing request message to user
    print("ATC Requesting Departure;SA202 Runway 09 Line Up And Wait")
    # Activate the runway and allow robot to move when user enters the right input
    getCommand = input()
    while(getCommand != "SA202 Runway 09 Line Up And Wait"):
        print("ATC Say Again;SA202 Runway 09 Line Up And Wait")
        getCommand = input()
    print("ATC Runway 09 Line Up And Wait;Please Wait...")
    print("[QuickConnect] Activating Runway...")
    gpio.setDeviceState("Backstage-Entrance", False)
    gpio.setDeviceState("Runway-Threshold", True)
    sleep(15)
    
    # Activate the backstage and allow robot to move
    print("Waiting for your response...;SA202 Cleared For Takeoff")
    getCommand = input()
    while(getCommand != "SA202 Cleared For Takeoff"):
        print("ATC Say Again;SA202 Cleared For Takeoff")
        getCommand = input()
    print("[QuickConnect] Activating Backstage...")
    print("ATC Cleared For Takeoff;Please Wait...")
    gpio.setDeviceState("Runway-Threshold", False)
    gpio.setDeviceState("Backstage-Entrance", True)
    sleep(15)
    # Update time so loop exits correctly
    currentTime = datetime.now()

# Turn off all devices and shut down model airport
print('[QuickConnect] Exiting...')
gpio.setDeviceState("Pavement-Lighting", False)
gpio.setDeviceState("Backstage-Entrance", False)
gpio.setDeviceState("Runway-Threshold", False)
