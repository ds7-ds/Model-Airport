import ast
from gpiozero import LEDBoard, ButtonBoard
from time import sleep

class ModelAirportGPIO:
    def __init__(self):
        f = open("/media/pi/9484-DE4D/model-airport/res/ModelAirportGPIO.txt", "r")
        s = f.read()
        self.layout = ast.literal_eval(s)
        tempInputPins = []
        tempOutputPins = []
        for y in self.layout:
            if 'Input_GPIO_Pin' in self.layout[y]:
                tempInputPins.append(self.layout[y]['Input_GPIO_Pin']['Pin'])
            if 'Output_GPIO_Pin' in self.layout[y]:
                tempOutputPins.append(self.layout[y]['Output_GPIO_Pin']['Pin'])
        inputPins = tuple(tempInputPins)
        outputPins = tuple(tempOutputPins)
        #print(inputPins)
        #print(outputPins)
        self.input = ButtonBoard(*inputPins)
        self.output = LEDBoard(*outputPins)
    def get_Device_State(self, device):
        if device["object"] in self.layout:
            if "Input_GPIO_Pin" in self.layout[device["object"]]:
                #self.input.value(self.layout[device["object"]]["Input_GPIO_Pin"]["Index"])
                pass
    def set_Device_State(self, device):
        if device["object"] in self.layout:
            if device["state"] == True:
                if "Output_GPIO_Pin" in self.layout[device["object"]]:
                    self.output.on(self.layout[device["object"]]["Output_GPIO_Pin"]["Index"])
            else:
                if "Output_GPIO_Pin" in self.layout[device["object"]]:
                    self.output.off(self.layout[device["object"]]["Output_GPIO_Pin"]["Index"])

test = ModelAirportGPIO()
test.set_Device_State({'object':'Pavement-Lighting', 'state': True})
sleep(5)
test.set_Device_State({'object':'Pavement-Lighting', 'state':False})