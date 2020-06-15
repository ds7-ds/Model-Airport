from time import sleep
from ModelAirportGPIO import ModelAirportGPIO
from datetime import datetime, timedelta

print("[ModelAirportAuto] Setting up GPIO...")
gpio = ModelAirportGPIO()

print("[ModelAirportAuto] Turning lights on...")
gpio.setDeviceState("Pavement-Lighting", True)

print("[ModelAirportAuto] Waiting for robot to align...")
gpio.setDeviceState("Backstage-Entrance", True)
sleep(15)

print("[ModelAirportAuto] Running on automatic mode...")
currentTime = datetime.now()
shutOffTime = currentTime + timedelta(minutes = 10)

while currentTime < shutOffTime:
    print("[ModelAirportAuto] Runway activated...")
    gpio.setDeviceState("Backstage-Entrance", False)
    gpio.setDeviceState("Runway-Threshold", True)
    sleep(20)
    print("[ModelAirportAuto] Backstage activated...")
    gpio.setDeviceState("Runway-Threshold", False)
    gpio.setDeviceState("Backstage-Entrance", True)
    sleep(20)
    currentTime = datetime.now()

print("[ModelAirportAuto] Ending operations...")
gpio.setDeviceState("Pavement-Lighting", False)
gpio.setDeviceState("Backstage-Entrance", False)
gpio.setDeviceState("Runway-Threshold", False)
