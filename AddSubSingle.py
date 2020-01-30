from FullAdder import FullAdder
from Gate import Gate

# Based on https://www.geeksforgeeks.org/4-bit-binary-adder-subtractor/

class SingleBitAddSub:

    def __init__(self, K, cIn, A, B):
        self.AddOrSub = K
        self.cIN = cIn
        self.A = A
        self.B = B

        # Prepare B input depending on addition or subtraction
        self.b_compliment = Gate(self.AddOrSub, self.B).XOR()

        # Full-adder
        self.sum, self.cOut = FullAdder(self.A, self.b_compliment, self.cIN).Output()

if __name__ == "__main__" :
    A = SingleBitAddSub(1,1,1,1,0)
    print(A.sum)
