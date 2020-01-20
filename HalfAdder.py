from Gate import Gate

class HalfAdder():
# Half adder
#
# Simple addition of two binary numbers
#
# Input : Top bit , bottom bit
# Output : Sum and Carry of operation

    def __init__(self,tI,bI):
        self.topInput = tI
        self.botInput = bI

        self.Calc()

    def Calc(self):
        self.sum = Gate(self.topInput,self.botInput).XOR()
        self.carry = Gate(self.topInput,self.botInput).AND()

    def Output(self):
       return self.sum, self.carry

if __name__ == "__main__" :
    print(HalfAdder(0,0).Output())
    print(HalfAdder(1,0).Output())
    print(HalfAdder(0,1).Output())
    print(HalfAdder(1,1).Output())
