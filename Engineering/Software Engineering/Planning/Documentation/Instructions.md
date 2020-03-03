# Python Files

## Files that need to be implemented and how to do it

Dictionaries are very useful in Python as it allows key/value pairs and is easily human readable. All methods will use dictionaries to pass information from one class to the next or if debugging purposes.

### ModelAircraft.py

This file will contain a class called ModelAircraft which contains these properties (JSON format as example):

```json

{"name" : "",
"id" : 999,
"aircraft" : "",
"current_location" : 999,
"current_location_time" : "",
"next_location_time" : ""}

```

The class needs to have these properties in the __init__(self). The class should provide value getter methods for each key. Setter methods are needed for current_location, current_location_time, and next_location_time. An abstract class will be provided to make implementation easier. Functions are written below:

```python

def 

```

### ModelAirportGraph.py


This file will contain a class called ModelAirportGraph which contains these properties (JSON format as example):

```json

{"location" : "",
"id" : 999,
"post_type" : "",
"next_forward_post" : 999,
"code" : "",
"GPIO_pin": 999,
"occupied" : false,
"will_be_occupied" : false}

```

Two different sensor posts will be on the airport: E-Post and RE-Post. E-Posts are sensor posts with just an emitter and no receiver. They can control the aircraft but cannot detect whether the aircraft is present at the post. RE-Posts are sensor posts with an emitter and a receiver but they can detect whether the aircraft is at the post or not. The property post_type records this information. The property "location" is a string and is named after where the sensor post is. Every post will have an id to track and this count starts from zero. The property "code" is a string which will be used by the interpreter in ModeAirportGTC class 

### ModelAirportGTC.py

### ConnectGTC.py