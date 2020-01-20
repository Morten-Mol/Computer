from Gate import Gate
from HalfAdder import HalfAdder

class FullAdder():
# Full adder
#
# Full Addition of two bytes 
#
# Input : Top bit , bottom bit, carry in
# Output : Sum and Carry out of operation

    def __init__(self,tI,bI,cI):
        self.topInput = tI
        self.botInput = bI
        self.carryIn = cI

        self.Calc()

    def Calc(self):
        # Full adder is realized using two half-adders and an OR-gate

        # First half-adder
        ha1Sum, ha1Carry = HalfAdder(self.topInput, self.botInput).Output()

        # Second half-adder
        ha2Sum, ha2Carry = HalfAdder(self.carryIn, ha1Sum).Output()

        # OR-gate
        self.carryOut = Gate(ha2Carry, ha1Carry).OR()

        self.sum = ha2Sum

    def Output(self):
       return self.sum, self.carryOut

if __name__ == "__main__" :
    print(FullAdder(0,0,1).Output())
