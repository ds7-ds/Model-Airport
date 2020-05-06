# Python Files Documentation

## ConnectATC.py

#### Description

ConnectATC is the bridge between the actual software that controls the model airport (ModelATC) and the software that connects to the user via server (Heroku, AWS, RedHat). Please see the overall software UML to get a clear idea on how and what ConnectATC.py does visually. The program itself is spawned by ModelAirport.js instance. In operation, unless the ConnectATC program does not receive a command from the user in certain amount of time, the airport runs itself automatically by calling next() repeatedly. If a command is received, the airport invokes the next(command) and gives the user the ability to command the airport for that moment. If the next(command) was unsuccessful in doing because the ModelAirportATC was unavailable to do so, the next(command) will be called repeatedly until its accomplished. Before each call to next() or next(**command), status() must be called. The status() function returns the state of the airport and its operability. ConnectATC also sends these messages to ModelAirport.js instance if in case the node process requests it.

#### Pseudocode

```python

'''

1. When spawned, sends a success message to ModelAirport.js process that the program itself is running.

2. Creates an instance of ModelAirportATC and this starts the model airport.

3. Waits for ModelAirportATC instance to setup completely. Robot must be aligned with sensors before operations (next()/next(command)) can begin.

4. Once setup is complete, if no user input is available for x amount of time, airport runs automatically through next() function. If user input is detected, then error checking is done. When verified, the next(command) is called. If next(command) did not successfully happen, it gets repeatedly called until it is successful.

5. If the client wants a model airport status, then just call status() and pass the information to ModelAirport.js to send it to the client.

6. Repeat Step 4 and 5 until the model airport time limit is reached. If time limit is reached, call the end(). Also, send a end request to the caller program ModelAirport.js.


'''

```

## ModelAirportATC.py

#### Description

This program provides ATC operations for ConnectATC instance to run the airport in a state by state fashion. There are no time-consuming while loops in any functions and should mostly consist of nested if statements that contain the airport logic.

#### Pseudocode

```python

class ModelAirportGTC:

  def __init__(self):
    setup()

  def setup(self):
    return None

  def next(self):
    return hasPerformed # returns -1 for error, 0 for unsuccessful, and 1 for successful

  def next(self, command):
    return hasPerformed # returns -1 for error, 0 for unsuccessful, and 1 for successful

  def status(self):
    return airportStatus

  def end(self):
    return None

```

## ModelAirportImager.py

#### Description

ModelAirportImager's main job is to create an image of the airport and also use ModelAirportGPIO to output the image. ModelAirportImager class will store that image using two dictionaries. The first dictionary is called ModelAirportCheckposts. ModelAirportCheckposts stores a "graph" of all the sensor posts on the model airport. The posts act as a checkpoint for all aircraft. Planes go from one post to another in most states. Two different sensor posts will be on the airport: E-Post and RE-Post. E-Posts are sensor posts with just an emitter and no receiver. They can control the aircraft but cannot detect whether the aircraft is present at the post. RE-Posts are sensor posts with an emitter and a receiver but they can detect whether the aircraft is at the post or not. The property "type" records this information. Also, there will be abstract posts which do not actually exist on the model airport but are there so that a map of the airport can be created. Overall, three posts types are there: E-Posts, RE-Posts, and No-Posts (Abstract Posts). The property "location" records where the post is. For example, a post could be named like "Backstage Entrance" or "Runway Line-Up". Every post has to be connected to the Raspberry Pi electronically through some pin, and hence the GPIO_pin property. The occupied properties help the ModelAirportGTC to be able to track the aircraft and the future state of the airport. ModelAircrafts stores information and history about the aircraft. Like it was stated before, these two different dictionaries which contain information about the airport which make up the virtual image of the airport. In every state, this image gets constantly modified and then reflected onto the real model airport. A third dictionary will contain objects of the model airport which do not link to other objects such as lighting and sound. This is to be used by ModelAirportImager.py process to control devices attached to them independently from the rest of the synchronized operations of the model airport.

#### Pseudocode

Data from ModelAirportCheckposts.txt:

```json

{
   "Runway Line-Up":{
      "Next_Location":"Backstage",
      "Type":"RE Post",
      "Occupied":false,
      "Will_Be_Occupied":false
   },
   "Backstage Line-Up":{
      "Next_Location":"Backstage",
      "Type":"RE Post",
      "Occupied":false,
      "Will_Be_Occupied":false
   }
}

```

Data from ModelAircrafts.txt:

```json
{
   "AA2345":{
      "airline":"American Airlines",
      "aircraft":"A330-300",
      "current_location":"Runway Line-Up",
      "previous_location":"Taxiway End",
      "next_location":"Backstage"
   },
   "AA2545":{
      "airline":"American Airlines",
      "aircraft":"A330-300",
      "current_location":"Runway Line-Up",
      "previous_location":"Taxiway End",
      "next_location":"Backstage"
   }
}

```

Data from ModelAirportAccessories.txt:

```json
{
   "Terminal-Lighting":{
      "type":"light",
      "description":"Lighting inside terminal",
      "available":true,
      "state":true
   },
   "Pavement-Lighting":{
      "type":"light",
      "description":"Lighting along runway and taxiway",
      "available":true,
      "state":true
   }
}

```



```python

class ModelAirportImager:

  def __init__(self)
    pass

  def get_Aircraft_List(self):
    return list

  def get_Aircraft_Information(self, aircraft):
    return aircraft_Info

  def move_Aircraft(self, aircraft):

  def get_AirCraft_At_Post(self, aircraft):
    return aircraft

  def is_Post_Occupied(self, post):
    return post_Occupied_Info

  def get_Aircraft_Post_Location(self, aircraft):
    return post_Info

  def get_Aircraft_Next_Post_Location(self, aircraft):
    return post_Info
  
  def set_Accessory_State(self, accessory, state):

  def get_Accessory_State(self, accessory):
  
  def get_Status(self):
    return status

```

## ModelAirportLogger.py

#### Description

Logs all actions that ModelAirportATC.py instance does.

#### Pseudocode

```python

class ModelAirportLogger:

  def __init__(self, file_path)

  def open_Log(self):

  def append_To_Log(self, message):

  def close_Log(self):

```

## ModelAirportGPIO.py

#### Description

Handles all GPIO operations including airport lighting. The class uses data from ModelAirportGPIO.txt which is formatted like this:

```json
{
   "Backstage":{
      "Device":"RE_Post_3",
      "Input_GPIO_Pin":{
         "Pin":23,
         "Index":3
      },
      "Output_GPIO_Pin":{
         "Pin":24,
         "Index":9
      }
   },
   "Taxiway-End":{
      "Device":"E_Post_5",
      "Output_GPIO_Pin":{
         "Pin":45,
         "Index":67
      }
   }
}

```
#### Pseudocode

```python

class ModelAirportGPIO:

  '''
  Creates an GPIO interface so caller may access the GPIO without any knowledge of it.
  Reads in pin data from text file and creates a dictionary. Input and output pins are
  organized and then used to create LEDBoard and ButtonBoard instances.
  '''
  def __init__(self):
    pass


  '''
  Sets device state using the object from the passed dictionary argument.
  To call this function, use the following example syntax:
  
  example.set_Device_State("Backstage" , True)

  Returns nothing after called.
  '''
  def set_Device_State(self, object)


  '''
  Reads and returns the state of a device.
  Caller Ex.:
  
  val = example.get_Device_State("Backstage")
  
  The only return values are True or False.
  '''
  def get_Device_State(self, object)
    return None

```