import ast
#from gpiozero import LEDBoard, ButtonBoard
from time import sleep

class ModelAirportGPIO:
    def __init__(self, path):
        try:
            f = open(path["filepath"], "r")
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
            print("[ModelAirportGPIO] Input Device Pins: ", inputPins)
            print("[ModelAirportGPIO] Output Device Pins: ", outputPins)
            #self.input = ButtonBoard(*inputPins)
            #self.output = LEDBoard(*outputPins)
        except:
            print("[ModelAirportGPIO] File Reading Error...")
    def get_Device_State(self, device):
        if device["object"] in self.layout:
            if "Input_GPIO_Pin" in self.layout[device["object"]]:
                print("[ModelAirportGPIO] Input Device Request Index: ", self.layout[device["object"]]["Input_GPIO_Pin"]["Index"])
                #self.input.is_pressed(self.layout[device["object"]]["Input_GPIO_Pin"]["Index"])
    def set_Device_State(self, device):
        if device["object"] in self.layout:
            if device["state"] == True:
                if "Output_GPIO_Pin" in self.layout[device["object"]]:
                    print("[ModelAirportGPIO] Output Device Request Index: ", self.layout[device["object"]]["Output_GPIO_Pin"]["Index"], "        State:  TRUE")
                    #self.output.on(self.layout[device["object"]]["Output_GPIO_Pin"]["Index"])
            else:
                if "Output_GPIO_Pin" in self.layout[device["object"]]:
                    print("[ModelAirportGPIO] Output Device Request Index: ", self.layout[device["object"]]["Output_GPIO_Pin"]["Index"], "        State:  FALSE")
                    #self.output.off(self.layout[device["object"]]["Output_GPIO_Pin"]["Index"])

test = ModelAirportGPIO({"filepath":"D:/Darshan/Personal/Hobbies/Model Airport/Model Airport Final/Model-Airport/Engineering/Software Engineering/Code/Raspberry Pi/model-airport/res/ModelAirportGPIO.txt"})
test.set_Device_State({'object':'Pavement-Lighting', 'state': True})
sleep(2)
test.set_Device_State({'object':'Pavement-Lighting', 'state':False})
