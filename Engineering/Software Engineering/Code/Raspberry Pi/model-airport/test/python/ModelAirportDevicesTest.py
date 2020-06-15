from time import sleep
from ModelAirportGPIO import ModelAirportGPIO

print("[ModelAirportDevicesTest] Setting up GPIO...")
gpio = ModelAirportGPIO()

print("[ModelAirportDevicesTest] Testing all devices...")

gpio.setDeviceState("Pavement-Lighting", True)
gpio.setDeviceState("Backstage-Entrance", True)
gpio.setDeviceState("Runway-Threshold", True)
print(gpio.getDeviceState("Backstage-Entrance"))
print(gpio.getDeviceState("Runway-Threshold"))

sleep(5)

print("[ModelAirportDevicesTest] Ending test...")

gpio.setDeviceState("Pavement-Lighting", False)
gpio.setDeviceState("Backstage-Entrance", False)
gpio.setDeviceState("Runway-Threshold", False)
print(gpio.getDeviceState("Backstage-Entrance"))
print(gpio.getDeviceState("Runway-Threshold"))

