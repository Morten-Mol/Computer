# Python Computer
Goal --> Make a X-bit computer using basic transistors

### Core classes

##### Transistor
Class containg source, gate and drain of a transistor. Initialzied using
```python
Transistor(source,gate)
```
where source and gate can be either 0 or 1 for ON or OFF states.
The output of the transistor is ON if the drain property is 1 and OFF if it is 0.

The source and gate states for an existing transistor can be changed by calling the methods
```python
Transistor.Source(source)
Transistor.Gate(gate)
```

##### Gate
Class for applying any logic gate to two inputs. Basic usage is as below,
```python
Gate(topInput,bottomInput).LOGICOPERATION()
```
where LOGICOPERATION can be AND,OR,NOT,NAND,NOR,XOR,XNOR. The value returned by the class method is the logic operation return value.

### Tests 
Run Tests.py to test and demonstrate the different features of the repository
+ Transistor based RNG
+ Logic gate truth tables for all common logic operations

### To do:
1. x-bit binary Adder-Subtractor : see https://www.geeksforgeeks.org/4-bit-binary-adder-subtractor/
2. n>2 Logic Gates
3. Instruction set sim
