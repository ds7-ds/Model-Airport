import ast
#from gpiozero import LEDBoard, ButtonBoard
#from time import sleep

class ModelAirportGPIO:
    def __init__(self, filepath):
        try:
            f = open(filepath, "r")
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
    def get_Device_State(self, item):
        if item in self.layout:
            if "Input_GPIO_Pin" in self.layout[item]:
                print("[ModelAirportGPIO] Input Device Request Index: ", self.layout[item]["Input_GPIO_Pin"]["Index"])
                #self.input[self.layout[item]["Input_GPIO_Pin"]["Index"]].is_pressed
                return self.layout[item]["Input_GPIO_Pin"]["Index"]
        print("[ModelAirportGPIO] Input Device Request Error: Device (", item,") Not Found...")
        return -1
    def set_Device_State(self, item, state):
        if item in self.layout:
            if state == True:
                if "Output_GPIO_Pin" in self.layout[item]:
                    print("[ModelAirportGPIO] Output Device Request Index: ", self.layout[item]["Output_GPIO_Pin"]["Index"], "        State:  TRUE")
                    #self.output.on(self.layout[object]["Output_GPIO_Pin"]["Index"])
            else:
                if "Output_GPIO_Pin" in self.layout[item]:
                    print("[ModelAirportGPIO] Output Device Request Index: ", self.layout[item]["Output_GPIO_Pin"]["Index"], "        State:  FALSE")
                    #self.output.off(self.layout[object]["Output_GPIO_Pin"]["Index"])

test = ModelAirportGPIO("D:/Darshan/Personal/Hobbies/Model Airport/Model Airport Final/Model-Airport/Engineering/Software Engineering/Code/Raspberry Pi/model-airport/res/ModelAirportGPIO.txt")
test.set_Device_State("Pavement-Lighting", True)
test.set_Device_State("Pavement-Lighting", False)
val = test.get_Device_State("Backstge-Exit")
