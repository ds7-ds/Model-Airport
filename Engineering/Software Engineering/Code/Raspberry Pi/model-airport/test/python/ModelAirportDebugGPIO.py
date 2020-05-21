import ast
#from gpiozero import LEDBoard, ButtonBoard
import os

class ModelAirportGPIO:
    def __init__(self):
        try:
            gpioPath = os.path.join(os.pardir, os.pardir, "res", "ModelAirportGPIO.txt")
            f = open(gpioPath, "r")
            s = f.read()
            f.close()
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
            print("[ModelAirportGPIO] Input Device Pins: ", inputPins)
            print("[ModelAirportGPIO] Output Device Pins: ", outputPins)
            #self.input = ButtonBoard(*inputPins)
            #self.output = LEDBoard(*outputPins)
        except:
            print("[ModelAirportGPIO] File Reading Error...")
    def getDeviceState(self, item):
        if item in self.layout:
            if "Input_GPIO_Pin" in self.layout[item]:
                print("[ModelAirportGPIO] Input Device Request Index: ", self.layout[item]["Input_GPIO_Pin"]["Index"])
                #self.input[self.layout[item]["Input_GPIO_Pin"]["Index"]].is_pressed
                return self.layout[item]["Input_GPIO_Pin"]["Index"]
        print("[ModelAirportGPIO] Input Device Request Error: Device (", item,") Not Found...")
        return -1
    def setDeviceState(self, item, state):
        if item in self.layout:
            if state == True:
                if "Output_GPIO_Pin" in self.layout[item]:
                    print("[ModelAirportGPIO] Output Device Request Index: ", self.layout[item]["Output_GPIO_Pin"]["Index"], "        State:  TRUE")
                    #self.output.on(self.layout[object]["Output_GPIO_Pin"]["Index"])
            else:
                if "Output_GPIO_Pin" in self.layout[item]:
                    print("[ModelAirportGPIO] Output Device Request Index: ", self.layout[item]["Output_GPIO_Pin"]["Index"], "        State:  FALSE")
                    #self.output.off(self.layout[object]["Output_GPIO_Pin"]["Index"])