from Converters import Bin2Dec
from TwosComp import TwosComp
from FullAdder import FullAdder
from Gate import Gate
from Transistor import Transistor

class SingleBitAddSub:
    # Based on https://www.geeksforgeeks.org/4-bit-binary-adder-subtractor/

    def __init__(self, K, cIn, A, B):
        self.AddOrSub = K
        self.cIN = cIn
        self.A = A
        self.B = B

        # Prepare B input depending on addition or subtraction
        self.b_compliment = Gate(self.AddOrSub, self.B).XOR()

        # Full-adder
        self.sum, self.cOut = FullAdder(self.A, self.b_compliment, self.cIN).Output()

def AddSub(Binary_A, Binary_B, operation):
    """
    Adds or subs two binary numbers of equal bit-length

    The function uses a series of full adders and twos compliment to do an
    arithmetic-like bit-wise operation
    """
    # Addition or subtraction
    if operation is 'Add' or operation is 'add':
        K = 0
    elif operation is 'Sub' or operation is 'sub':
        K = 1

    # position in binary number - counter
    pos = 0

    # List to put sums of each bit into
    sumList = []

    # Iterate over binary number, from right to left
    # i.e. flip the lists
    Binary_A.reverse()
    Binary_B.reverse()

    for bitA, bitB in zip(Binary_A, Binary_B):

        if pos is 0:
            firstBitOp = SingleBitAddSub(K,K,bitA.drain,bitB.drain)
            sumList.append(firstBitOp.sum)
            prev_cIn = firstBitOp.cOut

        elif pos == (len(Binary_A)-1):
            lastBitOp = SingleBitAddSub(K,prev_cIn,bitA.drain,bitB.drain)
            sumList.append(lastBitOp.sum)
            cOut = lastBitOp.cOut

        else:
            bitOp = SingleBitAddSub(K,prev_cIn,bitA.drain,bitB.drain)
            sumList.append(bitOp.sum)
            prev_cIn = bitOp.cOut

        pos += 1

    # Insert the signed bit into the result to get the final answer
    sumList.insert(0,cOut)
    ans = sumList

    # Takes twos compliment of answer if operation was subtraction
    # This is done to bring it back to normal form
    if operation == 'sub' or operation == 'Sub':
        ans = TwosComp(ans)
    return ans

if __name__ == "__main__" :
    binA = [Transistor(0,0),Transistor(1,1),Transistor(0,0)]
    binB = [Transistor(0,0),Transistor(1,1),Transistor(1,1)]
    operation = 'sub'

    ans = AddSub(binA,binB,operation)
    print(ans)
    ans = Bin2Dec(ans)

    print(ans)

