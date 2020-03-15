# Python Files Documentation

## Files that need to be implemented and how to do it

Dictionaries are very useful in Python as it allows key/value pairs and is easily human readable. All methods will use dictionaries to pass information from one class or method to the next and for debugging purposes.

### ModelAirportGraph.py

This file will contain a class called ModelAirportGraph.

It will have a dictionary called ModelAirportCheckposts which contain objects with these properties (JSON used as format):

```json

{"location" : "",
"id" : 999,
"type" : "",
"next_id" : 999,
"code" : "",
"GPIO_pin": 999,
"occupied" : false,
"will_be_occupied" : false}

```
as well as a dictionary called ModelAircrafts which contain objects with properties:


```json

{"name" : "",
"id" : 999,
"aircraft" : "",
"current_location" : 999,
"previous_location" : ,
"next_location" : }

```

ModelAirportCheckpoints stores a graph of all the sensor posts on the model airport. The posts act as a checkpoint for all aircraft. Planes go from one post to another in every state. The airport will be running on states as it allows for control and debugging ease. Two different sensor posts will be on the airport: E-Post and RE-Post. E-Posts are sensor posts with just an emitter and no receiver. They can control the aircraft but cannot detect whether the aircraft is present at the post. RE-Posts are sensor posts with an emitter and a receiver but they can detect whether the aircraft is at the post or not. The property post_type records this information. Also, there will be abstract posts which do not actually exist on the model airport but are there so that a map of the airport can be created. Overall, three posts types are there: E-Posts, RE-Posts, and No-Posts (Abstract Posts). The property "location" records where the post is. For example, a post could be named like "Backstage Entrance" or "Runway Line-Up". Every post will have an id and the first post starts from zero. The id is for the program to use as numbers are faster to compare than strings. Every post has to be connected to the Raspberry Pi electronically through some pin, and hence the GPIO_pin property. The occupied properties help the ModelAirportGTC to be able to track the aircraft and the future state of the airport.

ModelAircrafts stores information and history about the aircraft.

These two dictionaries will be used by the ModelAirportGraph class to track and run the airport. See the "Raspberry Pi Software UML.md" file for more details. Functions are listed below:

```python

class ModelAirportGraph:

  def __init__(self, **posts_file_path)
    pass

  def create_E_Post(**postInfo):
    return None

  def create_RE_Post(**postInfo):
    return None

  def create_Graph(**postInfo):
    return None

  def moveAircraft

```

### ModelAirportGTC.py



### ConnectGTC.py