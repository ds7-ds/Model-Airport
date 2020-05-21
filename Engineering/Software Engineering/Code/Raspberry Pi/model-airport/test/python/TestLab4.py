from time import sleep
from ModelAirportGPIO import ModelAirportGPIO

print("[TestLab4] Testing Model Airport Robot And Electronics...")

test = ModelAirportGPIO()

i = 1

while i < 3:
    print("[TestLab4] Round ", i, ":")
    print("[TestLab4] Activating Backstage")
    print("[TestLab4] Backstage-Entrance: ", test.getDeviceState("Backstage-Entrance"))
    print("[TestLab4] Runway-Threshold: ", test.getDeviceState("Runway-Threshold"))
    test.setDeviceState("Backstage-Entrance", True)
    test.setDeviceState("Runway-Threshold", False)
    sleep(30)
    print("[TestLab4] Activating Runway")
    print("[TestLab4] Backstage-Entrance: ",  test.getDeviceState("Backstage-Entrance"))
    print("[TestLab4] Runway-Threshold: ", test.getDeviceState("Runway-Threshold"))
    test.setDeviceState("Backstage-Entrance", False)
    test.setDeviceState("Runway-Threshold", True)
    sleep(30)
    i = i + 1
    
print("[TestLab4] Disabling All Devices")
print("[TestLab4] Backstage-Entrance: ",  test.getDeviceState("Backstage-Entrance"))
print("[TestLab4] Runway-Threshold: ", test.getDeviceState("Runway-Threshold"))
test.setDeviceState("Backstage-Entrance", False)
test.setDeviceState("Runway-Threshold", False)
