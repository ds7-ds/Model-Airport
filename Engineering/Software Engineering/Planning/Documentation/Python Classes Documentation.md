# Python Files

## Files that need to be implemented and how to do it

Dictionaries are very useful in Python as it allows key/value pairs and is easily human readable. All methods will use dictionaries to pass information from one class to the next or if debugging purposes.

### ModelAirportGraph.py

This file will contain a class called ModelAirportGraph.
It will have a dictionary called ModelAirportCheckpoints which contain objects with these properties (JSON used as format):

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
as well as a dictionary called ModelAircraft which contain objects with properties:


```json

{"name" : "",
"id" : 999,
"aircraft" : "",
"current_location" : 999,
"previous_location" : "",
"next_location" : ""}

```

ModelAirportCheckpoints stores a graph of all the sensor posts on the model airport. The posts act as a checkpoint for all aircraft. Planes go from one post to another. Two different sensor posts will be on the airport: E-Post and RE-Post. E-Posts are sensor posts with just an emitter and no receiver. They can control the aircraft but cannot detect whether the aircraft is present at the post. RE-Posts are sensor posts with an emitter and a receiver but they can detect whether the aircraft is at the post or not. The property post_type records this information. The property "location" is a string and is named after where the sensor post is. Every post will have an id and this count starts from zero.

### ModelAirportGTC.py



### ConnectGTC.py