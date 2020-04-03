# Test Lab 3 - Robot Circuit Test

### Hypothesis

> A NOT gate combined with a common transistor motor driver circuit. Testing to determine whether circuit works as planned.

### Materials:

* Multimeter

* 170 point breadboard black

* {Materials listed on circuit diagram}

### Instructions

1. Test 4 AA Battery Pack. Record voltage in table.

1. Test motor using battery pack. Record voltage and current.

1. Test resistance of both resistors. Record resistance.

1. Create circuit as shown on diagram.

1. Test circuit by flashing photodiode on and off. Circuit should work as planned.

1. Check voltage and current of different states of battery pack. Record those voltages and currents.

1. Check voltage and current of different states of motor. Record those voltages and currents.

1. Check voltage and current of different states of R2. Record those voltages and currents.

1. Check voltage and current of different states of the IR photodiode. Record those voltages and currents. Notice no testing is done for R1 on purpose.

### Results:

> Success. Circuit worked as planned and the simulation also proved to be very close.

### Data

* Battery Pack uses new 4 AA Duracell MN1500

| - | Voltage \(V\) | Current \(mA\) | Resistance \(ohms\) |
| :---: | :---: | :---: | :---: |
| Battery Pack | 5.94 (\No load\), 5.72 \(Motor off\), 5.82 \(Motor on\)| 5 mA \(Motor off\), 150 mA \(Motor no load peak on\), 55 mA \(Motor no load normal on\) | - |
| R1 | - | - | 990 |
| R2 | 5.06 \(Motor on\), 5.22 \(Motor off\) | 5.06 \(Motor on\), 5.72 \(Motor off\) | 10.49 K |
| Motor | 5.78 | 45 \(No load\), 50 \(Load\) | - |
| IR Photodiode | 5.15 \(Motor on\), 5.24 \(Motor off\) | 0.24 \(Light on, Motor on\), 0.24 \(Light on, Motor off\), 0 \(Light off, Motor on\), 0 \(Light off, Motor off\) | - |