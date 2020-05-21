import ast
from gpiozero import LEDBoard, ButtonBoard
from time import sleep
import os

class ModelAirportGPIO:
    def __init__(self):
        gpioPath = os.path.join(os.pardir, os.pardir, "res", "ModelAirportGPIO.txt")
        f = open(gpioPath, "r").read()
        self.layout = ast.literal_eval(f)
        tempInputPins = []
        tempOutputPins = []
        for y in self.layout:
            if 'Input_GPIO_Pin' in self.layout[y]:
                tempInputPins.append(self.layout[y]['Input_GPIO_Pin']['Pin'])
            if 'Output_GPIO_Pin' in self.layout[y]:
                tempOutputPins.append(self.layout[y]['Output_GPIO_Pin']['Pin'])
        inputPins = tuple(tempInputPins)
        outputPins = tuple(tempOutputPins)
        self.input = ButtonBoard(*inputPins)
        self.output = LEDBoard(*outputPins)
    def getDeviceState(self, item):
        return self.input[self.layout[item]["Input_GPIO_Pin"]["Index"]].is_pressed
    def setDeviceState(self, device, state):
            if state == True:
                self.output.on(self.layout[device]["Output_GPIO_Pin"]["Index"])
            else:
                self.output.off(self.layout[device]["Output_GPIO_Pin"]["Index"])