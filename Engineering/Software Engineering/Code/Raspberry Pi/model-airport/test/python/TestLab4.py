from time import sleep
from ModelAirportGPIO import ModelAirportGPIO

print("[TestLab4] Testing Model Airport Robot And Electronics...")

test = ModelAirportGPIO()

i = 1

while i < 3:
    print("[TestLab4] Round ", i, ":")
    print("[TestLab4] Activating Backstage")
    test.setDeviceState("Backstage-Entrance", True)
    print("[TestLab4] Backstage-Entrance: ", test.getDeviceState("Backstage-Entrance"))
    test.setDeviceState("Runway-Threshold", False)
    print("[TestLab4] Runway-Threshold: ", test.getDeviceState("Runway-Threshold"))
    sleep(30)
    print("[TestLab4] Activating Runway")
    test.setDeviceState("Backstage-Entrance", False)
    print("[TestLab4] Backstage-Entrance: ",  test.getDeviceState("Backstage-Entrance"))
    test.setDeviceState("Runway-Threshold", True)
    print("[TestLab4] Runway-Threshold: ", test.getDeviceState("Runway-Threshold"))
    sleep(30)
    i = i + 1
    
print("[TestLab4] Disabling All Devices")
test.setDeviceState("Backstage-Entrance", False)
print("[TestLab4] Backstage-Entrance: ",  test.getDeviceState("Backstage-Entrance"))
test.setDeviceState("Runway-Threshold", False)
print("[TestLab4] Runway-Threshold: ", test.getDeviceState("Runway-Threshold"))