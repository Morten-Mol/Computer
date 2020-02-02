from AddSubSingle import SingleBitAddSub
from Bin2Dec import Bin2Dec
from TwosComp import TwosComp
from BinList2TransList import Bin2Trans

def AddSub(Binary_A, Binary_B, operation):

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
            firstBitOp = SingleBitAddSub(K,K,bitA,bitB)
            sumList.append(firstBitOp.sum)
            prev_cIn = firstBitOp.cOut

        elif pos == (len(Binary_A)-1):
            lastBitOp = SingleBitAddSub(K,prev_cIn,bitA,bitB)
            sumList.append(lastBitOp.sum)
            cOut = lastBitOp.cOut

        else:
            bitOp = SingleBitAddSub(K,prev_cIn,bitA,bitB)
            sumList.append(bitOp.sum)
            prev_cIn = bitOp.cOut

        pos += 1

    sumList.insert(0,cOut)
    ans = sumList

    if operation == 'sub' or operation=='Sub':
        ans = TwosComp(ans)

    return ans

if __name__ == "__main__" :
    binA = [0,1,0]
    binB = [0,1,1]
    operation = 'sub'

    ans = AddSub(binA,binB,operation)
    ans = Bin2Dec(ans)

    print(ans)

