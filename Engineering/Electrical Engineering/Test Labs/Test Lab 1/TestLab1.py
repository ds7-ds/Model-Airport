from gpiozero import LED
from time import sleep

print("Running Test Lab 1")

led = LED(17)

i = 0

while i < 10:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    i = i + 1

print("Ending Test Lab 1")