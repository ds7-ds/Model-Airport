# Python Files Documentation

### Side Notes

Dictionaries are very useful in Python as it allows key/value pairs and is easily human readable. All methods will use dictionaries to pass or return information from one class or method to the next and for debugging purposes.

## ConnectGTC.py

ConnectGTC can be considered as the main program which calls ModelAirportGTC. It runs the airport like a CEO. The python program itself is actually spawned by ModelAirport.js. Unless the ConnectGTC does not receive a command from the user in certain amount of time, the airport runs itself automatically by calling next() repeatedly. If a command is received, the airport invokes the next(**command) and gives the user the ability to run the airport. Of course, error checking is done to prevent human input errors from causing a catastrophe. Before each call to next() or next(**command), status() must be called. The status() function returns the state of the airport and its operability. ConnectGTC also sends messages to the calling program ModelAirport about the airport status and other requested information such as aircraft information or lighting state.

Pseudocode:

```python

'''

1. When spawned, sends a success message to ModelAirport.js that the program itself is running.

2. Creates an instance of ModelAirportGTC and this starts the model airport.

3. Waits for ModelAirportGTC instance to setup completely. Robot must be aligned with sensors before operations (next()/next(command)) can begin.

4. Once setup is complete, if no user input is available for x amount of time, airport runs automatically through next() function. If user input is detected, then error checking is done. When verified, the next(command) is called.

5. Repeat Step 4 until the model airport time limit is reached. If time limit is reached, call the end(). Also, send a end request to the caller program ModelAirport.js.


'''

```

## ModelAirportGTC.py

This program provides GTC operations for the airport to run in a state by state fashion similar to how debuggers run. There are no time-consuming while loops in any functions and should mostly consist of nested if statements that contain the airport logic.

```python

class ModelAirportGTC:

  def __init__(self):
    setup()

  def setup(self):
    return None

  def next(self):
    return None

  def next(self, command):
    return None

  def status(self):
    return airportStatus

  def end(self):
    return None

```

## ModelAirportGraph.py


ModelAirportGraph will have a dictionary called ModelAirportCheckposts which contain objects with these properties:

```
location
next_location
type
occupied
will_be_occupied

```
as well as a dictionary called ModelAircrafts which contain objects with properties:


```
registration
airline
aircraft
current_location
previous_location
next_location

```

ModelAirportCheckposts stores a graph of all the sensor posts on the model airport. The posts act as a checkpoint for all aircraft. Planes go from one post to another in most states. The airport will be running on states as it allows for control and debugging ease. Two different sensor posts will be on the airport: E-Post and RE-Post. E-Posts are sensor posts with just an emitter and no receiver. They can control the aircraft but cannot detect whether the aircraft is present at the post. RE-Posts are sensor posts with an emitter and a receiver but they can detect whether the aircraft is at the post or not. The property post_type records this information. Also, there will be abstract posts which do not actually exist on the model airport but are there so that a map of the airport can be created. Overall, three posts types are there: E-Posts, RE-Posts, and No-Posts (Abstract Posts). The property "location" records where the post is. For example, a post could be named like "Backstage Entrance" or "Runway Line-Up". Every post will have an id and the first post starts from zero. Every post has to be connected to the Raspberry Pi electronically through some pin, and hence the GPIO_pin property. The occupied properties help the ModelAirportGTC to be able to track the aircraft and the future state of the airport.

ModelAircrafts stores information and history about the aircraft. The ModelAirportGraph class will update some properties when states change.

These two dictionaries will be used by the ModelAirportGraph class to track and run the airport based on ModelAirportGTC's orders. See the "Raspberry Pi Software UML.md" file for more details. Functions are listed below:

```python

class ModelAirportGraph:

  def __init__(self)
    pass

  def create_E_Post(self, postInfo):
    # private function
    return None

  def create_RE_Post(self, postInfo):
    # private function
    return None

  def create_No_Post(self, postInfo):
    # private function
    return None

  def create_Graph(self, postInfo):
    return None

  def get_Aircraft_List(self, message):
    return list

  def get_Aircraft_Information(self, aircraft):
    return aircraft_Info

  def move_Aircraft(self, aircraft):
    return None

  def get_AirCraft_At_Post(self, aircraft):
    return aircraft

  def is_Post_Occupied(self, post):
    return post_Occupied_Info

  def get_Aircraft_Post_Location(self, aircraft):
    return post_Info

  def get_Aircraft_Next_Post_Location(self, aircraft):
    return post_Info

  '''
  Add functions for airport lighting control.
  Make sure to update this documentation.
  '''

  def get_Status(self):
    return status

```

## ModelAirportLogger.py

```python

class ModelAirportLogger:

  def __init__(self, file_path)

  def create_Log(self):
    return None

  def append_To_Log(self, args):
    return None

  def close_Log(self):
    return None

```

## ModelAirportGPIO.py

Handles all GPIO operations including airport lighting. When class is called, the init() function will read in GPIO data from a text file conveniently called ModelAirportGPIO.txt with these properties for each object:

```
debug_mode

pin_description
GPIO_pin

pin_description
GPIO_pin

pin_description
GPIO_pin

...


```
The class will look like this:

```python

class ModelAirportGPIO:

  def __init__(self):
    pass

  def set_RE_Sensor_Pin(self, pin)
    # private function
    return None

  def set_E_Sensor_Pin(self, pin)
    # private function
    return None

  def set_Airport_Lighting_Pin(self, pin)
    # private function
    return None

  def set_Airport_Terminal_Lighting_Pin(self, pin)
    #private function
    return None

  def get_RE_Sensor_State(self, state)
    return value

  def set_RE_Sensor_State(self, state)
    return None

  def set_E_Sensor_State(self, state)
    return None

  def set_Airport_Lighting_State(self, state)
    return None

  def set_Airport_Terminal_Lighting_State(self, state)
    return None

```

The "state" dictionary must have the following properties:

```json
{
"sensor" : "",
"state" : "",
"debug" : ""
}
}
```