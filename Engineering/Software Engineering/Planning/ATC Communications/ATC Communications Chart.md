# ATC Communications Chart

## Possible Communications With 1 Airplane \(Scenario 1\)

Notes about table setup\: 

* Every row is a phase in the communication over time

* Internal messages are normal grammatical

* Communication messages have every letter in every word capatalised

* Actions are in parentheses

* The client will have two text boxes: P and A. P is where the pilot's response is entered while A is where the client enters an ATC command for the pilot to follow. Text box A will have a helper message located above the input and that's where the text goes.

* Communication setup is always as follows\: 

```
Client <----> Server <----> Raspberry Pi
```

| Client | Server | Raspberry Pi \(RPi\) |
| :---: | :---: | :---: |
| [P] Connecting to pilot...<br>[A] Please wait... | - | ATC Requesting Departure <br> SAA202 Runway 09 Taxi Via Alpha |
| [P] Connecting to pilot...<br>[A] Please wait... | \(Waiting for client to retrieve message\) | - |
| [P] ATC Requesting Departure<br>[A] SAA202 Runway 09 Taxi Via Alpha <br> \(Waiting for user input\)| - | - |
| [P] Waiting for pilot response...<br>[A] Please wait... | \(Waiting for RPi to retrieve message\) | - |
| [P] Waiting for pilot response...<br>[A] Please wait... | - | \(Retrieves, processes message and returns response\) <br> ATC Runway 09 Taxi Via Alpha<br>SAA202 Hold Short Runway 09|
| [P] Waiting for pilot response...<br>[A] Please wait... | \(Waiting for client to retrieve message\) | \(Moving airplane 1 if needed\) |
| [P] SAA202 Runway 09 Taxi Via Alpha <br> [A] SAA202 Hold Short Runway 09 \(Waiting for user input\) | - | - |
| [P] Waiting for pilot response...<br>[A] Please wait... | \(Waiting for RPi to retrieve message\) | - |
| [P] Waiting for pilot response...<br>[A] Please wait... | - | \(Retrieves, processes message and returns response\) <br> ATC Holding Short Runway 09 <br> SAA202 Runway 09 Line Up And Wait |
| [P] Waiting for pilot response...<br>[A] Please wait... | \(Waiting for client to retrieve message\) | \(Moving airplane 1 if needed\) |
| [P] ATC Holding Short Runway 09 <br> [A] SAA202 Runway 09 Line Up And Wait \(Waiting for user input\) | - | - |
| [P] Waiting for pilot response...<br>[A] Please wait... | \(Waiting for RPi to retrieve message\) | - |
| [P] Waiting for pilot response...<br>[A] Please wait... | - | \(Retrieves, processes message and returns response\) <br> ATC Runway 09 Line Up And Wait <br> SAA202 Runway 09 Cleared For Takeoff |
| [P] Waiting for pilot response...<br>[A] Please wait... | \(Waiting for client to retrieve message\) | \(Moving airplane 1 if needed\) |
| [P] SAA202 Runway 09 Cleared For Takeoff  <br> [A] Session over... | - | - |

## Possible Communications with 1 Airplane \(Scenario 2\)

TBD

## Possible Communications with 2 Airplanes

TBD