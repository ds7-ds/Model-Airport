# ATC Communications Chart

## Possible Communications With 1 Airplane

Notes about table setup\: 

* Every row is a phase in the communication over time

* Internal messages are normal grammatical

* Communication messages have every letter in every word capatalised

* Actions are in parentheses

* The Client will have two text boxes: P and A. P is where the pilot's response is entered while A is where the client enter an ATC command for the pilot to follow. Text box A will have a helper message located above the input and that's where the table text goes.


| Client | Server | Raspberry Pi \(RPi\) |
| :---: | :---: | :---: |
| \(P\) Connecting to pilot... \(A\) Please wait... | - | SAS202 Requesting Departure<br>SAS202 Runway 09 Taxi Via Alpha |
| \(P\) Connecting to pilot... \(A\) Please wait... | \(Send message to client\) | - |
| \(P\) SAS202 Requesting Departure \(A\) SAS202 Runway 09 Taxi Via Alpha \(Waiting for user input\)| - | - |
| \(P\) Waiting for pilot response... \(A\) Please wait... | \(Waiting for RPi to retrieve message\) | - |
| \(P\) Waiting for pilot response... \(A\) Please wait... | - | \(Retrieves, processes message and returns response\) SAS202 Runway 09 Taxi Via Alpha<br>  |
| \(P\) Waiting for pilot response... \(A\) Please wait... | \(Waiting for client to retrieve message\) | \(Moving airplanes if needed\) |

## Possible Communications with 2 Airplanes

TBD