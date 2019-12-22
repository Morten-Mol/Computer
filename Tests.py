from TestFunctions.BinaryRNG import BinaryRNG_Test
from TestFunctions.GateLogicCheck import TestGateTruth

# Tests functions to run
BinaryRNG_Test(8,1e4)

# Gate truthtable generator

gateTypes = ['AND', 'OR', 'NOT', 'NAND', 'NOR','XOR','XNOR']
print('Cross-refernce following table with truth tables at https://www.tutorialspoint.com/computer_logical_organization/logic_gates.htm')
for gate in gateTypes:
    TestGateTruth(gate)
